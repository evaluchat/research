---
type: Apparatus
id: revision-tracking-validity
lang: en
origin: native
status: draft
implementation_status: blocked
blockers:
  - id: experimental-assignment-condition
    status: missing
    reason: Canvas has no server-side, auditable assignment-group condition knob that can randomly bind individual students to immutable capability profiles while preserving assessor masking.
    feature_request: https://github.com/evaluchat/research/issues/1
version: 0.1.0
min_canvas_version: "0.5.9"
title: Revision-tracking validity — assessor-blind process-evidence study
description: "Apparatus #3: a randomised, assessor-blind assignment study that evaluates the validity, fairness, limitations, and practical usefulness of condition-neutral revision metrics as evidence about recorded Canvas AI events."
tags: [apparatus, revision-tracking, process-evidence, assessment-validity, fairness, privacy, ai]
timestamp: 2026-08-11T10:31:24Z
research_questions: [revision-tracking-validity-question]
question: "Under a randomly allocated, assessor-blind assignment condition, to what extent can a pre-specified, condition-neutral revision-metrics protocol distinguish an authoring episode with a recorded Canvas AI assistance event from one with no recorded Canvas AI event, and are its errors, confidence, burdens, and subgroup differences acceptable for the proposed research use?"
roles: [student, teacher, researcher, allocation-custodian]
required_capabilities: [experimental-assignment-condition, condition-neutral-revision-metrics, protected-process-telemetry, blinded-two-pass-assessment, data-lock-and-reveal, reproducibility-packet-export]
knobs:
  - id: assignment_condition
    type: enum
    values: [canvas-ai-enabled, canvas-ai-disabled]
    effect: Server-side random allocation selects one immutable profile; the label is hidden from the teacher and research metrics view until data lock.
  - id: canvas_ai_assistance
    type: boolean
    default: false
    requires: { assignment_condition: canvas-ai-enabled }
    effect: Makes Canvas's existing bounded, collaborative AI assistance available in the enabled profile; it never enables unrestricted AI behaviour.
  - id: task_set
    type: string
    default: equivalent-task-set-v1
    effect: Versioned equivalent materials, time allowance, rubric, and learning objective used in both conditions.
  - id: randomisation_protocol
    type: enum
    values: [server-side-stratified-block-v1]
    default: server-side-stratified-block-v1
    effect: The sealed allocation method and strata; its resolved record is preserved for audit and analysis.
  - id: assessment_workflow
    type: enum
    values: [two-pass-assessor-blind-v1]
    default: two-pass-assessor-blind-v1
    effect: Requires normal grading before a separate de-identified research judgment from the neutral metrics view.
  - id: metrics_schema
    type: string
    default: revision-metrics-v1.0
    effect: Frozen definitions, windows, derivations, suppression rules, and display fields for revision metrics.
  - id: focus_telemetry
    type: enum
    values: [off, ethics-approved-optional]
    default: off
    effect: Visibility and focus-change collection is disabled unless separately approved, consented, and included in an immutable profile.
  - id: data_minimisation_profile
    type: enum
    values: [counts-and-derived-metrics-v1]
    default: counts-and-derived-metrics-v1
    effect: Retains event categories, timestamps, and derived metrics needed by the protocol, not clipboard contents, raw student text, or AI transcripts in the research export.
  - id: outcome_reference
    type: enum
    values: [recorded-canvas-event-v1]
    default: recorded-canvas-event-v1
    effect: Defines E_any and E_content from immutable Canvas event records; these fields are withheld from assessors and excluded from the metrics view.
  - id: analysis_plan
    type: string
    default: revision-tracking-validity-analysis-v1
    effect: Versioned preregistered targets, exclusions, missing-data handling, thresholds, uncertainty methods, and fairness analyses.
telemetry: [derived-revision-metrics, protected-event-categories, locked-allocation-record, blinded-research-judgments, grading-workflow-status]
provenance:
  sources:
    - id: apparatus-method
      resource: https://github.com/evaluchat/research/blob/main/methods/apparatus.en.md
      title: The apparatus as research instrument
