# Theory/Finding `authors` Requirement — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Require a non-empty `authors` list (each entry a map with non-empty `name`) on every `Theory` and `Finding` concept, enforced by `okf_lint` on PRs targeting `main`.

**Architecture:** Extend the existing stdlib lint in `scripts/okf_lint.py` with a type-gated check. Document the rule in CONTRIBUTING/AGENTS/PR template. Backfill Finding fixtures. Narrow CI triggers to `main` only. `theory/camdle.en.md` already has authors — do not invent or rewrite them.

**Tech Stack:** Python 3.12 stdlib (`scripts/okf_lint.py`), GitHub Actions (`.github/workflows/ci.yml`), markdown/YAML frontmatter house conventions.

**Spec:** [docs/superpowers/specs/2026-08-13-theory-finding-authors-design.md](../specs/2026-08-13-theory-finding-authors-design.md)

## Global Constraints

- `authors` required only when `type` is exactly `Theory` or `Finding`
- Shape: non-empty list of maps; each map must have non-empty string `name`
- Extra keys on author entries are allowed; do not document or lint them yet
- Agents must not invent author names; leave for humans when unknown
- Do not edit human-set `authors` on `theory/camdle.en.md` (already populated)
- CI: PRs targeting `main` + pushes to `main`; remove `dev` trigger
- Set `generated.by` as `<producer>/<version>` only on files the agent substantively edits (not on camdle authors block)
- Never fabricate `verified: human:`

## File map

| File | Role |
| --- | --- |
| `scripts/okf_lint.py` | Enforce `authors` for Theory/Finding |
| `.github/workflows/ci.yml` | Gate: PRs → `main`, push → `main` |
| `CONTRIBUTING.md` | Document required field + template |
| `AGENTS.md` | Agent rule: do not invent authors |
| `.github/pull_request_template.md` | Checklist item |
| `scripts/tests/fixtures/scenario-*/findings/*.en.md` (5) | Synthetic `authors` backfill |
| `theory/camdle.en.md` | Already done — no change required for authors |
| `log.md` | Brief entry noting the convention |

---

### Task 1: Fail-first lint proof + implement `authors` check

**Files:**
- Modify: `scripts/okf_lint.py` (required-field block ~lines 292–330)
- Touch (verify only): `theory/camdle.en.md` (must already pass)
- Modify: five Finding fixtures under `scripts/tests/fixtures/`

**Interfaces:**
- Consumes: existing `meta` dict from `parse_simple_yaml`; `typ = meta.get("type")`
- Produces: new `ERROR:` lines when Theory/Finding `authors` invalid

- [ ] **Step 1: Confirm current lint passes (baseline)**

Run from repo root:

```bash
cd /home/cronjev/okf/research && python3 scripts/okf_lint.py
```

Expected: `OK: … files checked, 0 errors, … warnings` (or only pre-existing warnings). If errors exist unrelated to authors, stop and report them.

- [ ] **Step 2: Prove the gap (temporary failing case)**

Temporarily remove or comment out `authors` from `theory/camdle.en.md`, then:

```bash
python3 scripts/okf_lint.py
```

Expected today: still `OK` (no authors rule yet). Restore `authors` immediately after observing this — do not leave camdle broken. This step documents why the rule is needed; the real fail-first check is Step 3 after adding the rule before backfilling fixtures.

- [ ] **Step 3: Add the lint rule**

In `scripts/okf_lint.py`, inside the `else` branch that already checks `type` / `id` / `lang` / `description` (after the `description` check is fine), insert:

```python
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
```

Notes:
- Use the already-fetched `typ` variable; if you introduce `typ_s` earlier for emptiness checks, reuse it rather than duplicating.
- Do not require that unknown keys be absent.

- [ ] **Step 4: Run lint — expect Finding-fixture failures**

```bash
python3 scripts/okf_lint.py
```

Expected: `FAILED` with five (or more) errors like:

```text
ERROR: scripts/tests/fixtures/scenario-supported/findings/synth-finding-supported.en.md: type Finding requires a non-empty authors list
```

`theory/camdle.en.md` must **not** appear in the error list (authors already present).

- [ ] **Step 5: Backfill Finding fixtures**

Add the following block to the frontmatter of each of these files (after `type` or near other catalog fields; keep YAML valid):

- `scripts/tests/fixtures/scenario-provisional/findings/synth-finding-provisional.en.md`
- `scripts/tests/fixtures/scenario-tentative/findings/synth-finding-tentative.en.md`
- `scripts/tests/fixtures/scenario-supported/findings/synth-finding-supported.en.md`
- `scripts/tests/fixtures/scenario-challenge/findings/synth-finding-challenge.en.md`
- `scripts/tests/fixtures/scenario-dof-violation/findings/synth-finding-dof.en.md`

```yaml
authors:
  - name: Synthetic Fixture Author
```

- [ ] **Step 6: Run lint — expect pass**

```bash
python3 scripts/okf_lint.py
```

Expected: `OK: … files checked, 0 errors, …`

- [ ] **Step 7: Negative-check with a throwaway edit (optional but recommended)**

