---
type: Research Question
id: revision-tracking-validity-question
lang: en
origin: native
status: open
title: Revision-tracking validity — when can process metrics provide fair evidence about recorded Canvas AI assistance?
description: "Primary research question for Apparatus #3: whether a frozen, condition-neutral revision-metrics protocol can validly, fairly, and usefully distinguish a recorded Canvas AI assistance event from no recorded Canvas AI event under assessor-blind study conditions."
tags: [research-question, process-evidence, revision-tracking, assessment-validity, fairness, ai]
created: 2026-08-11T10:02:43Z
timestamp: 2026-08-11T10:02:43Z
generated: { by: codex/gpt-5, at: 2026-08-11T10:02:43Z }
sources:
  - id: testing-standards
    resource: https://www.testingstandards.net/uploads/7/6/6/4/76643089/standards_2014edition.pdf
    title: Standards for Educational and Psychological Testing (AERA, APA, & NCME, 2014)
  - id: kane-validity
    resource: https://eric.ed.gov/?id=EJ996447
    title: Kane (2013), Validating the Interpretations and Uses of Test Scores
  - id: apparatus-method
    resource: https://github.com/evaluchat/research/blob/main/methods/apparatus.en.md
    title: The apparatus as research instrument (research catalog)
---

# Revision-tracking validity — when can process metrics provide fair evidence about recorded Canvas AI assistance?

## Framing question

> **Under a randomly allocated, assessor-blind assignment condition, to what extent can a
> pre-specified, condition-neutral revision-metrics protocol distinguish an authoring episode with
> a recorded Canvas AI assistance event from one with no recorded Canvas AI event, and are its
> errors, confidence, burdens, and subgroup differences acceptable for the proposed research use?**

