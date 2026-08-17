#!/usr/bin/env python3
"""OKF lint (stdlib-only). Run from repo root: python3 scripts/okf_lint.py"""

from __future__ import annotations

import os
import re
import sys
from collections import defaultdict
from pathlib import Path

LANG_RE = re.compile(r"^[a-z]{2,3}(-[A-Za-z0-9]{2,8})*$")
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
MD_LINK_TARGET = re.compile(r"\.md(?:#.*)?$", re.IGNORECASE)

# Spec reserved + scaffold meta docs (not OKF concepts; no frontmatter).
RESERVED_NAMES = {
    "index.md",
    "log.md",
    "changelog.md",
    "readme.md",
    "license",
    "license-code",
    "contributing.md",
    "agents.md",
}
SKIP_DIR_NAMES = {".github", ".git", ".superpowers", "docs", "evidence-template"}
EVIDENCE_TEMPLATE_FILENAME = "evidence-template.en.md"
TEMPLATE_FIELD_TYPES = {"text", "textarea", "select", "number", "date"}

ROOT = Path(".").resolve()


def rel(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def is_reserved(path: Path) -> bool:
    return path.name.lower() in RESERVED_NAMES


def under_skip_dir(path: Path) -> bool:
    try:
        parts = path.resolve().relative_to(ROOT).parts
    except ValueError:
        parts = path.parts
    return any(p in SKIP_DIR_NAMES for p in parts[:-1])


def split_frontmatter(text: str) -> tuple[str | None, str | None]:
    """Return (yaml_block, body). Both None = missing/unterminated."""
    if text.startswith("\ufeff"):
        text = text[1:]
    if not (text.startswith("---") and len(text) > 3 and text[3] in "\r\n"):
        return None, None
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "\n".join(lines[1:i]), "\n".join(lines[i + 1 :])
    return None, None


def _parse_scalar(raw: str):
    s = raw.strip()
    if not s:
        return ""
    if (s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'")):
        return s[1:-1]
    if s.startswith("[") and s.endswith("]"):
        inner = s[1:-1].strip()
        if not inner:
            return []
        return [_parse_scalar(part) for part in _split_flow(inner)]
    if s.startswith("{") and s.endswith("}"):
        inner = s[1:-1].strip()
        if not inner:
            return {}
        obj = {}
        for part in _split_flow(inner):
            if ":" not in part:
                continue
            k, v = part.split(":", 1)
            obj[k.strip()] = _parse_scalar(v)
        return obj
    if s.lower() in ("true", "false"):
        return s.lower() == "true"
    if re.fullmatch(r"-?\d+", s):
        return int(s)
    return s


def _split_flow(inner: str) -> list[str]:
    parts: list[str] = []
    buf: list[str] = []
    depth = 0
    in_str = None
    for ch in inner:
        if in_str:
            buf.append(ch)
            if ch == in_str:
                in_str = None
            continue
        if ch in "\"'":
            in_str = ch
            buf.append(ch)
            continue
        if ch in "[{":
            depth += 1
            buf.append(ch)
            continue
        if ch in "]}":
            depth = max(0, depth - 1)
            buf.append(ch)
            continue
        if ch == "," and depth == 0:
            parts.append("".join(buf).strip())
            buf = []
            continue
        buf.append(ch)
    if buf or parts:
        parts.append("".join(buf).strip())
    return [p for p in parts if p]


def parse_simple_yaml(block: str) -> dict | None:
    """Parse this catalog's small YAML subset, including nested maps and lists."""
    lines = block.splitlines()

    def next_content(i: int) -> int | None:
        while i < len(lines):
            stripped = lines[i].strip()
            if stripped and not stripped.startswith("#"):
                return i
            i += 1
        return None

    def indent_of(line: str) -> int | None:
        prefix = line[: len(line) - len(line.lstrip(" \t"))]
        if "\t" in prefix:
            return None
        return len(prefix)

    def parse_block(i: int, indent: int) -> tuple[dict | list, int] | None:
        first = next_content(i)
        if first is None or indent_of(lines[first]) != indent:
            return None
        first_text = lines[first].strip()
        is_list = first_text == "-" or first_text.startswith("- ")
        result: dict | list = [] if is_list else {}
        i = first

        while True:
            current = next_content(i)
            if current is None:
                return result, len(lines)
            current_indent = indent_of(lines[current])
            if current_indent is None:
                return None
            if current_indent < indent:
                return result, current
            if current_indent > indent:
                return None

            text = lines[current].strip()
            item_is_list = text == "-" or text.startswith("- ")
            if item_is_list != is_list:
                return None

            if not is_list:
                if ":" not in text:
                    return None
                key, rest = text.split(":", 1)
                key = key.strip()
                if not key:
                    return None
                i = current + 1
                if rest.strip():
                    assert isinstance(result, dict)
                    result[key] = _parse_scalar(rest)
                    continue
                child_start = next_content(i)
                if child_start is not None:
                    child_indent = indent_of(lines[child_start])
                    if child_indent is None:
                        return None
                    if child_indent > indent:
                        child = parse_block(child_start, child_indent)
                        if child is None:
                            return None
                        value, i = child
                        assert isinstance(result, dict)
                        result[key] = value
                        continue
                assert isinstance(result, dict)
                result[key] = {}
                continue

            item = text[1:].strip()
            i = current + 1
            assert isinstance(result, list)
            if not item:
                child_start = next_content(i)
                if child_start is None:
                    result.append({})
                    continue
                child_indent = indent_of(lines[child_start])
                if child_indent is None or child_indent <= indent:
                    result.append({})
                    continue
                child = parse_block(child_start, child_indent)
                if child is None:
                    return None
                value, i = child
                result.append(value)
                continue

            if ":" not in item:
                result.append(_parse_scalar(item))
                child_start = next_content(i)
                if child_start is not None:
                    child_indent = indent_of(lines[child_start])
                    if child_indent is None or child_indent > indent:
                        return None
                continue

            key, rest = item.split(":", 1)
            key = key.strip()
            if not key:
                return None
            entry: dict = {}
            if rest.strip():
                entry[key] = _parse_scalar(rest)
            else:
                child_start = next_content(i)
                if child_start is not None:
                    child_indent = indent_of(lines[child_start])
                    if child_indent is None:
                        return None
                    if child_indent > indent:
                        child = parse_block(child_start, child_indent)
                        if child is None:
                            return None
                        entry[key], i = child
                    else:
                        entry[key] = {}
                else:
                    entry[key] = {}

            child_start = next_content(i)
            if child_start is not None:
                child_indent = indent_of(lines[child_start])
                if child_indent is None:
                    return None
                if child_indent > indent:
                    child = parse_block(child_start, child_indent)
                    if child is None:
                        return None
                    extra, i = child
                    if not isinstance(extra, dict):
                        return None
                    entry.update(extra)
            result.append(entry)

    start = next_content(0)
    if start is None:
        return {}
    if indent_of(lines[start]) != 0:
        return None
    parsed = parse_block(start, 0)
    if parsed is None:
        return None
    result, end = parsed
    if next_content(end) is not None or not isinstance(result, dict):
        return None
    return result


def is_evidence_template(path: Path) -> bool:
    """True only for a method's non-concept, single-file evidence template."""
    try:
        parts = path.resolve().relative_to(ROOT).parts
    except ValueError:
        return False
    return (
        len(parts) == 3
        and parts[0] == "methods"
        and path.name == EVIDENCE_TEMPLATE_FILENAME
    )


def validate_evidence_template(
    method_path: Path, method_meta: dict, errors: list[str]
) -> None:
    """Validate the typed, pinned template required by a Method."""
    method_ref = rel(method_path)
    pointer = method_meta.get("evidence_template")
    if not isinstance(pointer, str) or not pointer.strip():
        errors.append(
            f"ERROR: {method_ref}: missing evidence_template "
            "(expected evidence-template@<version>)"
        )
        return

    template_id, sep, template_version = pointer.strip().rpartition("@")
    if not sep or not template_id or not template_version:
        errors.append(
            f"ERROR: {method_ref}: evidence_template expected '<id>@<version>' "
            f"(got {pointer!r})"
        )
        return
    if template_id != "evidence-template":
        errors.append(
            f"ERROR: {method_ref}: evidence_template expected "
            f"'evidence-template@<version>' (got {pointer!r})"
        )

    method_id = method_meta.get("id")
    method_version = method_meta.get("version")
    if not isinstance(method_id, str) or not method_id.strip():
        errors.append(
            f"ERROR: {method_ref}: cannot validate evidence template without method id"
        )
        return
    if method_version is None or not str(method_version).strip():
        errors.append(
            f"ERROR: {method_ref}: cannot validate evidence template without method version"
        )
        return

    template_path = ROOT / "methods" / method_id / EVIDENCE_TEMPLATE_FILENAME
    template_ref = rel(template_path)
    try:
        template_text = template_path.read_text(encoding="utf-8")
    except OSError as exc:
        errors.append(
            f"ERROR: {method_ref}: evidence_template {pointer!r} requires readable "
            f"{template_ref} ({exc.strerror or exc})"
        )
        return

    raw, _body = split_frontmatter(template_text)
    if raw is None:
        errors.append(
            f"ERROR: {template_ref}: evidence template frontmatter is missing or unterminated"
        )
        return
    template_meta = parse_simple_yaml(raw)
    if template_meta is None:
        errors.append(
            f"ERROR: {template_ref}: evidence template frontmatter is not parseable simple YAML"
        )
        return

    def expected(field: str, value, wanted) -> None:
        if value != wanted:
            errors.append(
                f"ERROR: {template_ref}: {field} expected {wanted!r} (got {value!r})"
            )

    expected("type", template_meta.get("type"), "Form Template")
    expected("id", template_meta.get("id"), "evidence-template")
    expected("version", str(template_meta.get("version", "")), template_version)

    lang = template_meta.get("lang")
    if not isinstance(lang, str) or not lang.strip():
        errors.append(f"ERROR: {template_ref}: lang expected a non-empty BCP-47 tag (got {lang!r})")
    else:
        if not LANG_RE.match(lang):
            errors.append(
                f"ERROR: {template_ref}: lang expected a plausible BCP-47 tag (got {lang!r})"
            )
        _slug, suffix = filename_slug_and_lang(template_path)
        if suffix != lang:
            errors.append(
                f"ERROR: {template_ref}: filename language suffix expected {lang!r} "
                f"(got {suffix!r})"
            )

    expected("template_kind", template_meta.get("template_kind"), "form")
    expected(
        "applies_to_method",
        template_meta.get("applies_to_method"),
        f"{method_id}@{method_version}",
    )

    fields = template_meta.get("fields")
    if not isinstance(fields, dict) or not fields:
        errors.append(
            f"ERROR: {template_ref}: fields expected a non-empty mapping (got {fields!r})"
        )
    else:
        for field_id, declaration in fields.items():
            field_ref = f"fields.{field_id}"
            if not isinstance(declaration, dict):
                errors.append(
                    f"ERROR: {template_ref}: {field_ref} expected a mapping (got {declaration!r})"
                )
                continue
            field_type = declaration.get("type")
            if field_type not in TEMPLATE_FIELD_TYPES:
                errors.append(
                    f"ERROR: {template_ref}: {field_ref}.type expected one of "
                    f"{sorted(TEMPLATE_FIELD_TYPES)!r} (got {field_type!r})"
                )
            if field_type == "select" and not isinstance(declaration.get("options"), list):
                errors.append(
                    f"ERROR: {template_ref}: {field_ref}.options expected a list "
                    f"for select (got {declaration.get('options')!r})"
                )

    generated = template_meta.get("generated")
    if not isinstance(generated, dict):
        errors.append(
            f"ERROR: {template_ref}: generated expected a mapping with by and at (got {generated!r})"
        )
    else:
        by = generated.get("by")
        at = generated.get("at")
        if not isinstance(by, str) or "/" not in by or not all(by.split("/", 1)):
            errors.append(
                f"ERROR: {template_ref}: generated.by expected '<producer>/<version>' (got {by!r})"
            )
        if at is None or not str(at).strip():
            errors.append(
                f"ERROR: {template_ref}: generated.at expected a non-empty ISO timestamp (got {at!r})"
            )


def filename_slug_and_lang(path: Path) -> tuple[str, str | None]:
    stem = path.name[:-3] if path.name.lower().endswith(".md") else path.name
    if "." not in stem:
        return stem, None
    slug, lang = stem.rsplit(".", 1)
    return slug, lang


def normalize_link_target(target: str, from_file: Path) -> Path | None:
    t = target.strip()
    if not t or t.startswith("#"):
        return None
    if "://" in t or t.startswith("mailto:"):
        return None
    if t.startswith("resource:"):
        return None
    if "#" in t:
        t = t.split("#", 1)[0]
    if not t:
        return None
    if not MD_LINK_TARGET.search(t):
        return None
    if t.startswith("/"):
        return (ROOT / t.lstrip("/")).resolve()
    return (from_file.parent / t).resolve()


def collect_md_files() -> list[Path]:
    files: list[Path] = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIR_NAMES]
        for name in filenames:
            if not name.lower().endswith(".md"):
                continue
            p = Path(dirpath) / name
            if under_skip_dir(p):
                continue
            files.append(p)
    return sorted(files, key=lambda p: rel(p))


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    files = collect_md_files()
    checked = 0

    by_id: dict[str, list[tuple[Path, dict]]] = defaultdict(list)
    parsed: dict[Path, tuple[dict | None, str | None, str | None]] = {}

    for path in files:
        text = path.read_text(encoding="utf-8", errors="replace")
        raw, body = split_frontmatter(text)
        if raw is None:
            parsed[path] = (None, None, "missing or unterminated YAML frontmatter")
            continue
        meta = parse_simple_yaml(raw)
        if meta is None:
            parsed[path] = (None, body, "frontmatter is not parseable simple YAML")
            continue
        parsed[path] = (meta, body, None)
        cid = meta.get("id")
        if not is_evidence_template(path) and isinstance(cid, str) and cid:
            by_id[cid].append((path, meta))

    for path in files:
        r = rel(path)
        checked += 1
        reserved = is_reserved(path)
        meta, body, fm_err = parsed.get(path, (None, None, "unreadable"))

        if path.resolve() == (ROOT / "index.md").resolve():
            if fm_err or meta is None:
                errors.append(
                    f"ERROR: {r}: root index.md missing or invalid frontmatter (need okf_version)"
                )
            elif "okf_version" not in meta:
                errors.append(f"ERROR: {r}: missing okf_version")
            elif str(meta.get("okf_version")) != "0.2":
                errors.append(
                    f"ERROR: {r}: okf_version must be \"0.2\" (got {meta.get('okf_version')!r})"
                )

        if not reserved and not is_evidence_template(path):
            if fm_err or meta is None:
                errors.append(f"ERROR: {r}: {fm_err or 'missing frontmatter'}")
            else:
                typ = meta.get("type")
                if typ is None or (isinstance(typ, str) and not str(typ).strip()):
                    errors.append(f"ERROR: {r}: missing or empty type")

                slug, lang_suffix = filename_slug_and_lang(path)
                cid = meta.get("id")
                if cid is None or (isinstance(cid, str) and not str(cid).strip()):
                    errors.append(f"ERROR: {r}: missing or empty id")
                elif str(cid) != slug:
                    errors.append(
                        f"ERROR: {r}: id {cid!r} does not equal filename slug {slug!r}"
                    )

                lang = meta.get("lang")
                if lang is None or (isinstance(lang, str) and not str(lang).strip()):
                    errors.append(f"ERROR: {r}: missing or empty lang")
                else:
                    lang_s = str(lang)
                    if not LANG_RE.match(lang_s):
                        errors.append(
                            f"ERROR: {r}: lang {lang_s!r} is not a plausible BCP-47 tag"
                        )
                    if lang_suffix is None:
                        errors.append(
                            f"ERROR: {r}: filename language suffix missing (expected .{lang_s}.md)"
                        )
                    elif lang_suffix != lang_s:
                        errors.append(
                            f"ERROR: {r}: filename language suffix {lang_suffix!r} "
                            f"does not match lang {lang_s!r}"
                        )

                desc = meta.get("description")
                if desc is None or (isinstance(desc, str) and not str(desc).strip()):
                    errors.append(f"ERROR: {r}: missing or empty description")

                typ_s = str(typ).strip() if typ is not None else ""
                if typ_s in ("Theory", "Finding"):
                    authors = meta.get("authors")
                    if not isinstance(authors, list) or len(authors) == 0:
                        errors.append(
                            f"ERROR: {r}: type {typ_s} requires a non-empty authors list"
                        )
                    else:
                        for i, entry in enumerate(authors):
                            if not isinstance(entry, dict):
                                errors.append(
                                    f"ERROR: {r}: authors[{i}] must be a mapping with name"
                                )
                                continue
                            name = entry.get("name")
                            if name is None or (
                                isinstance(name, str) and not str(name).strip()
                            ):
                                errors.append(
                                    f"ERROR: {r}: authors[{i}] missing or empty name"
                                )

                if meta.get("origin") == "translation":
                    gen = meta.get("generated")
                    by = gen.get("by") if isinstance(gen, dict) else None
                    if not by or (isinstance(by, str) and not str(by).strip()):
                        warnings.append(
                            f"WARNING: {r}: origin: translation without generated.by"
                        )

                if "translations" in meta:
                    cid_s = str(meta.get("id") or "")
                    derived = sorted(
                        {
                            str(m.get("lang"))
                            for _p, m in by_id.get(cid_s, [])
                            if m.get("lang")
                        }
                    )
                    listed = meta.get("translations")
                    if isinstance(listed, list):
                        listed_norm = sorted(str(x) for x in listed)
                    elif isinstance(listed, str):
                        listed_norm = [listed]
                    else:
                        listed_norm = []
                    if listed_norm != derived:
                        warnings.append(
                            f"WARNING: {r}: translations {listed_norm} "
                            f"inconsistent with derived languages {derived}"
                        )

                try:
                    rel_parts = path.resolve().relative_to(ROOT).parts
                except ValueError:
                    rel_parts = ()
                if "findings" in rel_parts and body is not None:
                    if "## Evidence" not in body:
                        warnings.append(f"WARNING: {r}: findings file missing ## Evidence")
                    if "## Limitations" not in body:
                        warnings.append(
                            f"WARNING: {r}: findings file missing ## Limitations"
                        )

                if typ_s == "Method":
                    validate_evidence_template(path, meta, errors)

        # Link warnings: all non-reserved concept bodies, plus every index.md
        # (reserved indexes still get missing-target warnings).
        do_links = (not reserved) or path.name.lower() == "index.md"
        if do_links:
            scan = (
                body
                if body is not None
                else path.read_text(encoding="utf-8", errors="replace")
            )
            for m in LINK_RE.finditer(scan):
                target = m.group(1)
                resolved = normalize_link_target(target, path)
                if resolved is None:
                    continue
                try:
                    resolved.relative_to(ROOT)
                except ValueError:
                    continue
                if not resolved.is_file():
                    try:
                        trel = str(resolved.relative_to(ROOT)).replace("\\", "/")
                    except ValueError:
                        trel = target
                    if path.name.lower() == "index.md":
                        warnings.append(
                            f"WARNING: {r}: index entry target missing: {trel}"
                        )
                    else:
                        warnings.append(f"WARNING: {r}: broken link to {trel}")

    for e in errors:
        print(e)
    for w in warnings:
        print(w)

    n_err = len(errors)
    n_warn = len(warnings)
    if n_err:
        print(f"FAILED: {checked} files checked, {n_err} errors")
        return 1
    print(f"OK: {checked} files checked, {n_err} errors, {n_warn} warnings")
    return 0


if __name__ == "__main__":
    sys.exit(main())
