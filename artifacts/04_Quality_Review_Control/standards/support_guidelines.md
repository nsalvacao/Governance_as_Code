---
title: Support Guidelines
artifact_type: standard
status: public-draft
visibility: public
classification: public
owner: quality-platform
review_cadence: quarterly
applies_to: support intake, escalation boundaries, and contributor guidance
source_basis: GitHub Docs support and community guidance
source_manifests:
  - governance__github_docs.md
alignment_mode: direct-adaptation
updated: 2026-03-27
---

## Purpose

Define routing rules for support requests to prevent noisy issue intake and ensure each request reaches the right team without ambiguity.

## Request Type Routing

| Request Type | Where to Go | What NOT to Use |
|---|---|---|
| Bug report (reproducible defect) | GitHub Issues — Bug Report form | Support channels, email |
| Feature request or idea | GitHub Issues — Feature Request form or `{{DISCUSSION_CATEGORY}}` | Direct email to maintainers |
| Security vulnerability | Private advisory or `{{SECURITY_EMAIL}}` — see SECURITY.md | Public issues |
| Usage question / how-to | `{{DISCUSSION_CATEGORY_QA}}` (e.g., Discussions → Q&A) | Issues |
| Community discussion | `{{DISCUSSION_CATEGORY_GENERAL}}` | Issues |
| Commercial support / SLA | `{{COMMERCIAL_SUPPORT_LINK}}` or `{{SUPPORT_EMAIL}}` | GitHub Issues |
| Documentation error | GitHub Issues — Documentation form or PR | Email |

## Response Expectations

| Channel | First Response SLA | Resolution SLA | Owner |
|---|---|---|---|
| GitHub Issues (bugs) | `{{BUG_RESPONSE_SLA}}` (e.g., 5 business days) | `{{BUG_RESOLUTION_SLA}}` | `{{BUG_OWNER_TEAM}}` |
| GitHub Discussions | `{{DISCUSSION_RESPONSE_SLA}}` | Best-effort | Community + `{{MAINTAINER_TEAM}}` |
| Security reports | `{{SECURITY_ACK_SLA}}` | Per SECURITY.md SLA | `{{SECURITY_CONTACT}}` |
| Commercial support | Per `{{SUPPORT_AGREEMENT_REF}}` | Per agreement | `{{COMMERCIAL_SUPPORT_TEAM}}` |

## Escalation Path

1. **Community tier** — Discussions, issues: handled by contributors and maintainers on a best-effort basis
2. **Maintainer tier** — Bugs and confirmed defects: handled by `{{MAINTAINER_TEAM}}` within SLA
3. **Security tier** — Vulnerabilities: handled confidentially per SECURITY.md
4. **Executive tier** — Service-impacting incidents for commercial customers: escalate via `{{EXECUTIVE_ESCALATION_CONTACT}}`

## Out of Scope

The following are **not supported** through this repository:

- `{{OUT_OF_SCOPE_ITEM_1}}` (e.g., general programming help unrelated to this project)
- `{{OUT_OF_SCOPE_ITEM_2}}` (e.g., debugging user-specific infrastructure)
- Third-party integrations not maintained by `{{ORG_NAME}}`

## Canonical Relationship

- The repository-instance equivalent is `artifacts/01_Governance_Method/templates/repository-health/SUPPORT.md`.
- This standard is the reusable quality-layer companion for downstream repositories.

## Source Attribution

- Source manifests: `governance__github_docs.md`
- Primary source basis: GitHub Docs support and community guidance
- Alignment mode: direct-adaptation
- Reviewed on: 2026-03-27
