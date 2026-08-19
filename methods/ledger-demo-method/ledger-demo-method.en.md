---
type: Method
id: ledger-demo-method
lang: en
origin: native
status: stable
version: 1.0.0
min_canvas_version: "0.6.0"
title: Ledger demo method — synthetic evidence collection
description: "Synthetic method whose accepted evidence exercises every Evidence Ledger scope bucket (included, outside, unknown, unavailable, resolver exclusion). Used to verify the ledger configuration canvas and snapshots."
tags: [method, evidence-ledger, synthetic]
roles: [student, teacher, org-admin]
required_capabilities: [assignment-context, student-authoring, submission]
evidence_template: evidence-template@1.0.0
generated: { by: "evaluchat-hermes/1.0", at: 2026-08-19T14:57:46Z }
---

# Ledger demo method — synthetic evidence collection

This is a synthetic fixture method for Evidence Ledger verification. It is not a classroom investigation and has no real participants. Packets under [evidence/index.md](evidence/index.md) exercise the ledger buckets (included, outside declared scope, unknown, unavailable, resolver exclusion) against four ledger-dimension fields: `education_level`, `country_code`, `collection_date`, and `sample_size`.

The current packet shape is pinned by [evidence-template.en.md](evidence-template.en.md) (v1.0.0). A historical template without `collection_date` lives at [evidence-templates/evidence-template.en.md](evidence-templates/evidence-template.en.md) (v0.9.0) so that packets filed under that version resolve as unavailable when a collection-date filter is applied.
