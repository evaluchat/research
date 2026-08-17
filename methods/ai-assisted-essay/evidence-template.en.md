---
type: Form Template
id: evidence-template
lang: en
locale: en
origin: native
status: draft
version: 1.0.0
title: AI-assisted essay — concluded-run evidence
description: "Versioned conclusion form for one AI-assisted essay run: frozen run provenance and structured teacher judgements that can be aggregated without presenting a single response as proof."
tags: [evidence, form-template, ai-assisted-essay, threshold-calibration, subjective-evidence]
timestamp: 2026-08-17T14:33:56Z
template_kind: form
applies_to_method: ai-assisted-essay@0.1.0
default_stage: documented-experience
question_id: threshold-calibration
fields:
  method_id:
    label: Method ID
    type: text
    required: true
    read_only: true
    source: frozen_run.method.id
  method_version:
    label: Method version
    type: text
    required: true
    read_only: true
    source: frozen_run.method.version
  run_reference:
    label: Run reference
    type: text
    required: true
    read_only: true
    source: frozen_run.workspace_item_guid
  profile_id:
    label: Resolved profile
    type: text
    required: true
    read_only: true
    source: frozen_run.profile.id
  resolved_levers:
    label: Resolved levers
    type: textarea
    required: true
    read_only: true
    source: frozen_run.levers
    max_length: 4000
    display_lines: 8
  canvas_version:
    label: Canvas version
    type: text
    required: true
    read_only: true
    source: frozen_run.canvas.version
  run_started_at:
    label: Run started
    type: date
    required: true
    read_only: true
    source: frozen_run.started_at
  run_concluded_at:
    label: Run concluded
    type: date
    required: true
    read_only: true
    source: frozen_run.concluded_at
  participant_count:
    label: Participant count
    type: number
    required: true
    read_only: true
    source: frozen_run.participant_count
    min: 0
    max: 100000
  eligible_owner_count:
    label: Eligible evidence contributors
    type: number
    required: true
    read_only: true
    source: collection.eligible_owner_count
    min: 0
    max: 100000
  invited_owner_count:
    label: Invited evidence contributors
    type: number
    required: true
    read_only: true
    source: collection.invited_owner_count
    min: 0
    max: 100000
  responded_owner_count:
    label: Submitted evidence contributors
    type: number
    required: true
    read_only: true
    source: collection.responded_owner_count
    min: 0
    max: 100000
  collection_opened_at:
    label: Evidence invitation opened
    type: date
    required: true
    read_only: true
    source: collection.opened_at
  collection_closed_at:
    label: Evidence submitted
    type: date
    required: true
    read_only: true
    source: collection.submitted_at
  dialogic_contribution_summary:
    label: Dialogic contribution summary
    type: textarea
    required: true
    read_only: true
    source: frozen_run.analytics.dialogic_contribution_summary
    max_length: 4000
    display_lines: 6
  drafting_gate_outcome:
    label: Drafting-gate outcome
    type: text
    required: true
    read_only: true
    source: frozen_run.analytics.drafting_gate_outcome
  process_signal_summary:
    label: Process-signal summary
    type: textarea
    required: true
    read_only: true
    source: frozen_run.analytics.process_signal_summary
    max_length: 4000
    display_lines: 6
  transcript_retention:
    label: Transcript retention record
    type: text
    required: true
    read_only: true
    source: frozen_run.provenance.transcript_retention
  assignment_outcome_summary:
    label: Assignment outcome summary
    type: textarea
    required: true
    read_only: true
    source: frozen_run.analytics.assignment_outcome_summary
    max_length: 4000
    display_lines: 6
  institution_type:
    label: Institution type
    type: select
    required: true
    options: [school, college-or-university, adult-education, tutoring-or-small-group, other, prefer-not-to-say]
  assignment_genre:
    label: Assignment genre
    type: select
    required: true
    options: [argumentative-essay, analytical-essay, literature-essay, reflective-essay, other-written-assignment, mixed-or-other]
  learner_proficiency_context:
    label: Learner proficiency context
    type: select
    required: true
    options: [primarily-beginner, primarily-developing, primarily-proficient, mixed, not-assessed-or-not-known]
  learner_age_band:
    label: Learner age band
    type: select
    required: true
    options: [under-13, 13-to-15, 16-to-18, 19-to-24, 25-or-over, mixed, prefer-not-to-say]
  instruction_language:
    label: Primary language of instruction
    type: text
    required: true
    max_length: 120
    display_chars: 32
  writing_language:
    label: Primary language of writing
    type: text
    required: true
    max_length: 120
    display_chars: 32
  implementation_duration:
    label: Implementation duration
    type: text
    required: true
    max_length: 160
    display_chars: 48
  class_and_task_context:
    label: Class and task context
    type: textarea
    required: true
    max_length: 2000
    display_lines: 6
  assignment_public_summary:
    label: Public summary of the assignment
    type: textarea
    required: true
    max_length: 1200
    display_lines: 4
  implementation_deviation:
    label: Deviation from the frozen method run
    type: textarea
    required: true
    max_length: 1600
    display_lines: 5
  threshold_fit:
    label: Fit of the configured contribution threshold
    type: select
    required: true
    options: [much-too-low, somewhat-too-low, about-right, somewhat-too-high, much-too-high, insufficient-information, not-applicable-gate-disabled]
  threshold_fit_explanation:
    label: Threshold-fit explanation
    type: textarea
    required: true
    max_length: 2000
    display_lines: 6
  process_evidence_usefulness:
    label: Usefulness of the process evidence for this assignment
    type: select
    required: true
    options: [not-at-all-useful, slightly-useful, moderately-useful, very-useful, extremely-useful, insufficient-information, not-applicable]
  process_evidence_explanation:
    label: Process-evidence explanation
    type: textarea
    required: true
    max_length: 2000
    display_lines: 6
  review_burden:
    label: Perceived review burden
    type: select
    required: true
    options: [none, low, moderate, high, unacceptable, insufficient-information]
  learner_response_to_gate:
    label: Observed class response to the contribution-before-drafting constraint
    type: select
    required: true
    options: [strongly-negative, somewhat-negative, mixed-or-no-consistent-pattern, somewhat-positive, strongly-positive, insufficient-information, not-applicable-gate-disabled]
  future_use_intention:
    label: Intention to use this configuration again in a comparable assignment
    type: select
    required: true
    options: [definitely-would-not, probably-would-not, unsure, probably-would, definitely-would, not-applicable]
  narrative_observations:
    label: Observations from the concluded run
    type: textarea
    required: true
    max_length: 4000
    display_lines: 10
  missing_data:
    label: Missing or unavailable data
    type: textarea
    required: true
    max_length: 1600
    display_lines: 5
  reflection:
    label: Reflection and next-step interpretation
    type: textarea
    required: true
    max_length: 3000
    display_lines: 8
  limitations:
    label: Limitations and competing explanations
    type: textarea
    required: true
    max_length: 3000
    display_lines: 8
  contribution_stage:
    label: Declared contribution stage
    type: select
    required: true
    options: [documented-experience, structured-experiment, replication, challenge]
  publication_authorisation:
    label: Public contribution authorisation
    type: select
    required: true
    options: [confirmed-authorised-to-publish, not-confirmed-do-not-submit]
  anonymisation_status:
    label: Anonymisation status
    type: select
    required: true
    options: [confirmed-no-student-identifiers-or-raw-student-material, needs-human-privacy-review, not-ready-for-publication]
  data_sharing_limits:
    label: Public data-sharing limits
    type: textarea
    required: true
    max_length: 1600
    display_lines: 5
