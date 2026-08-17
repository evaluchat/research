# Contributing to the Research Catalog

Thank you for contributing. This is an open, multilingual, PR-able OKF (v0.2) research repository. Before opening a pull request or an issue, please read this document in full — it defines the house conventions that CI enforces and the terms under which your contribution is accepted.

## What belongs here

This repository holds **research truth**: research questions, hypotheses, theory, methods, evidence contributions, and tiered findings. Product documentation belongs in the [knowledge repository](https://github.com/evaluchat/knowledge). Internal strategy and competitive material never belongs in a public repository — strategic assumptions may enter this catalog only as explicit research questions, hypotheses, or shipped product truth.

## Type vocabulary

Every non-reserved file declares exactly one `type`:

`Method`, `Form Template`, `Theory`, `Research Question`, `Hypothesis`, `Intervention`, `Evidence Contribution`, `Observation`, `Measurement`, `Result`, `Reflection`, `Limitations`, `Finding`, `Synthesis`, `Replication`, `Challenge`, `Playbook`, `Reference`.

Method PRs must declare an immutable ID and semantic version, minimum Canvas
version, required capabilities, roles, telemetry, provenance, typed levers with
dependencies/exclusions, and immutable fully resolved profiles. Profiles must
leave students assignment context, an authoring surface, and submission. The
Canvas app executes only reviewed built-in implementations; a method PR
must never contain executable deployment code.

Form Template PRs define a versioned, non-executable input contract. Every
`Method` must declare `evidence_template: evidence-template@<version>` and carry the
corresponding single-file template at `methods/<method-id>/evidence-template.en.md`.
The template frontmatter declares the supported field types, requiredness, allowed
options, and protected assistant guidance; fields sourced from a concluded run are
read-only. Public evidence templates must keep system-authored measurements separate
from owner-authored observations and reflection, and require explicit publication
authorisation and anonymisation declarations. These method-local templates are
`template_kind: form`, not concepts: their shared `id: evidence-template` is exempt
from concept identity, description, vocabulary, and site-publication rules.

`scripts/okf_lint.py` enforces this evidence contract: it rejects a Method with no
pointer, an unreadable template, or a template whose version, method binding, typed
fields, language, provenance, or form kind does not match the contract. This is one
side of the two-sided publishing gate: the platform catalog also requires and mirrors
the same versioned template before a method can ship.

Reserved files (no frontmatter required): `index.md` (per-directory listing), `CHANGELOG.md` (update log), `README.md`, `AGENTS.md`.

## Multilingual house convention

### Two-layer split

| Layer | Where | Language |
|---|---|---|
| Catalog/machine layer | YAML frontmatter: `type`, `id`, `title`, `description`, `tags`, `lang`, `status`, `generated`, `verified`, `sources`, `origin` | **Always English** |
| Content layer | Markdown body (H1 onwards) | Any language, per `lang` |

English is the machine/catalogue language — **not** the epistemic source language. A teacher's native-language observations are first-class content, not "translations to be done"; the English summary is generated for discovery. Native-origin non-English content is authoritative in its own language.

### Required fields

- **`lang` — REQUIRED**, BCP-47 (`en`, `fr`, `es`, `pt-BR`, `zh-CN`, …). CI validates plausibility only (regex check, not RFC compliance).
- **`id` — REQUIRED**, stable, language-independent. The concept group's identity; the filename is merely one representation of it. CI validates that `id` equals the filename slug. `id` survives title changes, slug changes, splits, merges, and deprecations — agents never infer identity from stems.
- **`title` / `description` — REQUIRED, English** (index/snippet layer). Optional `title_local`: native display name.
- **`type` / `status`** — required per the type vocabulary and lifecycle values below.
- **`origin`** — `native` (default) = content originally authored in `lang`; `translation` = derived from another language's version.
- **`authors` — REQUIRED for `Theory` and `Finding`** — non-empty list of maps; each entry must include a non-empty `name` string. Extra keys on an entry are allowed and currently unvalidated. Other types: optional / TBD.

### Filename suffix rule (settled — not to be revisited)

All files use the uniform suffix `<slug>.<bcp47>.md` — **including English**: `camdle.en.md`, never bare `camdle.md`.

**Rationale:** with native-origin content, "bare filename = English" would make English the implicit default even when the English file is only the generated summary of a native Portuguese contribution. Uniform suffixes keep every language symmetric, and CI validates that the suffix matches `lang`.

### `translations` is derived metadata

Language lists are derived by tooling from `id` + `lang` across the tree (and emitted in `catalog.json`). Never hand-maintain a `translations` field — if present it is cache only, and CI may warn on asymmetry but never fails on it.

### Translation trust tiers

- Agent-generated translation → `generated: { by: <producer>/<version>, at: <ISO 8601> }` + `origin: translation` → **machine-confirmed** at best.
- Human-checked → add `verified: { by: human:<id>, at: <ISO 8601> }` → **human-reviewed**.
- Machine structuring can never masquerade as human review: `generated.by` never upgrades a trust tier.

### Lifecycle values

- Concepts: `status: draft | stable | deprecated`. `draft` means unproven — never present theory as established.
- Research questions: `status: open | investigating | answered | abandoned`.
- Evidence contributions: `stage:` names the contribution-ladder rung (observation → documented experience → structured experiment → replication/challenge → synthesis → finding).
- Findings: tier per the governance protocol (`provisional | tentative | supported`, plus `challenged | contested | amended | retracted`).

## Frontmatter template

```yaml
---
type: Theory
id: my-concept
title: Human-readable English title
description: One-line English summary, short enough for index listings.
tags: [tag1, tag2]
lang: en
origin: native
status: draft
authors:
  - name: Example Author
generated: { by: <producer>/<version>, at: 2026-08-09T00:00:00Z }
verified: { by: human:<id>, at: 2026-08-09T00:00:00Z }
sources:
  - id: source-id
    resource: https://github.com/evaluchat/research/blob/main/...
    title: Human-readable source title
---
```

## Evidence contributions

Each contribution is one completed packet under `methods/<method-id>/evidence/<slug>.md`,
rendered from that method version's `evidence-template.en.md` (evidence is organised
per method — one collection per method). The packet renders the shared roles in
[governance/evidence-roles.en.md](governance/evidence-roles.en.md): question, context,
intervention, observations (teacher narrative, verbatim, native origin), results
(structured measurements only — no interpretation; payload pinned by the method
version), reflection (interpretation), limitations (scope and confounders), and
provenance (sources plus consent/anonymisation record). Its system-authored provenance
must record `method: {id, version, levers, canvas}`.

