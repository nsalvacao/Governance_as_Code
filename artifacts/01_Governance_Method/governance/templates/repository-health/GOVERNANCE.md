---
title: Governance Overview
artifact_type: policy
status: public
visibility: public
classification: public
owner: "{{GOVERNANCE_OWNER}}"
review_cadence: quarterly
applies_to: reusable_governance
source_basis: GitHub Docs + Open Source Guides
source_manifests: governance__github_docs.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

# Governance

This document describes how `{{REPOSITORY_NAME}}` is governed: who has authority, how decisions are made, and how the governance model itself evolves.

---

## Governance Model

`{{REPOSITORY_NAME}}` follows a **`{{GOVERNANCE_MODEL}}`** model (e.g., maintainer-led / committee / BDFL / open-governance).

| Property | Value |
|---|---|
| Repository type | `{{REPOSITORY_TYPE}}` (e.g., governance library / service / platform) |
| Primary maintainer(s) | `{{MAINTAINER_LIST}}` |
| Governance team | `{{GOVERNANCE_TEAM}}` |
| Decision authority | `{{DECISION_AUTHORITY}}` |
| Review cadence | `{{REVIEW_CADENCE}}` |

**Core principles**:
- **Single source of truth**: every policy, workflow, and schema is auditable and version-controlled.
- **Automation-first**: GitHub Actions, issue forms, frontmatter, and validators are the enforcement instruments.
- **Selective instantiation**: downstream repos adopt only what applies to their context.
- **Dual audience**: conventions must be explicit and deterministic for both human reviewers and AI agents.

---

## Decision Rights

| Decision Type | Authority | Consultation | Record |
|---|---|---|---|
| New artifact creation | `{{ARTIFACT_CREATION_AUTHORITY}}` | `{{GOVERNANCE_TEAM}}` | Decision log or ADR |
| Artifact deprecation or removal | `{{DEPRECATION_AUTHORITY}}` | Downstream consumer notification | Decision log |
| Validator rule change | `{{VALIDATOR_AUTHORITY}}` | All contributors via PR | Changelog + PR |
| Frontmatter schema change | `{{SCHEMA_AUTHORITY}}` | `{{GOVERNANCE_TEAM}}` | ADR + version bump |
| Policy change | `{{POLICY_AUTHORITY}}` | `{{STAKEHOLDERS}}` | Decision log + PR |
| Emergency patch | `{{EMERGENCY_AUTHORITY}}` | Retroactive notification | Post-hoc decision log entry |

---

## Roles

| Role | Responsibilities | Current Holder |
|---|---|---|
| Owner | Strategic direction, emergency authority, final decisions | `{{REPO_OWNER}}` |
| Maintainer | Day-to-day governance, PR merges, review cadence | `{{MAINTAINER_LIST}}` |
| Governance Team | Policy review, Source Attribution, automation coordination | `{{GOVERNANCE_TEAM}}` |
| Contributor | Propose and implement changes per `CONTRIBUTING.md` | Community |

**Adding maintainers**: maintainers are added by `{{MAINTAINER_ADDITION_AUTHORITY}}` after demonstrating sustained quality contributions over `{{MAINTAINER_QUALIFICATION_PERIOD}}`.

---

## Change Process

1. **Propose**: open an issue using the appropriate intake form, or for large changes, start a discussion in `{{DISCUSSION_CHANNEL}}`.
2. **Draft**: create a branch and implement the change following `CONTRIBUTING.md`.
3. **Validate**: run `python3 scripts/validate_governance_artifacts.py` — must pass.
4. **Review**: open PR; requires `{{MIN_REVIEWERS}}` approvals from `{{GOVERNANCE_TEAM}}`.
5. **Merge**: maintainer merges after CI passes and all comments are resolved.
6. **Record**: structural or policy changes are recorded in `decision_log.md`.

---

## Artifact Classification

| Classification | Description | Location | Instantiation |
|---|---|---|---|
| `public` | Open to all downstream repos | `artifacts/` | Freely instantiate |
| `public-redacted` | Available but with redacted sensitive fields | `artifacts/` | Requires adaptation |
| `private` | Internal only — not for downstream use | `.private/` (if present) | Not permitted |

Classification changes require `{{CLASSIFICATION_CHANGE_AUTHORITY}}` approval.

---

## Review Cadence

| Artifact Type | Cadence | Owner |
|---|---|---|
| This governance file | `{{GOVERNANCE_REVIEW_CADENCE}}` | `{{GOVERNANCE_TEAM}}` |
| Policies | `{{POLICY_REVIEW_CADENCE}}` | `{{POLICY_OWNER}}` |
| Standards | `{{STANDARDS_REVIEW_CADENCE}}` | `{{STANDARDS_OWNER}}` |
| Templates | `{{TEMPLATE_REVIEW_CADENCE}}` | `{{TEMPLATE_OWNER}}` |
| Validator + scripts | `{{AUTOMATION_REVIEW_CADENCE}}` | `{{AUTOMATION_OWNER}}` |

Overdue reviews are tracked in `{{REVIEW_TRACKING_LINK}}`.

---

## Governance Evolution

Changes to this governance model follow the standard change process with heightened requirements:

- Requires `{{GOVERNANCE_CHANGE_APPROVERS}}` approvals.
- Must be recorded in `decision_log.md` as an accepted decision.
- Downstream consumer notification within `{{DOWNSTREAM_NOTIFICATION_SLA}}`.
- `{{GOVERNANCE_CHANGE_NOTICE_PERIOD}}` notice period before structural changes take effect.

## Source Attribution

- Source manifests: `governance__github_docs.md`
- Primary source basis: GitHub Docs community governance guidance + Open Source Guides
- Alignment mode: `hybrid-synthesis`
- Reviewed on: 2026-03-27
