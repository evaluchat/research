---
type: Reference
id: review-protocol
lang: en
status: stable
title: Claim governance — review protocol for findings
description: "Tiered claim governance: low-friction entry (auto-approval at provisional/tentative via deterministic rules), high-bar promotion (supported requires human review), challenge-anything, direction-of-fit pre-registration."
tags: [governance, findings, review-protocol]
generated: { by: opencode-go/deepseek-v4-flash, at: 2026-08-09T14:00:00Z }
---

# Claim governance — review protocol for findings

## Context

There are no findings yet: no classroom experiment exists, and the first findings arrive only with community classroom evidence. This protocol is designed now and proven by dry-run fixtures in CI — synthetic evidence bundles under `scripts/tests/fixtures/`, never merged as real findings. The findings registry ([findings/index.md](../findings/index.md)) stays empty until real evidence exists.

## Tiers

| Tier | Confidence | Auto-approvable? | Requirements |
| --- | --- | --- | --- |
| provisional | low | YES | single falsifiable claim + declared scope; links to ≥1 evidence contribution → intervention → research question; evidence bundle complete (observations, results with Measures, reflection, limitations, provenance + consent); no open challenge; no conflict with existing supported finding |
| tentative | medium | YES, if requirements met | ≥1 structured experiment OR ≥2 documented experiences by distinct contributors/contexts with declared independence; direction-of-fit check passes |
| supported | high | NO — human review required | human synthesis of the evidence chain; reviewer independence rule: a supported finding favourable to evaluchat requires ≥1 non-evaluchat reviewer once the reviewer pool exists; never auto-approved |

## State machine

- **provisional → tentative → supported** — progression through the tiers, each step gated by the requirements above.
- **any state → challenged** — anyone can challenge any finding, at any time. Challenges are always human-reviewed, never auto-adjudicated. A challenged finding enters **contested** (challenge pending).
- **contested → amended | retracted** — maintainer action after human review, with an amendment trail: `status: deprecated` on the old finding plus a link to its successor.

## The objectivity rule

- **Deterministic code decides form.** `okf_claim_check.py` is a rules engine: requirements, tier ceilings, link resolution, direction-of-fit, bundle completeness. No model calls, no judgment. Auto-approval is rule application, not AI adjudication.
- **Humans decide meaning.** The bounded review question is: *"does the documented evidence support the claim as stated, within the declared limitations?"* — never "is this true?" The review is checklist-scoped and recorded in the PR and in `review:` frontmatter.
- **AI assists but is structurally excluded from verdicts.** `generated.by` (an agent actor) can never upgrade a tier; only `verified: { by: human:<id> }` does. AI may draft structure, summarise diffs, and flag inconsistencies — nothing more.

## Roles

- **contributor** — anyone.
- **reviewer** — the maintainer today; community reviewers are earned at ≥3 accepted contributions later.
- **challenger** — anyone.

## Human-review triggers

- tentative → supported promotion;
- any challenge;
- conflict with an existing supported finding;
- causal-claim phrasing (routing rule via keyword heuristic — routes to human, never a verdict);
- direction-of-fit violation (evidence that predates its stated research question);
- maintainer call.

## Procedure

A bounded checklist applied to the documented evidence:

- claim falsifiable and scoped?
- evidence links resolve?
- observation/inference separated?
- limitations adequate?
- consent/privacy clean?
- independence declared?

Outcome: **approve** / **request-changes** / **reject**, recorded in the PR and in `review:` frontmatter.

## Governance cannot amend itself

Changes to this file are never auto-merged; they require human review like any escalation, even when automated checks pass.