profiles:
  - id: canvas-ai-enabled-v1
    version: 1.0.0
    label: Canvas AI enabled study profile
    description: Equivalent assignment context, authoring surface, submission, and bounded always-on Canvas AI assistance, with condition-neutral revision metrics and assessor masking.
    author: evaluchat-research
    immutable: true
    configuration: { assignment_condition: canvas-ai-enabled, canvas_ai_assistance: true, task_set: equivalent-task-set-v1, randomisation_protocol: server-side-stratified-block-v1, assessment_workflow: two-pass-assessor-blind-v1, metrics_schema: revision-metrics-v1.0, focus_telemetry: off, data_minimisation_profile: counts-and-derived-metrics-v1, outcome_reference: recorded-canvas-event-v1, analysis_plan: revision-tracking-validity-analysis-v1 }
  - id: canvas-ai-disabled-v1
    version: 1.0.0
    label: Canvas AI disabled study profile
    description: The same assignment context, authoring surface, submission, and integrity constraints, but without Canvas AI assistance; condition-neutral revision metrics and assessor masking remain identical.
    author: evaluchat-research
    immutable: true
    configuration: { assignment_condition: canvas-ai-disabled, canvas_ai_assistance: false, task_set: equivalent-task-set-v1, randomisation_protocol: server-side-stratified-block-v1, assessment_workflow: two-pass-assessor-blind-v1, metrics_schema: revision-metrics-v1.0, focus_telemetry: off, data_minimisation_profile: counts-and-derived-metrics-v1, outcome_reference: recorded-canvas-event-v1, analysis_plan: revision-tracking-validity-analysis-v1 }
catalog_urls:
  spec: https://github.com/evaluchat/research/blob/main/apparatus/revision-tracking-validity/revision-tracking-validity.en.md
  evidence: https://github.com/evaluchat/research/tree/main/apparatus/revision-tracking-validity/evidence
  questions:
    - https://github.com/evaluchat/research/blob/main/theory/revision-tracking-validity-question.en.md
generated: { by: codex/gpt-5, at: 2026-08-11T10:31:24Z }
sources:
  - id: revision-tracking-validity-question
    resource: https://github.com/evaluchat/research/blob/main/theory/revision-tracking-validity-question.en.md
    title: Revision-tracking validity — theory research question
  - id: apparatus-method
    resource: https://github.com/evaluchat/research/blob/main/methods/apparatus.en.md
    title: The apparatus as research instrument (research catalog)
  - id: experimental-assignment-condition-feature-request
    resource: https://github.com/evaluchat/research/issues/1
    title: Feature request — experimental assignment conditions with server-side randomisation
---

# Revision-tracking validity — assessor-blind process-evidence study

> `status: draft`. Apparatus #3 is a research-method specification, not an implementation and not
> a detector. Its intended outcome is credible evidence about when revision tracking is useful,
> when it misleads, and whether it should influence an educational judgment at all. No apparatus
> output is an integrity score, cheating verdict, authorship claim, or grade input.

> **Implementation status: blocked.** The design cannot enter simulated acceptance testing or an
> internal feasibility run until Canvas supplies the missing
> [`experimental-assignment-condition` capability request][feature-request]. Canvas currently has
> no server-side, per-assignment-group knob that randomly binds individual students to immutable
> `canvas-ai-enabled` / `canvas-ai-disabled` profiles while preserving assessment masking and an
> allocation audit trail. A teacher toggle, a client-side experiment, or post-hoc grouping is not
> an equivalent substitute.

## Public development trail

This apparatus is the first public acceptance example for the linked feature request. The sequence
is deliberately visible so that a proposed capability, its implementation evidence, and the later
research evidence are not conflated:

`blocked apparatus` → `public feature request` → `versioned capability contract` →
`synthetic acceptance demonstration` → `internal feasibility` → `ethics-reviewed low-stakes pilot` →
`independent challenge / replication`

