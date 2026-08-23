---
type: Form Template
id: evidence-template
lang: en
locale: en
origin: native
status: stable
version: 0.9.0
title: Ledger demo method — evidence packet (v0.9.0)
description: "Historical synthetic evidence packet for the ledger demo method: three ledger-dimension fields (education_level, country_code, sample_size) plus free-text context fields. Lacks collection_date."
tags: [evidence, form-template, ledger-demo-method, synthetic]
timestamp: 2026-08-19T14:57:46Z
template_kind: form
applies_to_method: ledger-demo-method@1.0.0
fields:
  education_level:
    type: select
    options: [k12, tertiary, adult, other, unknown]
    required: true
    ledger_dimension:
      role: context
      control: multi-select
    missing_semantics: unknown
  country_code:
    type: select
    options: [US, ZA, GB, NL, other, unknown]
    required: true
    ledger_dimension:
      role: context
      control: multi-select
    missing_semantics: unknown
  sample_size:
    type: number
    required: true
    ledger_dimension:
      role: context
      control: range
    missing_semantics: -1
  teacher_notes:
    type: textarea
    required: false
  run_comment:
    type: text
    required: false
  method_id:
    type: text
    required: true
    read_only: true
  method_version:
    type: text
    required: true
    read_only: true
generated: { by: "openrigor-hermes/1.0", at: 2026-08-19T14:57:46Z }
---

# Ledger demo method — evidence packet (v0.9.0)

Historical template version preceding the collection_date dimension. Packets filed against this version cannot supply a collection date, so a collection-date filter resolves them as Unavailable. Submitted packets store values under `field_values` using the declared field ids. `sample_size` uses numeric `missing_semantics: -1` as the recorded-unknown sentinel.
