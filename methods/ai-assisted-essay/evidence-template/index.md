# Evidence template — ai-assisted-essay@0.1.0

Copy this directory to `methods/ai-assisted-essay/evidence/<slug>/` when a run of **this method version** concludes. Shared roles are catalog convention ([evidence-roles](../../../governance/evidence-roles.en.md)); the payload below is pinned by `ai-assisted-essay` version `0.1.0`. If the measures change, bump the method version.

| File | Role | What it holds for this method |
| --- | --- | --- |
| [question.md](question.md) | question | [threshold-calibration](../../../theory/threshold-calibration.en.md) (must predate the run) |
| [context.md](context.md) | context | Setting, learners, subject, language, n, duration |
| [intervention.md](intervention.md) | intervention | Assignment, resolved levers (especially `threshold` and `drafting_gate`), instructions, deviations |
| [observations.md](observations.md) | observations | Teacher narrative — verbatim, any language |
| [results.md](results.md) | results | Process-signal summaries + transcript-retention record + assignment outcomes. No interpretation. |
| [reflection.md](reflection.md) | reflection | Teacher interpretation — inference kept separate |
| [limitations.md](limitations.md) | limitations | Scope, confounders, design limits |
| [provenance.md](provenance.md) | provenance | Consent/anonymisation + `method: {id, version, levers, canvas}` |

Each file is a concept with `id: <role>` and `lang`. A non-English submission keeps its native-language file (e.g. `observations.pt-BR.md`, `origin: native`) plus, where useful, an agent-generated English summary (`observations.en.md`, `origin: translation`).

**These files are templates.** Replace each `<!-- ... -->` instruction block with your content, then delete the comment. Every bundle carries a `stage:` field naming its ladder rung — see the [contribution ladder](../../../governance/contribution-ladder.en.md).
