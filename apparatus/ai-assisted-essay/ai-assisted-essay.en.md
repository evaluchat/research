---
type: Apparatus
id: ai-assisted-essay
lang: en
origin: native
status: draft
version: 0.1.0
min_canvas_version: "0.5.9"
title: AI-assisted essay — constrained dialogic drafting (CAMDLE)
description: "Apparatus #1: a constrained dialogic drafting assignment where drafting support is gated behind dialogic contribution. Investigates threshold-calibration and the evidential value of the AI chat transcript for student engagement."
tags: [apparatus, camdle, essays, threshold, engagement-evidence]
research_questions: [threshold-calibration]
question: "Does the AI chat transcript provide sufficient traceable evidence of student engagement with an assignment to validate it as an activity with academic merit if the AI is allowed to contribute to the canvas content?"
roles: [student, teacher, org-admin]
required_capabilities: [assignment-context, student-authoring, submission, ai-dialogue, ai-canvas-actions, drafting-gate, process-tracking]
knobs:
  - id: ai_assistance
    type: boolean
    default: true
    effect: Whether the assignment may call an AI agent.
  - id: ai_canvas_actions
    type: boolean
    default: true
    requires: { ai_assistance: true }
    effect: Whether AI generation and edit actions are available on the canvas.
  - id: drafting_gate
    type: enum
    values: [none, discussion-first, thesis-approved]
    default: discussion-first
    effect: The policy controlling when drafting assistance becomes available.
  - id: threshold
    type: integer
    min: 0
    max: 100
    default: 4
    effect: Visible student contributions before the escape hatch.
  - id: tracking
    type: boolean
    default: true
    effect: Whether process telemetry is captured and displayed.
telemetry: [process_signals, transcript, output]
provenance:
  sources:
    - id: essays-workflow
      resource: https://github.com/evaluchat/knowledge/blob/main/concepts/essays-workflow.en.md
      title: Essays workflow — proportional drafting unlock
profiles:
  - id: canonical-constrained-dialogue
    version: 1.0.0
    label: Canonical constrained dialogue
    description: Production-parity Essays workflow with a four-message escape hatch.
    author: evaluchat
    immutable: true
    configuration: { ai_assistance: true, ai_canvas_actions: true, drafting_gate: discussion-first, threshold: 4, tracking: true }
  - id: gate-off
    version: 1.0.0
    label: Drafting gate off
    description: AI assistance without a thesis gate.
    author: evaluchat
    immutable: true
    configuration: { ai_assistance: true, ai_canvas_actions: true, drafting_gate: none, threshold: 0, tracking: true }
  - id: ai-off
    version: 1.0.0
    label: Authoring without AI
    description: Assignment context, local authoring, and submission without agent calls.
    author: evaluchat
    immutable: true
    configuration: { ai_assistance: false, ai_canvas_actions: false, drafting_gate: none, threshold: 0, tracking: true }
  - id: canvas-actions-off
    version: 1.0.0
    label: Dialogue without canvas actions
    description: AI dialogue remains available while AI generation and edits are disabled.
    author: evaluchat
    immutable: true
    configuration: { ai_assistance: true, ai_canvas_actions: false, drafting_gate: discussion-first, threshold: 4, tracking: true }
  - id: tracking-off
    version: 1.0.0
    label: No process tracking
    description: Canonical workflow without process telemetry capture or display.
    author: evaluchat
    immutable: true
    configuration: { ai_assistance: true, ai_canvas_actions: true, drafting_gate: discussion-first, threshold: 4, tracking: false }
catalog_urls:
  spec: https://github.com/evaluchat/research/blob/main/apparatus/ai-assisted-essay/ai-assisted-essay.en.md
  evidence: https://github.com/evaluchat/research/tree/main/apparatus/ai-assisted-essay/evidence
  questions:
    - https://github.com/evaluchat/research/blob/main/theory/threshold-calibration.en.md