This is the theory question for [Apparatus #3 — revision-tracking validity](../apparatus/revision-tracking-validity/revision-tracking-validity.en.md).
It asks whether a narrow process-evidence interpretation can be supported, not whether a student
used AI in general, authored the work, or acted with or without integrity.

## Terms that must remain separate

| Term | Defined meaning in this research | It does not mean |
|---|---|---|
| `Z` — allocated condition | The server-recorded immutable assignment profile: `canvas-ai-enabled` or `canvas-ai-disabled`. | Whether a student actually used assistance, learned more, or authored the work. |
| `E_any` — recorded Canvas AI event | At least one eligible Canvas AI request completed for the assignment authoring episode. Canvas knows this platform event. | That any AI response affected the submitted text. |
| `E_content` — recorded content-affecting Canvas AI event | A recorded Canvas AI insertion or transformation of content in the assignment canvas. This is a secondary, narrower event label. | That the displayed content remains in the submission, was understood, or was authored by the student. |
| `E = 0` | No eligible Canvas AI event was recorded by Canvas for that episode. | No AI, copying, retyping, collaboration, or other assistance occurred elsewhere. |
| Revision metric | A derived description of recorded editing activity under the study's metric schema. | Proof of authorship, intent, learning, misconduct, or a reliable integrity score. |

Random allocation can estimate the consequences of making bounded Canvas AI available (`Z`). The
event-labelled comparison (`E_any` or `E_content`) is a validity comparison against a known
platform record, but it is not a causal estimate of AI use: students who choose to interact with
Canvas AI can differ from students who do not. Both analyses are useful only when their different
targets are named.

The intended interpretation is deliberately narrow: a frozen metrics display or a blinded
research judgment may be associated with the presence of a *recorded Canvas event* in this study.
The interpretation requires evidence about representation, generalisation, explanation, and
consequences; it cannot be promoted to an authorship or integrity inference merely because a
metric is statistically associated with `E`. This follows the interpretation-and-use framing in
the [Standards for Educational and Psychological Testing][testing-standards] and Kane's
argument-based account of validity.[kane-validity]

## Falsifiable primary question and hypotheses

### Primary question

For a held-out or independently assessed set of completed study episodes, do the pre-registered
condition-neutral metrics view and the assessor's recorded `E_any` judgment have discrimination,
calibration, and error rates consistent with the protocol's pre-registered research-use bounds
when compared with the locked Canvas event record?

The primary unit is one submitted assignment authoring episode. The reference standard is the
immutable Canvas event record, released only after grades and research judgments are locked. The
primary judgment asks, *"Does this de-identified metrics summary support `recorded Canvas AI
interaction` or `no recorded Canvas AI interaction`?"* The separate required condition judgment
asks, *"Which allocated profile is more likely?"* It is evaluated against `Z`, not substituted for
`E_any`.

### Primary hypotheses

- **H1 — discriminative signal.** The pre-registered metrics protocol and blinded `E_any` judgment
  show more than chance discrimination of `E_any` in the evaluation set, with uncertainty intervals
  reported. If the observed discrimination is null or the interval includes practically trivial
  discrimination, H1 is not supported.
- **H2 — bounded error and calibration.** Sensitivity, specificity, precision, recall,
  false-positive rate, false-negative rate, and confidence calibration satisfy the explicit,
  context-approved bounds set before data inspection. If a bound is missed, H2 is not supported;
  a positive average association cannot offset the failure.
- **H3 — no material fairness failure.** Error rates and calibration do not show a pre-specified,
  practically material disadvantage for protected or plausibly confounded groups after accounting
  for task and ordinary drafting behaviour. If estimates show such a disadvantage, or are too
  imprecise to rule it out, H3 is not supported.

These are falsifiable protocol hypotheses, not a claim that useful discrimination will be found.
The protocol must specify its chance comparator, acceptable error and calibration bounds, minimum
subgroup precision, and decision rule before inspecting outcome labels. In a small feasibility
study, estimates and intervals are reported without asserting that a bound has been met.

### Secondary hypotheses

- **H4 — event granularity matters.** Diagnostic quantities for `E_content` differ from those for
  `E_any` by more than the pre-specified practically trivial margin. This tests whether chat-only
  and canvas-changing events should be treated as one reference class; it does not assume which
  event will be more discriminable.
- **H5 — ordinary drafting does not wholly explain the result.** The primary event-judgment
  association remains outside the pre-specified practically trivial region after the declared
  adjustment for task and ordinary drafting variables. If it does not, the protocol has not shown
  a revision-specific signal.
- **H6 — assessors can use the view with restraint.** Assessors meet the pre-specified
  comprehension, completion, and burden criteria while correctly endorsing the view's non-claims.
  This hypothesis fails when a view produces over-confidence, unacceptable burden, or confusion
  about its inability to establish authorship or misconduct.

## Secondary questions

- **Allocation agreement:** How accurately and with what confidence do blinded teachers identify
  `canvas-ai-enabled` versus `canvas-ai-disabled` from the standardised metrics view, relative to
  the locked allocation `Z`? An enabled episode with no event is an expected source of disagreement,
  not a labelling error.
- **Event definition:** Do findings differ for `E_any` and the more content-proximal `E_content`?
  A difference would show that chat-only and canvas-changing events should not be collapsed.
- **Metric contribution:** Which individual metrics show distributional separation, overlap, or no
  usable signal after a direction is frozen in advance? Individual metrics are described; none is
  converted into a production score.
- **Ordinary-drafting adjustment:** Do associations persist after task type and pre-study or
  concurrent measures of ordinary drafting cadence, writing fluency, device, language background,
  and approved accessibility tools are accounted for? This is explanatory, not an excuse to erase
  unequal error.
- **Heterogeneity and fairness:** How do accuracy, error, and confidence vary by task type, writing
  fluency, self-described language background, device/input method, accessibility tools, prior
  revision habits, and other pre-registered plausible confounders?
- **Practical usefulness and consequences:** Can assessors use the condition-neutral view
  consistently without material grading burden, privacy intrusion, or harmful over-confidence, and
  do they understand its stated limits?

## Validity argument to test

| Inference | Claim to be tested | Required evidence | Disconfirming result |
|---|---|---|---|
| Representation | The schema records the declared revision events and reports the same neutral view in both profiles. | Event-schema tests, profile snapshots, simulated traces, and masking audits. | Missing, profile-dependent, or incorrectly classified events. |
| Generalisation | Observed signal and error are not an artefact of one task, device, or ordinary drafting style. | Replicated task types, prespecified subgroup analyses, baseline drafting measures, and uncertainty intervals. | Large task or subgroup variation, or uncertainty too wide to support transport. |
| Explanation | A judgment reflects the declared metrics, not access to a condition leak or direct event evidence. | Assessor masking checks, view inspection, reasoning-code audit, and negative-control cases. | Labels can be inferred from a leaked field or judgments lack a stable relationship to the frozen metrics. |
| Consequences | The research use is proportionate and does not create unacceptable privacy, equity, or grading harm. | Consent records, burden measures, withdrawal handling, fairness analysis, and participant/assessor feedback. | Harm, unmanageable burden, or error patterns that make the intended research interpretation unsafe. |

## Non-claims

This question does not test, and no result may be represented as testing:

- AI use outside Canvas, on another device, in another application, or before or after the recorded
  Canvas session;
- manual retyping, copying from notes, collaboration, use of another person's work, or any other
  source of text not recorded by the Canvas event schema;
- authorship, understanding, learning, intent, academic-integrity compliance, or misconduct;
- a generalisable AI detector, an automated integrity score, a cheating verdict, or a grading
  decision.

The corresponding apparatus must preserve these boundaries in its interface, access controls,
analysis plan, and publication rules.

## Related

- [Revision-tracking validity apparatus](../apparatus/revision-tracking-validity/revision-tracking-validity.en.md)
- [The apparatus as research instrument](../methods/apparatus.en.md)
- [AI assignment stress-test validity](ai-assignment-stress-test-validity.en.md) — the related
  assignment-level question; this question concerns process evidence, not the assignment's design.

[testing-standards]: https://www.testingstandards.net/uploads/7/6/6/4/76643089/standards_2014edition.pdf
[kane-validity]: https://eric.ed.gov/?id=EJ996447
