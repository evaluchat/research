---
type: Method
id: ai-assignment-stress-test
lang: en
origin: native
status: draft
version: 0.1.0
min_canvas_version: "0.5.9"
title: AI Assignment Stress Test — assignment-level measurement analysis
description: "Method: a teacher-facing, assignment-level stress test that probes what current AI can do, maps what the task measures, identifies delegation loss, and offers alternative designs without requiring AI prohibition."
tags: [method, assessment, measurement-validity, ai, stress-test, teacher-tool]
timestamp: 2026-08-11T09:41:42Z
research_questions: [ai-assignment-stress-test-validity]
question: "To what extent, and under which task conditions, do standardized AI stress-test probes provide valid, reliable, and useful evidence about the human capabilities an assignment can still measure when generative AI is available?"
roles: [teacher, org-admin]
required_capabilities: [input-artefact-analysis, multi-model-probing, capability-mapping, redesign-generation, assignment-reporting]
levers:
  - id: model_set
    type: string
    default: stress-test-v0.1
    effect: The immutable, version-pinned model set used for comparable task-completion probes.
  - id: ai_mode
    type: enum
    values: [chat-only, constrained, full]
    default: full
    effect: How the probing AI may act; full permits the completion probe to attempt the task as a capable student would.
  - id: drafting_gate
    type: enum
    values: [none, discussion-first, thesis-approved]
    default: none
    effect: Reserved shared vocabulary for a future Canvas workflow; it has no effect in the teacher-only stress test.
  - id: mode_coverage
    type: array
    values: [A, B, C, D, E, F]
    default: [A, B, C, D, E, F]
    effect: The AI-use modes included in the probe and delegation analysis.
  - id: rubric_input
    type: enum
    values: [none, pasted-rubric]
    default: none
    effect: Whether a supplied rubric is used to report rubric-pass rather than descriptive quality only.
  - id: capability_focus
    type: array
    values: [closed-book-recall, unaided-production, ai-assisted-performance, error-detection, explanation, transfer, adaptation, argument-defence, ai-judgement, delayed-retention]
    default: [closed-book-recall, unaided-production, ai-assisted-performance, error-detection, explanation, transfer, adaptation, argument-defence, ai-judgement, delayed-retention]
    effect: The subset of multi-dimensional outcomes mapped by the measure stage.
  - id: redesign_count
    type: integer
    min: 2
    max: 5
    default: 3
    effect: The number of alternative task designs generated in the report.
  - id: telemetry
    type: enum
    values: [report]
    default: report
    effect: Records assignment-level stage outputs in the report only; no learner-level telemetry is collected.
telemetry: [report]
provenance:
  sources:
    - id: ai-assignment-stress-test-design
      resource: https://github.com/evaluchat/knowledge/blob/main/okf/bundles/evaluchat/concepts/ai-assignment-stress-test.md
      title: AI Assignment Stress Test — method design
profiles:
  - id: canonical-all-modes
    version: 1.0.0
    label: Canonical all-modes stress test
    description: Teacher-facing assignment analysis using the version-pinned model set, all AI-use modes, the full outcomes vocabulary, and three redesign alternatives.
    author: evaluchat
    immutable: true
    configuration: { model_set: stress-test-v0.1, ai_mode: full, drafting_gate: none, mode_coverage: [A, B, C, D, E, F], rubric_input: none, capability_focus: [closed-book-recall, unaided-production, ai-assisted-performance, error-detection, explanation, transfer, adaptation, argument-defence, ai-judgement, delayed-retention], redesign_count: 3, telemetry: report }
catalog_urls:
  spec: https://github.com/evaluchat/research/blob/main/methods/ai-assignment-stress-test/ai-assignment-stress-test.en.md
  evidence: https://github.com/evaluchat/research/tree/main/methods/ai-assignment-stress-test/evidence
  questions:
    - https://github.com/evaluchat/research/blob/main/theory/ai-assignment-stress-test-validity.en.md
generated: { by: cursor-grok/4.6, at: 2026-08-13T14:48:00Z }
sources:
  - id: ai-assignment-stress-test-design
    resource: https://github.com/evaluchat/knowledge/blob/main/okf/bundles/evaluchat/concepts/ai-assignment-stress-test.md
    title: AI Assignment Stress Test — method design (knowledge catalog)
  - id: research-method
    resource: https://github.com/evaluchat/knowledge/blob/main/concepts/research-method.en.md
    title: Research methods — how Methods use platform capabilities and levers (knowledge catalog)
  - id: evidence-roles
    resource: https://github.com/evaluchat/research/blob/main/governance/evidence-roles.en.md
    title: Shared evidence roles — how evidence cites a method (research catalog)
---

# AI Assignment Stress Test — assignment-level measurement analysis

> `status: draft`. This method is a design specification, not an implementation. It is a
> teacher-side instrument for analysing an assignment as written; it is not a learner workflow,
> a submission surface, or an AI-use detector. It applies the [shared evidence roles](../../governance/evidence-roles.en.md)
> to the assignment side of the measurement-validity question.

