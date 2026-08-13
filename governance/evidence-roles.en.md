---
type: Reference
id: evidence-roles
lang: en
origin: native
status: draft
title: Shared evidence roles — how every method files a run
description: "Catalog convention for evidence: shared document roles, observation/inference separation, and provenance that cites method {id, version, levers, canvas}. Payload shape is pinned by each method version."
tags: [governance, evidence, methods, provenance]
generated: { by: cursor-grok/4.6, at: 2026-08-13T14:48:00Z }
sources:
  - id: research-method
    resource: https://github.com/evaluchat/knowledge/blob/main/concepts/research-method.en.md
    title: Research methods — how Methods use platform capabilities and levers (knowledge catalog)
  - id: contribution-ladder
    resource: https://github.com/evaluchat/research/blob/main/governance/contribution-ladder.en.md
    title: The contribution ladder — how teachers contribute to research
---

# Shared evidence roles — how every method files a run

> `status: draft`. These roles apply to every published method. They are catalog convention, not a measurement schema. Each method version pins its own payload (what `results` actually contains) in `methods/<id>/evidence-template/`.

A **Method** is a versioned, profiled way of investigating a research question. Evaluchat applies a method profile in a workspace. When a run concludes, evidence is filed under that method — never in a second, catalog-wide evidence cabinet.

Findings may *cite* several methods; they do not *own* evidence. Evidence belongs to exactly one method, at `methods/<id>/evidence/<slug>/`.

## Shared roles (every method)

| Role file | What it holds | What it must not hold |
|---|---|---|
| `question` | The research question that predates this run | A question invented after the data |
| `context` | Setting, learners, subject, language, n, duration | Student identifiers |
| `intervention` | What the method actually did this run (task, resolved levers, instructions, deviations) | Interpretation of outcomes |
| `observations` | Teacher/researcher narrative of what happened (verbatim, any language) | Causal claims |
| `results` | Structured measurements only — shape pinned by the method version | Interpretation |
| `reflection` | Interpretation of observations and results | New undeclared measures presented as primary results |
| `limitations` | Scope, confounders, missing data, competing explanations | Softening of a claim that belongs in a finding |
| `provenance` | Sources, consent/anonymisation, and `method: {id, version, levers, canvas}` | Raw student material |

Observation and measurement are not interpretation. A claim ("students who spent 12 minutes learned more") is neither: it requires the findings machinery and the [contribution ladder](contribution-ladder.en.md).

Every bundle carries a `stage:` naming its ladder rung. Post-hoc analyses are labelled exploratory.

## Provenance: cite the method, not a global format

Two runs of the same method version are comparable only when the resolved levers are recorded. Same method version + different lever values = different intervention.

```yaml
method:
  id: ai-assisted-essay
  version: 0.1.0
  levers:
    threshold: 3
    drafting_gate: discussion-first
    ai_assistance: true
  canvas:
    version: 0.5.9
```

Rules:

1. **Always cite `id` + `version`.** The method version is the behaviour and evidence contract. Never substitute the Canvas version for it; they are independent.
2. **Record `levers` whenever the method exposes them.** A bundle without resolved levers is comparable only at the version level.
3. **Record `canvas.version`** so the substrate is identifiable, separately from the method version.
4. **Link the research question** the method was configured to investigate, so direction-of-fit machinery can verify the question predates the evidence.

The evidence graph is `Question → Method → Version → Levers → Intervention → Evidence`. An evidence bundle that cites a method version or lever set that did not exist when the question was registered is a red flag, not an ordinary submission.

## Privacy

Raw student material is never committed. A public artifact requires a consent and anonymisation record in `provenance`. If data cannot be public, say exactly what cannot be reproduced and provide the strongest lawful substitute (synthetic fixtures, data dictionary, restricted-access note).

Participants produce activity inside Evaluchat; a teacher or researcher submits the anonymised evidence PR. Students do not file raw work into this catalog.

## Where the payload lives

Do not treat these shared roles as if every method measured the same thing. Essays, the stress test, and revision-tracking produce different payloads on purpose. Copy the method version's `evidence-template/` when filing a run. If the measures change, bump the method version.

Until Evaluchat can generate the document at "Ready to conclude", humans fill the same template by hand. The catalog shape does not wait on that product work.
