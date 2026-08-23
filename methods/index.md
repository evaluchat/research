# Methods

A **Method** is a published, versioned way of investigating a research question. It is the object a teacher adds to a workspace: it names the question, the platform capabilities it uses, the **levers** (named switches such as `threshold` or `drafting_gate`), immutable profiles, and the evidence contract for this version.

OpenRigor **runs** a method profile. It does not own research truth. Knowledge documents what each lever means on the platform; this catalog documents which levers an investigation uses and what evidence a concluded run must file.

Evidence for a method lives only under that method, at `methods/<id>/evidence/`. There is no catalog-wide evidence cabinet. The document you file is the method version's `evidence-template/`. Shared roles (question, observations vs results vs reflection vs limitations, provenance) are defined in [governance](../governance/).

| Method | Question(s) | Status | Min Canvas |
|---|---|---|---|
| [AI-assisted essay — constrained dialogic drafting (CAMDLE)](ai-assisted-essay/ai-assisted-essay.en.md) | [threshold-calibration](../theory/threshold-calibration.en.md) | draft | 0.5.9 |
| [AI Assignment Stress Test — assignment-level measurement analysis](ai-assignment-stress-test/ai-assignment-stress-test.en.md) | [ai-assignment-stress-test-validity](../theory/ai-assignment-stress-test-validity.en.md) | draft | 0.5.9 |
| [Ledger demo method — synthetic evidence collection](ledger-demo-method/ledger-demo-method.en.md) | (ledger configuration) | stable | 0.6.0 |
| [Synthetic layout method — GitHub research repository contract](synthetic-method/synthetic-method.en.md) | [synthetic-question](../theory/synthetic-question.en.md) | draft | 0.8.0 |

The Essays method publishes immutable canonical, gate-off, AI-off, canvas-action-off, and tracking-off profiles plus [synthetic fixtures](ai-assisted-essay/fixtures/index.md).

The Revision-tracking method specifies immutable `canvas-ai-enabled` and `canvas-ai-disabled` profiles for an assessor-blind validity study. It is currently blocked by the missing, reusable [`experimental-assignment-condition` capability request](https://github.com/openrigor/research/issues/1), which must provide server-side random allocation within a defined assignment group. It is a research-method proposal, not a detector or an integrity feature.

- [Shared evidence roles](../governance/evidence-roles.en.md)
- [Contribution ladder](../governance/contribution-ladder.en.md)
- [Catalog index](../index.md)
