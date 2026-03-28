---
title: Production Readiness Standard
artifact_type: policy
status: public-draft
visibility: public
classification: public
owner: reliability-platform
review_cadence: semiannual
applies_to: releases carrying new services or significant changes
source_basis: Google SRE Production Readiness Review & AWS Operational Readiness guidance
source_manifests: operations__google_sre.md platform__aws_well_architected.md platform__microsoft_learn.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Purpose

Define the criteria a service or significant change must meet before receiving production traffic, following Google SRE Production Readiness Review (PRR) and AWS Operational Readiness Review (ORR) practices.

## Applicability

A PRR is required for:

| Scenario | PRR Type | Approver |
|---|---|---|
| New service going to production | Full PRR | `{{SRE_APPROVER}}` |
| Existing service: new critical dependency | Partial PRR (dependency section) | `{{SRE_APPROVER}}` |
| Existing service: traffic × `{{TRAFFIC_SCALE_THRESHOLD}}` | Capacity PRR | `{{CAPACITY_PLANNER}}` |
| Existing service: annual review | Refresh PRR | `{{SERVICE_OWNER}}` |
| Infrastructure-only change | Infra ORR | `{{PLATFORM_APPROVER}}` |

## PRR Pillars and Required Evidence

### 1. Service Understanding

| Requirement | Evidence Required |
|---|---|
| Architecture diagram (current) | `{{ARCH_DIAGRAM_LINK}}` |
| Dependency inventory (all upstream/downstream) | `{{DEPENDENCY_INVENTORY_LINK}}` |
| Data classification and privacy review | `{{DATA_CLASSIFICATION_DOC}}` |
| Service owner and on-call rotation defined | `{{ONCALL_SCHEDULE_LINK}}` |

### 2. Observability

| Requirement | Evidence Required |
|---|---|
| SLI definition documented | `{{SLI_DOC_LINK}}` |
| SLO target set and agreed with product | `{{SLO_DOC_LINK}}` |
| Dashboards cover SLI signals | `{{DASHBOARD_LINK}}` |
| Burn rate alerts configured (fast and slow burn) | `{{ALERT_CONFIG_LINK}}` |
| Alerts have been tested (fired in staging) | `{{ALERT_TEST_EVIDENCE}}` |
| Log query patterns documented in runbook | `{{RUNBOOK_LINK}}` |

### 3. Deployment and Automation

| Requirement | Evidence Required |
|---|---|
| Deployment workflow is automated and reproducible | `{{DEPLOY_WORKFLOW_LINK}}` |
| Rollback procedure documented and tested | `{{ROLLBACK_PLAN_LINK}}` |
| Canary/staged rollout configured | `{{ROLLOUT_CONFIG_LINK}}` |
| Feature flags available for emergency disable | `{{FEATURE_FLAG_DOC}}` |

### 4. Capacity Planning

| Requirement | Evidence Required |
|---|---|
| Load test at `{{LOAD_TEST_MULTIPLIER}}`× expected peak | `{{LOAD_TEST_REPORT_LINK}}` |
| Autoscaling configured with limits | `{{AUTOSCALING_CONFIG_LINK}}` |
| Capacity plan covers `{{CAPACITY_FORECAST_HORIZON}}` | `{{CAPACITY_PLAN_LINK}}` |
| Cost estimate per unit of traffic | `{{COST_MODEL_LINK}}` |

### 5. Security and Compliance

| Requirement | Evidence Required |
|---|---|
| SAST scan: no unresolved Critical/High | `{{SAST_REPORT_LINK}}` |
| DAST scan completed | `{{DAST_REPORT_LINK}}` |
| Dependency vulnerability scan clean | `{{DEP_SCAN_LINK}}` |
| Secrets management approach documented | `{{SECRETS_DOC_LINK}}` |
| Compliance requirements verified: `{{COMPLIANCE_REQS}}` | `{{COMPLIANCE_EVIDENCE_LINK}}` |

### 6. Support Readiness

| Requirement | Evidence Required |
|---|---|
| Incident playbook written | `{{PLAYBOOK_LINK}}` |
| Escalation matrix defined | `{{ESCALATION_MATRIX_LINK}}` |
| On-call training completed | `{{TRAINING_EVIDENCE}}` |
| Postmortem template available | `{{POSTMORTEM_TEMPLATE_LINK}}` |

## PRR Decision Criteria

- **Approved**: All pillar requirements met; all evidence links verified.
- **Approved with conditions**: Minor gaps accepted by `{{SRE_APPROVER}}`; remediation plan with due date `{{REMEDIATION_DUE_DATE}}`.
- **Deferred**: Launch date moved; re-review scheduled for `{{RECHECK_DATE}}`.
- **Rejected**: One or more mandatory requirements unmet; service cannot go to production until resolved.

## Process Notes

- PRR must be completed minimum `{{PRR_LEAD_TIME}}` business days before planned launch.
- Evidence links must resolve to real, current artifacts — not placeholders.
- Downstream repos instantiate the canonical production readiness review template at `artifacts/04_Quality_Review_Control/quality/templates/production_readiness_review.md`.

## Source Attribution

- Source manifests: `operations__google_sre.md`, `platform__aws_well_architected.md`, `platform__microsoft_learn.md`
- Primary source basis: Google SRE Production Readiness Review, AWS ORR, Microsoft Learn deployment guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
