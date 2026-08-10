# Research Catalog — Update Log

## 2026-08-10
* **Apparatus structure (rev 2)**: Added `apparatus/` directory — `apparatus/ai-assisted-essay/ai-assisted-essay.en.md` (type: Apparatus, spec as frontmatter: version 0.1.0, min_platform 0.5.9, research_questions, roles, knobs, telemetry, sources) + `apparatus/index.md` registry + `apparatus/ai-assisted-essay/evidence/index.md` (one evidence collection per apparatus — structural). Evidence registry now points to per-apparatus collections (`apparatus/<id>/evidence/`); CONTRIBUTING evidence-contribution path updated; root index gains Apparatus section.

## 2026-08-09
* **Addition**: Added `methods/apparatus.en.md` (Reference, draft) — the instrument view of a research apparatus: dialogic contribution as a measured quantity, process signals at the abstraction level (no telemetry blueprints), the threshold as a research variable, measurement/observation/evidence separation, configuration-in-provenance (`apparatus: {id, version, configuration, canvas}`), and how evidence bundles cite apparatus identity.
* **Templates**: `templates/evidence-bundle/provenance.md` gained an optional `apparatus:` configuration block (id, version, configuration, canvas) with instructions; `templates/evidence-bundle/index.md` listing note updated.
* **Cross-links**: Added "Research apparatus" section to `theory/camdle.en.md` and Related entries in `theory/threshold-calibration.en.md`, both pointing to `methods/apparatus.en.md` and (via resource URL) the knowledge repo's `research-apparatus` concept.
