#!/usr/bin/env python3
"""Deterministic claim governance rules engine (stdlib only, zero model calls).

Usage:
  python3 scripts/okf_claim_check.py <path-to-finding.md> [--repo-root DIR]
  python3 scripts/okf_claim_check.py findings/ [--repo-root DIR]

Exit code is always 0 — this script reports; the workflow gates.
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path

# Reuse the lint frontmatter parser (same minimal YAML subset).
sys.path.insert(0, str(Path(__file__).resolve().parent))
from okf_lint import (  # noqa: E402
    LINK_RE,
    parse_simple_yaml,
    split_frontmatter,
)

CONFIDENCE_TIER = {
    "low": "provisional",
    "medium": "tentative",
    "high": "supported",
}
ACTIVE_TIERS = frozenset({"provisional", "tentative", "supported"})
STATUS_VALUES = frozenset(
    {
        "provisional",
        "tentative",
        "supported",
        "challenged",
        "contested",
        "amended",
        "retracted",
        "deprecated",
    }
)
OPEN_CHALLENGE = frozenset({"challenged", "contested"})
BUNDLE_ROLES = (
    "index",
    "question",
    "context",
    "intervention",
    "observations",
    "results",
    "reflection",
    "limitations",
    "provenance",
)
ISO_RE = re.compile(
    r"(\d{4}-\d{2}-\d{2}(?:[T ]\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:?\d{2})?)?)"
)


def load_md(path: Path) -> tuple[dict | None, str, str | None]:
    text = path.read_text(encoding="utf-8", errors="replace")
    raw, body = split_frontmatter(text)
    if raw is None:
        return None, text, "missing or unterminated YAML frontmatter"
    meta = parse_simple_yaml(raw)
    if meta is None:
        return None, body or "", "frontmatter is not parseable simple YAML"
    return meta, body or "", None


def parse_ts(value) -> datetime | None:
    if value is None:
        return None
    if isinstance(value, dict):
        return parse_ts(value.get("at"))
    s = str(value).strip()
    if not s:
        return None
    m = ISO_RE.search(s)
    if not m:
        return None
    raw = m.group(1).replace(" ", "T")
    if raw.endswith("Z"):
        raw = raw[:-1] + "+00:00"
    # allow YYYY-MM-DD
    if len(raw) == 10:
        raw = raw + "T00:00:00+00:00"
    try:
        return datetime.fromisoformat(raw)
    except ValueError:
        return None


def meta_ts(meta: dict | None) -> datetime | None:
    if not meta:
        return None
    for key in ("created", "timestamp"):
        ts = parse_ts(meta.get(key))
        if ts:
            return ts
    gen = meta.get("generated")
    if isinstance(gen, dict):
        return parse_ts(gen.get("at"))
    return parse_ts(gen)


def contributor_key(meta: dict | None) -> str | None:
    if not meta:
        return None
    verified = meta.get("verified")
    if isinstance(verified, dict) and verified.get("by"):
        return f"verified:{verified.get('by')}"
    if meta.get("contributor"):
        return f"contributor:{meta.get('contributor')}"
    gen = meta.get("generated")
    if isinstance(gen, dict) and gen.get("by"):
        return f"generated:{gen.get('by')}"
    return None


def resolve_md_link(target: str, from_file: Path, root: Path) -> Path | None:
    t = target.strip()
    if not t or t.startswith("#") or "://" in t or t.startswith("mailto:"):
        return None
    if "#" in t:
        t = t.split("#", 1)[0]
    if not t:
        return None
    if t.startswith("/"):
        cand = (root / t.lstrip("/")).resolve()
    else:
        cand = (from_file.parent / t).resolve()
    try:
        cand.relative_to(root.resolve())
    except ValueError:
        return None
    return cand


def find_role_file(bundle_dir: Path, role: str) -> Path | None:
    for name in (f"{role}.md", f"{role}.en.md"):
        p = bundle_dir / name
        if p.is_file():
            return p
    matches = sorted(bundle_dir.glob(f"{role}.*.md"))
    return matches[0] if matches else None


def evidence_bundle_dirs(linked_paths: list[Path], root: Path) -> list[Path]:
    """Paths that resolve into evidence/<slug>/ (file or dir)."""
    found: list[Path] = []
    seen: set[Path] = set()
    root = root.resolve()
    for p in linked_paths:
        try:
            rel = p.resolve().relative_to(root)
        except ValueError:
            continue
        parts = rel.parts
        if "evidence" not in parts:
            continue
        idx = parts.index("evidence")
        if len(parts) <= idx + 1:
            continue
        slug = parts[idx + 1]
        if slug in ("index.md",):
            continue
        bundle = (root / Path(*parts[: idx + 2])).resolve()
        if not bundle.is_dir():
            # link pointed at a file; parent may be the bundle
            if p.is_file() and p.parent.name != "evidence":
                bundle = p.parent.resolve()
            else:
                continue
        try:
            brel = bundle.relative_to(root)
        except ValueError:
            continue
        bparts = brel.parts
        if "evidence" not in bparts:
            continue
        if bundle not in seen and bundle.is_dir():
            seen.add(bundle)
            found.append(bundle)
    return found


def link_targets(body: str, from_file: Path, root: Path) -> list[tuple[str, Path]]:
    out: list[tuple[str, Path]] = []
    for m in LINK_RE.finditer(body):
        target = m.group(1)
        resolved = resolve_md_link(target, from_file, root)
        if resolved is not None:
            out.append((target, resolved))
    return out


def is_under(path: Path, root: Path, dirname: str) -> bool:
    try:
        parts = path.resolve().relative_to(root.resolve()).parts
    except ValueError:
        return False
    return dirname in parts


def collect_findings(path: Path) -> list[Path]:
    if path.is_file():
        return [path]
    files: list[Path] = []
    for p in sorted(path.rglob("*.md")):
        if p.name.lower() in ("index.md", "log.md", "readme.md"):
            continue
        files.append(p)
    return files


def existing_supported_claims(root: Path, exclude: Path) -> list[tuple[Path, str]]:
    findings_dir = root / "findings"
    if not findings_dir.is_dir():
        return []
    out: list[tuple[Path, str]] = []
    for p in findings_dir.rglob("*.md"):
        if p.name.lower() in ("index.md", "log.md", "readme.md"):
            continue
        if p.resolve() == exclude.resolve():
            continue
        meta, _, err = load_md(p)
        if err or not meta:
            continue
        if str(meta.get("status", "")).lower() != "supported":
            continue
        claim = meta.get("claim")
        if isinstance(claim, str) and claim.strip():
            out.append((p, claim.strip()))
    return out


def check_finding(path: Path, root: Path) -> dict:
    checks: list[tuple[str, str, str]] = []  # name, PASS|FAIL, reason
    meta, body, err = load_md(path)

    # --- 1. Claim shape ---
    if err or meta is None:
        checks.append(("claim_shape", "FAIL", f"cannot parse finding: {err}"))
        return _verdict(path, "unknown", checks, "parse failure")
    claim = meta.get("claim")
    confidence = str(meta.get("confidence", "")).lower().strip()
    status = str(meta.get("status", "")).lower().strip()
    typ = meta.get("type")
    shape_ok = True
    shape_reasons: list[str] = []
    if not (isinstance(claim, str) and claim.strip()):
        shape_ok = False
        shape_reasons.append("missing claim")
    if confidence not in CONFIDENCE_TIER:
        shape_ok = False
        shape_reasons.append(f"confidence {confidence!r} not low|medium|high")
    if status not in STATUS_VALUES:
        shape_ok = False
        shape_reasons.append(f"status {status!r} not in vocabulary")
    if typ != "Finding":
        shape_ok = False
        shape_reasons.append(f"type {typ!r} != Finding")
    checks.append(
        (
            "claim_shape",
            "PASS" if shape_ok else "FAIL",
            "ok" if shape_ok else "; ".join(shape_reasons),
        )
    )

    # --- 2. Tier ceiling ---
    expected_tier = CONFIDENCE_TIER.get(confidence)
    if status in ACTIVE_TIERS:
        tier = status
        if expected_tier and status != expected_tier:
            checks.append(
                (
                    "tier_ceiling",
                    "FAIL",
                    f"confidence {confidence} maps to {expected_tier}, status is {status}",
                )
            )
        else:
            checks.append(
                (
                    "tier_ceiling",
                    "PASS",
                    f"confidence {confidence} ↔ status {status}",
                )
            )
    else:
        tier = expected_tier or "unknown"
        checks.append(
            (
                "tier_ceiling",
                "PASS",
                f"status {status} (non-active); tier from confidence → {tier}",
            )
        )

    links = link_targets(body, path, root)
    linked_paths = [p for _, p in links]

    # --- 3. Evidence links + chain ---
    bundles = evidence_bundle_dirs(linked_paths, root)
    intervention_links = []
    question_links = []
    for _t, p in links:
        if not p.exists():
            continue
        rel = str(p.relative_to(root.resolve())).replace("\\", "/")
        # intervention: path contains intervention or type Intervention
        if "intervention" in p.name.lower() or "/intervention" in rel.lower():
            intervention_links.append(p)
        else:
            m, _, e = load_md(p) if p.is_file() else (None, "", "not a file")
            if m and m.get("type") == "Intervention":
                intervention_links.append(p)
        if is_under(p, root, "theory"):
            question_links.append(p)

    chain_ok = bool(bundles) and bool(intervention_links) and bool(question_links)
    missing_roles_any = False
    bundle_role_notes: list[str] = []
    for b in bundles:
        missing = [r for r in BUNDLE_ROLES if find_role_file(b, r) is None]
        if missing:
            missing_roles_any = True
            bundle_role_notes.append(f"{b.name}: missing {', '.join(missing)}")
    if not bundles:
        checks.append(
            (
                "evidence_links",
                "FAIL",
                "no markdown link to evidence/<slug>/ bundle",
            )
        )
    elif missing_roles_any:
        checks.append(
            (
                "evidence_links",
                "FAIL",
                "bundle incomplete: " + "; ".join(bundle_role_notes),
            )
        )
    elif not intervention_links:
        checks.append(
            (
                "evidence_links",
                "FAIL",
                "no link to an intervention",
            )
        )
    elif not question_links:
        checks.append(
            (
                "evidence_links",
                "FAIL",
                "no link to a research question under theory/",
            )
        )
    else:
        checks.append(
            (
                "evidence_links",
                "PASS",
                f"{len(bundles)} bundle(s), intervention+question chain ok",
            )
        )

    # --- 4. Bundle completeness ---
    completeness_fail: list[str] = []
    for b in bundles:
        for role in BUNDLE_ROLES:
            f = find_role_file(b, role)
            if f is None:
                completeness_fail.append(f"{b.name}/{role}: missing")
                continue
            m, body_r, e = load_md(f)
            if e or m is None:
                # index.md may be reserved listing without frontmatter — still require
                # parseable frontmatter for completeness per protocol.
                completeness_fail.append(f"{b.name}/{role}: {e or 'no frontmatter'}")
                continue
            if role == "results":
                if "Measures:" not in body_r and "measures:" not in body_r:
                    # allow "## Measures" with trailing content as soft; protocol asks Measures:
                    if not re.search(r"(?m)^#+\s*Measures\b", body_r):
                        completeness_fail.append(
                            f"{b.name}/results: no Measures: line"
                        )
            if role == "provenance":
                has_consent_key = "consent" in {k.lower() for k in m}
                has_consent_section = bool(
                    re.search(r"(?im)^##\s+Consent\b", body_r)
                )
                if not has_consent_key and not has_consent_section:
                    completeness_fail.append(
                        f"{b.name}/provenance: no consent key or ## Consent section"
                    )
    if not bundles:
        checks.append(
            ("bundle_completeness", "FAIL", "no evidence bundles to check")
        )
    elif completeness_fail:
        checks.append(
            (
                "bundle_completeness",
                "FAIL",
                "; ".join(completeness_fail[:6]),
            )
        )
    else:
        checks.append(
            (
                "bundle_completeness",
                "PASS",
                f"all {len(bundles)} bundle(s) complete with Measures + consent",
            )
        )

    # --- 5. Direction-of-fit ---
    dof_fail: list[str] = []
    for b in bundles:
        # bundle time: earliest generated.at/timestamp among role files
        bundle_times: list[datetime] = []
        for role in BUNDLE_ROLES:
            f = find_role_file(b, role)
            if f is None:
                continue
            m, _, e = load_md(f)
            if e or not m:
                continue
            ts = meta_ts(m)
            if ts:
                bundle_times.append(ts)
        bundle_ts = min(bundle_times) if bundle_times else None
        # questions: from finding links under theory/, and from bundle question.md links
        q_seen: set[Path] = set()
        q_files: list[Path] = []
        for qp in question_links:
            rp = qp.resolve()
            if rp not in q_seen and rp.is_file():
                q_seen.add(rp)
                q_files.append(rp)
        qf = find_role_file(b, "question")
        if qf:
            qm, qb, qe = load_md(qf)
            if not qe and qb:
                for _t, rp in link_targets(qb, qf, root):
                    rpr = rp.resolve()
                    if (
                        is_under(rp, root, "theory")
                        and rpr.is_file()
                        and rpr not in q_seen
                    ):
                        q_seen.add(rpr)
                        q_files.append(rp)
        if not q_files:
            dof_fail.append(f"{b.name}: no linked theory question for DoF")
            continue
        if bundle_ts is None:
            dof_fail.append(f"{b.name}: no generated.at/timestamp on bundle")
            continue
        for qpath in q_files:
            qm, _, qe = load_md(qpath)
            if qe or not qm:
                dof_fail.append(f"{b.name}: cannot parse question {qpath.name}")
                continue
            q_ts = meta_ts(qm)
            if q_ts is None:
                dof_fail.append(
                    f"{b.name}: question {qpath.name} lacks created/generated.at"
                )
                continue
            if bundle_ts < q_ts:
                dof_fail.append(
                    f"{b.name}: evidence at {bundle_ts.isoformat()} predates "
                    f"question {qpath.name} at {q_ts.isoformat()} (post-hoc framing)"
                )
    if not bundles:
        checks.append(("direction_of_fit", "FAIL", "no bundles"))
    elif dof_fail:
        checks.append(("direction_of_fit", "FAIL", "; ".join(dof_fail[:4])))
    else:
        checks.append(
            (
                "direction_of_fit",
                "PASS",
                "question timestamps ≤ evidence timestamps",
            )
        )

    # --- 6. No open challenge ---
    challenge_hits: list[str] = []
    if status in OPEN_CHALLENGE:
        challenge_hits.append(f"finding status={status}")
    for b in bundles:
        for role in BUNDLE_ROLES:
            f = find_role_file(b, role)
            if f is None:
                continue
            m, _, e = load_md(f)
            if e or not m:
                continue
            st = str(m.get("status", "")).lower()
            if st in OPEN_CHALLENGE:
                challenge_hits.append(f"{b.name}/{role} status={st}")
    if challenge_hits:
        checks.append(
            ("no_open_challenge", "FAIL", "; ".join(challenge_hits[:4]))
        )
    else:
        checks.append(("no_open_challenge", "PASS", "no challenged/contested markers"))

    # --- 7. No conflict with supported findings ---
    conflict_hits: list[str] = []
    claim_text = claim.strip() if isinstance(claim, str) else ""
    if claim_text:
        for other_path, other_claim in existing_supported_claims(root, path):
            # crude: identical claim text, or mutual substring, with different status/claim sense
            a, b_ = claim_text.lower(), other_claim.lower()
            if a == b_ or (len(a) > 20 and a in b_) or (len(b_) > 20 and b_ in a):
                # conflict if this finding is not itself that supported claim with same status
                if status != "supported" or a != b_:
                    conflict_hits.append(
                        f"overlaps supported claim in {other_path.name}"
                    )
    if conflict_hits:
        checks.append(("no_conflict", "FAIL", "; ".join(conflict_hits)))
    else:
        checks.append(("no_conflict", "PASS", "no conflicting supported claim"))

    # --- 8. Tentative requirements ---
    if tier != "tentative":
        checks.append(
            (
                "tentative_requirements",
                "PASS",
                f"not applicable (tier is {tier})",
            )
        )
    else:
        stages: list[tuple[str, str | None]] = []
        for b in bundles:
            stage = None
            contrib = None
            for role in BUNDLE_ROLES:
                f = find_role_file(b, role)
                if f is None:
                    continue
                m, _, e = load_md(f)
                if e or not m:
                    continue
                if stage is None and m.get("stage"):
                    stage = str(m.get("stage")).strip().lower()
                if contrib is None:
                    contrib = contributor_key(m)
            stages.append((stage or "", contrib))
        has_structured = any(s == "structured-experiment" for s, _ in stages)
        doc_exp = [(s, c) for s, c in stages if s == "documented-experience"]
        distinct = {c for _, c in doc_exp if c}
        if has_structured:
            checks.append(
                (
                    "tentative_requirements",
                    "PASS",
                    "≥1 structured-experiment bundle",
                )
            )
        elif len(doc_exp) >= 2 and len(distinct) >= 2:
            checks.append(
                (
                    "tentative_requirements",
                    "PASS",
                    f"≥2 documented-experience bundles from {len(distinct)} contributors",
                )
            )
        else:
            checks.append(
                (
                    "tentative_requirements",
                    "FAIL",
                    "need ≥1 structured-experiment OR ≥2 documented-experience "
                    f"by distinct contributors (got stages={stages})",
                )
            )

    report_lines = [
        f"evidence bundles resolved: {len(bundles)}",
        f"intervention links: {len(intervention_links)}; theory question links: {len(question_links)}",
        f"claim: {claim_text[:120] if claim_text else '(none)'}",
    ]
    return _verdict(path, tier if tier else "unknown", checks, "; ".join(report_lines))


def _verdict(
    path: Path, tier: str, checks: list[tuple[str, str, str]], report: str
) -> dict:
    failed = [c for c in checks if c[1] == "FAIL"]
    # Check 9 / verdict rules
    if tier == "supported":
        route = "needs-review"
        auto = "no"
        reason = "supported tier never auto-approved (human review)"
    elif any(c[0] == "no_open_challenge" and c[1] == "FAIL" for c in checks):
        route = "needs-review"
        auto = "no"
        reason = "open challenge/contested state"
    elif failed:
        route = "needs-review"
        auto = "no"
        reason = "failed: " + ", ".join(c[0] for c in failed)
    elif tier == "provisional":
        route = "auto-approve"
        auto = "yes"
        reason = "all checks pass; provisional"
    elif tier == "tentative":
        route = "auto-approve"
        auto = "yes"
        reason = "all checks pass; tentative requirements met"
    else:
        route = "needs-review"
        auto = "no"
        reason = f"tier {tier} not auto-approvable"

    return {
        "path": str(path),
        "tier": tier,
        "auto_approvable": auto,
        "route": route,
        "checks": checks,
        "report": report,
        "reason": reason,
    }


def format_report(v: dict) -> str:
    lines = [
        f"FILE: {v['path']}",
        f"TIER: {v['tier']}",
        f"AUTO_APPROVABLE: {v['auto_approvable']}",
        f"ROUTE: {v['route']}",
        "CHECKS:",
    ]
    for name, result, reason in v["checks"]:
        lines.append(f"  {result}: {name} — {reason}")
    lines.append("REPORT:")
    for part in str(v["report"]).split("; "):
        lines.append(f"  {part}")
    lines.append(f"  verdict_note: {v['reason']}")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="OKF claim governance rules engine")
    ap.add_argument(
        "path",
        nargs="?",
        default="findings",
        help="Finding file or directory (default: findings/)",
    )
    ap.add_argument(
        "--repo-root",
        default=".",
        help="Repository root for resolving evidence/theory links (default: cwd)",
    )
    args = ap.parse_args(argv)
    root = Path(args.repo_root).resolve()
    target = Path(args.path)
    if not target.is_absolute():
        target = (Path.cwd() / target).resolve()
    if not target.exists():
        print(f"FILE: {target}")
        print("TIER: unknown")
        print("AUTO_APPROVABLE: no")
        print("ROUTE: needs-review")
        print("CHECKS:")
        print("  FAIL: claim_shape — path does not exist")
        print("REPORT:")
        print("  path missing")
        return 0

    findings = collect_findings(target)
    if not findings:
        print("REPORT:")
        print(f"  no finding files under {target}")
        print("ROUTE: needs-review")
        print("AUTO_APPROVABLE: no")
        print("TIER: unknown")
        return 0

    for i, f in enumerate(findings):
        if i:
            print("---")
        v = check_finding(f, root)
        print(format_report(v))
    return 0


if __name__ == "__main__":
    sys.exit(main())
