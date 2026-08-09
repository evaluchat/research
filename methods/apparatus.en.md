---
type: Reference
id: apparatus
lang: en
origin: native
status: draft
title: The apparatus as research instrument — measurement, observation, evidence
description: "Instrument view of a Canvas research apparatus: what dialogic contribution means as a measured quantity, what process signals conceptually record, the threshold as a research variable, and how evidence cites apparatus identity and configuration."
tags: [apparatus, methods, measurement, evidence, provenance, camdle]
generated: { by: opencode-go/deepseek-v4-flash, at: 2026-08-09T16:40:00Z }
sources:
  - id: research-apparatus-concept
    resource: https://github.com/evaluchat/knowledge/blob/main/concepts/research-apparatus.en.md
    title: Research apparatus — reproducible research on Canvas (knowledge catalog)
  - id: apparatus-recipe
    resource: https://github.com/evaluchat/knowledge/blob/main/playbooks/apparatus-recipe.en.md
    title: The apparatus recipe — from research question to built apparatus (knowledge catalog)
  - id: essays-workflow
    resource: https://github.com/evaluchat/knowledge/blob/main/concepts/essays-workflow.en.md
    title: Essays workflow — proportional drafting unlock (knowledge catalog)
  - id: camdle-white-paper
    resource: https://docs.evaluchat.com/research/camdle-white-paper.pdf
    title: CAMDLE white paper (docs.evaluchat.com/research/)
---

# The apparatus as research instrument — measurement, observation, evidence

> `status: draft`. This reference defines the *instrument view* of a research apparatus: what it measures, how measurement relates to evidence, and how evidence must cite the apparatus that produced it. It is the research-catalog counterpart of the [research-apparatus-concept] knowledge concept and the [apparatus-recipe] playbook.

## The instrument view

A research apparatus is a reproducible configuration of Canvas capabilities, workflows, and measurements designed to investigate one or more research questions and produce specified evidence. From the research catalog's point of view, the apparatus is an **instrument**: it turns a designed workflow into recorded observations that can later be submitted as evidence.

The Essays assignment flow (Apparatus #1) is the reference instance — see [CAMDLE — constrained AI-mediated dialogic writing (theory, unproven)](../theory/camdle.en.md) for the construct and [Threshold calibration — what counts as sufficient dialogic contribution?](../theory/threshold-calibration.en.md) for the central research question it serves.

## Dialogic contribution as a measured quantity

CAMDLE's design makes drafting support conditional on prior dialogic contribution. To study that design, "dialogic contribution" must be treated as a **measured quantity**: a count of the learner's contributions along the dialogue-and-drafting workflow, aggregated per session, per phase, and per learner.

At the abstraction level of this catalog, the quantity is defined by the apparatus's *threshold policy*: the apparatus declares which learner actions count toward contribution and how many are required before drafting support unlocks. The concrete definition of a countable contribution lives in the apparatus's own manifest and concept (per-apparatus, not universal), and **the threshold is a research variable, not a design constant** — its calibration is the subject of [threshold-calibration].

Exactly which low-level signals feed the count is an implementation matter of the apparatus (the knowledge catalog's [essays-workflow] concept describes the shipped process-signal categories). This reference deliberately does **not** specify telemetry blueprints, internal analytics, or orchestration internals — the public record describes what is measured and why, not how the measurement machinery is built.

## What process signals conceptually record

Process signals are the apparatus's measurement layer. Conceptually they record categories of learner activity:

- **Composition activity** — how the learner's text is produced (typing, bursts, revisions to the document).
- **Verbatim insertion** — pasted or copied content entering the document.
- **Engagement continuity** — focus, interruption, and time-in-phase patterns.

These categories are **observations about how work came together**; they are not authorship detection, not integrity scores, and not evidence of learning. The boundary is explicit in the product concept ([essays-workflow]) and is preserved here: signals are context for human judgment, recorded so that a teacher or researcher can read them alongside the transcript, the draft, and the assignment context.

## Measurement, observation, evidence — the separation

The epistemic spine of the apparatus platform keeps four terms distinct (see [research-apparatus-concept]):

| Term | What it is | Example |
|---|---|---|
| **Apparatus** | What is intended to be investigated (the configured workflow) | Essays apparatus: dialogic constraint before drafting |
| **Intervention** | What the apparatus actually does to the user's workflow | Drafting unlocks after N dialogic contributions |
| **Measurement** | What the apparatus records (mechanism, not evidence) | Engagement metrics / process signals |
| **Evidence** | What can subsequently be submitted to Research | "Student spent 12 min in Socratic phase" (observation) |

The evidence-bundle shape enforces this separation: `observations` and `results` hold what was recorded, `reflection` holds interpretation, `limitations` holds what we don't know why. A claim ("students who spent 12 minutes learned more") is neither measurement nor observation — it requires the findings machinery and the [contribution ladder](contribution-ladder.en.md).

## The threshold as a research variable

The drafting-unlock threshold is the one manipulable variable the CAMDLE design introduces into writing education. Because the apparatus makes the threshold a configuration value, it can be set, varied, pre-registered, and compared — a pedagogical constraint becomes a research variable. The open question is how the threshold should vary by task type, proficiency level, language background, and learner strategy ([threshold-calibration]). Any evidence contribution that bears on that question must therefore record **which threshold configuration** it ran under — the same apparatus version with different thresholds runs materially different interventions.

## Configuration in provenance

Evidence contributions record the actual apparatus configuration used, so that evidence can be grouped by configuration, not just by apparatus and version:

```yaml
apparatus:
  id: essays
  version: 0.5.9
  configuration:
    threshold: 3
    defense_required: true
    ai_modes: [socratic, critique]
  canvas:
    version: 0.5.9
```

The evidence graph is `Question → Apparatus → Version → Configuration → Intervention → Evidence`. Because the pre-registered question, apparatus, and configuration all predate the evidence, this strengthens direction-of-fit checking: an evidence bundle that cites an apparatus version or configuration that did not exist when the question was registered is a red flag, not an ordinary submission.

## How evidence bundles cite apparatus identity

The [evidence-bundle template](../templates/evidence-bundle/index.md) is the canonical shape; its `provenance` file carries the optional `apparatus: {id, version, configuration}` and `canvas: {version}` blocks. Rules for citing apparatus identity in an evidence bundle:

1. **Always cite `id` + `version`** — the apparatus version is the behaviour/evidence contract; never substitute the canvas version for it (they are independent).
2. **Record `configuration` whenever the apparatus exposes it** — especially the threshold, defense policy, and AI modes. A bundle without configuration is still comparable at the version level, but its bearing on threshold calibration is limited.
3. **Record `canvas.version`** so the substrate is identifiable, separately from the apparatus version.
4. **Link the research question** the apparatus was configured to investigate, so direction-of-fit machinery can verify the question predates the evidence.

## Status

`status: draft`. The instrument view is defined here and instantiated by Apparatus #1 (Essays). As real evidence bundles arrive, this reference will be revised against what the bundles actually needed to cite.

[research-apparatus-concept]: https://github.com/evaluchat/knowledge/blob/main/concepts/research-apparatus.en.md
[apparatus-recipe]: https://github.com/evaluchat/knowledge/blob/main/playbooks/apparatus-recipe.en.md
[essays-workflow]: https://github.com/evaluchat/knowledge/blob/main/concepts/essays-workflow.en.md
[threshold-calibration]: https://github.com/evaluchat/research/blob/main/theory/threshold-calibration.en.md
