---
type: Form Template
id: evidence-template
lang: en
locale: en
origin: native
status: stable
version: 1.0.0
title: Ledger demo method — evidence packet
description: "Synthetic evidence packet for the ledger demo method: four ledger-dimension fields (education_level, country_code, collection_date, sample_size) plus free-text context fields."
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
  collection_date:
    type: date
    required: true
    ledger_dimension:
      role: collection
      control: range
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
generated: { by: "evaluchat-hermes/1.0", at: 2026-08-19T14:57:46Z }
---

# Ledger demo method — evidence packet

This form template is the current (v1.0.0) packet shape for the ledger demo method. Submitted packets store values under `field_values` using the declared field ids. `sample_size` uses numeric `missing_semantics: -1` as the recorded-unknown sentinel. Select fields use `missing_semantics: unknown`.
