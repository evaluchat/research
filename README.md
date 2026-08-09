# Evaluchat Research Catalog

An open research catalog for AI-compatible education research, maintained by the evaluchat community. This repository is where research questions are asked, theory and methods are recorded, classroom evidence is submitted, and tiered findings are built — in the Open Knowledge Format (OKF) v0.2.

The catalog is a companion to the [knowledge repository](https://github.com/evaluchat/knowledge), which holds product truth (what the product does and how it is implemented). This repository holds research truth: what we are investigating and what the evidence currently supports — never as undifferentiated "knowledge."

## Three layers

| Layer | Role |
|---|---|
| **Git / OKF** | The open substrate — provenance and contribution. Every claim traces to a file, a diff, and a review. |
| **Website** | The human interface — a rendered, language-first view of the catalog (GitHub Pages). |
| **AI** | The reasoning interface — agents navigate questions → hypotheses → interventions → evidence → claims via [AGENT.md](AGENT.md). |

## Multilingual

Frontmatter (the catalog/machine layer) is always in English; content bodies may be in any language. Every file carries a `lang` (BCP-47) and a stable `id`, and filenames follow `<slug>.<bcp47>.md` for all languages — English included. Translations are trust-tiered: machine-confirmed until verified by a human. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) for the house conventions, and use the issue templates for translation requests, spec changes, research questions, and evidence submissions. Agents that edit this repository must follow [AGENTS.md](AGENTS.md).

## License

Content: CC-BY-4.0 ([LICENSE](LICENSE)). Code and tooling: MIT ([LICENSE-CODE](LICENSE-CODE)).

## Links

- Knowledge repository: https://github.com/evaluchat/knowledge
- OKF specification: https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf
