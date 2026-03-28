---
title: Governance Overview
artifact_type: template
status: public-draft
visibility: public
classification: public
owner: "{{OWNER_NAME}}"
review_cadence: quarterly
applies_to: repository governance surfaces
source_basis: GitHub Docs community governance guidance
source_manifests:
  - governance__github_docs.md
alignment_mode: direct-adaptation
updated: 2026-03-27
---

## Purpose

Describe how `{{REPOSITORY_NAME}}` is governed: who decides, how decisions are made, how changes are proposed and reviewed, and how the governance model evolves. Replace all `{{PLACEHOLDER}}` values before publishing.

---

## Scope and Governance Model

| Field | Value |
|---|---|
| Repository | `{{REPOSITORY_NAME}}` |
| Governance model | `{{GOVERNANCE_MODEL}}` (e.g., maintainer-led / BDFL / committee / open) |
| Primary audience | `{{PRIMARY_AUDIENCE}}` |
| Downstream consumers | `{{DOWNSTREAM_REPOS}}` |
| Instantiation method | Selective — consult the classification grid before copying artifacts |

**Model description**: `{{GOVERNANCE_MODEL_DESCRIPTION}}`

---

## Decision Rights and Ownership

| Decision Type | Decision Authority | Consultation Required | Record |
|---|---|---|---|
| New artifact creation | `{{ARTIFACT_CREATION_AUTHORITY}}` | `{{GOVERNANCE_TEAM}}` | ADR or decision log |
| Artifact deprecation | `{{DEPRECATION_AUTHORITY}}` | Downstream consumer notification | Decision log |
| Validator rule change | `{{VALIDATOR_AUTHORITY}}` | All contributors | Changelog + PR |
| Frontmatter schema change | `{{SCHEMA_AUTHORITY}}` | `{{GOVERNANCE_TEAM}}` | ADR + schema version bump |
| Policy changes | `{{POLICY_AUTHORITY}}` | `{{STAKEHOLDERS}}` | Decision log + PR |
| Emergency patch | `{{EMERGENCY_AUTHORITY}}` | Retroactive notification | Post-hoc decision log entry |

Maintainers: `{{MAINTAINER_LIST}}`

Governance team: `{{GOVERNANCE_TEAM}}`

---

## Review Cadence and Change Process

| Artifact Type | Review Cadence | Trigger | Owner |
|---|---|---|---|
| Policies | `{{POLICY_REVIEW_CADENCE}}` | Cadence or material change | `{{POLICY_OWNER}}` |
| Standards | `{{STANDARDS_REVIEW_CADENCE}}` | Cadence or framework update | `{{STANDARDS_OWNER}}` |
| Templates | `{{TEMPLATE_REVIEW_CADENCE}}` | Cadence or consumer feedback | `{{TEMPLATE_OWNER}}` |
| Workflows / scripts | `{{AUTOMATION_REVIEW_CADENCE}}` | Cadence or CI failure | `{{AUTOMATION_OWNER}}` |
| Governance docs (this file) | `{{GOVERNANCE_DOCS_CADENCE}}` | Cadence or structural change | `{{GOVERNANCE_TEAM}}` |

### Change Process

1. Propose via issue using the appropriate intake form.
2. Draft the change in a feature branch.
3. Run `python3 scripts/validate_governance_artifacts.py` — must pass before opening PR.
4. Open PR using `.github/PULL_REQUEST_TEMPLATE.md` with scope (`instance` / `artifact library` / `both`).
5. Await `{{MIN_REVIEWERS}}` approvals and CI gate pass.
6. Merge — maintainer records decision in `decision_log.md` for structural changes.

---

## Public versus Private Material

| Classification | Location | Access | Instantiation |
|---|---|---|---|
| `public` | `artifacts/` root, public templates | Anyone | Open to downstream repos |
| `public-redacted` | `artifacts/` with redacted fields | Read-only for external | Requires org membership for full detail |
| `private` | `.private/` | Internal only | Not for downstream instantiation |

Rules:
- `.private/` contents MUST NOT appear in any public artifact.
- `public-redacted` artifacts MUST document which fields are redacted and why.
- Classification downgrades (private → public) require `{{DOWNGRADE_AUTHORITY}}` approval.

---

## Validation and Publication Rules

| Rule | Enforcement |
|---|---|
| All Markdown artifacts must pass `validate_governance_artifacts.py` | CI gate (PR merge block) |
| All artifacts must include `## Source Attribution` | Validator check |
| All frontmatter must include 11 required keys | Validator check |
| README catalog must have 103 rows with valid canonical links | Validator check |
| GitHub-native files must include Source Attribution comment | Validator check |
| Artifact path must be `artifacts/<dimension>/<artifact-type>/` | Validator check |

Publication checklist before any merge:
- [ ] Validation: `python3 scripts/validate_governance_artifacts.py` exits `0`
- [ ] Classification confirmed and label applied
- [ ] Source Attribution updated with correct reviewed-on date
- [ ] Downstream impact assessed and documented in PR

---

## Governance Evolution

Changes to this governance model follow the same change process above with heightened scrutiny:
- Requires `{{GOVERNANCE_CHANGE_APPROVERS}}` approvals.
- Must be recorded in `decision_log.md` as an accepted decision.
- Notification to `{{DOWNSTREAM_REPOS}}` must be sent within `{{NOTIFICATION_SLA}}`.

## Source Attribution

- Source manifests: governance__github_docs.md
- Primary source basis: GitHub Docs community governance guidance
- Alignment mode: direct-adaptation
- Reviewed on: 2026-03-27

