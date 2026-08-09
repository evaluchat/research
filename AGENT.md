# AGENT.md — Consumer-Agent Contract

Machine-readable navigation contract for agents that READ this catalog. Follow these rules when consuming the repository. This contract keeps agent navigation of the research graph possible: the catalog is a graph of typed, provenance-rich objects — not a folder of documents.

1. **Discover** — read `index.md`, then `catalog.json` (once built); filter by `type` / `tags` / `lang` / `status`.
2. **Identity** — `id` is the stable concept identity; the filename is a representation; `id` + `lang` selects a representation.
3. **Language** — pick the requested `lang`; fall back to `en` for the same `id`; `origin` tells native vs translated.
4. **Trust** — derive the trust tier from `verified`; `status: draft` means unproven; evidence has a `stage`; a finding has a tier per the governance protocol.
5. **Epistemics** — observation ≠ inference ≠ claim; check the `observations` / `results` / `reflection` / `limitations` roles; a Finding requires its evidence chain and tier.
6. **Relationships** — follow markdown links as typed edges: question → hypothesis → intervention → evidence → claim; challenge and replication edges included.
7. **Provenance** — cite `sources` plus `generated` / `verified`; attribute per claim.
8. **Missing translations** — never fabricate content; request the translation or fall back to another language of the same `id`.
