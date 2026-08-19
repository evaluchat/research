# Synthetic ledger-demo-method fixtures

These fixtures contain no real participants and no classroom data. They exist only to verify the Evidence Ledger configuration canvas and snapshots.

- **p01–p06** — accepted packets with filter-friendly values (included under a typical k12/tertiary × US/ZA/GB/NL × 2024 × 60–240 filter).
- **p07–p08** — accepted packets with known values outside that plausible filter (`adult`; `country_code: other`).
- **p09** — accepted packet with recorded unknown (`education_level: unknown`).
- **p10** — accepted packet with omitted `country_code` (unknown by omission).
- **p11–p12** — accepted packets filed against template v0.9.0 (no `collection_date` → Unavailable when that dimension is filtered).
- **p13–p14** — resolver-exclusion probes (wrong `method.version`; `status: draft`).

Baseline accepted count for the method is 12 (p01–p12). Fixtures are not evidence of learning or efficacy.