## Research question

This method serves [AI assignment stress-test validity — when can task probes identify what an
assessment still measures?](../../theory/ai-assignment-stress-test-validity.en.md). The question
evaluates the validity, reliability, and consequences of this assignment-level method; it does not
ask whether a student used AI or whether AI can be detected in student work.

Its secondary analyses concern expert agreement with the capability map, probe stability, delegation
loss across Modes A–F, and the costs and consequences of redesign alternatives. The Essays method's
[threshold-calibration](../../theory/threshold-calibration.en.md) is the student-side counterpart:
both instruments ask what a workflow actually measures when AI is available, from opposite ends of
the assignment.

## Instrument and boundary

The teacher supplies an assignment prompt and, optionally, its rubric, criteria, and expected
artefact. The method returns a structured assignment-level report. Its workflow is:

`input task` → `probe` → `measure` → `delegate analysis` → `redesign` → `report`

| Stage | What it does | Output |
|---|---|---|
| Input task | Receives the teacher-authored assignment artefact and optional rubric. | Structured task and rubric input. |
| Probe | Has each pinned model attempt the task as a capable student would, beginning with Mode A and optionally covering Modes B–F. | Per-model `task_completable`, `rubric_pass` when a rubric exists, and `modes_vulnerable`. |
| Measure | Maps task demands to the multi-dimensional outcomes vocabulary and identifies what the task can still detect after the probes. | Capability and measurement-validity map. |
| Delegate analysis | Distinguishes capabilities delegation bypasses from those the task still exposes. | Mode-by-mode delegation-loss analysis. |
| Redesign | Produces several alternatives that preserve the task's intent while exposing understanding. | Alternatives with their measurements and costs. |
| Report | Packages the stage outputs and exact configuration for review or optional evidence publication. | Assignment-level structured report. |

This is explicitly **not** authorship scoring, an academic-integrity verdict, or a detector of
AI use in submitted work. It analyses the task, never an individual student. It collects no
learner transcripts, process signals, submissions, or learner-level telemetry.

## Platform requirement

`min_canvas_version: 0.5.9` adopts the shared lever vocabulary. The five declared required
capabilities describe the additional teacher-side platform surface this draft needs: input-artefact
analysis, multi-model comparison, capability mapping, redesign generation, and assignment-level
reporting. They are requirements for a future Canvas implementation, not a claim that the current
platform implements or executes this method.

The method uses the recipe's deliberate divergence: it needs neither class management nor a
student workspace, managed submission, drafting gate, or student defence. That divergence is part
of the experiment's design, not a missing student workflow.

## Levers and profile

`model_set` is pinned by method version. Results are comparable only within the same pinned
model set, method version, and resolved configuration. The `canonical-all-modes` profile is an
immutable treatment record for the complete teacher-side analysis; before any execution, its
`stress-test-v0.1` model-set identifier must resolve to a published fixed model list.

| Lever | Default | Meaning |
|---|---|---|
| `model_set` | `stress-test-v0.1` | Version-pinned models that attempt the task. |
| `ai_mode` | `full` | Permitted behaviour for the probing AI. |
| `mode_coverage` | Modes A–F | AI-use modes included in the probe. |
| `rubric_input` | `none` | Whether rubric-pass can be reported. |
| `capability_focus` | all outcomes | Outcomes included in the measurement map. |
| `redesign_count` | `3` | Alternatives to include in the report. |
| `telemetry` | `report` | Assignment-level stage outputs only. |

`drafting_gate` is retained as reserved shared vocabulary with the value `none`; it has no effect
in this teacher-only workflow.

## Measurement and report

The report names the model set, method version, resolved levers, and Canvas version.
It records what the configured workflow produced; a published report is an assignment-level
observation, not a finding and not a universal statement about task quality. The redesign section
offers alternatives rather than one asserted best design, and identifies the teacher effort,
class time, marking load, and task complexity each alternative may cost.

## Evidence collection and privacy

Evidence lives in the method-owned [evidence collection](evidence/index.md). File a concluded
run using this version's [evidence-template/](evidence-template/index.md). Shared roles are in
[shared evidence roles](../../governance/evidence-roles.en.md); this version pins an
assignment-level report (probe, measure, delegate, redesign) — not learner telemetry. A report may be
published only at the teacher's option and only after the assignment has been appropriately
anonymised. Its provenance must record:

```yaml
method:
  id: ai-assignment-stress-test
  version: 0.1.0
  levers: # the resolved lever values, including the pinned model set
  canvas:
    version: <canvas-version>
```

The teacher's assignment is the sole input. Retention beyond the report requires the teacher's
opt-in publication decision; raw learner material does not belong in this method or its evidence
collection.

## Status and versioning

- `status: draft`; no Canvas implementation, completed probe, or evidence contribution exists.
- Method version `0.1.0` describes this design. A change to report semantics, the outcomes
  vocabulary, or a pinned model set is a comparability change and requires a method-version
  decision.
- The method version and Canvas version are independent and are both required in evidence
  provenance.
