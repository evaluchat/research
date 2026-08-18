from __future__ import annotations

import importlib.util
import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
BUILD_SITE = REPO_ROOT / "scripts" / "build_site.py"


def load_builder():
    spec = importlib.util.spec_from_file_location("build_site_under_test", BUILD_SITE)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def write_fixture(repo: Path) -> None:
    (repo / "methods" / "sample" / "evidence").mkdir(parents=True)
    (repo / "README.md").write_text(
        "# Catalog\n\nBrowse [methods](methods/).\n", encoding="utf-8"
    )
    (repo / "index.md").write_text(
        '---\nokf_version: "0.2"\n---\n# Catalog\n\n## Methods\n\n[Methods](methods/)\n',
        encoding="utf-8",
    )
    (repo / "methods" / "index.md").write_text(
        "# Methods\n\n[Sample](sample/sample.en.md)\n", encoding="utf-8"
    )
    (repo / "methods" / "sample" / "sample.en.md").write_text(
        "---\n"
        "type: Method\n"
        "id: sample\n"
        "lang: en\n"
        "status: draft\n"
        "version: 1.0.0\n"
        "title: Sample method\n"
        "description: A build-site fixture.\n"
        "evidence_template: evidence-template@1.0.0\n"
        "---\n"
        "# Sample method\n\n"
        "Use the [evidence template](evidence-template.en.md) and browse "
        "[evidence](evidence/).\n",
        encoding="utf-8",
    )
    (repo / "methods" / "sample" / "evidence-template.en.md").write_text(
        "---\n"
        "type: Form Template\n"
        "id: evidence-template\n"
        "version: 1.0.0\n"
        "lang: en\n"
        "title: Sample evidence template\n"
        "template_kind: form\n"
        "applies_to_method: sample@1.0.0\n"
        "fields:\n"
        "  note:\n"
        "    type: textarea\n"
        "assistant:\n"
        "  guidance: Preserve provenance.\n"
        "generated: { by: codex/test, at: 2026-08-18T00:00:00Z }\n"
        "---\n"
        "# Sample evidence template\n\nFull form specification.\n",
        encoding="utf-8",
    )
    (repo / "methods" / "sample" / "evidence" / "index.md").write_text(
        "# Evidence\n\nComplete the "
        "[evidence template](../evidence-template.en.md).\n",
        encoding="utf-8",
    )


def test_method_tree_and_template_pages_preserve_catalog_contract(tmp_path: Path) -> None:
    write_fixture(tmp_path)
    builder = load_builder()
    builder.ROOT = tmp_path.resolve()
    builder.OUT = builder.ROOT / "site"
    builder.render_markdown = lambda text: builder.LINK_RE.sub(
        lambda match: f'<a href="{match.group(2)}">{match.group(1)}</a>', text
    )

    assert builder.build() == 0

    method_page = builder.OUT / "methods" / "sample" / "index.html"
    template_page = builder.OUT / "methods" / "sample" / "evidence-template.html"
    evidence_page = builder.OUT / "methods" / "sample" / "evidence" / "index.html"
    redirect_page = builder.OUT / "methods" / "sample.html"
    assert method_page.is_file()
    assert template_page.is_file()
    assert evidence_page.is_file()
    assert redirect_page.is_file()

    method_html = method_page.read_text(encoding="utf-8")
    template_html = template_page.read_text(encoding="utf-8")
    assert 'href="evidence-template.html"' in method_html
    assert 'href="evidence/index.html"' in method_html
    assert '../../assets/style.css' in method_html
    assert "Full form specification." in template_html

    evidence_html = evidence_page.read_text(encoding="utf-8")
    assert 'href="../evidence-template.html"' in evidence_html
    assert '../../../assets/style.css' in evidence_html

    methods_html = (builder.OUT / "methods" / "index.html").read_text(encoding="utf-8")
    landing_html = (builder.OUT / "index.html").read_text(encoding="utf-8")
    assert 'href="sample/index.html"' in methods_html
    assert 'href="methods/index.html"' in landing_html

    redirect_html = redirect_page.read_text(encoding="utf-8")
    assert "url=sample/index.html" in redirect_html

    catalog = json.loads((builder.OUT / "catalog.json").read_text(encoding="utf-8"))
    assert [entry["id"] for entry in catalog] == ["sample"]
    assert "methods/sample/evidence-template.en.md" not in builder.CONCEPT_PAGES
    assert (
        builder.TEMPLATE_PAGES["methods/sample/evidence-template.en.md"]
        == "methods/sample/evidence-template.html"
    )
