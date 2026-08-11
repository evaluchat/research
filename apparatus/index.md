# Apparatuses

Research apparatuses: reproducible configurations of Canvas capabilities, workflows, and measurements
for one or more research questions. Each apparatus owns exactly one evidence collection
(`apparatus/<id>/evidence/`).

| Apparatus | Question(s) | Status | Min Canvas |
|---|---|---|---|
| [AI-assisted essay — constrained dialogic drafting (CAMDLE)](ai-assisted-essay/ai-assisted-essay.en.md) | [threshold-calibration](../theory/threshold-calibration.en.md) | draft | 0.5.9 |
| [AI Assignment Stress Test — assignment-level measurement analysis](ai-assignment-stress-test/ai-assignment-stress-test.en.md) | [ai-assignment-stress-test-validity](../theory/ai-assignment-stress-test-validity.en.md) | draft | 0.5.9 |
| [Revision-tracking validity — assessor-blind process-evidence study](revision-tracking-validity/revision-tracking-validity.en.md) | [revision-tracking-validity-question](../theory/revision-tracking-validity-question.en.md) | draft — implementation blocked | 0.5.9 |

The Essays apparatus publishes immutable canonical, gate-off, AI-off,
canvas-action-off, and tracking-off profiles plus [synthetic fixtures](ai-assisted-essay/fixtures/index.md).

The Revision-tracking apparatus specifies immutable `canvas-ai-enabled` and `canvas-ai-disabled`
profiles for an assessor-blind validity study. It is currently blocked by the missing, reusable
[`experimental-assignment-condition` capability request](https://github.com/evaluchat/research/issues/1),
which must provide server-side random allocation within a defined assignment group. It is a
research-method proposal, not a detector or an integrity feature.

- [Instrument view: the apparatus as research instrument](../methods/apparatus.en.md)
