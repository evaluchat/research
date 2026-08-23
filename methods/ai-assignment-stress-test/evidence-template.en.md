---
type: Form Template
id: evidence-template
lang: en
locale: en
origin: native
status: draft
version: 1.0.0
title: AI Assignment Stress Test — concluded-run evidence
description: "Versioned conclusion form for one teacher-facing assignment stress test, preserving frozen report summaries and structured owner judgements without treating one report as proof."
tags: [evidence, form-template, ai-assignment-stress-test, measurement-validity, teacher-tool]
timestamp: 2026-08-17T22:14:52Z
template_kind: form
applies_to_method: ai-assignment-stress-test@0.1.0
default_stage: documented-experience
question_id: ai-assignment-stress-test-validity
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
  probe_summary:
    label: Probe summary
    type: textarea
    required: true
    read_only: true
    source: frozen_run.analytics.probe_summary
    max_length: 4000
    display_lines: 7
  capability_map_summary:
    label: Capability-map summary
    type: textarea
    required: true
    read_only: true
    source: frozen_run.analytics.capability_map_summary
    max_length: 4000
    display_lines: 7
  delegation_loss_summary:
    label: Delegation-loss summary
    type: textarea
    required: true
    read_only: true
    source: frozen_run.analytics.delegation_loss_summary
    max_length: 4000
    display_lines: 7
  redesign_output_summary:
    label: Redesign-output summary
    type: textarea
    required: true
    read_only: true
    source: frozen_run.analytics.redesign_output_summary
    max_length: 4000
    display_lines: 7
  institution_type:
    label: Institution type
    type: select
    required: true
    options: [school, college-or-university, adult-education, tutoring-or-small-group, other, prefer-not-to-say]
  assignment_genre:
    label: Assignment genre
    type: select
    required: true
    options: [written-analysis, problem-solving, project-or-performance, exam-or-quiz, mixed-or-other, insufficient-information]
  learner_proficiency_context:
    label: Learner proficiency context
    type: select
    required: true
    options: [primarily-beginner, primarily-developing, primarily-proficient, mixed, not-assessed-or-not-known]
  instruction_language:
    label: Primary language of instruction
    type: text
    required: true
    max_length: 120
    display_chars: 32
  assignment_duration:
    label: Assignment duration
    type: text
    required: true
    max_length: 160
    display_chars: 48
  assignment_context:
    label: Assignment context
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
  probe_usefulness:
    label: Usefulness of the configured probe for this assignment review
    type: select
    required: true
    options: [not-at-all-useful, slightly-useful, moderately-useful, very-useful, extremely-useful, insufficient-information, not-applicable-probe-not-complete]
  capability_map_fit:
    label: Fit of the capability map to the assignment
    type: select
    required: true
    options: [very-poor-fit, somewhat-poor-fit, mixed-fit, somewhat-good-fit, very-good-fit, insufficient-information, not-applicable-map-not-produced]
  delegation_loss_usefulness:
    label: Usefulness of the delegation-loss analysis
    type: select
    required: true
    options: [not-at-all-useful, slightly-useful, moderately-useful, very-useful, extremely-useful, insufficient-information, not-applicable-analysis-not-produced]
  redesign_output_usefulness:
    label: Usefulness of the redesign alternatives
    type: select
    required: true
    options: [not-at-all-useful, slightly-useful, moderately-useful, very-useful, extremely-useful, insufficient-information, not-applicable-redesign-not-produced]
  report_review_burden:
    label: Perceived burden of reviewing the report
    type: select
    required: true
    options: [none, low, moderate, high, unacceptable, insufficient-information]
  future_use_intention:
    label: Intention to use this configuration again for a comparable assignment
    type: select
    required: true
    options: [definitely-would-not, probably-would-not, unsure, probably-would, definitely-would, not-applicable]
  structured_judgement_explanation:
    label: Explanation of the structured judgements
    type: textarea
    required: true
    max_length: 2400
    display_lines: 7
  narrative_observations:
    label: Observations from the concluded run
    type: textarea
    required: true
    max_length: 4000
    display_lines: 10
  missing_data:
    label: Missing or unavailable report data
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
  guidance: "Help the owner describe only their concluded assignment-level run. Never infer, invent, or expose student information, raw student work, raw submissions, or consent. Render the frozen system-authored fields exactly as provided; never alter, duplicate, or add system measurements. Keep observations factual and separate from reflection; describe judgements as this owner's report, not proof of task quality, learning, AI use, or the views of teachers beyond this response. A response that is not authorised or not anonymised must not be submitted for public publication."
generated: { by: codex/gpt-5, at: 2026-08-17T22:14:52Z }
sources:
  - id: ai-assignment-stress-test
    resource: https://github.com/openrigor/research/blob/main/methods/ai-assignment-stress-test/ai-assignment-stress-test.en.md
    title: AI Assignment Stress Test — assignment-level measurement analysis
  - id: ai-assignment-stress-test-validity
    resource: https://github.com/openrigor/research/blob/main/theory/ai-assignment-stress-test-validity.en.md
    title: AI assignment stress-test validity — when can task probes identify what an assessment still measures?
  - id: evidence-roles
    resource: https://github.com/openrigor/research/blob/main/governance/evidence-roles.en.md
    title: Shared evidence roles — how every method files a run
---