assistant:
  guidance: "Help the owner describe only their concluded run. Never infer, invent, or expose student information, raw student work, raw transcripts, or consent. Render the frozen system-authored fields exactly as provided; never alter, duplicate, or add system measurements. Keep observations factual and separate from reflection; describe perceptions as perceptions, not proof of learning, engagement, effectiveness, or the views of teachers beyond this response. A response that is not authorised or not anonymised must not be submitted for public publication."
generated: { by: codex/gpt-5, at: 2026-08-17T14:33:56Z }
sources:
  - id: ai-assisted-essay
    resource: https://github.com/evaluchat/research/blob/main/methods/ai-assisted-essay/ai-assisted-essay.en.md
    title: AI-assisted essay — constrained dialogic drafting (CAMDLE)
  - id: threshold-calibration
    resource: https://github.com/evaluchat/research/blob/main/theory/threshold-calibration.en.md
    title: Threshold calibration — what counts as sufficient dialogic contribution?
  - id: measuring-subjective-evidence
    resource: https://github.com/evaluchat/knowledge/blob/main/references/how-to-measure-anything-evidence.md
    title: Measuring Subjective Evidence — Hubbard Reference
---

# AI-assisted essay — concluded-run evidence

> This packet documents one concluded run and one owner response. It is not a
> finding, a learning-effect claim, an integrity score, or a statement about all
> teachers or learners. Public submission is allowed only when the authorisation
> and anonymisation fields are confirmed.

## Question

This evidence serves [Threshold calibration — what counts as sufficient dialogic
contribution?](../../theory/threshold-calibration.en.md):

> What counts as sufficient dialogic contribution to unlock drafting support,
> and how does that threshold vary by task type, proficiency level, language
> background, and learner strategy?

## Measurement contract

- **Decision this collection can inform:** whether to refine the threshold,
  process-evidence review surface, or a future study in comparable settings.
- **Unit of analysis:** one method-run owner response, with one frozen run
  snapshot; this is not a learner-level measure.
- **Observable:** the owner’s response to the versioned, context-specific
  usefulness, threshold-fit, burden, learner-response, and reuse-intention
  items below.
