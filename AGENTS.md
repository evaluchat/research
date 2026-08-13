# AGENTS.md — Agent Contract

Contract for agents that read or edit this catalog. Follow these rules in addition to [CONTRIBUTING.md](CONTRIBUTING.md). The catalog is a graph of typed, provenance-rich objects — not a folder of documents.

## Purpose

This catalog is a research layer, not a publication venue: open, versioned, auditable artifacts that academics can inspect, challenge, reuse, and extend. A public finding is downstream of a question, protocol, ethics decision, apparatus, data, analysis, and independent human review. Never imply that an internal observation, product telemetry, or AI-generated report is peer-reviewed research. No claim may be stronger than the design, evidence, provenance, and review supporting it.

Governing methods: [contribution ladder](methods/contribution-ladder.en.md), [review protocol](governance/review-protocol.en.md).

## Consuming

1. **Discover** — read `index.md`, then `catalog.json` (once built); filter by `type` / `tags` / `lang` / `status` / `stage`.
2. **Identity** — `id` is the stable concept identity; the filename is a representation; `id` + `lang` selects a representation.
3. **Language** — pick the requested `lang`; fall back to `en` for the same `id`; `origin` tells native vs translated.
4. **Trust** — derive trust from `verified` plus contribution `stage` and finding tier; `status: draft` means unproven. Distinguish product observation, documented experience, structured experiment, synthesis/finding, and peer-reviewed publication. Polished prose does not upgrade any of these.
5. **Epistemics** — observation ≠ inference ≠ claim; check the `observations` / `results` / `reflection` / `limitations` roles; a Finding requires its evidence chain, review record, and tier.
6. **Relationships** — traverse typed edges along the research chain: question → protocol/preregistration → ethics/consent → apparatus → intervention → data/analysis → evidence → independent human review → finding; then challenge, replication, or knowledge update. Do not skip ethics, apparatus identity, or review.
7. **Provenance** — cite `sources` plus `generated` / `verified`; attribute per claim. Record apparatus `{id, version, configuration}`, Canvas version, and data-sharing limits — including what cannot be independently reproduced.
8. **Missing translations** — never fabricate content; request the translation or fall back to another language of the same `id`.

## Contributing

AI may draft structure, check completeness, and prepare review packets. AI may not make ethical or scientific decisions, fabricate participants, data, quotations, results, or reviewer approval, or present a load-bearing claim. Humans remain accountable for consent, participant inclusion, interpretation, publication status, and any claim.

1. **Always set `generated.by` as `<producer>/<version>`** — every file you create or substantively edit records the producing agent and its version, e.g. `generated: { by: <producer>/<version>, at: 2026-08-09T00:00:00Z }`. Never omit the actor, never use a bare model name without a producer. Disclose model/provider when AI materially affected the artifact.
2. **Never fabricate `verified: human:`** — you cannot verify. Only a human sets `verified`; if it is absent, leave it absent. An AI-authored or AI-structured file without `verified` is machine-confirmed at best. `generated.by` never upgrades a trust tier or finding tier.
3. **Keep observation/inference separation** — observations and measurements are not interpretation. In evidence bundles: `observations.md` / `results.md` record what happened (no interpretation); `reflection.md` is interpretation; `limitations.md` states what we do not know and why. Never blend these roles. Label post-hoc analyses exploratory.
4. **Don't edit `verified` state or publication status** — never add, remove, or change a `verified` field set by a human; never promote a finding tier; never mark material as peer-reviewed. If you believe a verification or claim is wrong, open an issue or a challenge instead of editing.
5. **Human-only gates** — leave consent, participant inclusion, interpretation of results, publication status, and load-bearing claims for humans. Route causal language, commercially favourable findings, and challenges to independent human review. Do not describe product observations or proposals as demonstrating learning gains, treatment effects, or validated thresholds.
6. **Privacy** — never commit raw student material. Classroom data is private by default. A public artifact requires a consent/anonymisation record in `provenance.md`. If data cannot be public, say exactly what cannot be reproduced and provide the strongest lawful substitute (synthetic fixtures, data dictionary, restricted-access note).
7. **Do not hide uncertainty** — record null results, missing data, failed interventions, deviations, and competing explanations. Evidence must link a research question that predates it. Apparatus and protocol versions are immutable after data collection; amend via a new version and an explicit change record.
8. **Canvas vs research** — apparatus files specify method (question, version, capabilities, knobs, immutable profiles, telemetry, provenance). They never contain executable Canvas deployment code. Keep Canvas capability ownership separate from research method ownership.
9. **`authors` on Theory/Finding** — required by lint. Never invent author names; never list the agent as an author. If authors are unknown, leave the field for a human (lint will fail until filled).
10. **House-convention checklist** — before finishing any edit, confirm: frontmatter is English; `type` is non-empty and in the vocabulary; `id` is present and equals the filename slug; `lang` is present (BCP-47) and matches the filename suffix; filename follows `<slug>.<bcp47>.md` (including `.en.md`); `description` is present; `origin` is correct; for Theory/Finding, `authors` is a non-empty list with at least one `{ name: ... }` entry (human-set only); `translations` is never hand-maintained; missing translations are never fabricated — request or fall back.

Full convention, type vocabulary, and licensing terms: [CONTRIBUTING.md](CONTRIBUTING.md).
