---
title: Production Readiness Review Template
artifact_type: template
status: public-draft
visibility: public
classification: public
owner: reliability-platform
review_cadence: semiannual
applies_to: production launches and major updates
source_basis: Google SRE Production Readiness Review / AWS ORR combined
source_manifests: operations__google_sre.md platform__aws_well_architected.md platform__microsoft_learn.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Review Metadata

| Field | Value |
|---|---|
| Service / Change | `{{SERVICE_NAME}}` |
| Version | `{{VERSION}}` |
| Review Type | `{{REVIEW_TYPE}}` (new service / major change / annual refresh / infra ORR) |
| Planned Launch Date | `{{PLANNED_LAUNCH_DATE}}` |
| Review Date | `{{REVIEW_DATE}}` |
| Review Owner | `{{REVIEW_OWNER}}` |
| SRE Approver | `{{SRE_APPROVER}}` |

## Pillar 1 — Service Understanding

| Requirement | Status | Evidence |
|---|---|---|
| Architecture diagram current | `{{ARCH_STATUS}}` | `{{ARCH_DIAGRAM_LINK}}` |
| Dependency inventory complete | `{{DEP_INVENTORY_STATUS}}` | `{{DEPENDENCY_INVENTORY_LINK}}` |
| Data classification reviewed | `{{DATA_CLASS_STATUS}}` | `{{DATA_CLASSIFICATION_DOC}}` |
| Service owner defined | `{{OWNER_STATUS}}` | `{{SERVICE_OWNER}}` |
| On-call rotation configured | `{{ONCALL_STATUS}}` | `{{ONCALL_SCHEDULE_LINK}}` |

## Pillar 2 — Observability

| Requirement | Status | Evidence |
|---|---|---|
| SLI defined and implemented | `{{SLI_STATUS}}` | `{{SLI_DOC_LINK}}` |
| SLO target set (`{{SLO_TARGET}}`%) | `{{SLO_STATUS}}` | `{{SLO_DOC_LINK}}` |
| Error budget = `{{ERROR_BUDGET_PERCENT}}`% | Derived | See SLO doc |
| Dashboard covers SLI signals | `{{DASHBOARD_STATUS}}` | `{{DASHBOARD_LINK}}` |
| Fast-burn alert (`{{FAST_BURN_RATE}}`×) configured | `{{FAST_BURN_ALERT_STATUS}}` | `{{ALERT_CONFIG_LINK}}` |
| Slow-burn alert (`{{SLOW_BURN_RATE}}`×) configured | `{{SLOW_BURN_ALERT_STATUS}}` | `{{ALERT_CONFIG_LINK}}` |
| Runbook linked from alerts | `{{RUNBOOK_LINK_STATUS}}` | `{{RUNBOOK_LINK}}` |

## Pillar 3 — Deployment and Automation

| Requirement | Status | Evidence |
|---|---|---|
| Deployment workflow automated | `{{DEPLOY_WORKFLOW_STATUS}}` | `{{DEPLOY_WORKFLOW_LINK}}` |
| Rollback tested in staging | `{{ROLLBACK_STATUS}}` | `{{ROLLBACK_TEST_EVIDENCE}}` |
| Canary / staged rollout configured | `{{CANARY_STATUS}}` | `{{ROLLOUT_CONFIG_LINK}}` |
| Feature flags available | `{{FEATURE_FLAGS_STATUS}}` | `{{FEATURE_FLAG_DOC}}` |

## Pillar 4 — Capacity Planning

| Requirement | Status | Evidence |
|---|---|---|
| Load test at `{{LOAD_TEST_MULTIPLIER}}`× expected peak | `{{LOAD_TEST_STATUS}}` | `{{LOAD_TEST_REPORT_LINK}}` |
| Autoscaling configured with limits | `{{AUTOSCALING_STATUS}}` | `{{AUTOSCALING_CONFIG_LINK}}` |
| Capacity plan: `{{CAPACITY_FORECAST_HORIZON}}` forecast | `{{CAPACITY_PLAN_STATUS}}` | `{{CAPACITY_PLAN_LINK}}` |

## Pillar 5 — Security and Compliance

| Requirement | Status | Evidence |
|---|---|---|
| SAST clean (no unresolved Critical/High) | `{{SAST_STATUS}}` | `{{SAST_REPORT_LINK}}` |
| Dependency scan clean | `{{DEP_SCAN_STATUS}}` | `{{DEP_SCAN_LINK}}` |
| Compliance: `{{COMPLIANCE_REQUIREMENTS}}` | `{{COMPLIANCE_STATUS}}` | `{{COMPLIANCE_EVIDENCE_LINK}}` |

## Pillar 6 — Support Readiness

| Requirement | Status | Evidence |
|---|---|---|
| Incident playbook written | `{{PLAYBOOK_STATUS}}` | `{{PLAYBOOK_LINK}}` |
| Escalation matrix defined | `{{ESCALATION_STATUS}}` | `{{ESCALATION_MATRIX_LINK}}` |
| On-call training complete | `{{TRAINING_STATUS}}` | `{{TRAINING_EVIDENCE}}` |

## Open Risks

| Risk | Severity | Mitigation | Owner | Due Date |
|---|---|---|---|---|
| `{{RISK_1}}` | `{{RISK_1_SEVERITY}}` | `{{RISK_1_MITIGATION}}` | `{{RISK_1_OWNER}}` | `{{RISK_1_DUE_DATE}}` |

## Review Decision

| Field | Value |
|---|---|
| Decision | `{{DECISION}}` (Approved / Approved with conditions / Deferred / Rejected) |
| Conditions | `{{CONDITIONS}}` |
| Required actions before launch | `{{REQUIRED_ACTIONS}}` |
| Action owner | `{{ACTION_OWNER}}` |
| Actions due by | `{{DUE_DATE}}` |
| Next review | `{{NEXT_REVIEW_DATE}}` |
| Approver | `{{SRE_APPROVER}}` |

## Source Attribution

- Source manifests: `operations__google_sre.md`, `platform__aws_well_architected.md`, `platform__microsoft_learn.md`
- Primary source basis: Google SRE PRR, AWS ORR, Microsoft deployment guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
