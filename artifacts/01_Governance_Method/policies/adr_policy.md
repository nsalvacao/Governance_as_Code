---
title: Architecture Decision Record Policy
artifact_type: policy
status: public
visibility: public
classification: public
owner: "{{OWNER_NAME}}"
review_cadence: quarterly
applies_to: architecture and governance decisions
source_basis: MADR (Markdown Architectural Decision Records) lifecycle specification
source_manifests:
  - governance__github_docs.md
  - platform__microsoft_learn.md
alignment_mode: hybrid-synthesis
updated: 2026-03-30
---

## Policy Statement

Record architecture-shaping decisions when the cost of re-discovery exceeds the cost of writing the decision down. Use MADR as the canonical format for all Architecture Decision Records.

## Policy Scope

This policy applies to all repositories under `{{APPLIES_TO_SCOPE}}` that produce or consume architectural decisions with a cross-team or lasting operational impact. Teams must use this policy as the minimum bar; they may add stricter local rules but may not relax it.

## When an ADR Is Required

Create an ADR when a decision meets any of the following criteria. Borderline cases default to "write it."

- **Affects multiple teams or repositories** — the decision changes interfaces, contracts, or shared infrastructure used by more than one group.
- **Is hard or costly to reverse** — rolling back would require migration, data cleanup, or coordinated downtime.
- **Involves significant trade-offs** — two or more reasonable alternatives were evaluated; rationale for the chosen option is not obvious from the code alone.
- **Changes a previously documented ADR** — superseding an existing record requires a new ADR that references the old one.

Decisions that do not meet these criteria (local implementation details, minor tooling choices) may be captured as inline comments or PR descriptions instead.

## ADR Lifecycle States

Every ADR transitions through a defined set of states. Automation may validate that only legal transitions occur.

| State | Meaning | Allowed next states |
|---|---|---|
| `proposed` | Under discussion; not yet binding | `accepted`, `rejected` |
| `accepted` | Approved and in force | `deprecated`, `superseded` |
| `rejected` | Evaluated but not adopted; kept for historical context | — |
| `deprecated` | No longer recommended; replaced by evolving practice without a direct successor | — |
| `superseded` | Replaced by a newer ADR; the superseding ADR number must be recorded | — |

Transition rules:
- Only the `{{DECISION_AUTHORITY}}` role may move an ADR from `proposed` to `accepted` or `rejected`.
- When an ADR is superseded, update its header to `status: superseded by ADR-{{SUPERSEDING_NUMBER}}` and link the new ADR.
- Deprecated ADRs must include a note explaining why deprecation was chosen over supersession.

## Naming Convention

All ADR files follow the pattern: `ADR-{{SEQUENCE_NUMBER}}-{{SLUG}}.md`

- `{{SEQUENCE_NUMBER}}` is a zero-padded integer (e.g., `0042`) assigned sequentially within the repository.
- `{{SLUG}}` is a short, lowercase, hyphen-separated description of the decision (e.g., `use-postgres-for-primary-store`).
- Example: `ADR-0042-use-postgres-for-primary-store.md`

Do not reuse sequence numbers, even for rejected ADRs.

## Storage Location

All ADRs for a repository reside under `{{ADR_STORAGE_PATH}}` (e.g., `docs/decisions/`). Do not split ADRs across multiple directories within the same repository scope. Cross-repository decisions may reference each other by URL.

## Review Cadence

ADRs are reviewed on a `{{REVIEW_CADENCE}}` schedule. The review confirms that accepted ADRs still reflect current practice and that deprecated or superseded entries are accurately labeled. Stale ADRs that no longer reflect reality must be either updated or superseded.

## Superseding Rules

When a new decision replaces an existing one:

1. Create a new ADR in `proposed` state that explicitly references the ADR being superseded.
2. After acceptance, update the old ADR's status line to: `status: superseded by ADR-{{SUPERSEDING_NUMBER}}`.
3. Add a link in the old ADR body pointing to the new ADR.
4. Do not delete the old ADR; historical context is preserved.

## Automation Hooks

Link each accepted ADR to the decision log entry at `{{DECISION_LOG_PATH}}` so that audit trails remain intact. Automation may enforce this link via `{{GOVERNANCE_VALIDATION_WORKFLOW}}`. CI checks should flag ADRs that lack a decision log reference or that reference a non-existent superseding ADR number.

## Source Attribution

- Source manifests: governance__github_docs.md, platform__microsoft_learn.md
- Primary source basis: MADR (Markdown Architectural Decision Records) lifecycle specification
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-30
