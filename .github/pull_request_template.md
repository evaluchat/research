## Type of change

- [ ] **Spec** — change to house conventions, governance, or the review protocol
- [ ] **Translation** — new or updated translation of an existing concept
- [ ] **Evidence** — evidence contribution (mini-bundle under `evidence/`)
- [ ] **Theory** — theory, research question, or hypothesis content
- [ ] **Methods** — methodology or measurement definitions
- [ ] **Correction** — fix to existing content (errors, broken links, frontmatter)

## Description

<!-- What does this PR change and why? Link any related issues. -->

## Checks

- [ ] Lint green: frontmatter parses; `type` / `id` / `lang` / `description` present; `id` == filename slug; filename suffix matches `lang`; Theory/Finding `authors` with at least one `{ name: ... }` entry
- [ ] Theory / Finding PRs: `authors` present with at least one `{ name: ... }` entry
- [ ] Filename follows `<slug>.<bcp47>.md` (English included)
- [ ] `generated.by` set to `<producer>/<version>` where applicable; no fabricated `verified: human:`

## For evidence PRs

- [ ] Observation/inference separation maintained (`observations`/`results` vs `reflection`/`limitations`)
- [ ] Consent/privacy record present in `provenance.md`; no raw student material committed
