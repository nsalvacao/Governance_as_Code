---
title: Knowledge Lifecycle Policy
artifact_type: policy
status: public
visibility: public
classification: public
owner: "{{OWNER_NAME}}"
review_cadence: quarterly
applies_to: knowledge artifacts and documentation lifecycle
source_basis: GitHub Docs and Diataxis documentation lifecycle guidance
source_manifests:
  - governance__github_docs.md
  - documentation__diataxis.md
alignment_mode: hybrid-synthesis
updated: 2026-03-30
---

## Policy Statement

Treat knowledge as a managed asset with creation, review, update, archive, and retirement stages. Every artifact must have an owner, a type, and a cadence — undated or unowned documents are not assets, they are liabilities.

## Document Types Covered

This policy governs all knowledge artifacts. Each type maps to one quadrant of the Diataxis framework; mixing quadrants in a single document is prohibited (see `documentation_policy.md`).

| Diataxis type | Orientation | Reader need | Example artifact |
|---|---|---|---|
| **Tutorial** | Learning-oriented | Learning by doing | Onboarding walkthrough, getting-started guide |
| **How-to guide** | Task-oriented | Achieving a specific goal | Step-by-step runbook, recipe |
| **Reference** | Information-oriented | Accurate, complete lookup | API reference, schema definition, glossary |
| **Explanation** | Understanding-oriented | Context, background, reasoning | Architecture overview, design rationale |

Assign each new artifact to exactly one type at creation. Reclassification requires an explicit update entry in the artifact's history.

## Creation Triggers

A new knowledge artifact must be created when any of the following events occur. The owner named at creation is responsible for the artifact throughout its lifecycle.

- A new system component, service, or process is introduced and no existing document covers it.
- A recurring question is answered in a chat, ticket, or meeting for the third time without a canonical reference to point to.
- A decision is made that requires explanation of context or trade-offs not captured elsewhere.
- An existing artifact is split because it serves more than one Diataxis quadrant.

New artifacts are created in `proposed` state and must pass the quality gates in `definition_of_done_quality_gates.md` before being published.

## Review Triggers

Reviews are initiated by both time-based and event-based signals.

**Time-based:** Every artifact is reviewed on a `{{REVIEW_CADENCE}}` schedule. The `review_cadence` frontmatter field declares this cadence; tooling reads it to generate review reminders.

**Event-based:** A review is triggered immediately when any of the following occur:
- The system, process, or concept the artifact describes changes in a material way.
- A user reports the artifact as inaccurate or outdated.
- A dependent artifact (one that links to or imports this one) is superseded or deprecated.
- Automated monitoring detects that a referenced resource (URL, file path, ADR number) no longer resolves.

## Deprecation Criteria

An artifact is marked `deprecated` when it no longer represents current practice and no direct successor exists. Criteria:

- The described system, process, or concept has been decommissioned or replaced by something materially different.
- The artifact has not been reviewed in more than `{{MAX_UNREVIEWED_PERIOD}}` and the owner cannot confirm its accuracy.
- The artifact's Diataxis type no longer matches its content and reclassification would require a full rewrite.

A deprecated artifact must include a `deprecated_note` field or inline notice explaining why it was deprecated and what (if anything) supersedes it.

## Archival Process

Archived artifacts are moved to `{{ARCHIVAL_LOCATION}}` and are no longer discoverable via the primary catalog, but remain accessible by direct link for audit and historical reference.

Archival procedure:
1. The owner confirms archival intent in a PR description.
2. The PR updates the artifact's `status` to `archived` and adds the current date as `archived_on`.
3. The artifact is moved to `{{ARCHIVAL_LOCATION}}`.
4. Any catalog entries referencing the artifact are updated to reflect its archived state.

## Deletion Rules

Permanent deletion is reserved for artifacts that contain no historical, legal, or audit value and whose retention creates active harm (e.g., dangerously outdated security instructions with no deprecation notice).

- Deletion requires explicit approval from `{{DELETION_AUTHORITY}}`.
- Artifacts that have been referenced by any released version of a downstream repository may not be deleted; archive them instead.
- Deleted artifacts must be recorded in the audit log at `{{AUDIT_LOG_PATH}}` with the reason and approver.

## Owner Assignment

Every artifact must declare an `owner` in frontmatter using the value `{{DOCUMENT_OWNER}}`. The owner is responsible for:
- Responding to review triggers within `{{OWNER_RESPONSE_SLA}}`.
- Confirming accuracy at each scheduled review.
- Initiating deprecation or archival when appropriate.
- Delegating ownership if they leave the team (an unowned artifact triggers an automated alert).

## Audit Trail Requirements

All lifecycle transitions — creation, review, update, deprecation, archival, deletion — must be traceable. Minimum requirements:

- Frontmatter `updated` field reflects the date of the last content change.
- Git history provides the change record; squash merges that lose individual commit context are discouraged.
- Significant transitions (deprecation, archival, deletion) are recorded in `{{AUDIT_LOG_PATH}}` with actor, date, and reason.
- Automation may validate that `updated` matches the date of the most recent frontmatter or content change.

## Source Attribution

- Source manifests: governance__github_docs.md, documentation__diataxis.md
- Primary source basis: GitHub Docs and Diataxis documentation lifecycle guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-30
