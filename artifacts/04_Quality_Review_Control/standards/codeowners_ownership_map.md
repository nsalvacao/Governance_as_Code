---
title: CODEOWNERS and Ownership Map
artifact_type: standard
status: public
visibility: public
classification: public
owner: quality-platform
review_cadence: quarterly
applies_to: file ownership and review routing
source_basis: GitHub Docs CODEOWNERS guidance
source_manifests:
  - governance__github_docs.md
alignment_mode: direct-adaptation
updated: 2026-03-30
---

## Purpose

Define how ownership is assigned using GitHub CODEOWNERS syntax so review routing is deterministic, traceable, and maintainable.

## Ownership Model

All paths are matched relative to repository root. The last matching rule wins (bottom-up precedence).

```
# Syntax: <pattern> <owner> [<owner2> ...]
# Owners: @username, @org/team-name, or user@example.com

# Default owners for everything not explicitly assigned
*                               @{{DEFAULT_OWNER_TEAM}}

# Dimension-level ownership
artifacts/01_Governance_Method/                            @{{ORG_NAME}}/{{GOVERNANCE_TEAM}}
artifacts/02_Discovery_Planning_Early_Learning/           @{{ORG_NAME}}/{{PRODUCT_TEAM}}
artifacts/03_Architecture_Security_Decision/              @{{ORG_NAME}}/{{ARCHITECTURE_TEAM}}
artifacts/04_Quality_Review_Control/                      @{{ORG_NAME}}/{{QUALITY_TEAM}}
artifacts/05_Delivery_Change_Readiness/                   @{{ORG_NAME}}/{{DELIVERY_TEAM}}
artifacts/06_Platform_Delivery_Automation_AI_Operations/  @{{ORG_NAME}}/{{PLATFORM_TEAM}}
artifacts/07_Operations_Incidents_Continuity/             @{{ORG_NAME}}/{{OPS_TEAM}}
artifacts/08_Knowledge_Documentation_Continuous_Improvement/ @{{ORG_NAME}}/{{SRE_TEAM}}
artifacts/09_Project_Portfolio_Service_Governance/        @{{ORG_NAME}}/{{PMO_TEAM}}
artifacts/10_Risk_Exceptions_Traceability/                @{{ORG_NAME}}/{{RISK_TEAM}}

# Critical governance files — require explicit owner approval
scripts/                        @{{AUTOMATION_OWNER}}
.github/workflows/              @{{DEVOPS_OWNER}}
SECURITY.md                     @{{SECURITY_OFFICER}}
```

## Team Registration

| Team Slug | GitHub Team | Responsibility | Review SLA |
|---|---|---|---|
| `{{ARCHITECTURE_TEAM}}` | `@{{ORG_NAME}}/{{ARCHITECTURE_TEAM}}` | Architecture decisions and ADRs | `{{ARCH_REVIEW_SLA}}` |
| `{{SRE_TEAM}}` | `@{{ORG_NAME}}/{{SRE_TEAM}}` | Reliability, operations, postmortems | `{{SRE_REVIEW_SLA}}` |
| `{{PLATFORM_TEAM}}` | `@{{ORG_NAME}}/{{PLATFORM_TEAM}}` | CI/CD, GitOps, infrastructure | `{{PLATFORM_REVIEW_SLA}}` |
| `{{QUALITY_TEAM}}` | `@{{ORG_NAME}}/{{QUALITY_TEAM}}` | Quality standards, security policy | `{{QUALITY_REVIEW_SLA}}` |
| `{{GOVERNANCE_TEAM}}` | `@{{ORG_NAME}}/{{GOVERNANCE_TEAM}}` | Governance templates, contribution rules | `{{GOVERNANCE_REVIEW_SLA}}` |

## Maintenance Rules

- Add new path ownership entries when a new directory or artifact dimension is introduced.
- Review ownership entries when team membership or organisational structure changes.
- Never leave a critical path (e.g., `scripts/`, `.github/`) without at least one named owner.
- Validate CODEOWNERS syntax before merging: `.github/` enforced file must parse correctly.

## Canonical Relationship

- The GitHub-native file used for enforcement lives in `artifacts/01_Governance_Method/templates/github-native/CODEOWNERS`.
- This standard documents the ownership model and how it should be maintained.

## Source Attribution

- Source manifests: `governance__github_docs.md`
- Primary source basis: GitHub Docs CODEOWNERS guidance
- Alignment mode: direct-adaptation
- Reviewed on: 2026-03-30
