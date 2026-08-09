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
Traceability + ethics. Raw student material is never committed to this repository — only reviewed, anonymised artifacts with a consent record.
-->

## Apparatus configuration

<!-- OPTIONAL but strongly recommended: if this contribution ran inside a Canvas research apparatus, record the exact apparatus and configuration used. The apparatus version is the behaviour/evidence contract — NOT the canvas version; they are independent. Configuration matters because two runs of the same apparatus version with different settings (threshold, defense policy, AI modes) are materially different interventions. See methods/apparatus.en.md in this catalog for the instrument view, and concepts/research-apparatus.en.md in the knowledge catalog for the pattern.

Delete this whole section if the contribution did not run inside a research apparatus (e.g. ordinary classroom use without the essays workflow).
-->

```yaml
apparatus:
  id: essays              # apparatus id (e.g. essays)
  version: 0.5.9          # apparatus version — behaviour/evidence contract
  configuration:          # the ACTUAL configuration used in this run
    threshold: 3          # e.g. required dialogic contributions before drafting unlocks
    defense_required: true
    ai_modes: [socratic, critique]
  canvas:
    version: 0.5.9        # canvas version the apparatus ran on
```

## Sources

<!-- Replace: worksheets, conversation exports, drafts, or other artifacts this contribution draws on (anonymised, and only those you are permitted to share) -->

## Consent record

<!-- Replace: who approved what — institutional ethics approval, parental/guardian consent, student assent, data minimisation and retention terms. Say what consent covers and what it does not. -->

## Anonymisation record

<!-- Replace: what was removed or transformed to protect learners (names, school identifiers, voice/face data, distinctive phrasing), and who reviewed the anonymisation -->
