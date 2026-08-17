---
type: Method
id: ai-assisted-essay
lang: en
origin: native
status: draft
version: 0.1.0
min_canvas_version: "0.5.9"
title: AI-assisted essay — constrained dialogic drafting (CAMDLE)
description: "Method: a constrained dialogic drafting assignment where drafting support is gated behind dialogic contribution. Investigates threshold-calibration and the evidential value of the AI chat transcript for student engagement."
tags: [method, camdle, essays, threshold, engagement-evidence]
research_questions: [threshold-calibration]
question: "Does the AI chat transcript provide sufficient traceable evidence of student engagement with an assignment to validate it as an activity with academic merit if the AI is allowed to contribute to the canvas content?"
roles: [student, teacher, org-admin]
required_capabilities: [assignment-context, student-authoring, submission, ai-dialogue, ai-canvas-actions, drafting-gate, process-tracking]
levers:
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
run_brief_template: evaluchat-assignment-brief@1.0.0
evidence_template: evidence-template@1.0.0
platform:
  participant_invitations: required
  review_surface: essay-process-review
catalog_urls:
  spec: https://github.com/evaluchat/research/blob/main/methods/ai-assisted-essay/ai-assisted-essay.en.md
  evidence: https://github.com/evaluchat/research/tree/main/methods/ai-assisted-essay/evidence
  questions:
    - https://github.com/evaluchat/research/blob/main/theory/threshold-calibration.en.md
generated: { by: cursor-grok/4.6, at: 2026-08-13T14:48:00Z }
sources:
  - id: essays-workflow
    resource: https://github.com/evaluchat/knowledge/blob/main/concepts/essays-workflow.en.md
    title: Essays workflow — proportional drafting unlock (knowledge catalog)
  - id: research-method
    resource: https://github.com/evaluchat/knowledge/blob/main/concepts/research-method.en.md
    title: Research methods — how Methods use platform capabilities and levers (knowledge catalog)
  - id: evidence-roles
    resource: https://github.com/evaluchat/research/blob/main/governance/evidence-roles.en.md
    title: Shared evidence roles — how evidence cites a method (research catalog)
---

# AI-assisted essay — constrained dialogic drafting (CAMDLE)

> `status: draft`. Method: the Essays assignment flow as a research method. The drafting-unlock
> constraint turns a pedagogical design (CAMDLE) into a measurable intervention; the AI chat transcript
> is collected as candidate engagement evidence. See [CAMDLE — constrained AI-mediated dialogic writing (theory, unproven)](../../theory/camdle.en.md) for the construct, [Threshold calibration — what counts as sufficient dialogic contribution?](../../theory/threshold-calibration.en.md) for the central research question, and the [shared evidence roles](../../governance/evidence-roles.en.md) for how measurement and evidence relate.

## Research question

> Does the AI chat transcript provide sufficient traceable evidence of student engagement with an
> assignment to validate it as an activity with academic merit if the AI is allowed to contribute
> to the canvas content?

This method serves the [threshold-calibration] question family: the drafting-unlock threshold is a
research variable (see [levers](#levers)), and the transcript + process signals are the evidence substrate
for the engagement question above.

## Platform requirement

- `min_canvas_version: 0.5.9` — requires the Canvas platform to expose: markdown canvas with configurable
  edit permissions, an optional AI chat panel with configurable system prompt and constraints, the
  drafting gate policy, and the telemetry surfaces listed below. If a lever has no platform surface in
  the running version, the method must run with the closest supported value and record the deviation
  in evidence provenance.

## Levers

| Lever | Values | Default | Notes |
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

## Measurement (this method version)

CAMDLE makes drafting support conditional on prior dialogic contribution. For this method,
"dialogic contribution" is a **measured quantity**: a count of the learner's contributions along
the dialogue-and-drafting workflow, aggregated per session, per phase, and per learner.

The quantity is defined by this method's *threshold* lever: which learner actions count, and how
many are required before drafting support unlocks. The concrete definition of a countable
contribution lives in this spec (not as a catalog-wide constant). **The threshold is a research
variable, not a design constant** — its calibration is the subject of [threshold-calibration].
The same method version with different threshold values runs materially different interventions.

Exactly which low-level signals feed the count is an implementation matter (the knowledge catalog's
[essays-workflow] concept describes the shipped process-signal categories). This spec describes
what is measured and why, not how the measurement machinery is built.

Process signals record categories of learner activity:

- **Composition activity** — how the learner's text is produced (typing, bursts, revisions).
- **Verbatim insertion** — pasted or copied content entering the document.
- **Engagement continuity** — focus, interruption, and time-in-phase patterns.

These categories are **observations about how work came together**; they are not authorship
detection, not integrity scores, and not evidence of learning. Signals are context for human
judgment, read alongside the transcript, the draft, and the assignment context.

| Term | What it is in this method | Example |
|---|---|---|
| **Method** | The configured Essays workflow under investigation | Dialogic constraint before drafting |
| **Intervention** | What this run actually did to the learner's workflow | Drafting unlocks after N dialogic contributions |
| **Measurement** | What this method records (mechanism, not evidence) | Process signals, transcript, output |
| **Evidence** | What can subsequently be filed under this method | "Student spent 12 min in Socratic phase" (observation) |

## Evidence contract (version 0.1.0)

Evidence lives under [evidence/](evidence/index.md). File a concluded run using this version's
[evidence template](evidence-template.en.md). Shared roles (question, observations vs results
vs reflection vs limitations, provenance) are rendered as sections of the single completed packet and are defined in
[shared evidence roles](../../governance/evidence-roles.en.md). This version pins the payload:

- **results** — process-signal summaries, transcript-policy record (what was retained vs withheld),
  and assignment outcome measures. Not an integrity score.
- **provenance** — `method: {id: ai-assisted-essay, version: 0.1.0, levers, canvas}`. Resolved
  levers must include `threshold`, `drafting_gate`, `ai_assistance`, `ai_canvas_actions`, and
  `tracking`.

If those measures change, bump this method version. Two runs of `ai-assisted-essay@0.1.0` are
comparable only when the resolved levers are recorded.

## Status

- `status: draft` — spec version 0.1.0; platform 0.5.9 ships the constrained flow (see [essays-workflow]).
- No evidence contributions yet. Threshold-calibration experiments may pre-register lever values here.

[threshold-calibration]: https://github.com/evaluchat/research/blob/main/theory/threshold-calibration.en.md
[essays-workflow]: https://github.com/evaluchat/knowledge/blob/main/concepts/essays-workflow.en.md