| State | Public artefact or evidence | Current status | Advance only when |
|---|---|---|---|
| Blocked dependency | [Feature request #1][feature-request] names the missing platform capability and its non-goals. | **Open / blocked** | The request has a reviewed capability contract and an owner accepts the acceptance example. |
| Contract | Immutable profile schema, permission model, masking rules, audit record, and reproducibility-packet schema. | Not started | The contract preserves server-side allocation and does not create a detector or integrity workflow. |
| Synthetic acceptance | Synthetic assignment-group allocations exercise the `canvas-ai-enabled-v1` and `canvas-ai-disabled-v1` profiles; masking, locks, audit, and export are checked. | Not started | All acceptance checks pass without student data or raw content. |
| Internal feasibility | Reviewed implementation is exercised with synthetic or voluntary non-student traces. | Not started | Independent internal audit finds no critical allocation, privacy, accessibility, masking, or reveal failure. |
| Ethics-reviewed pilot | Consented, low-stakes student study under the frozen protocol. | Not started | Required ethics, consent, data-protection, and grading-equivalence gates have been met. |
| Independent challenge / replication | Independent deployment tests both the capability and the stated research interpretation. | Not started | Results and limitations are published through the evidence process. |

### E2E acceptance example

The missing capability is sufficient to unblock the apparatus only when this end-to-end flow can be
demonstrated in a reviewed test environment:

1. A study owner selects one defined, low-stakes assignment group and the frozen equivalent task.
2. Canvas server-side randomisation binds each eligible, consented student to exactly one immutable
   profile: `canvas-ai-enabled-v1` or `canvas-ai-disabled-v1`.
3. Both profiles retain the same task, authoring surface, time, rubric, learning objective, and
   submission path. The enabled profile exposes only Canvas's existing bounded collaborative AI
   behaviour; the disabled profile removes that one capability.
4. The teacher completes normal grading without allocation labels, AI transcript, raw AI-event log,
   or research interpretation. A separate de-identified metrics review is then locked.
5. Only the allocation custodian can make the minimum pseudonymised release of `Z`, `E_any`, and
   `E_content`, after both locks and with an append-only reveal audit.
6. The reproducibility packet proves the apparatus version, Canvas version, resolved profiles,
   allocation method, metric schema, analysis plan, and reveal history—without exporting student
   text, transcripts, raw traces, or identity mappings.

This is an acceptance demonstration for a comparative-study platform capability. It is neither a
student trial nor evidence that revision metrics are valid.

## 1. Apparatus definition and rationale

This apparatus runs an equivalent-task, randomised assignment study with an assessor-blind,
two-pass workflow. The platform randomly allocates each consenting student to an immutable profile:

- `canvas-ai-enabled` — the normal Canvas authoring surface with Canvas's existing bounded,
  collaborative, always-on AI behaviour and academic-integrity constraints available;
- `canvas-ai-disabled` — the same Canvas authoring surface, task materials, time, rubric, learning
  objective, and integrity constraints, but no Canvas AI assistance.

The platform records a narrow reference event: an eligible Canvas AI interaction, and, separately,
an eligible Canvas AI content-affecting event. The metrics protocol never treats either event as
proof that AI text appeared in a submission or that a student did or did not author the work.

The study asks a limited validity question: whether a frozen, condition-neutral description of
revision activity carries useful information about those *known Canvas events* under stated
conditions. Random allocation estimates the impact of providing the bounded capability; comparison
to the event record evaluates the narrow association with recorded interaction. Neither comparison
can establish unrecorded assistance or authorship. See the preceding
[theory research question](../../theory/revision-tracking-validity-question.en.md).

## 2. Experimental conditions and masking

### Equivalent-task intervention

The study owner freezes an equivalent `task_set` before allocation. It states the prompt or
counterbalanced prompt form, target learning objective, time window, resources, rubric, submission
rule, accessibility accommodation plan, and any permitted non-AI collaboration. Conditions may not
differ in teaching, due date, feedback, rubric, normal authoring features, or the assessment rule;
only availability of the declared bounded Canvas AI capability differs.

Enabled does **not** mean unrestricted AI. Existing Canvas collaboration and academic-integrity
constraints remain active. Disabled does **not** represent proof that a student had no other source
of assistance; it only removes Canvas AI from the shared authoring environment.

### Condition and event labels

| Label | Definition | Use in analysis |
|---|---|---|
| `Z` | Server-side allocation to `canvas-ai-enabled` or `canvas-ai-disabled`. | Intention-to-treat comparison and the target for the assessor's required condition judgment. |
| `E_any` | One or more completed, eligible Canvas AI interaction events for the assignment episode. | Primary event-reference label for the blinded event judgment. |
| `E_content` | A recorded Canvas AI insertion or transformation of canvas content. | Secondary, more content-proximal reference label. |
| `E = 0` | No eligible Canvas AI event was recorded. | Never described as absence of all AI use or all assistance. |

An eligible interaction is a Canvas AI request with a recorded completed response in the assignment
session. An eligible content event is an AI insertion or transformation recorded by the canvas. The
pre-registration names the exact event types and handling of failed requests, retries, preview-only
responses, and system errors. Direct event types, counts, timestamps, transcript text, and content
payloads are excluded from the teacher's metrics view and from every predictive analysis input.

### Condition matrix

| Actor | Before and during authoring | Pass 1: normal assessment | Pass 2: research assessment | After locked release |
|---|---|---|---|---|
| Student | Their task, authoring surface, submission path, consent information, and the enabled AI surface when allocated. They do not see another student's profile, allocation records, or raw research logs. | Receives normal feedback under the local course process. | May receive the study explanation and withdrawal route, never another student's data or condition labels. | May receive an approved aggregate summary; no individual event trace, transcript, or peer allocation is published. |
| Teacher / assessor | Assignment administration and normal pedagogical context, but no allocation label, AI transcript, raw AI-event log, or treatment dashboard. | Grades against the normal rubric without condition labels or research interpretation. Grade is frozen before research review. | Sees a de-identified, standardised condition-neutral metrics summary for every submitted episode; records (a) profile judgment, (b) `E_any` judgment, (c) confidence, and (d) optional structured rationale. It cannot change the grade. | Receives only the approved aggregate study report unless separately authorised by the ethics protocol. |
| Researcher | Protocol, metric schema, pseudonymised operational status, and aggregate quality-control checks; no identity-to-condition join or raw text/transcript by default. | Cannot reveal allocations or alter grades; checks data-lock readiness only. | Can monitor completion and missingness without condition labels; cannot amend recorded judgments. | Receives the pseudonymised allocation and event-reference fields required by the pre-registered analysis, after custodian release and audit. |
| Allocation custodian | Holds the sealed allocation mapping, randomisation record, and capability-policy snapshots; cannot grade or make research judgments. | Blocks release until grading lock is attested. | Blocks release until all required research judgments are time-stamped and locked. | Performs the minimum authorised reveal, logs actor, purpose, scope, time, and approver; never publishes the identity mapping. |
| Privacy-protected analysis service | Derives the schema-defined metrics from minimised event categories. It keeps raw event payloads in the protected layer only for the approved retention period. | Supplies no research fields to grade view. | Generates the same neutral display for every episode and withholds `Z`, `E_any`, `E_content`, and all raw logs. | Produces a pseudonymised analysis table and reproducibility packet subject to the protocol. |

The condition-neutral view must have the same fields, layouts, suppression rules, and missing-value
codes for both profiles. Any field that directly exposes Canvas AI availability or its event count
is a masking failure, even if the field is technically a revision metric.

## 3. Pre-specified revision-metrics dictionary (`revision-metrics-v1.0`)

The dictionary uses aggregate counts, event categories, and timestamps. It neither retains clipboard
contents nor reads external applications. Metrics are calculated in the privacy-protected layer and
shown only in the stated form. A metric may suggest a pattern of activity; no individual metric,
combination, or display is an authorship or misconduct inference.

| Metric and v1.0 definition | What it can suggest | What it cannot establish | Plausible false-positive and false-negative paths | Availability |
|---|---|---|---|---|
| **Typed-to-pasted character ratio** — typed inserted characters divided by typed plus pasted inserted characters; deletions excluded; no pasted content retained. | Whether an episode contains relatively more direct typing or insertion. | Source, authorship, meaning, or whether a paste came from AI. | **FP:** a student pastes their own notes, dictated text, accessibility output, template text, or cited material. **FN:** AI text is manually retyped, typed after reading an AI response, or heavily revised. | Derived ratio: teacher neutral view and researcher after lock. Source event detail: protected layer only. |
| **Insertion, deletion, and replacement mix** — counts and proportions of local text-edit operation categories. | Whether the recorded canvas shows additive, subtractive, or replacement-heavy revision. | Who made an edit, why it was made, or intellectual engagement. | **FP:** normal restructuring, feedback incorporation, keyboard shortcuts, speech input, or a template workflow. **FN:** AI-supported work is composed gradually or transformed outside the captured operation pattern. | Aggregate mix: teacher and researcher after lock. Raw event sequence: protected layer only. |
| **Edit bursts and idle periods** — a burst is activity separated by no more than 30 seconds; an idle period is at least 120 seconds without a recorded canvas edit. | Cadence within the recorded canvas session. | Time thinking, reading, researching, working elsewhere, attention, effort, or time on task. | **FP:** interruptions, network loss, device sleep, accessibility pacing, reading, or ordinary planning. **FN:** assistance occurs during active editing or is used on another device. | Aggregate distribution only: teacher and researcher after lock. Timestamps: protected layer only. |
| **Document-version progression** — version snapshots every 60 seconds of active editing and on submission; summary reports count, active span, and net character change, not text. | Whether the stored document changed over the recorded episode. | A coherent drafting process, authorship, or the provenance of a version. | **FP:** autosave or formatting changes create many versions. **FN:** a single late paste or external drafting creates few informative snapshots. | Summary: teacher and researcher after lock. Version text and hashes: protected layer only; raw text not exported. |
| **Revision depth** — count and proportion of changed character spans that modify pre-existing non-whitespace canvas content, reported by size band. | Extent of visible revision to already present material. | Quality of revision, understanding, or whether text originated with AI. | **FP:** teacher-requested redrafting, formatting repair, assistive editing, or ordinary revisions. **FN:** AI-supported work is produced through small edits or changes occur outside Canvas. | Aggregated bands: teacher and researcher after lock. Span locations/content: protected layer only. |
| **Revision duration and cadence** — first-to-last recorded edit span, active-edit time proxy, and inter-event distribution; described as recorded-canvas timing. | The timing pattern of canvas edits. | Actual work duration, diligence, focus, or learning. | **FP:** connectivity, breaks, reading, planning, disability-related pacing, or shared devices. **FN:** AI assistance can occur without a distinctive timing pattern. | Summary: teacher and researcher after lock. Event timestamps: protected layer only. |
| **Visibility and focus changes** — count and duration bands for canvas visibility changes, only in an approved opt-in profile. Default: off. | Changes in the visibility state of the Canvas authoring tab. | Destination, off-screen activity, AI use, attention, intent, or cheating. | **FP:** notifications, accessibility software, device switching, technical issues, or ordinary research. **FN:** outside assistance may occur without a focus change. | If enabled: coarse aggregate only for teacher/researcher; browser-level events protected. Never collect without separate approval and consent. |
| **Canvas AI interaction events** — immutable counts/types used to derive `E_any` and `E_content`; no transcript content in the metric export. | That the defined Canvas platform event occurred. | That a response was used, the text was submitted, authorship, understanding, or any AI use outside Canvas. | **FP:** none for the narrow fact of a successfully logged platform event, but logs can be incomplete or misclassified. **FN:** failed logging, offline/error paths, or any outside-Canvas assistance is not captured. | Privacy-protected analysis layer and post-lock authorised researcher only. Never in the teacher view or a predictor input. |

The study may record a consented, non-biometric baseline drafting task to describe ordinary within-person
variation. It must not create a typist identity profile, be used for discipline, or be presented as
a ground truth for authorship. Self-described writing fluency, language background, input method,
accessibility tools, and device class are optional contextual variables, with a `prefer-not-to-say`
option and an analysis plan for missingness.

## 4. Primary outcomes and analysis

### Outcomes

The apparatus evaluates two related but non-interchangeable comparisons:

1. **Event-reference validity (primary):** blinded `E_any` research judgments against the locked
   `E_any` event record. Repeat for `E_content` as a secondary outcome.
2. **Allocation agreement (secondary):** blinded profile judgments against locked allocation `Z`.
   This evaluates whether the neutral view leaks or reflects profile-associated behaviour; it does
   not prove AI interaction.

For each binary blinded judgment and reference label, report the confusion matrix, sensitivity,
specificity, precision (positive predictive value), recall (sensitivity), false-positive rate,
false-negative rate, and the observed event prevalence on which precision depends. Confidence is
recorded on a pre-specified 0–100 scale or fixed ordered categories. Report calibration plots,
calibration-in-the-large, calibration slope where estimable, and Brier score for the confidence
mapping, without converting confidence into an operational integrity score.

For each continuous metric, report missingness, distribution by reference group, pre-specified
direction if one exists, effect size with uncertainty interval, and overlap. A univariate ROC curve
may be descriptive only where its direction was fixed in advance; it is not a deployed classifier.
The primary analysis does not fit or release a composite prediction model. Direct Canvas AI event
fields are excluded from every metrics-only analysis and from the assessor display to avoid the
tautology of "detecting" a field already known to Canvas.

Where sample size permits, use two-sided 95% confidence intervals (Wilson or exact binomial intervals
for rates; bootstrap intervals for suitable derived quantities), state the method, and avoid a
definitive accuracy conclusion when intervals are wide. Report estimates even for null, adverse,
or inconclusive outcomes. Precision is local to the study prevalence and must not be transported to
another course without new evidence.

### Accounting for ordinary drafting and confounding

The pre-registered analysis first reports unadjusted results, then adjusted descriptive models with
task form or task type, course/cohort, baseline ordinary-drafting measures where available, writing
fluency, language background, input method/accessibility tools, device class, and relevant planned
interactions. Adjustment changes neither the reference label nor the unadjusted fairness report.
It can clarify whether apparent signal follows ordinary drafting patterns; it cannot make a harmful
error pattern acceptable.

Strata with inadequate consent, low counts, or unsafe re-identification risk are suppressed and
reported as unavailable rather than silently pooled. The analysis records which comparisons were
estimable. No deficit interpretation is assigned to a group.

## 5. Preregistration-ready experimental protocol

### Design, eligibility, and allocation

- Start with a low-stakes or ungraded feasibility assignment. A graded study may proceed only after
  ethics approval and a documented, independently reviewed grading-equivalence and grade-protection
  plan establish that participation and allocation cannot disadvantage a student.
- Before recruitment, register the question, apparatus version, profiles, task set, learning
  objective, metric schema, reference-event definitions, hypotheses, sample-size rationale,
  exclusions, missing-data handling, outcome thresholds, analysis scripts or pseudocode, retention,
  and stopping rule. Time-stamp and hash the registration.
- Recruit only participants with the required consent, assent, guardian permission, ethics approval,
  or documented exemption. Declining or withdrawing must not affect grade, access, teacher approval,
  or discipline. Provide a non-research route to the same learning activity.
- Allocate consenting students server-side after eligibility, using `server-side-stratified-block-v1`.
  Strata, block-size policy, randomness source, allocation seed escrow, and fallback for technical
  failure are declared before the first allocation. The allocation service stores an immutable
  sealed record and profile snapshot.
- Use equivalent task materials, time, normal authoring surface, rubric, learning objective, and
  submission rule in both profiles. Counterbalance equivalent task forms when task order matters;
  record the form. Do not infer that allocation controlled AI use outside Canvas.

### Two-pass assessor-blind procedure

1. **Authoring and submission:** Canvas enforces the assigned immutable capability policy. The
   enabled policy retains bounded collaborative AI and integrity constraints; the disabled policy
   removes Canvas AI only. The protected layer derives the frozen metric schema.
2. **Pass 1 — grading:** the teacher grades the submitted work against the normal rubric without
   `Z`, event labels, transcript, raw event logs, or research interpretation. The grade and grading
   timestamp are locked.
3. **Pass 2 — research judgment:** separately, an assessor sees a de-identified, standardised
   metrics summary for every submitted episode in a randomized display order. For each, they record
   a binary profile judgment, a binary `E_any` judgment, confidence for each, and an optional
   constrained rationale selected from non-diagnostic metric categories. These records are locked.
4. **Release and analysis:** only after both locks are attested does the allocation custodian release
   the minimum pseudonymised `Z`, `E_any`, and `E_content` fields to the authorised research role.
   The pre-registered analysis runs without grade modification. Any protocol deviation is recorded
   before analysis and reported.

### Exclusions, adherence, and missing data

The pre-registration declares exclusions before labels are released. Suitable examples are an
unrecoverable platform-log failure, a duplicate submission episode, a profile-enforcement failure,
or absence of consent for research use. A student is never excluded because their metrics appear
unusual, a judgment is inconvenient, or an external-AI suspicion exists.

Report flow by allocation, eligibility, consent, completion, valid telemetry, judgment completion,
and analysis inclusion. Analyse allocation (`Z`) by intention to treat. Analyse `E_any` and
`E_content` as observed event-reference comparisons and label them non-causal. For missing metrics,
missing assessor judgments, and withdrawals, report counts and reasons by allocated profile; use the
pre-registered complete-case approach plus appropriate sensitivity analyses if assumptions are
plausible. Never impute a Canvas AI event from revision metrics.

### Sample size and decision interpretation

Before the formal pilot, simulate the registered analysis across plausible event prevalence, event
logging failure, observer agreement, subgroup sizes, and non-differential ordinary drafting. Choose
a target sample that can estimate the primary error rates and pre-specified fairness contrasts with
useful interval width; do not use a post-result power calculation as validation evidence. The
feasibility phase reports process rates and uncertainty rather than claiming the apparatus passes
an accuracy standard.

Any interpretation bound — for example, a maximum tolerable false-positive rate for a *research-only*
judgment, a calibration tolerance, or a subgroup-disparity bound — is set with ethics and assessment
governance before data access. It cannot be relaxed after results. The default consequence of a
missed bound, a wide interval, or a fairness concern is non-endorsement for expanded use, not a
search for a more opaque score.

## 6. Required Canvas capability extension: `experimental-assignment-condition`

This is a general comparative-study capability, not a detection feature and not a request to
implement it here. It must support arbitrary reviewed assignment profiles and outcomes, including
future non-AI education studies.

### Capability contract

| Capability element | Required behaviour |
|---|---|
| **Study definition** | Stores a study ID, apparatus/version, protocol and ethics references, eligible population rule, task-set version, allocation protocol, profile identifiers, masking plan, metric schema, retention policy, and reproducibility-packet schema. It does not encode a cheating label. |
| **Server-side allocation** | Allocates after eligibility with a recorded randomisation method, strata, time, sealed randomness record or escrow reference, and immutable profile snapshot. A client may not choose or alter a condition. Retries and technical exceptions are audit events. |
| **Immutable profiles** | Binds each allocated student to a complete assignment profile with the same assignment context, authoring surface, accessibility baseline, and submission path. Condition-specific capability policies may enable or disable bounded Canvas AI or other future study features. Profile changes create a new version, never rewrite a prior allocation. |
| **Policy enforcement** | Enforces condition capabilities server-side and records enforcement or failure without exposing treatment evidence in assessor surfaces. Existing Canvas AI safety, collaboration, and academic-integrity constraints remain in force. |
| **Condition-neutral metrics view** | Generates the same versioned, de-identified revision-metrics display for every episode; suppresses allocation, direct treatment event types/counts/timestamps, transcript content, raw text, and any field that reveals a profile. It has an accessibility review and a masking test. |
| **Role separation** | Separates teacher/assessor, researcher, allocation custodian, and protected analysis service permissions. No single ordinary role can grade, inspect raw treatment evidence, and release labels. Least-privilege access is the default. |
| **Data lock and reveal** | Enforces ordered locks for grade and research judgment, then permits only the authorised minimum label reveal. Every reveal records actor, purpose, scope, time, approval, dataset identifier, and result. Records are append-only and independently reviewable. |
| **Reproducibility export** | Produces a versioned packet with apparatus and Canvas versions, resolved profiles, configuration hashes, allocation method, metric schema, display schema, analysis plan, data dictionary, retention/de-identification statement, and reveal-audit digest. Public export contains no student-identifiable text, transcripts, raw revision trace, or identity mapping. |

### Permission model

| Permission | Teacher / assessor | Researcher | Allocation custodian |
|---|---|---|---|
| Create a study from reviewed profiles | May request; may not modify allocated profile values. | May prepare a protocol draft; cannot self-authorise a live study. | May activate only after required approvals. |
| Allocate or change a student condition | No | No | Allocate once; no silent changes. |
| Grade submitted work | Yes, before release | No | No |
| View raw AI transcript/event log or raw revision trace | No | Not by default; only a separately approved protected-analysis route, never for grading. | Only sealed metadata needed to administer release, not content by default. |
| View neutral metrics summary | Yes, Pass 2 only | Quality-control aggregate before release; pseudonymised analysis table after release. | Only as needed to audit release. |
| Reveal `Z`, `E_any`, or `E_content` | No | May receive authorised pseudonymised release after locks. | Performs and logs approved release. |
| Export public reproducibility packet | May view approved aggregate report. | May prepare de-identified export. | Confirms no sealed mapping or raw data is included. |

The capability is reusable because `condition` points to policy profiles rather than to "AI use" or
"detection." A future study could compare feedback timing, scaffolding, accessibility supports, or
other reviewed policies with the same allocation, masking, locking, and packet mechanisms.

## 7. Privacy, consent, fairness, and grading-equivalence plan

### Privacy and consent

- Collect the minimum data necessary for the registered metrics. Do not collect clipboard contents,
  raw student text, raw AI transcripts, application history, other-device activity, or location in
  the research export. Do not publish any raw student text, transcript, identifiable trace, or
  identity-to-condition mapping.
- Explain in accessible language what Canvas records, what it cannot know, who sees each layer,
  retention and deletion rules, withdrawal limits once data are de-identified or aggregated, and
  that metrics are research context for a human judgment—not proof of misconduct.
- Obtain all required consent, assent, guardian permission, ethics approval, data-protection review,
  or documented exemption before research collection. Use purpose limitation, role-based access,
  encryption, retention limits, and an incident-response route appropriate to the institution.
- The default focus/visibility setting is off. Enable it only when necessary to the registered
  question, ethically approved, separately consented, demonstrably proportionate, and amenable to
  a meaningful non-participation route.

### Fairness and accessibility

- Co-design the neutral view, consent materials, task route, and metric definitions with accessibility
  and language-support expertise before enrolment. Test keyboards, speech input, screen readers,
  assistive writing tools, intermittent connectivity, shared devices, and multilingual authoring as
  legitimate drafting pathways—not anomaly cases.
- Pre-register which fairness comparisons are warranted, why each contextual variable is collected,
  how small cells are protected, and how materially harmful error will be handled. Report both
  adjusted and unadjusted error, calibration, missingness, and burden where estimable.
- Treat evidence of false positives, false negatives, differential calibration, privacy burden,
  unusable accessibility experience, or null discrimination as substantive findings. Do not tune a
  student-facing flag to make these results disappear.

### Grades and participation

The default phase is low-stakes or ungraded. Participation, refusal, withdrawal, allocation,
research judgment, and any metric must have no effect on grades, access, teacher approval, or
discipline. The teacher's Pass 1 grade is separated from Pass 2 and may never be retroactively
changed using a research view.

For any proposed graded expansion, an ethics-reviewed grading-equivalence and grade-protection plan
must be attached to the protocol before recruitment. It must explain why unequal AI availability
cannot produce unequal assessment disadvantage, how alternatives and accommodations remain fair,
how ordinary grading is kept blind, and how the study task's grade is protected if equivalence is
not defensible. If that plan is not approved, the study remains ungraded.

## 8. Provenance and reproducibility packet

The allocation custodian exports a signed, versioned packet after the required locks. It has a
restricted research form and a safely shareable form; neither contains raw student text, Canvas AI
transcripts, raw revision traces, browser history, or identity mapping.

| Packet component | Contents | Shareability |
|---|---|---|
| `manifest` | Apparatus ID/version, Canvas version/build, study ID, packet version, creation time, hashes, licences, and retention class. | Shareable after review. |
| `protocol` | Frozen research question, hypotheses, eligibility, consent/ethics reference, task-set version, sample-size rationale, exclusions, missing-data plan, stopping rule, and analysis-plan hash. | Shareable after review. |
| `profiles` | Fully resolved immutable profiles, condition-specific policy snapshots, capability versions, and configuration hashes. | Shareable after review. |
| `allocation` | Randomisation method, strata definition, allocation time range, escrow/commitment identifier, profile counts, technical exceptions, and release-audit digest. The seed and identity mapping remain sealed. | Aggregate/commitment only. |
| `metrics` | Metric schema version, derivation specification, display schema, validity limits, missingness codes, suppression rules, and code or pseudocode hash. | Shareable after review. |
| `analysis` | Pseudonymised analysis dataset schema, reference-label definition, output tables, interval methods, fairness comparison definitions, and executed-analysis hash. | Restricted dataset; schema and aggregate outputs shareable. |
| `provenance` | Consent and ethics status, de-identification method, data location class, retention/deletion schedule, deviations, reveal audit, and approver roles. | Shareable in redacted form. |

The packet records `apparatus: {id, version, configuration}` and `canvas: {version}` for every
future evidence contribution. It makes the research process inspectable without making student
work inspectable.

## 9. Explicit non-claims and failure conditions

### Non-claims enforced by the apparatus

- No output detects or rules out AI use outside Canvas, on another device, manual retyping, copied
  work, collaboration, another person's work, or any unrecorded process.
- No revision metric proves authorship, learning, understanding, intent, academic-integrity status,
  or misconduct.
- A recorded Canvas AI interaction proves only that the defined platform event was logged; it does
  not prove that AI output entered, remained in, or determined the submission.
- The apparatus does not create an automated integrity score, risk band, alert, disciplinary record,
  grade modifier, or admissions/advancement decision.
- Results apply only to the declared apparatus version, Canvas version, profiles, tasks, participants,
  event definitions, and local prevalence. They do not validate a general detector.

### Failure conditions with useful results

The apparatus must report non-endorsement for the proposed research use, or stop a phase pending
review, when any pre-registered condition occurs, including:

- insufficient consent, ethics approval, privacy protections, or grade-equivalence evidence;
- profile leakage, allocation immutability failure, missing audit records, inaccurate event logging,
  or an assessor view that exposes a direct treatment field;
- no practically useful discrimination, wide uncertainty, poor calibration, excessive false positives
  or false negatives, or condition judgments no better than chance after accounting for uncertainty;
- materially unequal error, confidence, burden, access, or missingness for a pre-specified group,
  or insufficient evidence to rule out a material disparity;
- task- or ordinary-drafting dependence so strong that a result cannot support the stated scope;
- participant harm, coercion, an inaccessible workflow, unacceptable data exposure, or an attempt to
  repurpose a research result for grading or discipline.

These outcomes are findings about the limits of revision tracking. They are not failures to be
hidden by a more complex model.

## 10. Phased implementation plan

| Phase | Purpose and permitted work | Gate to next phase |
|---|---|---|
| **1. Simulated data** | Create only synthetic event traces spanning ordinary drafting, pasted self-authored notes, speech input, assistive tools, interruptions, late drafting, and recorded Canvas AI events. Test metric derivations, masking, data locks, audit logging, uncertainty code, and failure detection. No claim about students or real-world validity. | Metric schema, neutral view, allocation protocol, and preregistration materials are frozen; simulations demonstrate that direct event fields cannot leak. |
| **2. Internal feasibility** | With staff volunteers or equivalent non-student participants and approved synthetic/voluntary tasks, test allocation, profile enforcement, data minimisation, de-identification, two-pass ordering, usability, accessibility, and reproducibility export. Do not make accuracy claims. | Independent internal audit finds no critical masking, privacy, accessibility, or lock failure; protocol and retention plan are ready for ethics review. |
| **3. Ethics-reviewed low-stakes pilot** | Recruit consenting students for an ungraded or low-stakes task under the registered protocol. Estimate completion, event prevalence, metric quality, assessor agreement, error, calibration, burden, missingness, and fairness with intervals. Publish only approved aggregate/de-identified evidence. | Ethics and governance review finds the results, including nulls and harms, support a carefully bounded replication question. A graded expansion requires a separate approved equivalence plan. |
| **4. Independent challenge and replication** | An independent team, Canvas deployment, assessor group, and task family rerun the frozen protocol or explicitly versioned variation. Include adversarial but legitimate drafting pathways and challenge the masking, labels, fairness analyses, and claimed use. | Results enter the evidence and finding process only with preserved disagreements, limitations, and provenance; contradictory results remain visible. |

## Status and versioning

- `status: draft`; `implementation_status: blocked`. This is a design proposal. It implements no
  Canvas capability, collects no student data, and asserts no evidence result. The blocking
  capability and public development trail are recorded in [feature request #1][feature-request].
- Apparatus version `0.1.0` fixes the proposed profile pair, two-pass method, metric schema label,
  reference-event definitions, and boundary statements. A change to any of these is a comparability
  decision requiring a new apparatus or metric-schema version.
- Evidence belongs in the apparatus-owned [evidence collection](evidence/index.md), with the required
  consent, anonymisation, configuration, Canvas-version, and provenance record. Observation,
  measurement, interpretation, and limitations remain in their separate evidence-bundle documents.

[feature-request]: https://github.com/evaluchat/research/issues/1