Copy camdle’s authors block aside, set `authors: []` briefly, run lint, confirm error mentions camdle, restore the human authors exactly as they were.

- [ ] **Step 8: Commit**

```bash
git add scripts/okf_lint.py \
  scripts/tests/fixtures/scenario-provisional/findings/synth-finding-provisional.en.md \
  scripts/tests/fixtures/scenario-tentative/findings/synth-finding-tentative.en.md \
  scripts/tests/fixtures/scenario-supported/findings/synth-finding-supported.en.md \
  scripts/tests/fixtures/scenario-challenge/findings/synth-finding-challenge.en.md \
  scripts/tests/fixtures/scenario-dof-violation/findings/synth-finding-dof.en.md
git commit -m "$(cat <<'EOF'
Require authors on Theory and Finding via okf_lint.

EOF
)"
```

Only commit if the user asked for a commit in this session; otherwise stage mentally and leave commit for the handoff report.

---

### Task 2: Narrow CI to `main`

**Files:**
- Modify: `.github/workflows/ci.yml`

**Interfaces:**
- Consumes: GitHub Actions `on:` triggers
- Produces: lint job only for PRs targeting `main` and pushes to `main`

- [ ] **Step 1: Replace the `on:` block**

Set `.github/workflows/ci.yml` to:

```yaml
name: okf-lint

on:
  pull_request:
    branches:
      - main
  push:
    branches:
      - main

jobs:
  okf-lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: Run OKF lint
        run: python3 scripts/okf_lint.py
```

Do **not** remove `dev` from `pages.yml` in this task unless the user has already merged/deleted `dev` and asked for that cleanup — pages deploy is out of the authors-spec success criteria. Optional follow-up: drop `dev` from `pages.yml` after branch deletion.

- [ ] **Step 2: Commit (if committing)**

```bash
git add .github/workflows/ci.yml
git commit -m "$(cat <<'EOF'
Gate okf-lint CI on PRs and pushes to main only.

EOF
)"
```

---

### Task 3: Document the house convention

**Files:**
- Modify: `CONTRIBUTING.md`
- Modify: `AGENTS.md`
- Modify: `.github/pull_request_template.md`
- Modify: `log.md` (newest-first entry)

**Interfaces:**
- Consumes: design schema text
- Produces: human/agent-facing required-field docs

- [ ] **Step 1: Update `CONTRIBUTING.md` required fields**

Under `### Required fields`, after the existing bullets, add:

```markdown
- **`authors` — REQUIRED for `Theory` and `Finding`** — non-empty list of maps; each entry must include a non-empty `name` string. Extra keys on an entry are allowed and currently unvalidated. Other types: optional / TBD.
```

In the Frontmatter template, add an `authors` example under the Theory template:

```yaml
authors:
  - name: Example Author
```

Update the PR checklist bullet about lint to mention Theory/Finding `authors`.

- [ ] **Step 2: Update `AGENTS.md`**

In **Contributing**, strengthen the existing “AI may not … list itself as author” line into an explicit numbered rule (or extend rule 9 checklist):

```markdown
- **`authors` on Theory/Finding** — required by lint. Never invent author names; never list the agent as an author. If authors are unknown, leave the field for a human (lint will fail until filled).
```

Also add `authors` to the house-convention checklist when `type` is Theory or Finding.

- [ ] **Step 3: Update `.github/pull_request_template.md` Checks**

Add:

```markdown
- [ ] Theory / Finding PRs: `authors` present with at least one `{ name: ... }` entry
```

Extend the lint checklist line to mention `authors` for those types.

- [ ] **Step 4: Append `log.md` entry (newest first)**

```markdown
## 2026-08-13

* **Authors required on Theory and Finding**: Catalog convention + `okf_lint` now require a non-empty `authors` list (each entry needs `name`). CI `okf-lint` runs on PRs/pushes to `main` only. See [design](docs/superpowers/specs/2026-08-13-theory-finding-authors-design.md).
```

Match whatever heading/date style `log.md` already uses.

- [ ] **Step 5: Final lint**

```bash
python3 scripts/okf_lint.py
```

Expected: `OK` with 0 errors.

- [ ] **Step 6: Commit (if committing)**

```bash
git add CONTRIBUTING.md AGENTS.md .github/pull_request_template.md log.md \
  docs/superpowers/specs/2026-08-13-theory-finding-authors-design.md \
  docs/superpowers/plans/2026-08-13-theory-finding-authors.md
git commit -m "$(cat <<'EOF'
Document Theory/Finding authors requirement and CI main gate.

EOF
)"
```

---

## Spec coverage checklist

| Spec requirement | Task |
| --- | --- |
| Schema: list of maps with `name` | Task 1 |
| Theory + Finding only | Task 1 |
| Extra keys allowed | Task 1 (no reject) |
| `okf_lint` ERROR | Task 1 |
| CI PRs to `main` / push `main`; drop `dev` | Task 2 |
| CONTRIBUTING / AGENTS / PR template | Task 3 |
| Backfill Finding fixtures | Task 1 |
| Leave camdle authors as human-set | Task 1 (no rewrite) |
