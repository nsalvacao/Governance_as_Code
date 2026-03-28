---
title: Architectural Decision Record Standard
artifact_type: policy
status: public
visibility: public
classification: public
owner: GOVERNANCE
review_cadence: quarterly
applies_to: all architecture and delivery decisions that threaten irreversible outcomes
source_basis: MADR 3.x (adr.github.io/madr) — Markdown Architectural Decision Records
source_manifests:
  - platform__aws_well_architected.md
  - platform__microsoft_learn.md
  - governance__github_docs.md
alignment_mode: hybrid-synthesis
updated: 2026-03-28
---

## Purpose

This standard explains when an ADR is required, how it follows MADR 3.x structure, and how to author an ADR that stays automation-friendly and reuse-ready.

## ADR versus Decision Log

- **ADR**: captures the full context, options considered, trade-offs, and technical consequences of a hard-to-reverse decision (architecture, platform, delivery contracts, automation safety). Each ADR follows the template in `artifacts/01_Governance_Method/templates/architecture_decision_record.md` and is the single source for the working rationale.
- **Decision log**: publishes the distilled acceptance outcome once the ADR (or other governance process) is approved. Decision log entries point back to one or more ADRs for context and keep the public corpus lightweight.
- Always link the ADR ID inside the decision log template under `Linked ADR`. Automation can then follow the link to fetch the reasoning, review status, and superseded history.

## When to Write an ADR

Write an ADR when any of the following conditions apply:

1. The decision is consequential — it changes an organizational standard, baseline, automation contract, or release pathway.
2. The decision affects multiple components, teams, or repositories — scope goes beyond a single sprint deliverable.
3. The decision is hard to reverse — undoing it would require significant effort such as pipeline rewrites or baseline migrations.
4. Avoid capturing easily reversed or single-component choices in ADRs; keep those in the decision log unless they touch governance or automation baselines.

## MADR 3.x Required Structure

Every ADR must include the following sections in order. Use the template in `artifacts/01_Governance_Method/templates/architecture_decision_record.md`.

| Section | Purpose |
|---|---|
| **Context and Problem Statement** | Describe the architectural or technical challenge, its scope, and why a decision is needed now. |
| **Decision Drivers** | List the quality attributes, constraints, and forces that shape the decision (e.g., performance, cost, maintainability). |
| **Considered Options** | Enumerate all options evaluated. Each must be named and later analyzed in the Pros and Cons section. |
| **Decision Outcome** | State the chosen option and justify why it best satisfies the decision drivers. |
| **Positive Consequences** | List the expected benefits and improvements that result from the chosen option. |
| **Negative Consequences** | List the accepted trade-offs, risks, and technical debt introduced by the chosen option. |
| **Pros and Cons of the Options** | For each considered option, provide at least one "Good, because …" and one "Bad, because …" bullet. |

## Lifecycle States

ADRs move through a defined set of states. State transitions must be explicit in the `Status` field.

| State | Meaning |
|---|---|
| `proposed` | Draft under review; not yet authoritative. |
| `accepted` | Ratified by the decision authority; becomes immutable. |
| `deprecated` | No longer recommended but still in effect; superseding ADR not yet required. |
| `superseded` | Replaced by a newer ADR; reference the superseding ADR ID in the status line. |

## State Transition Rules

- `proposed` → `accepted`: requires explicit sign-off from `{{DECISION_AUTHORITY}}`.
- `accepted` → `deprecated`: allowed when context changes but no replacement decision is ready.
- `accepted` → `superseded`: requires a new ADR in `accepted` state that explicitly references this one.
- No other transitions are valid without authoring a superseding ADR.

## Immutability Rule

Once an ADR reaches `accepted` state it must not be edited. New information, corrections, or changed context require authoring a new ADR that supersedes the original. Append the superseding ADR ID to the original's status field (e.g., `superseded by [ADR-007](path/adr-007.md)`).

## Naming Convention

File names follow the pattern: `ADR-{{SEQUENCE_NUMBER}}-{{KEBAB-CASE-TITLE}}.md`

Examples: `ADR-001-use-postgres-as-primary-store.md`, `ADR-042-adopt-opentelemetry.md`.

## Storage Location

Store ADRs in `{{ADR_DIRECTORY}}` within the consuming repository (e.g., `docs/decisions/` or `docs/adr/`). The directory must be referenced in the repository's `README.md` or governance overview.

## Link to Decision Log

After an ADR reaches `accepted` state, append a corresponding entry to `decision_log.md` using the template in `artifacts/01_Governance_Method/templates/decision_log_entry.md`. The decision log entry must include the ADR ID under `Linked ADR`.

## Review Process

1. Author opens a pull request with the ADR in `proposed` state.
2. Reviewers from `{{REVIEW_TEAM}}` evaluate the options, drivers, and consequences.
3. `{{DECISION_AUTHORITY}}` ratifies or rejects; ratification changes status to `accepted`.
4. On acceptance, the author updates `decision_log.md`, merges, and closes the pull request.
5. Quarterly, the governance owner scans for `deprecated` ADRs and triggers superseding ADRs where required.

## Source Attribution

- Source manifests: platform__aws_well_architected.md, platform__microsoft_learn.md, governance__github_docs.md
- Primary source basis: MADR 3.x (adr.github.io/madr) — Markdown Architectural Decision Records
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
