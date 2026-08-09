---
type: Theory
id: camdle
lang: en
status: draft
title: CAMDLE — constrained AI-mediated dialogic writing (theory, unproven)
description: "CAMDLE as a proposed learning design: a generative writing assistant whose drafting support is conditional on prior dialogic contribution — a research agenda, not an efficacy claim."
tags: [camdle, theory, dialogic-writing, ai-mediation]
generated: { by: opencode-go/deepseek-v4-flash, at: 2026-08-09T14:00:00Z }
sources:
  - id: camdle-white-paper
    resource: https://docs.evaluchat.com/research/camdle-white-paper.pdf
    title: CAMDLE white paper (docs.evaluchat.com/research/)
  - id: research-apparatus-concept
    resource: https://github.com/evaluchat/knowledge/blob/main/concepts/research-apparatus.en.md
    title: Research apparatus — reproducible research on Canvas (knowledge catalog)
---

# CAMDLE — constrained AI-mediated dialogic writing (theory, unproven)

## Overview

CAMDLE (Constrained AI-Mediated Dialogic Language Education) is a **proposed learning design** for writing education with generative AI: a conversational AI writing partner supports learners through dialogue and drafting, but substantial drafting assistance is released only after the learner has first contributed ideas, evidence, questions, and language through dialogue. The constraint is not intended to prove who typed each word. It functions as a pedagogical condition: the learner must negotiate meaning before more powerful assistance becomes available, while the system retains the responsiveness and scalability that make generative AI educationally significant.

CAMDLE is a **proposed synthesis and a research agenda, not a completed study**. The component theories below are established research traditions; their combination, implementation, and predicted effects are not established by the existence of those traditions. This document makes no efficacy claims. A prototype implementation exists as a research apparatus; the apparatus is not evidence that the proposed mechanism works.

The design responds to a sharpened version of Bloom's (1984) 2-sigma challenge: generative AI makes scalable, responsive assistance technically plausible, but it also automates the planning, linguistic, and evaluative activity that writing instruction is meant to develop. CAMDLE proposes dialogic constraint as a way to keep the learner's contribution visible and consequential.

## The construct

Five principles define the construct:

1. **Dialogic contribution precedes substantial generation.** Learners articulate, question, select, or defend ideas before higher-powered assistance becomes available.
2. **The constraint is proportional, not absolute.** Learners may use assistance; the design regulates when and how much assistance is available.
3. **The learner remains the executive controller.** The learner evaluates, accepts, rejects, and revises AI suggestions.
4. **Process is evidence, not verdict.** Dialogue and revision traces support teacher interpretation without pretending to prove authorship.
5. **The threshold is an empirical variable.** It must be calibrated against learning, equity, usability, and circumvention outcomes.

## Theoretical synthesis

- **Sociocultural theory and the zone of proximal development** (Vygotsky, 1978). Assistance should be contingent on what a learner can currently do with support. Operationally, the ZPD is treated as a task- and time-specific difference between independent performance and performance with contingent assistance — not a latent quantity readable from message length or an unlock threshold. When the "more knowledgeable other" is a language model, the term describes a functional role in a particular interaction, not a claim that the system is a teacher or globally more knowledgeable than the learner.
- **Extended mind and cognitive offloading** (Clark & Chalmers, 1998; Risko & Gilbert, 2016). External artefacts can participate in cognitive activity when actively integrated into problem solving; the educational effect depends on what is offloaded and what the learner continues to control. CAMDLE distinguishes **strategic offloading** of operational burdens (syntax, formatting, routine retrieval) from **substitutive offloading** of conceptual work (warranting an argument, adopting a stance, deciding what a revision should accomplish). This is a hypothesis about interaction and learning, not a fact inferable from a single metric.
- **Self-regulated learning** (Zimmerman, 2000). Cycles of forethought, performance, and self-reflection are the model; the interface makes planning, composing, evaluating, and revising available for study. It does not automatically produce self-regulation.
- **Cognitive process writing** (Flower & Hayes, 1981; Bereiter & Scardamalia, 1987). Composing is recursive planning, translating, reviewing, and knowledge transformation. The relevant outcome is not "more chat" or "more text," but better explanations, decisions, and substantive revision.
- **Formative assessment** (Black & Wiliam, 1998). Evidence is used during learning to improve the learner's next move. Generative dialogue is only formative when feedback is understood, evaluated, and acted upon — the teacher remains in the interpretive loop.
- **Bloom's 2-sigma challenge** (Bloom, 1984). One-to-one tutoring with mastery-learning techniques produced large achievement gains relative to ordinary classroom instruction, motivating the search for scalable approximations. CAMDLE treats this as a **design problem** — a reason to build and test a scalable dialogic apparatus — **not a claimed outcome**. No measured 2-sigma gains are claimed, and an engagement unlock is not equated with mastery learning.

