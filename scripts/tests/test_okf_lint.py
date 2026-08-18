from __future__ import annotations

import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
LINT = REPO_ROOT / "scripts" / "okf_lint.py"


def run_lint(repo: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(LINT)],
        cwd=repo,
        check=False,
        text=True,
        capture_output=True,
    )


def write_catalog_root(repo: Path) -> None:
    (repo / "index.md").write_text('---\nokf_version: "0.2"\n---\n', encoding="utf-8")


def write_method(repo: Path, method_id: str, pointer: str | None) -> Path:
    method_dir = repo / "methods" / method_id
    method_dir.mkdir(parents=True)
    evidence_pointer = f"evidence_template: {pointer}\n" if pointer else ""
    (method_dir / f"{method_id}.en.md").write_text(
        "---\n"
        "type: Method\n"
        f"id: {method_id}\n"
        "lang: en\n"
        "origin: native\n"
        "status: draft\n"
        "version: 1.0.0\n"
        f"title: {method_id} method\n"
        f"description: Method for {method_id} test coverage.\n"
        f"{evidence_pointer}"
        "---\n",
        encoding="utf-8",
    )
    return method_dir


def write_template(
    method_dir: Path,
    *,
    version: str = "1.0.0",
    applies_to_method: str,
) -> None:
    (method_dir / "evidence-template.en.md").write_text(
        "---\n"
        "type: Form Template\n"
        "id: evidence-template\n"
        f"version: {version}\n"
        "lang: en\n"
        "template_kind: form\n"
        f"applies_to_method: {applies_to_method}\n"
        "fields:\n"
        "  frozen_value:\n"
        "    type: text\n"
        "    read_only: true\n"
        "    source: frozen_run.value\n"
        "  owner_judgement:\n"
        "    type: select\n"
        "    options: [yes, no, insufficient-information]\n"
        "assistant:\n"
        "  guidance: Preserve the evidence boundary.\n"
        "generated: { by: codex/test, at: 2026-08-17T00:00:00Z }\n"
        "---\n"
        "# Evidence template\n",
        encoding="utf-8",
    )


def test_method_without_evidence_template_is_an_error(tmp_path: Path) -> None:
    write_catalog_root(tmp_path)
    write_method(tmp_path, "missing-pointer", None)

    result = run_lint(tmp_path)

    assert result.returncode == 1
    assert "methods/missing-pointer/missing-pointer.en.md: missing evidence_template" in result.stdout


def test_missing_evidence_template_file_is_an_error(tmp_path: Path) -> None:
    write_catalog_root(tmp_path)
    write_method(tmp_path, "missing-file", "evidence-template@1.0.0")

    result = run_lint(tmp_path)

    assert result.returncode == 1
    assert "requires readable methods/missing-file/evidence-template.en.md" in result.stdout


def test_evidence_template_version_must_match_method_pointer(tmp_path: Path) -> None:
    write_catalog_root(tmp_path)
    method_dir = write_method(tmp_path, "version-check", "evidence-template@1.0.0")
    write_template(
        method_dir,
        version="2.0.0",
        applies_to_method="version-check@1.0.0",
    )

    result = run_lint(tmp_path)

    assert result.returncode == 1
    assert "evidence-template.en.md: version expected '1.0.0' (got '2.0.0')" in result.stdout


def test_evidence_template_must_bind_to_its_method_version(tmp_path: Path) -> None:
    write_catalog_root(tmp_path)
    method_dir = write_method(tmp_path, "binding-check", "evidence-template@1.0.0")
    write_template(
        method_dir,
        applies_to_method="other-method@1.0.0",
    )

    result = run_lint(tmp_path)

    assert result.returncode == 1
    assert (
        "evidence-template.en.md: applies_to_method expected 'binding-check@1.0.0' "
        "(got 'other-method@1.0.0')"
    ) in result.stdout


def test_method_local_templates_are_exempt_from_concept_identity_rules(tmp_path: Path) -> None:
    write_catalog_root(tmp_path)
    for method_id in ("first-method", "second-method"):
        method_dir = write_method(tmp_path, method_id, "evidence-template@1.0.0")
        write_template(method_dir, applies_to_method=f"{method_id}@1.0.0")

    result = run_lint(tmp_path)

    assert result.returncode == 0, result.stdout
    assert "OK: 5 files checked, 0 errors" in result.stdout


def test_valid_method_and_evidence_template_pair_passes(tmp_path: Path) -> None:
    write_catalog_root(tmp_path)
    method_dir = write_method(tmp_path, "valid-method", "evidence-template@1.0.0")
    write_template(method_dir, applies_to_method="valid-method@1.0.0")

    result = run_lint(tmp_path)

    assert result.returncode == 0, result.stdout
    assert "OK: 3 files checked, 0 errors" in result.stdout