# AI Assignment Stress Test — concluded-run evidence

> This packet documents one concluded teacher-facing assignment analysis and one
> owner response. It is not a finding, a statement about all assignments, an
> authorship score, or an AI-use detection result. Public submission is allowed
> only when the authorisation and anonymisation fields are confirmed.

## Question

This evidence serves [AI assignment stress-test validity — when can task probes
identify what an assessment still measures?](../../theory/ai-assignment-stress-test-validity.en.md):

> To what extent, and under which task conditions, do standardized AI stress-test
> probes provide valid, reliable, and useful evidence about the human capabilities
> an assignment can still measure when generative AI is available?

## Measurement contract

- **Decision this collection can inform:** whether to refine the versioned probe,
  capability map, delegation analysis, redesign output, or a future study in a
  comparable assignment context.
- **Unit of analysis:** one assignment-level method-run owner response with one
  frozen run snapshot; it is not a learner-level measure.
- **Observable:** the frozen report summaries and the owner’s versioned,
  context-specific usefulness, fit, burden, and reuse-intention responses.
- **Aggregation rule:** later synthesis must retain report and instrument versions,
  resolved levers, full response distributions, denominators, contexts, missing
  and not-applicable responses. Narrative text requires an explicit coding method.

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
snapshot. The public packet must never contain raw learner material, submissions,
or other non-public assignment content.

## Collection metadata — system-authored

| Field | Value |
| --- | --- |
| Participants in the run | {{participant_count}} |
| Eligible evidence contributors | {{eligible_owner_count}} |
| Invited evidence contributors | {{invited_owner_count}} |
| Submitted evidence contributors | {{responded_owner_count}} |
| Invitation opened | {{collection_opened_at}} |
| Evidence submitted | {{collection_closed_at}} |

The denominator distinguishes a completed owner response from a representative
survey or a result about teachers generally.

## Context — owner-authored

| Field | Response |
| --- | --- |
| Institution type | {{institution_type}} |
| Assignment genre | {{assignment_genre}} |
| Learner proficiency context | {{learner_proficiency_context}} |
| Primary language of instruction | {{instruction_language}} |
| Assignment duration | {{assignment_duration}} |

### Assignment context

{{assignment_context}}

Describe only transfer-relevant course and task constraints. Do not include a
student, school, or other direct identifier.

## Intervention — frozen report plus owner-recorded deviation

### Public summary of the assignment

{{assignment_public_summary}}

Describe the task sufficiently for another reader to understand the analysis.
Do not include the unredacted brief, raw student work, distinctive institutional
details, or material that cannot be published.

### Frozen assignment-report summaries

| Report stage | Frozen summary |
| --- | --- |
| Probe | {{probe_summary}} |
| Capability map | {{capability_map_summary}} |
| Delegation analysis | {{delegation_loss_summary}} |
| Redesign output | {{redesign_output_summary}} |

These are the configured assignment-level report outputs. They are measurements
or descriptions of a task analysis, not an authorship judgment, integrity verdict,
or interpretation.

### Deviation from the frozen run

{{implementation_deviation}}

State what differed from the planned or resolved intervention and why. Write
“None” if there was no deviation.

## Structured owner judgements

Each response records this owner’s experience of this assignment. Later work must
retain the complete ordinal value — including `insufficient-information` and
`not-applicable` — rather than converting a response into a claim about teaching,
learning, or task quality.

| Versioned item | Response |
| --- | --- |
| How useful was the configured probe for reviewing this assignment? | {{probe_usefulness}} |
| How well did the capability map fit this assignment? | {{capability_map_fit}} |
| How useful was the delegation-loss analysis? | {{delegation_loss_usefulness}} |
| How useful were the redesign alternatives? | {{redesign_output_usefulness}} |
| How burdensome was it to review the report? | {{report_review_burden}} |
| Would you use this configuration again for a comparable assignment? | {{future_use_intention}} |

### Explanation of the structured judgements

{{structured_judgement_explanation}}

Name the task, time, implementation, or report constraint that most affected the
responses. Do not claim that the method caused a learning outcome or detected AI use.

## Observations — owner-authored narrative

{{narrative_observations}}

Record what happened while running the probe and reviewing the report, including
surprising or disconfirming cases. Do not interpret observations here or identify
a learner.

## Results — missing or unavailable data

{{missing_data}}

Record report stages, models, modes, rubric inputs, or data that were unavailable,
withheld, failed, or not applicable. Write “None” only when nothing is missing.

## Reflection — owner-authored interpretation

{{reflection}}

This is interpretation, not a result or finding. State what remains uncertain and
what you would change or investigate next.

## Limitations

{{limitations}}

State scope, model-set sensitivity, selection or non-response limits, possible
confounders, and competing explanations. One assignment-level report cannot
establish a learning effect, represent all assignments, or validate the method.

## Publication provenance and stage

| Field | Declaration |
| --- | --- |
| Contribution stage | {{contribution_stage}} |
| Public contribution authorisation | {{publication_authorisation}} |
| Anonymisation status | {{anonymisation_status}} |

### Public data-sharing limits

{{data_sharing_limits}}

State what cannot be shared or independently reproduced, why, and the strongest
lawful substitute, such as an aggregate report, data dictionary, or redacted
summary. A non-confirmed authorisation or anonymisation status blocks submission.