## Research propositions

Six propositions structure the research programme:

1. **Threshold calibration:** there is a range of contribution levels at which additional AI drafting support improves progress without reducing explanation, evaluation, or revision.
2. **Conditional assistance:** compared with unconstrained assistance, conditional assistance increases sessions containing learner-generated explanations, questions, or revisions.
3. **Learning transfer:** a better supported text does not demonstrate learning; transfer requires independent or delayed writing, explanation, or revision tasks.
4. **Input and output:** exposure, transcription, and learner-generated production may have different effects and should remain an open comparison.
5. **Equity:** a single lexical or turn-volume threshold may disadvantage different proficiency levels, L1 backgrounds, disabilities, or communication styles.
6. **Teacher interpretation:** process evidence is most defensible when read with the transcript, draft, assignment context, and student explanation.

## Boundary statements

- **No efficacy claims are made.** This document does not establish that CAMDLE improves language proficiency, writing quality, critical thinking, or academic integrity outcomes.
- **Process signals are mechanical observations, not authorship proof.** Keystrokes, paste events, focus changes, and interaction counts may prompt a conversation, but they do not prove who authored a sentence or whether learning occurred.
- **Dialogue volume is not language quality.** More chat or more text is not evidence of better explanations, decisions, or revision.
- **Results from one context may not generalise.** Effects observed in one age group, genre, language, or institution may not transfer to another.

## Evidence map

| Literature stream | Supports | Does not establish |
| --- | --- | --- |
| Process writing | Recursive planning, translating, and reviewing | That chat logs proxy all composing cognition |
| Formative assessment | Feedback can improve the next learning move | That AI feedback equals expert teacher feedback |
| Bloom 2-sigma / tutoring | One-to-one tutoring plus mastery techniques can produce large gains; scalable approximations are a long-standing design problem | That GenAI dialogue produces 2-sigma gains, or that an engagement unlock equals mastery learning |
| Self-regulated learning | Planning, monitoring, and reflection matter | That interface activity represents self-regulation |
| Cognitive offloading | External tools can reduce task burden | That offloading improves durable learning |
| GenAI writing reviews | AI can support fluency, organisation, feedback, and language development | That unconstrained assistance produces independent proficiency |
| L2 / EAP writing | AI raises questions of voice, critical literacy, and equity | That machine fluency is a fair human benchmark |
| Process-based AI assessment | Interaction traces can be analysed as candidate evidence | That any trace is a validated learning measure |

## Research apparatus

The CAMDLE design is instrumented on Canvas as **Apparatus #1 (Essays)** — a reproducible configuration of Canvas capabilities, workflows, and measurements. The instrument view — what dialogic contribution means as a measured quantity, what process signals conceptually record, and how evidence cites apparatus identity and configuration — is defined in [The apparatus as research instrument](../methods/apparatus.en.md). The pattern itself (four-dimension invariant, versioning, configuration model) is defined in the knowledge catalog as the [research-apparatus-concept].

## Status

`status: draft`. This document is a proposal; nothing here is established by the existence of the cited traditions. The central open question is threshold calibration — see [Threshold calibration — what counts as sufficient dialogic contribution?](threshold-calibration.en.md).

Source: [CAMDLE white paper (PDF)](https://docs.evaluchat.com/research/camdle-white-paper.pdf)

Translations: none yet — contribute one via PR (see CONTRIBUTING.md).

[research-apparatus-concept]: https://github.com/evaluchat/knowledge/blob/main/concepts/research-apparatus.en.md
