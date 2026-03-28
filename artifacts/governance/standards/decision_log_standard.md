---
title: Decision Log Standard
artifact_type: policy
status: draft
visibility: public
classification: public
owner: GOVERNANCE
review_cadence: quarterly
applies_to: all repositories inheriting these governance conventions
source_basis: GitHub Docs, AWS Well-Architected, Microsoft Learn
source_manifests:
  - governance__github_docs.md
  - platform__aws_well_architected.md
  - platform__microsoft_learn.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Purpose

The decision log is the single authoritative record of accepted decisions for a repository or program. It is not a discussion forum, a changelog, or a rationale document. Its purpose is to:

- Keep one public, reviewable stream where accepted governance decisions accumulate.
- Surface `DL-` identifiers that appear in the published log and link every entry to the decision or ADR that triggered it.
- Make the log consumable by humans, reusable agents, and automation tooling through consistent metadata and attribution.

## Decision Types Covered

The decision log captures decisions in the following categories:

| Type | Examples |
|---|---|
| Architectural | Platform choices, integration patterns, data stores |
| Governance | Policy ratification, standard adoption, ownership changes |
| Policy | Security controls, access rules, compliance posture |
| Methodology | Process adoption, delivery model changes, tooling standards |

Routine project-level decisions that do not affect organizational standards belong in sprint notes or issue trackers, not the decision log.

## Entry Requirements

Each entry in the decision log must include the following fields:

| Field | Format | Description |
|---|---|---|
| ID | `{{DL_ID}}` (e.g., `DL-0001`) | Unique sequential identifier; never reused. |
| Date | `{{DATE}}` (ISO 8601) | Date the decision was accepted. |
| Status | `{{STATUS}}` | One of the entry states defined below. |
| Context | `{{CONTEXT}}` | Brief situation that forced the decision. |
| Decision | `{{DECISION}}` | The chosen option, stated clearly and unambiguously. |
| Consequences | `{{CONSEQUENCES}}` | Trade-offs accepted and follow-up actions required. |

Use the template in `artifacts/governance/templates/decision_log_entry.md` for every new entry.

## Entry States

| State | Meaning |
|---|---|
| `proposed` | Entry is under review; not yet authoritative. |
| `accepted` | Ratified by `{{DECISION_AUTHORITY}}`; entry is immutable. |
| `superseded` | Replaced by a newer entry; reference the superseding ID. |
| `revoked` | Overturned without a replacement; reason must be documented. |

## Y-Statements Format Guidance

For entries where structured reasoning aids comprehension, use the Y-Statement pattern as the decision summary:

> In the context of `{{SITUATION}}`, facing `{{CONCERN}}`, we decided `{{OPTION}}`, to achieve `{{QUALITY}}`, accepting `{{DOWNSIDE}}`.

This format makes the trade-off explicit and machine-readable. It is recommended but not required for all entries; use it whenever the decision involves a meaningful quality-versus-cost trade-off.

## Immutability Rule

Once an entry reaches `accepted` state it must not be edited. If the decision changes:

- Author a new entry in `proposed` state with updated context and decision.
- Once the new entry is accepted, update the old entry's status to `superseded by DL-YYYY`, referencing the new entry's ID.
- The new entry's status is `accepted`; it does not carry a superseded marker.

Never delete or silently overwrite accepted entries.

## Cross-Reference with ADRs

Every decision log entry that corresponds to an ADR must include the `linked_adr` field referencing the ADR ID (e.g., `ADR-007`). The ADR is the authoritative source for full context, options, and rationale; the decision log entry is the summary record.

## Review Cadence

The decision log is reviewed `{{REVIEW_CADENCE}}` (default: quarterly). During each review:

1. Scan entries in `proposed` state older than `{{STALE_THRESHOLD}}` and escalate or close them.
2. Verify that `superseded` entries correctly reference their successors.
3. Confirm that `accepted` entries with a `next_review` date have been re-evaluated.

## Authority to Accept or Revoke Decisions

Only `{{DECISION_AUTHORITY}}` may change an entry's status from `proposed` to `accepted`, or from `accepted` to `revoked`. This authority is defined in the repository's governance overview and must be an identified role or team, not an individual by name.

## Source Attribution

- Source manifests: governance__github_docs.md, platform__aws_well_architected.md, platform__microsoft_learn.md
- Primary source basis: GitHub Docs community governance guidance plus AWS/Microsoft guidance on decision records and reviews
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
