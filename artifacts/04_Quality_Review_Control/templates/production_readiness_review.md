---
title: Production Readiness Review Template
artifact_type: template
status: public-draft
visibility: public
classification: public
owner: quality-platform
review_cadence: quarterly
applies_to: readiness checks before a change or service is treated as production-ready
source_basis: Google SRE production readiness practices; AWS Well-Architected operational readiness guidance
source_manifests:
  - operations__google_sre.md
  - platform__aws_well_architected.md
alignment_mode: direct-adaptation
updated: 2026-03-27
---

## Review Metadata

| Field | Value |
|---|---|
| Service / Change | `{{SERVICE_OR_CHANGE_NAME}}` |
| Version / Release | `{{VERSION}}` |
| Review Date | `{{REVIEW_DATE}}` |
| Review Owner | `{{REVIEW_OWNER}}` |
| PRR Approver | `{{PRR_APPROVER}}` |
| Review Type | `{{REVIEW_TYPE}}` (new service / major change / annual refresh) |

## Architecture and Design

| Criterion | Status | Evidence |
|---|---|---|
| Architecture diagram current and reviewed | `{{ARCH_DIAGRAM_STATUS}}` | `{{ARCH_DIAGRAM_LINK}}` |
| Data flow diagram includes all external dependencies | `{{DATA_FLOW_STATUS}}` | `{{DATA_FLOW_LINK}}` |
| Security threat model completed (STRIDE) | `{{THREAT_MODEL_STATUS}}` | `{{THREAT_MODEL_LINK}}` |
| Privacy review completed | `{{PRIVACY_REVIEW_STATUS}}` | `{{PRIVACY_REVIEW_LINK}}` |

## SLO and Alerting

| Criterion | Status | Evidence |
|---|---|---|
| SLO defined (SLI, target, error budget) | `{{SLO_DEFINED_STATUS}}` | `{{SLO_LINK}}` |
| Alerts configured for SLO burn rate | `{{ALERTING_STATUS}}` | `{{ALERTING_LINK}}` |
| Alerting tested (fired at least once in staging) | `{{ALERT_TEST_STATUS}}` | `{{ALERT_TEST_EVIDENCE}}` |
| On-call rotation configured | `{{ONCALL_STATUS}}` | `{{ONCALL_SCHEDULE_LINK}}` |

## Operational Readiness

| Criterion | Status | Evidence |
|---|---|---|
| Runbook written and reviewed | `{{RUNBOOK_STATUS}}` | `{{RUNBOOK_LINK}}` |
| Incident playbook available | `{{PLAYBOOK_STATUS}}` | `{{PLAYBOOK_LINK}}` |
| Rollback plan documented and tested | `{{ROLLBACK_STATUS}}` | `{{ROLLBACK_PLAN_LINK}}` |
| Deployment procedure documented | `{{DEPLOY_PROCEDURE_STATUS}}` | `{{DEPLOY_PROCEDURE_LINK}}` |

## Capacity and Performance

| Criterion | Status | Evidence |
|---|---|---|
| Load test executed at `{{LOAD_TEST_TARGET}}`× expected peak | `{{LOAD_TEST_STATUS}}` | `{{LOAD_TEST_RESULTS_LINK}}` |
| Capacity plan covers `{{CAPACITY_HORIZON}}` growth | `{{CAPACITY_PLAN_STATUS}}` | `{{CAPACITY_PLAN_LINK}}` |
| Resource limits and autoscaling configured | `{{AUTOSCALING_STATUS}}` | `{{AUTOSCALING_CONFIG_LINK}}` |

## Dependency Review

| Dependency | Type | Criticality | Fallback if Unavailable |
|---|---|---|---|
| `{{DEPENDENCY_1}}` | `{{DEP_1_TYPE}}` | `{{DEP_1_CRITICALITY}}` | `{{DEP_1_FALLBACK}}` |
| `{{DEPENDENCY_2}}` | `{{DEP_2_TYPE}}` | `{{DEP_2_CRITICALITY}}` | `{{DEP_2_FALLBACK}}` |

## Security and Compliance

| Criterion | Status | Evidence |
|---|---|---|
| SAST / DAST scan clean (no unresolved critical/high) | `{{SECURITY_SCAN_STATUS}}` | `{{SECURITY_SCAN_LINK}}` |
| Dependency vulnerability scan clean | `{{DEP_SCAN_STATUS}}` | `{{DEP_SCAN_LINK}}` |
| Secrets not hardcoded (secret scan passed) | `{{SECRET_SCAN_STATUS}}` | `{{SECRET_SCAN_LINK}}` |
| Compliance requirements verified: `{{COMPLIANCE_REQUIREMENTS}}` | `{{COMPLIANCE_STATUS}}` | `{{COMPLIANCE_EVIDENCE_LINK}}` |

## Open Risks and Mitigations

| Risk | Severity | Mitigation | Owner | Target Resolution |
|---|---|---|---|---|
| `{{RISK_1_DESCRIPTION}}` | `{{RISK_1_SEVERITY}}` | `{{RISK_1_MITIGATION}}` | `{{RISK_1_OWNER}}` | `{{RISK_1_TARGET_DATE}}` |

## PRR Decision

| Field | Value |
|---|---|
| Decision | `{{DECISION}}` (Approved / Approved with conditions / Deferred / Rejected) |
| Conditions | `{{CONDITIONS}}` |
| Next review | `{{NEXT_REVIEW_DATE}}` |
| Approver signature | `{{APPROVER_SIGNATURE}}` |

## Guidance

- Tie each criterion to an observable test or operational signal.
- A criterion marked `Pending` must be resolved before launch unless explicitly accepted by `{{PRR_APPROVER}}`.

## Source Attribution

- Source manifests: `operations__google_sre.md`, `platform__aws_well_architected.md`
- Primary source basis: Google SRE production readiness practices and AWS operational readiness guidance
- Alignment mode: direct-adaptation
- Reviewed on: 2026-03-27
