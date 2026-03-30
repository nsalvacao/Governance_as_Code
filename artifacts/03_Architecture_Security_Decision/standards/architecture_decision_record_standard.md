---
title: Architecture Decision Record Standard
artifact_type: standard
status: public
visibility: public
classification: public
owner: architecture-platform
review_cadence: quarterly
applies_to: architecture decisions that require durable justification and review
source_basis: MADR 3.x (adr.github.io/madr); AWS Well-Architected decision practices; Microsoft Learn architecture review guidance
source_manifests:
  - platform__aws_well_architected.md
  - platform__microsoft_learn.md
  - governance__github_docs.md
alignment_mode: hybrid-synthesis
updated: 2026-03-30
---

## Purpose

This standard defines the architecture-layer entry point for recording durable decisions that shape system design, platform choices, and delivery constraints. It follows MADR 3.x (Markdown Any Decision Records) as the canonical format.

## Canonical relationship

- The detailed ADR body lives in the reusable template at `artifacts/01_Governance_Method/templates/architecture_decision_record.md`.
- The governance-layer ADR standard at `artifacts/01_Governance_Method/standards/adr_standard.md` defines the broader decision policy.
- This artifact exists so the architecture dimension has a clear, public canonical primary artifact for the catalog.

## When to write an ADR

Write an ADR when a decision is:
- **Significant** — it affects system structure, platform choice, security posture, or team boundaries.
- **Durable** — the rationale should outlive the discussion thread where it was made.
- **Contested or non-obvious** — at least two viable options existed and the choice carries trade-offs.
- **Reversible only at cost** — undoing the decision would require non-trivial rework.

Do not write an ADR for routine implementation details that have no architectural consequence.

## Naming convention

Each record uses a stable identifier: `ADR-{{SEQUENCE_NUMBER}}` where `{{SEQUENCE_NUMBER}}` is a zero-padded integer (e.g. `ADR-0001`). The file name follows the pattern `ADR-{{SEQUENCE_NUMBER}}-{{SLUG}}.md`.

## Required MADR 3.x sections

Every ADR must contain the following sections in order:

### ADR-{{SEQUENCE_NUMBER}}: {{TITLE}}

**Status:** `{{STATUS}}`
Allowed values: `proposed` | `accepted` | `deprecated` | `superseded by ADR-{{SUPERSEDED_BY}}`

### Context and Problem Statement

Describe the architectural challenge or force that requires a decision. State the problem in one to three sentences. Include the system scope (`{{SYSTEM_SCOPE}}`), key constraints, and quality attributes at stake. This section must be understandable without prior context.

### Decision Drivers

List the forces that shaped the decision space — requirements, constraints, quality attributes (e.g. security, cost, operability). Each driver should be stated as a brief, testable condition. Example: `{{DRIVER_EXAMPLE}}`.

### Considered Options

Enumerate each realistic option that was evaluated. Use a short label for each option: `{{OPTION_NAME}}`. Do not pre-select; list all options neutrally.

### Decision Outcome

State the chosen option: `{{CHOSEN_OPTION}}`. Explain briefly why it was selected relative to the decision drivers.

#### Positive Consequences

List the concrete benefits that follow from this decision. Each entry should be traceable to a decision driver: `{{POSITIVE_CONSEQUENCE}}`.

#### Negative Consequences

List the trade-offs or risks accepted. Be explicit: `{{NEGATIVE_CONSEQUENCE}}`. These are the costs the team accepts in exchange for the benefits above.

### Pros and Cons of the Options

For each option listed under Considered Options, provide a sub-section:

#### {{OPTION_NAME}}

- **Good, because** `{{PRO}}`
- **Bad, because** `{{CON}}`
- **Neutral, because** `{{NEUTRAL_NOTE}}`

Repeat this block for every option. This section enables future reviewers to understand why alternatives were not chosen.

## Lifecycle states

ADRs follow a linear lifecycle with the following allowed states:

| State | Meaning |
|---|---|
| `proposed` | Decision is under discussion; not yet binding. |
| `accepted` | Decision is binding and in effect. |
| `deprecated` | Decision is no longer recommended but has not been replaced. |
| `superseded` | Decision has been replaced by a newer ADR. Link to the superseding record. |

## Immutability rule

Once an ADR reaches `accepted` status it **must not be edited**. If the decision needs to change, create a new ADR with status `superseded by ADR-{{NEW_SEQUENCE_NUMBER}}` and update the old record's status field to point to the new one. This preserves the historical record of the decision and its rationale.

## Required structure (checklist)

- Stable identifier `ADR-{{SEQUENCE_NUMBER}}`
- Status field with lifecycle value
- Context and Problem Statement
- Decision Drivers (at least two)
- Considered Options (at least two)
- Decision Outcome with Positive/Negative Consequences
- Pros and Cons for each option
- Links to related ADRs or design records if applicable

## Automation guidance

- Link each ADR to the decision log when the outcome is `accepted`.
- Keep the artifact stable once accepted; superseding decisions should produce a new record.
- Use the sequence number as a stable cross-reference in code comments, PR descriptions, and runbooks.

## Source Attribution

- Source manifests: `platform__aws_well_architected.md`, `platform__microsoft_learn.md`, `governance__github_docs.md`
- Primary source basis: MADR 3.x (adr.github.io/madr); AWS Well-Architected decision practices; Microsoft Learn architecture review guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-30
