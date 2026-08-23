---
type: Form Template
id: evidence-template
lang: en
locale: en
origin: native
status: draft
version: 1.0.0
title: Revision-tracking validity — concluded-run evidence
description: "Versioned conclusion form for one assessor-blind revision-tracking study run, preserving frozen aggregate protocol records and structured owner reports without presenting a result as a detector or finding."
tags: [evidence, form-template, revision-tracking, assessor-blind, privacy, reproducibility]
timestamp: 2026-08-17T22:14:52Z
template_kind: form
applies_to_method: revision-tracking-validity@0.1.0
default_stage: documented-experience
question_id: revision-tracking-validity-question
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
  profile_pair:
    label: Resolved condition profiles
    type: textarea
    required: true
    read_only: true
    source: frozen_run.profiles
    max_length: 4000
    display_lines: 6
  resolved_levers:
    label: Resolved study levers
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
  allocation_summary:
    label: De-identified allocation summary
    type: textarea
    required: true
    read_only: true
    source: frozen_run.analytics.allocation_summary
    max_length: 4000
    display_lines: 7
  blinded_judgement_summary:
    label: Blinded two-pass assessment summary
    type: textarea
    required: true
    read_only: true
    source: frozen_run.analytics.blinded_judgement_summary
    max_length: 4000
    display_lines: 7
  revision_metrics_summary:
    label: Condition-neutral revision-metrics summary
    type: textarea
    required: true
    read_only: true
    source: frozen_run.analytics.revision_metrics_summary
    max_length: 4000
    display_lines: 7
  lock_and_reveal_summary:
    label: Data-lock and reveal audit summary
    type: textarea
    required: true
    read_only: true
    source: frozen_run.provenance.lock_and_reveal_summary
    max_length: 4000
    display_lines: 7
  reproducibility_packet_summary:
    label: Reproducibility-packet summary
    type: textarea
    required: true
    read_only: true
    source: frozen_run.provenance.reproducibility_packet_summary
    max_length: 4000
    display_lines: 7
  institution_type:
    label: Institution type
    type: select
    required: true
    options: [school, college-or-university, adult-education, other, prefer-not-to-say]
  study_phase:
    label: Study phase
    type: select
    required: true
    options: [synthetic-acceptance-demonstration, internal-feasibility, ethics-reviewed-low-stakes-pilot, independent-challenge-or-replication, insufficient-information]
  task_stakes:
    label: Task stakes
    type: select
    required: true
    options: [synthetic-or-no-student-task, ungraded, low-stakes, graded-with-approved-protection, insufficient-information]
  instruction_language:
    label: Primary language of instruction
    type: text
    required: true
    max_length: 120
    display_chars: 32
  study_context:
    label: Study and task context
    type: textarea
    required: true
    max_length: 2200
    display_lines: 7
  assignment_public_summary:
    label: Public summary of the equivalent task set
    type: textarea
    required: true
    max_length: 1200
    display_lines: 4
  implementation_deviation:
    label: Deviation from the frozen protocol
    type: textarea
    required: true
    max_length: 1800
    display_lines: 6
  consent_and_ethics_status:
    label: Consent and ethics record status
    type: select
    required: true
    options: [not-applicable-synthetic-only, recorded-and-approved-for-this-phase, documented-exemption-or-non-student-route, not-confirmed-do-not-submit]
  grade_protection_status:
    label: Grade-protection status
    type: select
    required: true
    options: [not-applicable-synthetic-or-ungraded, documented-grade-protection-in-place, insufficient-information, not-confirmed-do-not-submit]
  masking_integrity:
    label: Observed integrity of assessor masking
    type: select
    required: true
    options: [no-observed-masking-incident, observed-incident-contained, observed-incident-not-contained, insufficient-information, not-applicable-not-run]
  neutral_metrics_usability:
    label: Usability of the condition-neutral metrics view
    type: select
    required: true
    options: [not-at-all-usable, slightly-usable, moderately-usable, very-usable, extremely-usable, insufficient-information, not-applicable-not-run]
  lock_sequence_integrity:
    label: Completion of the required data-lock and reveal sequence
    type: select
    required: true
    options: [completed-as-specified, completed-with-recorded-deviation, not-completed, insufficient-information, not-applicable-not-run]
  reproducibility_packet_completeness:
    label: Completeness of the reproducibility packet for this run
    type: select
    required: true
    options: [incomplete, partially-complete, complete-for-declared-scope, insufficient-information, not-applicable-not-exported]
  research_workflow_burden:
    label: Perceived burden of the research workflow
    type: select
    required: true
    options: [none, low, moderate, high, unacceptable, insufficient-information, not-applicable-not-run]
  future_protocol_reuse:
    label: Intention to reuse this protocol in a comparable approved study
    type: select
    required: true
    options: [definitely-would-not, probably-would-not, unsure, probably-would, definitely-would, not-applicable]
  structured_judgement_explanation:
    label: Explanation of the structured judgements
    type: textarea
    required: true
    max_length: 2600
    display_lines: 8
  narrative_observations:
    label: Observations from the concluded run
    type: textarea
    required: true
    max_length: 4000
    display_lines: 10
  missing_data:
    label: Missing, withheld, or suppressed data
    type: textarea
    required: true
    max_length: 1800
    display_lines: 6
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
    max_length: 3200
    display_lines: 9
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
    max_length: 1800
    display_lines: 6
