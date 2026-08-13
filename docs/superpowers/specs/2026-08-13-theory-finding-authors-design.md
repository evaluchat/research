# Design: Required `authors` on Theory and Finding

**Status:** approved  
**Date:** 2026-08-13  
**Scope:** Research catalog house convention + `okf_lint` CI gate

## Problem

Theory and Finding documents are load-bearing attribution surfaces. Today they have no required author field; `camdle.en.md` (the only live Theory) and all Finding fixtures omit authorship. Agents must not invent authors (`AGENTS.md`), so the catalog needs an explicit, lint-enforced place for humans to declare them.

## Decision

Require a top-level `authors` list on every concept with `type: Theory` or `type: Finding`. Other types remain out of scope (TBD).

### Schema

```yaml
authors:
  - name: Monica van Heerden Doctor in Education
```

| Rule | Detail |
| --- | --- |
| When | `type` is exactly `Theory` or `Finding` |
| Shape | Non-empty YAML list of maps |
| Required per entry | Non-empty string `name` |
| Optional per entry | Any other keys allowed; not documented or validated yet (organic growth) |
| Reject | Missing `authors`, empty list, non-list, list items that are not maps, missing/empty `name` |

`authors` is catalog/machine-layer English frontmatter (same layer as `title` / `description`). It does not replace `generated` / `verified`; it names human (or organisational) intellectual authors of the theory or finding.

### Non-goals

- Requiring `authors` on Research Question, Hypothesis, Apparatus, Evidence, etc.
- Documenting or linting optional fields (`specialty`, `orcid`, `affiliation`, …)
- Rendering authors in the public site (follow-up if desired)
- Letting agents invent author names when unknown

## Enforcement

### Lint (`scripts/okf_lint.py`)

After existing required-field checks, when `type` is `Theory` or `Finding`:

1. Require `authors` present and a non-empty list.
2. For each item: require a mapping with `name` a non-empty string.
3. Emit `ERROR:` (not warning) so CI fails.

No change to the YAML parser beyond consuming the structure it already supports (indented lists of maps).

### CI gate

Workflow [`.github/workflows/ci.yml`](../../../.github/workflows/ci.yml) runs:

```bash
python3 scripts/okf_lint.py
```

**Scope (post-`dev` retirement):** trigger only on pull requests **targeting `main`**, and optionally on pushes to `main`. Do not keep a `dev` branch trigger. Adding the lint rule **is** the PR gate to `main`; no second workflow is required. Branch protection on `main` should require this check (ops concern; not a repo file change unless protection is missing).

Implementation note: today’s `ci.yml` still lists `dev` under `push.branches` and runs on PRs to any base — narrow it as part of this change.

### Docs / agent contract

- `CONTRIBUTING.md` — required-fields note for Theory/Finding; update frontmatter template example.
- `AGENTS.md` — agents must not invent `authors`; if unknown, leave the field for a human (and expect lint to fail until filled).
- PR checklist / template — Theory/Finding must include `authors` with at least one `name`.

## Backfill

| File | Action |
| --- | --- |
| `theory/camdle.en.md` | **Done** — `authors` already set (`Cronje van Heerden`; `Monica van Heerden, Doctor in Education, specialty: Language Education`) |
| `scripts/tests/fixtures/**/findings/*.en.md` (5 files) | Add synthetic author so lint stays green, e.g. `name: Synthetic Fixture Author` |
| Live `findings/` | None yet |

Fixtures under `scripts/` are currently walked by `okf_lint.py` (unlike `build_site.py`, which skips `scripts/`). Finding fixtures therefore need `authors` or CI fails.

## Success criteria

- [ ] Lint fails on Theory/Finding without valid `authors`
- [ ] Lint passes on the repo after backfill
- [ ] CONTRIBUTING + AGENTS + PR template updated
- [ ] CI runs `okf_lint` on PRs targeting `main` (and pushes to `main`); `dev` trigger removed; new authors rule covered