- **Aggregation rule:** later synthesis must retain the full response
  distribution, instrument version, denominators, context, and missing or
  not-applicable responses. It may pool only comparable method versions,
  resolved levers, and contexts; narrative text requires an explicit coding
  method.

## Question and provenance — system-authored

| Field | Frozen value |
| --- | --- |
| Method | {{method_id}}@{{method_version}} |
| Run reference | {{run_reference}} |
| Profile | {{profile_id}} |
| Resolved levers | {{resolved_levers}} |
| Canvas version | {{canvas_version}} |
| Run window | {{run_started_at}} to {{run_concluded_at}} |

The platform, not the owner, writes these values from the concluded-run
snapshot. The public packet must never contain raw student work or raw
transcripts.

## Collection metadata — system-authored

| Field | Value |
| --- | --- |
| Participants in the run | {{participant_count}} |
| Eligible evidence contributors | {{eligible_owner_count}} |
| Invited evidence contributors | {{invited_owner_count}} |
| Submitted evidence contributors | {{responded_owner_count}} |
| Invitation opened | {{collection_opened_at}} |
| Evidence submitted | {{collection_closed_at}} |

The denominator is published so a later reader can distinguish a completed
owner response from a representative survey.

## Context — owner-authored

| Field | Response |
| --- | --- |
| Institution type | {{institution_type}} |
| Assignment genre | {{assignment_genre}} |
| Learner proficiency context | {{learner_proficiency_context}} |
| Learner age band | {{learner_age_band}} |
| Primary language of instruction | {{instruction_language}} |
| Primary language of writing | {{writing_language}} |
| Implementation duration | {{implementation_duration}} |

### Class and task context

{{class_and_task_context}}

Describe the subject or course and other transfer-relevant constraints. Do not
include student, school, or other direct identifiers.

## Intervention — frozen run plus owner-recorded deviation

### Platform record

| Measure | Value |
| --- | --- |
| Dialogic contribution summary | {{dialogic_contribution_summary}} |
| Drafting-gate outcome | {{drafting_gate_outcome}} |
| Process-signal summary | {{process_signal_summary}} |
| Transcript retention record | {{transcript_retention}} |
| Assignment outcome summary | {{assignment_outcome_summary}} |

These are measurements and retention records, not authorship detection,
integrity scores, or interpretations.

### Deviation from the frozen run

{{implementation_deviation}}

State what differed from the planned or resolved intervention and why. Write
“None” if there was no deviation.

### Public summary of the assignment

{{assignment_public_summary}}

Describe the task sufficiently for another reader to understand the intervention.
Do not include raw student work, the unredacted assignment brief, school
identifiers, or any material that cannot be published.

## Structured owner judgements

Each response is a report of this owner’s experience of this assignment. The
full ordinal value — including `insufficient-information` and
`not-applicable` — is retained for later tabulation; it must not be silently
converted into a claim about pedagogical effect.

| Versioned item | Response |
| --- | --- |
| How well did the configured contribution threshold fit this class and assignment? | {{threshold_fit}} |
| For this assignment, how useful was the process evidence for helping you inspect students’ reasoning process? | {{process_evidence_usefulness}} |
| How burdensome was it to review the process evidence for this assignment? | {{review_burden}} |
| At the time of this assignment, how would you characterise the class’s response to the contribution-before-drafting constraint? | {{learner_response_to_gate}} |
| Would you use this configuration again for a comparable assignment? | {{future_use_intention}} |

### Threshold-fit explanation

{{threshold_fit_explanation}}

Name the task, class, time, or implementation constraint that most affected the
threshold judgement. Do not state that the threshold caused a learning outcome.

### Process-evidence explanation

{{process_evidence_explanation}}

Explain what made the process evidence more or less useful for this review.

## Observations — owner-authored narrative

{{narrative_observations}}

Record what happened, what was seen, and any surprising or disconfirming case.
Do not interpret the observations here or identify a learner.

## Results — missing or unavailable data

{{missing_data}}

Record measures that were not captured, withheld, lost, unavailable, or not
applicable. Write “None” only when nothing is missing.

## Reflection — owner-authored interpretation

{{reflection}}

This is interpretation, not a result or finding. State what remains uncertain
and what you would change or investigate next.

## Limitations

{{limitations}}

State the scope, likely confounders, selection or non-response limitations,
recall limits, and competing explanations. A single response cannot establish a
learning effect, represent all teachers, or validate the method.

## Publication provenance and stage

| Field | Declaration |
| --- | --- |
| Contribution stage | {{contribution_stage}} |
| Public contribution authorisation | {{publication_authorisation}} |
| Anonymisation status | {{anonymisation_status}} |

### Public data-sharing limits

{{data_sharing_limits}}

State what cannot be shared or independently reproduced, the reason, and the
strongest lawful substitute (for example, aggregate counts, a data dictionary,
or a redacted summary). A non-confirmed authorisation or anonymisation status
blocks submission.
