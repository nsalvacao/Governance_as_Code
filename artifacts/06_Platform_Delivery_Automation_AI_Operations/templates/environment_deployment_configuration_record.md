---
title: Environment / Deployment Configuration Record
artifact_type: template
status: public-draft
visibility: public
classification: public
owner: platform-governance
review_cadence: quarterly
applies_to: repositories that configure deployable environments
source_basis: GitHub environment variables and GitOps configuration guidance
source_manifests:
  - governance__github_docs.md
  - platform__gitops.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

# Environment / Deployment Configuration Record

## Environment Metadata

| Field | Value |
|---|---|
| Environment Name | `{{ENVIRONMENT_NAME}}` |
| Environment ID | `{{ENVIRONMENT_ID}}` |
| Environment Type | `{{ENVIRONMENT_TYPE}}` (Development / Integration / Staging / Canary / Production / DR) |
| Deployment Target | `{{DEPLOYMENT_TARGET}}` (e.g., Kubernetes cluster `{{CLUSTER_NAME}}`, AWS account `{{AWS_ACCOUNT_ID}}`) |
| Region / Zone | `{{REGION}}` |
| Owner | `{{OWNER}}` |
| Record Version | `{{RECORD_VERSION}}` |
| Last Updated | `{{LAST_UPDATED}}` |
| Protection Rules | `{{PROTECTION_RULES}}` (e.g., required reviewers: `{{REQUIRED_REVIEWERS}}`, wait timer: `{{WAIT_TIMER}}` minutes) |

## Environment Variables

| Variable Name | Source | Classification | Notes |
|---|---|---|---|
| `{{VAR_1_NAME}}` | `{{VAR_1_SOURCE}}` (env config / GitHub Env / Vault) | Non-sensitive | `{{VAR_1_NOTES}}` |
| `{{VAR_2_NAME}}` | `{{VAR_2_SOURCE}}` | Non-sensitive | `{{VAR_2_NOTES}}` |

## Secrets References

Secrets are NEVER stored in this record. Reference the secret store location only.

| Secret Name | Store | Path / Key Name | Owner | Rotation Cadence |
|---|---|---|---|---|
| `{{SECRET_1_NAME}}` | `{{SECRET_1_STORE}}` (GitHub Secrets / Vault / AWS Secrets Manager) | `{{SECRET_1_PATH}}` | `{{SECRET_1_OWNER}}` | `{{SECRET_1_ROTATION}}` |
| `{{SECRET_2_NAME}}` | `{{SECRET_2_STORE}}` | `{{SECRET_2_PATH}}` | `{{SECRET_2_OWNER}}` | `{{SECRET_2_ROTATION}}` |

## Promotion Criteria (OpenGitOps / DORA Progressive Delivery)

This environment is the `{{PROMOTION_STAGE}}` stage in the promotion chain:
`{{PREVIOUS_ENV}}` → `{{ENVIRONMENT_NAME}}` → `{{NEXT_ENV}}`

| Promotion Criterion | Required Value | Verification Method |
|---|---|---|
| CI pipeline status | All required checks pass | `{{CI_STATUS_CHECK}}` |
| Test coverage | ≥ `{{COVERAGE_THRESHOLD}}`% | `{{COVERAGE_TOOL}}` |
| Security scan | No critical/high unresolved | `{{SECURITY_SCAN_TOOL}}` |
| Change approval | `{{MIN_APPROVALS}}` approval(s) from `{{APPROVAL_TEAM}}` | GitHub environment protection |
| `{{CUSTOM_CRITERION_1}}` | `{{CUSTOM_CRITERION_1_VALUE}}` | `{{CUSTOM_CRITERION_1_METHOD}}` |

## Infrastructure References

| Resource | Type | Identifier | IaC Source |
|---|---|---|---|
| `{{RESOURCE_1_NAME}}` | `{{RESOURCE_1_TYPE}}` | `{{RESOURCE_1_ID}}` | `{{RESOURCE_1_IAC_PATH}}` |
| `{{RESOURCE_2_NAME}}` | `{{RESOURCE_2_TYPE}}` | `{{RESOURCE_2_ID}}` | `{{RESOURCE_2_IAC_PATH}}` |

IaC baseline record: `{{IAC_BASELINE_RECORD_LINK}}`

## Compliance and Access

| Property | Value |
|---|---|
| Access restricted to | `{{ACCESS_TEAMS}}` |
| Audit logging | `{{AUDIT_LOGGING_STATUS}}` |
| Data classification | `{{DATA_CLASSIFICATION}}` |
| Compliance requirements | `{{COMPLIANCE_REQUIREMENTS}}` |

## Source Attribution

- Source manifests: `governance__github_docs.md`, `platform__gitops.md`
- Primary source basis: GitHub environment and GitOps configuration guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