assistant:
  guidance: "Help the owner describe only a concluded run under the frozen protocol. This method is currently implementation-blocked: do not fabricate a run, allocation, consent, ethics approval, locks, reveal, reproducibility packet, measurement, or result. Never infer, invent, or expose student information, raw student work, AI transcripts, raw revision traces, direct event logs, or identity-to-condition mappings. Preserve read-only system fields. Keep observations factual and separate from reflection; do not describe a revision metric as proof of authorship, AI use, learning, intent, integrity, or a grade-relevant outcome. A response without confirmed authorisation and anonymisation must not be submitted for public publication."
generated: { by: codex/gpt-5, at: 2026-08-17T22:14:52Z }
sources:
  - id: revision-tracking-validity
    resource: https://github.com/openrigor/research/blob/main/methods/revision-tracking-validity/revision-tracking-validity.en.md
    title: Revision-tracking validity — assessor-blind process-evidence study
  - id: revision-tracking-validity-question
    resource: https://github.com/openrigor/research/blob/main/theory/revision-tracking-validity-question.en.md
    title: Revision-tracking validity — theory research question
  - id: evidence-roles
    resource: https://github.com/openrigor/research/blob/main/governance/evidence-roles.en.md
    title: Shared evidence roles — how every method files a run
---

# Revision-tracking validity — concluded-run evidence

> This packet defines the public evidence record for one concluded protocol run.
> It is not a finding, an integrity score, an authorship claim, a detector, or a
> grade input. The method is currently implementation-blocked; this template does
> not imply that any run, capability, approval, or result exists. Public submission
> is allowed only when the authorisation and anonymisation fields are confirmed.

## Question

This evidence serves [Revision-tracking validity — theory research question](../../theory/revision-tracking-validity-question.en.md):

> Under a randomly allocated, assessor-blind assignment condition, to what extent
> can a pre-specified, condition-neutral revision-metrics protocol distinguish an
> authoring episode with a recorded Canvas AI assistance event from one with no
> recorded Canvas AI event, and are its errors, confidence, burdens, and subgroup
> differences acceptable for the proposed research use?

## Measurement contract

- **Decision this collection can inform:** whether a frozen, research-only protocol
  needs revision, non-endorsement, a challenge, or a separately approved future
  study; it cannot make an educational or integrity decision.
- **Unit of analysis:** one concluded study-run owner response with de-identified,
  aggregate frozen records; never a student-level public profile.
- **Observable:** the frozen protocol and aggregate record summaries, plus owner
  reports of masking, lock sequence, packet completeness, burden, and context.
- **Aggregation rule:** later analysis retains method, metrics-schema, task-set,
  profile, and analysis-plan versions; denominators; missingness; suppression;
  not-applicable responses; and all documented deviations. It never pools raw
  student records or treats revision metrics as direct evidence of authorship.

## Question and provenance — system-authored

| Field | Frozen value |
| --- | --- |
| Method | {{method_id}}@{{method_version}} |
| Run reference | {{run_reference}} |
| Resolved condition profiles | {{profile_pair}} |
| Resolved study levers | {{resolved_levers}} |
| Canvas version | {{canvas_version}} |
| Run window | {{run_started_at}} to {{run_concluded_at}} |

The platform, not the owner, writes these values from the concluded-run snapshot.
No public packet may contain raw student text, AI transcript, raw revision trace,
direct event log, or identity-to-condition mapping.