generated: { by: evaluchat-continuation, at: 2026-08-10T10:30:00Z }
sources:
  - id: essays-workflow
    resource: https://github.com/evaluchat/knowledge/blob/main/concepts/essays-workflow.en.md
    title: Essays workflow — proportional drafting unlock (knowledge catalog)
  - id: research-apparatus-concept
    resource: https://github.com/evaluchat/knowledge/blob/main/concepts/research-apparatus.en.md
    title: Research apparatus — reproducible research on Canvas (knowledge catalog)
  - id: apparatus-method
    resource: https://github.com/evaluchat/research/blob/main/methods/apparatus.en.md
    title: The apparatus as research instrument (research catalog)
---

# AI-assisted essay — constrained dialogic drafting (CAMDLE)

> `status: draft`. Apparatus #1: the Essays assignment flow as a research apparatus. The drafting-unlock
> constraint turns a pedagogical design (CAMDLE) into a measurable intervention; the AI chat transcript
> is collected as candidate engagement evidence. See [CAMDLE — constrained AI-mediated dialogic writing (theory, unproven)](../../theory/camdle.en.md) for the construct, [Threshold calibration — what counts as sufficient dialogic contribution?](../../theory/threshold-calibration.en.md) for the central research question, and the [instrument view](../../methods/apparatus.en.md) for how measurement and evidence relate.

## Research question

> Does the AI chat transcript provide sufficient traceable evidence of student engagement with an
> assignment to validate it as an activity with academic merit if the AI is allowed to contribute
> to the canvas content?

This apparatus serves the [threshold-calibration] question family: the drafting-unlock threshold is a
research variable (see [knobs](#knobs)), and the transcript + process signals are the evidence substrate
for the engagement question above.

## Platform requirement

- `min_canvas_version: 0.5.9` — requires the Canvas platform to expose: markdown canvas with configurable
  edit permissions, an optional AI chat panel with configurable system prompt and constraints, the
  drafting gate policy, and the telemetry surfaces listed below. If a knob has no platform surface in
  the running version, the apparatus must run with the closest supported value and record the deviation
  in evidence provenance.

## Knobs

| Knob | Values | Default | Notes |
|---|---|---|---|
| `ai_assistance` | true, false | true | whether agent calls are allowed |
| `ai_canvas_actions` | true, false | true | whether AI can generate or edit canvas content |
| `drafting_gate` | none, discussion-first, thesis-approved | discussion-first | the contribution→drafting unlock policy |
| `threshold` | integer 0–100 | 4 | visible contributions before the escape hatch |
| `tracking` | true, false | true | whether process telemetry is captured and displayed |

Profiles are immutable treatment records. Teachers select one enabled profile;
they do not edit these values in the assignment form. Existing assignments
retain their resolved snapshot if a newer profile is published.

## Telemetry

| Stream | Records | Evidence use |
|---|---|---|
| `process_signals` | keystroke bursts, paste volume, canvas edit types | engagement intensity, authoring patterns |
| `transcript` | full LLM agent conversation | candidate traceable evidence of engagement |
| `output` | final submission | outcome comparison across configurations |

Boundary: process evidence is **not** authorship detection and yields **no integrity score** — see the
[essays-workflow] concept for the shipped behaviour.

## Evidence collection

Evidence for this apparatus lives under [evidence/](evidence/index.md) — one collection per apparatus,
with each contribution bundle recording `apparatus: {id, version, configuration}` and `canvas: {version}`
in provenance (see the [instrument view](../../methods/apparatus.en.md) and the
[evidence-bundle template](../../templates/evidence-bundle/index.md)).

## Status

- `status: draft` — spec version 0.1.0; platform 0.5.9 ships the constrained flow (see [essays-workflow]).
- No evidence contributions yet. Threshold-calibration experiments may pre-register configurations here.

[threshold-calibration]: https://github.com/evaluchat/research/blob/main/theory/threshold-calibration.en.md
[essays-workflow]: https://github.com/evaluchat/knowledge/blob/main/concepts/essays-workflow.en.md
