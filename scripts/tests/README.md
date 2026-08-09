# Claim-check fixtures (synthetic)

These fixtures prove the findings state machine. They are **not** real evidence and must never be copied into `findings/` or `evidence/` at the repo root.

Run from the repository root with the default `--repo-root` (cwd):

```bash
python3 scripts/okf_claim_check.py scripts/tests/fixtures/<scenario>/findings/
```

## Dry-run sequence

| # | Scenario | Expected `ROUTE` | What it proves |
| --- | --- | --- | --- |
| 1 | `scenario-provisional` | `auto-approve` | Provisional + complete bundle + direction-of-fit OK |
| 2 | `scenario-tentative` | `auto-approve` | Tentative with ≥2 `documented-experience` bundles from distinct contributors |
| 3 | `scenario-supported` | `needs-review` | Supported (confidence high) never auto-approves |
| 4 | `scenario-challenge` | `needs-review` | Open `challenged` marker on linked evidence |
| 5 | `scenario-dof-violation` | `needs-review` | Evidence `generated.at` predates its research question (`direction_of_fit` FAIL) |

Quick check of all five verdicts:

```bash
for s in scenario-provisional scenario-tentative scenario-supported scenario-challenge scenario-dof-violation; do
  echo "### $s"
  python3 scripts/okf_claim_check.py "scripts/tests/fixtures/$s/findings/" | grep -E '^(TIER|ROUTE):'
done
```

`workflow_dispatch` on `.github/workflows/claim-review.yml` runs this sequence and fails the job if any route differs from the table above.
