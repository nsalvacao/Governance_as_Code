---
title: Infrastructure as Code / Platform Baseline Record
artifact_type: template
status: public
visibility: public
classification: public
owner: platform-governance
review_cadence: quarterly
applies_to: repositories with declarative infrastructure or platform baselines
source_basis: OpenGitOps, AWS Well-Architected, and Microsoft platform baseline guidance
source_manifests:
  - platform__gitops.md
  - platform__aws_well_architected.md
  - platform__microsoft_learn.md
alignment_mode: hybrid-synthesis
updated: 2026-03-30
---

# Infrastructure as Code / Platform Baseline Record

## Baseline Metadata

| Field | Value |
|---|---|
| Baseline Name | `{{BASELINE_NAME}}` |
| Baseline ID | `{{BASELINE_ID}}` |
| Scope | `{{SCOPE}}` (e.g., production platform / shared services / `{{TEAM}}` team infrastructure) |
| IaC Framework | `{{IAC_FRAMEWORK}}` (Terraform `{{TERRAFORM_VERSION}}` / Pulumi / CDK / Helm `{{HELM_VERSION}}` / Kustomize) |
| Source Repository | `{{SOURCE_REPO}}` |
| Source Path | `{{SOURCE_PATH}}` |
| Revision / Tag | `{{REVISION}}` |
| Owner | `{{OWNER}}` |
| Last Reviewed | `{{LAST_REVIEWED}}` |

## Platform Components

| Component | Resource Type | Desired State | Current State | Drift? | Evidence |
|---|---|---|---|---|---|
| `{{COMPONENT_1_NAME}}` | `{{COMPONENT_1_TYPE}}` (e.g., VPC, K8s Namespace) | `{{COMPONENT_1_DESIRED}}` | `{{COMPONENT_1_CURRENT}}` | `{{COMPONENT_1_DRIFT}}` | `{{COMPONENT_1_EVIDENCE}}` |
| `{{COMPONENT_2_NAME}}` | `{{COMPONENT_2_TYPE}}` | `{{COMPONENT_2_DESIRED}}` | `{{COMPONENT_2_CURRENT}}` | `{{COMPONENT_2_DRIFT}}` | `{{COMPONENT_2_EVIDENCE}}` |

## Configuration Baseline

| Configuration Item | Value | Classification | Source |
|---|---|---|---|
| `{{CONFIG_1_NAME}}` | `{{CONFIG_1_VALUE}}` | `{{CONFIG_1_CLASS}}` (public / internal / secret-ref) | `{{CONFIG_1_SOURCE}}` |
| `{{CONFIG_2_NAME}}` | `{{CONFIG_2_VALUE}}` | `{{CONFIG_2_CLASS}}` | `{{CONFIG_2_SOURCE}}` |

## Security Baselines

| Control | Expected Value | Validation Method | Status |
|---|---|---|---|
| Encryption at rest | `{{ENCRYPTION_AT_REST}}` | `{{ENCRYPTION_VALIDATION}}` | `{{ENCRYPTION_STATUS}}` |
| Encryption in transit | `{{ENCRYPTION_IN_TRANSIT}}` | `{{TRANSIT_VALIDATION}}` | `{{TRANSIT_STATUS}}` |
| IAM least privilege | `{{IAM_POLICY}}` | `{{IAM_VALIDATION}}` | `{{IAM_STATUS}}` |
| Secrets management | `{{SECRETS_POLICY}}` | `{{SECRETS_VALIDATION}}` | `{{SECRETS_STATUS}}` |
| Network segmentation | `{{NETWORK_POLICY}}` | `{{NETWORK_VALIDATION}}` | `{{NETWORK_STATUS}}` |
| Audit logging | `{{AUDIT_POLICY}}` | `{{AUDIT_VALIDATION}}` | `{{AUDIT_STATUS}}` |

## Drift Detection

| Method | Tool | Cadence | Alert Destination |
|---|---|---|---|
| Automated plan | `{{DRIFT_TOOL}}` (e.g., `terraform plan`, Argo CD) | `{{DRIFT_CADENCE}}` | `{{DRIFT_ALERT_DESTINATION}}` |
| Manual review | `{{MANUAL_REVIEW_METHOD}}` | `{{MANUAL_REVIEW_CADENCE}}` | `{{MANUAL_REVIEW_OWNER}}` |

Drift tolerance: `{{DRIFT_TOLERANCE}}` (e.g., zero tolerance for security controls; `{{GRACE_PERIOD}}` for minor configuration drift).

Drift remediation SLA: `{{DRIFT_REMEDIATION_SLA}}`

## AWS Well-Architected Pillar Alignment

| Pillar | Compliance Status | Evidence |
|---|---|---|
| Operational Excellence | `{{OE_STATUS}}` | `{{OE_EVIDENCE_LINK}}` |
| Security | `{{SEC_STATUS}}` | `{{SEC_EVIDENCE_LINK}}` |
| Reliability | `{{REL_STATUS}}` | `{{REL_EVIDENCE_LINK}}` |
| Performance Efficiency | `{{PERF_STATUS}}` | `{{PERF_EVIDENCE_LINK}}` |
| Cost Optimization | `{{COST_STATUS}}` | `{{COST_EVIDENCE_LINK}}` |
| Sustainability | `{{SUST_STATUS}}` | `{{SUST_EVIDENCE_LINK}}` |

## Change History

| Date | Change | Commit / PR | Author |
|---|---|---|---|
| `{{CHANGE_DATE_1}}` | `{{CHANGE_DESC_1}}` | `{{CHANGE_REF_1}}` | `{{CHANGE_AUTHOR_1}}` |

## Source Attribution

- Source manifests: `platform__gitops.md`, `platform__aws_well_architected.md`, `platform__microsoft_learn.md`
- Primary source basis: declarative infrastructure and platform baseline guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-30