## Collection metadata — system-authored

| Field | Value |
| --- | --- |
| Participants in the run | {{participant_count}} |
| Eligible evidence contributors | {{eligible_owner_count}} |
| Invited evidence contributors | {{invited_owner_count}} |
| Submitted evidence contributors | {{responded_owner_count}} |
| Invitation opened | {{collection_opened_at}} |
| Evidence submitted | {{collection_closed_at}} |

The denominator is descriptive. It does not establish a representative sample
or a valid study result.

## Context — owner-authored

| Field | Response |
| --- | --- |
| Institution type | {{institution_type}} |
| Study phase | {{study_phase}} |
| Task stakes | {{task_stakes}} |
| Primary language of instruction | {{instruction_language}} |
| Consent and ethics record status | {{consent_and_ethics_status}} |
| Grade-protection status | {{grade_protection_status}} |

### Study and task context

{{study_context}}

Describe the study phase and transfer-relevant constraints without identifying a
student, institution, class, or cohort.

## Intervention — frozen protocol plus owner-recorded deviation

### Public summary of the equivalent task set

{{assignment_public_summary}}

Describe the task set at a safe level of detail. Do not include raw student work,
the unredacted assignment, a participant list, or material that cannot be public.

### Frozen protocol and aggregate record summaries

| Protocol record | Frozen summary |
| --- | --- |
| Server-side allocation | {{allocation_summary}} |
| Blinded two-pass assessment | {{blinded_judgement_summary}} |
| Condition-neutral revision metrics | {{revision_metrics_summary}} |
| Data lock and authorised reveal | {{lock_and_reveal_summary}} |
| Reproducibility packet | {{reproducibility_packet_summary}} |

These are de-identified protocol or measurement records. They do not demonstrate
that revision metrics detect AI use, establish authorship, or justify a grade or
disciplinary judgment.

### Deviation from the frozen protocol

{{implementation_deviation}}

State every deviation, masking incident, technical exception, suppression, or
reason the planned run did not proceed. Write “None” only when there was no deviation.

## Structured owner judgements

Each response records the owner’s account of this protocol run. Later synthesis
must retain every ordinal value, including `insufficient-information` and
`not-applicable`, and must not convert a process report into an efficacy or
detector claim.

| Versioned item | Response |
| --- | --- |
| Observed integrity of assessor masking | {{masking_integrity}} |
| Usability of the condition-neutral metrics view | {{neutral_metrics_usability}} |
| Completion of the required lock and reveal sequence | {{lock_sequence_integrity}} |
| Completeness of the reproducibility packet | {{reproducibility_packet_completeness}} |
| Perceived burden of the research workflow | {{research_workflow_burden}} |
| Intention to reuse this protocol in a comparable approved study | {{future_protocol_reuse}} |

### Explanation of the structured judgements

{{structured_judgement_explanation}}

Describe the protocol, task, access, masking, privacy, or implementation constraint
that affected these responses. Do not interpret a metric as an individual verdict.

## Observations — owner-authored narrative

{{narrative_observations}}

Record what happened in the protocol, including null, adverse, missing, or
disconfirming events. Keep this factual; do not identify a participant or interpret
the observations here.

## Results — missing, withheld, or suppressed data

{{missing_data}}

Record data that were unavailable, excluded, withdrawn, suppressed for privacy,
or not applicable, including the reason. Do not fill gaps by inferring a Canvas AI
event from revision metrics.

## Reflection — owner-authored interpretation

{{reflection}}

This is interpretation, not a result or finding. State what remains uncertain and
what a human should reconsider, challenge, or investigate next.

## Limitations

{{limitations}}

State scope, consent and non-response limits, task dependence, masking or logging
risk, uncertainty, fairness concerns, competing explanations, and all reasons the
record cannot support a general detector or a student-facing use.

## Publication provenance and stage

| Field | Declaration |
| --- | --- |
| Contribution stage | {{contribution_stage}} |
| Public contribution authorisation | {{publication_authorisation}} |
| Anonymisation status | {{anonymisation_status}} |

### Public data-sharing limits

{{data_sharing_limits}}

State what cannot be shared or independently reproduced, why, and the strongest
lawful substitute, such as aggregate counts, a data dictionary, a protocol hash,
or a redacted reproducibility-packet manifest. A non-confirmed authorisation or
anonymisation status blocks submission.
