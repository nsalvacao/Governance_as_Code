---
title: Service Recovery Playbook
artifact_type: template
status: public-draft
visibility: public
classification: public
owner: "{{OWNER_NAME}}"
review_cadence: quarterly
applies_to: recovery playbook
source_basis: NIST SP 800-61r3, Google SRE
source_manifests: operations__nist_cisa.md, operations__google_sre.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Playbook Metadata

| Field | Value |
|---|---|
| Playbook ID | `{{PLAYBOOK_ID}}` |
| Service | `{{SERVICE_NAME}}` |
| Incident ID | `{{INCIDENT_ID}}` |
| Owner | `{{RECOVERY_OWNER}}` |
| Last Reviewed | `{{LAST_REVIEWED}}` |

## Recovery Objectives

| Objective | Target | Source |
|---|---|---|
| Recovery Time Objective (RTO) | `{{RTO}}` | SLA / SLO definition |
| Recovery Point Objective (RPO) | `{{RPO}}` | Data loss tolerance |
| Max allowable downtime | `{{MAX_DOWNTIME}}` | Error budget |
| Systems prioritized for recovery | `{{SYSTEMS_PRIORITIZED}}` | By criticality tier |

## Pre-Recovery Checklist

Before initiating recovery:

- [ ] Incident is in "Containment" phase — active threat mitigated
- [ ] Root cause is known or mitigated enough to proceed
- [ ] Change freeze confirmed: `{{CHANGE_FREEZE_STATUS}}`
- [ ] Data integrity verified: `{{DATA_INTEGRITY_CHECK}}`
- [ ] Rollback plan available: `{{ROLLBACK_PLAN_LINK}}`
- [ ] Recovery owner assigned: `{{RECOVERY_OWNER}}`

## Recovery Steps

### Step 1 — Containment Verification

1. Confirm containment runbook completed for: `{{SYSTEMS_CONTAINED}}`
2. Verify no active data loss or ongoing attack vector
3. Check: `{{CONTAINMENT_VERIFICATION_COMMAND}}`
4. Expected output: `{{CONTAINMENT_EXPECTED_OUTPUT}}`

### Step 2 — Data and State Recovery

| Data Type | Recovery Method | Source | Verification |
|---|---|---|---|
| `{{DATA_TYPE_1}}` | `{{RECOVERY_METHOD_1}}` (restore from backup / replay / re-derive) | `{{DATA_SOURCE_1}}` | `{{DATA_VERIFICATION_1}}` |
| `{{DATA_TYPE_2}}` | `{{RECOVERY_METHOD_2}}` | `{{DATA_SOURCE_2}}` | `{{DATA_VERIFICATION_2}}` |

Backup location: `{{BACKUP_LOCATION}}`
Last known good backup: `{{LAST_GOOD_BACKUP_TIMESTAMP}}`

### Step 3 — Service Restoration

1. `{{RESTORATION_STEP_1}}` — command: `{{RESTORATION_CMD_1}}`
2. `{{RESTORATION_STEP_2}}` — command: `{{RESTORATION_CMD_2}}`
3. Enable traffic gradually: `{{TRAFFIC_ENABLEMENT_PROCEDURE}}`
4. Monitor during ramp-up: `{{RAMP_UP_MONITORING_DASHBOARD}}`

Failover procedure (if applicable): `{{FAILOVER_RUNBOOK_LINK}}`

### Step 4 — Functional Validation

| Validation Check | Method | Expected Result | Pass? |
|---|---|---|---|
| `{{VALIDATION_CHECK_1}}` | `{{VALIDATION_METHOD_1}}` | `{{EXPECTED_RESULT_1}}` | `{{PASS_1}}` |
| `{{VALIDATION_CHECK_2}}` | `{{VALIDATION_METHOD_2}}` | `{{EXPECTED_RESULT_2}}` | `{{PASS_2}}` |
| SLI signals returning to normal | `{{SLI_DASHBOARD_LINK}}` | Within 5% of baseline after `{{STABILIZATION_PERIOD}}` | `{{SLI_PASS}}` |

### Step 5 — Error Budget Reconciliation

1. Calculate error budget consumed by this incident: `{{BUDGET_CALCULATION_PROCEDURE}}`
2. Update error budget dashboard: `{{ERROR_BUDGET_TRACKING_LINK}}`
3. Determine if feature freeze is triggered: threshold = `{{FREEZE_THRESHOLD}}`%
4. Record in postmortem: `{{INCIDENT_REPORT_URL}}`

## Recovery Confirmation

| Field | Value |
|---|---|
| Recovery owner | `{{RECOVERY_OWNER}}` |
| Recovery declared at | `{{RECOVERY_TIMESTAMP_UTC}}` (UTC) |
| Total downtime | `{{TOTAL_DOWNTIME}}` |
| RTO met? | `{{RTO_MET}}` (Yes / No — if No: `{{RTO_MISS_EXPLANATION}}`) |
| RPO met? | `{{RPO_MET}}` |
| Validation evidence | `{{VALIDATION_ARTIFACT_URL}}` |
| Incident report | `{{INCIDENT_REPORT_URL}}` |
| Postmortem initiated? | `{{POSTMORTEM_INITIATED}}` — link: `{{POSTMORTEM_LINK}}` |

## Source Attribution
- Source manifests: `operations__nist_cisa.md`, `operations__google_sre.md`
- Primary source basis: NIST SP 800-61r3, Google SRE Incident Management Guide
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
