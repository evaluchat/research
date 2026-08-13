---
type: Reference
id: provenance
lang: en
title: Provenance — sources, consent, anonymisation (template)
description: Template — replace with one-line description
status: draft
---

# Provenance

<!-- TEMPLATE INSTRUCTIONS:
Traceability + ethics. Public export contains no student-identifiable text, transcripts, raw revision traces, or identity mapping.
-->

## Method (required)

```yaml
method:
  id: revision-tracking-validity
  version: 0.1.0
  levers:                 # resolved study levers (not a student-level profile dump)
    task_set: equivalent-task-set-v1
    randomisation_protocol: server-side-stratified-block-v1
    assessment_workflow: two-pass-assessor-blind-v1
    metrics_schema: revision-metrics-v1.0
    focus_telemetry: off
    data_minimisation_profile: counts-and-derived-metrics-v1
    outcome_reference: recorded-canvas-event-v1
    analysis_plan: revision-tracking-validity-analysis-v1
  canvas:
    version: 0.5.9
```

## Reproducibility packet

<!-- Replace: packet version, hashes, retention class. Link the shareable packet components; do not attach sealed mappings. -->

## Sources

<!-- Replace: protocol hash, metric-schema hash, analysis-plan hash. No raw traces. -->

## Consent record

<!-- Replace: ethics approval, consent/assent/guardian permission, withdrawal terms, grade-protection status. -->

## Anonymisation record

<!-- Replace: de-identification method, suppression rules, what cannot be reproduced from the public record. -->
