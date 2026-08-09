# AGENTS.md — Contributor-Agent Contract

Rules for AI-assisted contributors to this repository: Canvas "save as evidence" agents, coding copilots, and any agent that edits catalog files. If you are an agent, you MUST follow these rules in addition to [CONTRIBUTING.md](CONTRIBUTING.md).

1. **Always set `generated.by` as `<producer>/<version>`** — every file you create or substantively edit records the producing agent and its version, e.g. `generated: { by: <producer>/<version>, at: 2026-08-09T00:00:00Z }`. Never omit the actor, never use a bare model name without a producer.
2. **Never fabricate `verified: human:`** — you cannot verify. Only a human sets `verified`; if it is absent, leave it absent. An AI-authored or AI-structured file without `verified` is machine-confirmed at best.
3. **Keep observation/inference separation** — observations and measurements are not interpretation. In evidence bundles: `observations.md` / `results.md` record what happened (no interpretation); `reflection.md` is interpretation; `limitations.md` states what we do not know and why. Never blend these roles.
4. **Don't edit `verified` state** — never add, remove, or change a `verified` field set by a human. If you believe a verification is wrong, open an issue or a challenge instead of editing.
5. **House-convention checklist** — before finishing any edit, confirm: frontmatter is English; `type` is non-empty and in the vocabulary; `id` is present and equals the filename slug; `lang` is present (BCP-47) and matches the filename suffix; filename follows `<slug>.<bcp47>.md` (including `.en.md`); `description` is present; `origin` is correct; `translations` is never hand-maintained; missing translations are never fabricated — request or fall back.

Full convention, type vocabulary, and licensing terms: [CONTRIBUTING.md](CONTRIBUTING.md).
