# Evidence template — revision-tracking-validity@0.1.0

Copy this directory to `methods/revision-tracking-validity/evidence/<slug>/` when a run of **this method version** concludes. Shared roles are catalog convention ([evidence-roles](../../../governance/evidence-roles.en.md)); the payload below is the assessor-blind validity study's public, de-identified record. No raw student text, AI transcript, identifiable revision trace, or identity-to-condition mapping.

| File | Role | What it holds for this method |
| --- | --- | --- |
| [question.md](question.md) | question | [revision-tracking-validity-question](../../../theory/revision-tracking-validity-question.en.md) (must predate the run) |
| [context.md](context.md) | context | Setting, n, task-set version, stakes (low-stakes default) — no identifiers |
| [intervention.md](intervention.md) | intervention | Profiles, allocation protocol, two-pass workflow, resolved levers |
| [observations.md](observations.md) | observations | Process narrative (completion, masking incidents, deviations) — not student work |
| [results.md](results.md) | results | Blinded judgment matrices, metric summaries, fairness/missingness tables. No interpretation. |
| [reflection.md](reflection.md) | reflection | Interpretation — inference kept separate |
| [limitations.md](limitations.md) | limitations | Scope, confounders, uncertainty, non-endorsement conditions |
| [provenance.md](provenance.md) | provenance | Consent/anonymisation + `method: {id, version, levers, canvas}` + packet hashes |

**These files are templates.** Replace each `<!-- ... -->` instruction block with your content, then delete the comment. Every bundle carries a `stage:` field naming its ladder rung — see the [contribution ladder](../../../governance/contribution-ladder.en.md).
