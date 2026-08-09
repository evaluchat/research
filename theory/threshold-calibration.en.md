---
type: Research Question
id: threshold-calibration
lang: en
status: open
title: Threshold calibration — what counts as sufficient dialogic contribution?
description: "Central research question: how the drafting-unlock threshold should vary by task type, proficiency level, language background, and learner strategy."
tags: [camdle, research-question, threshold, equity]
created: 2026-08-09T14:00:00Z
generated: { by: opencode-go/deepseek-v4-flash, at: 2026-08-09T14:00:00Z }
sources:
  - id: camdle-white-paper
    resource: https://docs.evaluchat.com/research/camdle-white-paper.pdf
    title: CAMDLE white paper (docs.evaluchat.com/research/)
  - id: research-apparatus-concept
    resource: https://github.com/evaluchat/knowledge/blob/main/concepts/research-apparatus.en.md
    title: Research apparatus — reproducible research on Canvas (knowledge catalog)
---

# Threshold calibration — what counts as sufficient dialogic contribution?

## The question

> What counts as sufficient dialogic contribution to unlock drafting support, and how does that threshold vary by task type, proficiency level, language background, and learner strategy?

This is the central research question of the CAMDLE programme (see [CAMDLE — constrained AI-mediated dialogic writing (theory, unproven)](camdle.en.md)).

## Why it matters

The drafting-unlock threshold is the one manipulable variable the CAMDLE design introduces into writing education. Because the design makes substantial drafting assistance conditional on prior dialogic contribution, the threshold can be set, varied, pre-registered, and compared — a pedagogical constraint becomes a research variable.

A miscalibrated threshold fails in one of two directions. If the threshold is too low, the constraint is inert: the assistant behaves like an ordinary chatbot, and the design contributes nothing beyond unconstrained assistance. If the threshold is too high, it becomes friction that learners route around — gaming the dialogue, pasting prefabricated text, or abandoning the environment — which distorts the very process evidence the design is meant to expose. Calibration is therefore an empirical question about learning, equity, usability, and circumvention, not a design preference.

## Sub-questions

- **Task type variation.** Does the appropriate threshold differ between task types — for example argumentative essays, summaries, and reflective writing?
- **Proficiency variation.** Does a single threshold disadvantage lower-proficiency learners, who may need more assistance earlier?
- **L1 background variation.** Do learners from different first-language backgrounds interact with the dialogue-and-draft structure differently?
- **Learner strategy variation.** Do differences in planning, note-taking, and revision strategies change how much contribution precedes drafting?
- **Equity.** Could a single lexical or turn-volume threshold disadvantage particular proficiency levels, L1 backgrounds, disabilities, or communication styles?

## Evidence needed

- A structured comparison of pre-registered threshold policies, including an unconstrained-assistance condition where appropriate, in an EAP or L2 academic writing context.
- Measures: independent writing improvement (blinded baseline and post writing), quality of learner explanations, and evidence-centred process-and-outcome measures (dialogue and revision traces, motivation, agency, workload, circumvention).
- Note: a higher final essay score alone is insufficient. The primary endpoint must be specified before deployment; quality of the supported product does not demonstrate learning.

## Related

- [CAMDLE — constrained AI-mediated dialogic writing (theory, unproven)](camdle.en.md)
- [The apparatus as research instrument](../methods/apparatus.en.md) — the instrument view: what dialogic contribution means as a measured quantity, what process signals record, and how evidence must cite apparatus identity and configuration.
- [Research apparatus — reproducible research on Canvas (knowledge catalog)][research-apparatus-concept] — the apparatus pattern: four-dimension invariant, versioning, and the Apparatus → Version → Configuration → Experiment model.

Translations: none yet — contribute one via PR (see CONTRIBUTING.md).

[research-apparatus-concept]: https://github.com/evaluchat/knowledge/blob/main/concepts/research-apparatus.en.md
