---
title: Documentation Review and Ownership Matrix
artifact_type: standard
status: public-draft
visibility: public
classification: public
owner: knowledge-platform
review_cadence: quarterly
applies_to: document governance and review workflows
source_basis: GitHub Docs repository ownership and review guidance
source_manifests:
  - governance__github_docs.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Purpose

Define who owns each document class in `{{REPOSITORY_NAME}}` and who reviews it, so that maintenance stays explicit, traceable, and actionable. This matrix uses the RACI model as its accountability framework.

## RACI Definitions

The RACI model assigns exactly one of four roles to each stakeholder for each document type:

| Role | Meaning | Rule |
|---|---|---|
| **Responsible** | Does the work — writes, updates, or corrects the document | At least one per document type; may be shared |
| **Accountable** | Owns the outcome — ensures the document is accurate and current | Exactly one per document type; cannot be shared |
| **Consulted** | Provides input before the document is published or changed | Two-way communication; optional but recommended for high-impact docs |
| **Informed** | Kept updated on changes after they occur | One-way communication; no approval authority |

A person or role may appear in multiple RACI positions across different document types but cannot be both Accountable and Responsible for the same document type in the same review cycle (unless the team is too small to separate them — document this exception explicitly).

## Document Types Covered

This matrix covers the following document types in `{{REPOSITORY_NAME}}`:

1. `{{DOC_TYPE_1}}`
2. `{{DOC_TYPE_2}}`
3. `{{DOC_TYPE_3}}`
4. `{{DOC_TYPE_N}}`

Add additional rows as the corpus grows. Every document in the repository must map to exactly one document type in this list.

## RACI Matrix

| Document type | Responsible (author) | Accountable (owner) | Consulted | Informed | Review cadence |
|---|---|---|---|---|---|
| `{{DOC_TYPE_1}}` | `{{AUTHOR_ROLE_1}}` | `{{APPROVER_ROLE_1}}` | `{{REVIEWER_ROLE_1}}` | `{{INFORMED_ROLE_1}}` | `{{CADENCE_1}}` |
| `{{DOC_TYPE_2}}` | `{{AUTHOR_ROLE_2}}` | `{{APPROVER_ROLE_2}}` | `{{REVIEWER_ROLE_2}}` | `{{INFORMED_ROLE_2}}` | `{{CADENCE_2}}` |
| `{{DOC_TYPE_3}}` | `{{AUTHOR_ROLE_3}}` | `{{APPROVER_ROLE_3}}` | `{{REVIEWER_ROLE_3}}` | `{{INFORMED_ROLE_3}}` | `{{CADENCE_3}}` |
| `{{DOC_TYPE_N}}` | `{{AUTHOR_ROLE_N}}` | `{{APPROVER_ROLE_N}}` | `{{REVIEWER_ROLE_N}}` | `{{INFORMED_ROLE_N}}` | `{{CADENCE_N}}` |

Populate each cell with a role name (not a person's name) to keep this matrix stable across team changes. Where a role is not yet defined, use `{{ROLE_TBD}}` as a placeholder and create a task to resolve it.

## Review Trigger Events

Reviews are triggered by two categories of events:

### Time-based triggers

A document must be reviewed according to its cadence in the matrix above. The clock resets after each completed review. The minimum review interval is `{{TIME_TRIGGER}}` (e.g., `quarterly`, `semiannual`, `annual`).

### Event-based triggers

The following events require an immediate out-of-cycle review regardless of scheduled cadence:

1. `{{EVENT_TRIGGER_1}}` (e.g., a breaking change to the system the document describes)
2. `{{EVENT_TRIGGER_2}}` (e.g., a security incident that reveals a documentation gap)
3. `{{EVENT_TRIGGER_3}}` (e.g., a change in ownership or team restructuring)
4. `{{EVENT_TRIGGER_N}}`

When an event-based review is triggered, the Accountable role must acknowledge it within `{{EVENT_TRIGGER_SLA}}` and schedule the review within `{{EVENT_REVIEW_WINDOW}}`.

## Escalation Path

When the Accountable owner is unavailable (leave, departure, role gap), the following escalation path applies:

`{{ESCALATION_PATH}}`

Example: `Primary owner → Backup owner → Team lead → Engineering manager`. Document the active escalation in the decision log so it is traceable.

Ownership gaps lasting more than `{{MAX_OWNERSHIP_GAP}}` must be resolved by reassigning the Accountable role. Unresolved gaps are a documentation health risk.

## Documentation Health Metrics

Track the following metrics to assess the health of the documentation corpus:

| Metric | Target | Measurement method |
|---|---|---|
| Coverage (% of system surfaces documented) | `{{COVERAGE_TARGET}}` | `{{COVERAGE_MEASUREMENT}}` |
| Freshness (days since last review, per document) | ≤ `{{FRESHNESS_DAYS}}` days | `{{FRESHNESS_MEASUREMENT}}` |
| Broken link SLA (time to fix a broken internal link) | `{{BROKEN_LINK_SLA}}` | `{{BROKEN_LINK_MEASUREMENT}}` |
| Ownership gap rate (% of docs without an Accountable owner) | 0% | Matrix completeness check |

Review health metrics at each `{{HEALTH_REVIEW_CADENCE}}` team sync. Metrics that miss target for two consecutive cycles must trigger a remediation task.

## Onboarding Process for New Document Owners

When a person or role takes on ownership of one or more document types, follow these steps:

1. Add the new owner to the RACI matrix and commit the change.
2. Schedule a handover meeting with the outgoing owner (if applicable).
3. Read all documents in the inherited document type and note any gaps or inaccuracies.
4. Complete any overdue reviews within `{{ONBOARDING_REVIEW_WINDOW}}` of taking ownership.
5. Record the ownership change in the decision log with effective date and rationale.

## Source Attribution

- Source manifests: governance__github_docs.md
- Primary source basis: GitHub Docs repository ownership and review guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
