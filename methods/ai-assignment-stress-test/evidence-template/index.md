# Evidence template — ai-assignment-stress-test@0.1.0

Copy this directory to `methods/ai-assignment-stress-test/evidence/<slug>/` when a run of **this method version** concludes. Shared roles are catalog convention ([evidence-roles](../../../governance/evidence-roles.en.md)); the payload below is an **assignment-level report**. This method collects no learner telemetry.

| File | Role | What it holds for this method |
| --- | --- | --- |
| [question.md](question.md) | question | [ai-assignment-stress-test-validity](../../../theory/ai-assignment-stress-test-validity.en.md) (must predate the run) |
| [context.md](context.md) | context | Discipline, task genre, language, institution type — not a student cohort |
| [intervention.md](intervention.md) | intervention | Assignment artefact (anonymised), resolved levers including pinned `model_set`, probe protocol |
| [observations.md](observations.md) | observations | Teacher narrative of running the probe and reading the report |
| [results.md](results.md) | results | Assignment-level report: probe, measure, delegate, redesign. No learner data. |
| [reflection.md](reflection.md) | reflection | Teacher interpretation — inference kept separate |
| [limitations.md](limitations.md) | limitations | Scope, model-set sensitivity, missing data |
| [provenance.md](provenance.md) | provenance | Consent/anonymisation of the assignment artefact + `method: {id, version, levers, canvas}` |

**These files are templates.** Replace each `<!-- ... -->` instruction block with your content, then delete the comment. Every bundle carries a `stage:` field naming its ladder rung — see the [contribution ladder](../../../governance/contribution-ladder.en.md).