- **Observation/inference separation is mandatory**: measurements and observations are not interpretation, and interpretation is not a claim.
- **Pre-registration**: every evidence bundle links a research question that predates the evidence. A contribution that "discovers" its question after the fact is a CI flag and goes to human review.
- **Consent/privacy**: raw student material is never committed. Only reviewed, appropriately anonymised artifacts with a consent record in `provenance.md`.

## Licensing terms for contributions

- **Content** (markdown, data): contributed under **CC-BY-4.0** (the repository `LICENSE`). On merge, your contribution is distributed under that license; attribution is preserved through git history and the `sources` / `verified` / `generated` fields.
- **Code** (scripts, tooling, CI): contributed under **MIT** (`LICENSE-CODE`).
- **Evidence**: submission requires the consent/privacy record described above; anonymisation is a condition of merge.
- By opening a pull request you confirm you have the right to contribute the material under these terms.

## PR checklist

Before opening a pull request:

- [ ] Type of change declared: **spec / translation / evidence / theory / methods / correction**
- [ ] Lint green (frontmatter parses; `type` / `id` / `lang` / `description` present; `id` == filename slug; filename suffix matches `lang`; Theory/Finding `authors` with at least one `{ name: ... }` entry; root `index.md` declares `okf_version`)
- [ ] Filename follows `<slug>.<bcp47>.md`, English included
- [ ] `generated.by` set to `<producer>/<version>` where applicable; no fabricated `verified: human:`
- [ ] For evidence PRs: observation/inference separation maintained, and the consent/privacy record present in `provenance.md`
- [ ] For method PRs: catalog validation passes and every profile has a viable student workflow

Use the pull request template (`.github/pull_request_template.md`) — it mirrors this checklist. Governance and spec changes are never auto-merged.
