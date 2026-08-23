---
type: Research Question
id: ai-assignment-stress-test-validity
lang: en
origin: native
status: open
title: AI assignment stress-test validity — when can task probes identify what an assessment still measures?
description: "Primary research question for the AI Assignment Stress Test method: when standardized AI task probes provide valid, reliable, and useful evidence about the human capabilities an assignment can still measure in AI-permissive contexts."
tags: [research-question, assessment-validity, ai, task-analysis, measurement-validity]
created: 2026-08-11T09:41:42Z
timestamp: 2026-08-11T09:41:42Z
authors:
  - name: Cronje van Heerden
sources:
  - id: ai-assignment-stress-test-design
    resource: https://github.com/openrigor/knowledge/blob/main/okf/bundles/openrigor/concepts/ai-assignment-stress-test.md
    title: AI Assignment Stress Test — method design (knowledge catalog)
  - id: testing-standards
    resource: https://www.testingstandards.net/uploads/7/6/6/4/76643089/standards_2014edition.pdf
    title: Standards for Educational and Psychological Testing (AERA, APA, & NCME, 2014)
  - id: kane-validity
    resource: https://eric.ed.gov/?id=EJ996447
    title: Kane (2013), Validating the Interpretations and Uses of Test Scores
  - id: evidence-roles
    resource: https://github.com/openrigor/research/blob/main/governance/evidence-roles.en.md
    title: Shared evidence roles — how evidence cites a method (research catalog)
generated: { by: cursor-grok/4.6, at: 2026-08-13T14:48:00Z }
---

# AI assignment stress-test validity — when can task probes identify what an assessment still measures?

## The question

> **To what extent, and under which task conditions, do standardized AI stress-test probes provide
> valid, reliable, and useful evidence about the human capabilities an assignment can still measure
> when generative AI is available?**

This is the primary research question for [AI Assignment Stress Test](../methods/ai-assignment-stress-test/ai-assignment-stress-test.en.md).
It evaluates an assignment-level assessment method, not a student's authorship, integrity, or
learning.

## Why it matters

When an AI system can produce an assignment's expected artefact, that fact alone does not establish
what a student knows, whether a student used AI, or whether the assignment has no educational value.
It does, however, raise a validity question: which inferences about a student's capabilities can the
assignment still support under the conditions in which it is used?

The stress test makes a narrower, inspectable contribution to that question. It standardises a task
probe, documents the model set and prompts, maps potential delegation routes, and presents the result
as a report for human review. Assessment validity concerns the proposed interpretation and use of an
assessment, and the evidence needed to support them; it is not an intrinsic property of a task or a
score alone. [Kane's argument-based account][kane-validity] and the [Standards for Educational and
Psychological Testing][testing-standards] provide the framing for this question.

## Intended interpretation and use

| The report may support | The report does not support |
|---|---|
| A conditional account of which task demands a declared AI model set can discharge under the stated probe configuration. | A verdict that a particular student used AI or authored submitted work. |
| A capability map for expert and teacher scrutiny of what the task can still expose. | A direct measure of learning, knowledge, skill, or future performance. |
| A menu of redesign hypotheses, with stated costs and trade-offs. | A universal ranking of assignments or a claim that one redesign is best. |

The intended use is therefore formative: to help teachers and researchers examine the validity of
assignment designs in AI-permissive contexts. Any stronger claim requires separate evidence.

## Validity argument to test

The research will test the following inferences rather than assuming them.

| Inference | Claim to evaluate | Evidence needed |
|---|---|---|
| Representation | The standardised probe faithfully represents the assignment and the declared delegation condition. | Transparent task inputs, prompts, model versions, rubric handling, and documented deviations. |
| Generalisation | The report is sufficiently stable within a pinned model set and configuration to compare like with like. | Repeated probes, sensitivity analyses, and explicitly versioned model sets and configurations. |
| Explanation | The report's capability map corresponds to defensible expert judgements about the task's intended and observable demands. | Independent, subject-informed task analyses; agreement and disagreement analysis; review of counterexamples. |
| Decision and consequences | Using the report to consider redesign improves the clarity of assessment decisions without unacceptable burden or harm. | Teacher review studies, redesign comparisons, workload data, accessibility and fairness analysis, and unintended-consequence records. |

Failure at any inference is informative. For example, a report that varies materially across repeated
probes may still be useful for exploration, but not as comparable structured evidence.

## Sub-questions

- **Agreement:** When do subject experts agree or disagree with the report's capability map and its
  stated delegation-loss pathways?
- **Stability:** How sensitive are conclusions to model-set version, prompt configuration, rubric
  availability, discipline, task genre, language, and repeat runs?
- **Boundary conditions:** Which assessment designs retain observable evidence of explanation,
  transfer, error detection, argument defence, or AI judgement after an AI completion probe succeeds?
- **Consequences:** Do report-guided redesigns make the intended measurement clearer to teachers and
  learners, and what teacher effort, class time, marking load, accessibility, or fairness costs do
  they introduce?

## Evidence needed

A credible programme begins with a pre-registered and diverse task sample rather than selected
examples that make AI appear unusually capable or incapable. For each task, the evidence bundle
should preserve the assignment artefact, declared intent, probe protocol, model-set version, resolved
configuration, optional rubric, raw probe outputs where they may be shared ethically, and the
assignment-level report.

At minimum, a structured experiment should compare the method report with independently produced
expert task analyses that are blinded to the report until their initial analysis is recorded. It should
report agreement as well as disagreement, repeated-run stability, missing data, and limitations. A
subsequent teacher study may examine the consequences of using the report to redesign a task; it must
not substitute teacher satisfaction for validity evidence.

## Boundaries and ethics

The unit of analysis is the assignment, not the student. The method collects neither student
submissions nor learner process telemetry, and its reports must never be repurposed as authorship
detection or disciplinary evidence. Publication of teacher-supplied assignments and outputs remains
opt-in, with appropriate anonymisation, provenance, and retention records.

## Related

- [AI Assignment Stress Test — assignment-level measurement analysis](../methods/ai-assignment-stress-test/ai-assignment-stress-test.en.md)
- [Shared evidence roles](../governance/evidence-roles.en.md) — distinguishes method,
  intervention, measurement, evidence, and finding.
- [Threshold calibration](threshold-calibration.en.md) — the complementary student-side research
  question for the Essays method.

[testing-standards]: https://www.testingstandards.net/uploads/7/6/6/4/76643089/standards_2014edition.pdf
[kane-validity]: https://eric.ed.gov/?id=EJ996447
