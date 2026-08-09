# Evidence bundle — template

This directory is the starting skeleton for one evidence contribution. Copy it to `evidence/<slug>/` and fill in each file. A complete bundle has all nine parts:

| File | Role (id) | What it holds |
| --- | --- | --- |
| [question.md](question.md) | question | Which research question(s) this contribution bears on |
| [context.md](context.md) | context | Setting, learners, subject, language, n, duration |
| [intervention.md](intervention.md) | intervention | What was actually done (assignment, threshold settings) |
| [observations.md](observations.md) | observations | Teacher narrative — verbatim, any language |
| [results.md](results.md) | results | Structured measurements only (Measures / Observed differences / Missing data) |
| [reflection.md](reflection.md) | reflection | Teacher interpretation — inference kept separate |
| [limitations.md](limitations.md) | limitations | Scope, confounders, design limits |
| [provenance.md](provenance.md) | provenance | Sources, consent + anonymisation record |

Each file is a concept with `id: <role>` and `lang`. A non-English submission keeps its native-language file (e.g. `observations.pt-BR.md`, `origin: native`) plus, where useful, an agent-generated English summary (`observations.en.md`, `origin: translation`).

**These files are templates.** Replace each `<!-- ... -->` instruction block with your content, then delete the comment. Every bundle carries a `stage:` field (in the registry or frontmatter) naming its ladder rung — see the [contribution ladder](../../methods/contribution-ladder.en.md).
