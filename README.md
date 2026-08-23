# OpenRigor Research Catalog

This repository holds **research truth**: what we are investigating and what the evidence currently supports. It is the companion to the [knowledge repository](https://github.com/openrigor/knowledge), which holds **product truth**: what OpenRigor can do.

```text
Knowledge                          Research
product truth                      research truth
what OpenRigor can do              what we are investigating
features, capabilities,            theory → questions → methods
workspace templates                → evidence → findings
```

OpenRigor **runs** a method profile. It does not own research truth. Knowledge does not store classroom evidence. Research does not store executable product templates.

## The chain

```text
Theory / question
    → Method  (published way of investigating that question)
         → selects levers  (which Knowledge-documented features this run engages)
         → OpenRigor applies that profile in a workspace
         → when the run concludes, evidence is filed under that method
    → Finding  (a human claim, reviewed; not the raw export)
```

A **Method** is the object a teacher adds to a workspace: versioned, profiled, measurable. Published methods live under [`methods/`](methods/). **Levers** are the named switches on a method (`ai_assistance`, `drafting_gate`, `threshold`, …). Knowledge defines what each lever *means* on the platform. The method spec says which levers this investigation uses, defaults, and immutable profiles. Same method version + different lever values = different intervention; evidence records the resolved values.

Evidence belongs to exactly one method, at `methods/<id>/evidence/`. Findings may cite several methods; they do not own evidence. A CSV dump is not a finding.

## Two catalogs, one human intro

| Layer | Role |
|---|---|
| **Git / OKF** | The open substrate — provenance and contribution. Every claim traces to a file, a diff, and a review. |
| **Website** | The human interface — this README rendered at [research.openrigor.org](https://research.openrigor.org). The OKF section listing stays in [`index.md`](index.md). |
| **AI** | The reasoning interface — agents traverse question → method → evidence → review → finding via [AGENTS.md](AGENTS.md). |

## Multilingual

Frontmatter (the catalog/machine layer) is always in English; content bodies may be in any language. Every file carries a `lang` (BCP-47) and a stable `id`, and filenames follow `<slug>.<bcp47>.md` for all languages — English included. Translations are trust-tiered: machine-confirmed until verified by a human. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) for the house conventions, and use the issue templates for translation requests, spec changes, research questions, and evidence submissions. Agents that read or edit this repository must follow [AGENTS.md](AGENTS.md). How evidence is produced: [contribution ladder](governance/contribution-ladder.en.md). How claims are reviewed: [review protocol](governance/review-protocol.en.md).

## License

Content: CC-BY-4.0 ([LICENSE](LICENSE)). Code and tooling: MIT ([LICENSE-CODE](LICENSE-CODE)).

## Links

- Knowledge repository: https://github.com/openrigor/knowledge
- Live research catalog: https://research.openrigor.org
- Live knowledge catalog: https://knowledge.openrigor.org
- OKF specification: https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf
