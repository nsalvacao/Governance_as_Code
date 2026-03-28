---
title: Incident Response Plan
artifact_type: template
status: public-draft
visibility: public
classification: public
owner: "{{OWNER_NAME}}"
review_cadence: quarterly
applies_to: incident response planning
source_basis: NIST SP 800-61r3 and Google SRE incident management guidance
source_manifests:
  - operations__nist_cisa.md
  - operations__google_sre.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Purpose

Provide the reusable plan structure for response phases, decision rights, communications, and recovery coordination following the NIST SP 800-61r2 Incident Response Lifecycle.

## Plan Metadata

| Field | Value |
|---|---|
| Plan ID | `{{IRP_ID}}` |
| Service / Scope | `{{SERVICE_OR_SCOPE}}` |
| Plan Owner | `{{PLAN_OWNER}}` |
| Version | `{{PLAN_VERSION}}` |
| Approved By | `{{PLAN_APPROVER}}` |
| Last Reviewed | `{{LAST_REVIEWED}}` |
| Next Review | `{{NEXT_REVIEW}}` |

## Phase 1 — Preparation

Activities performed BEFORE an incident occurs:

| Activity | Owner | Status | Evidence |
|---|---|---|---|
| On-call rotation configured | `{{ONCALL_OWNER}}` | `{{ONCALL_STATUS}}` | `{{ONCALL_SCHEDULE_LINK}}` |
| Runbooks written and accessible | `{{RUNBOOK_OWNER}}` | `{{RUNBOOK_STATUS}}` | `{{RUNBOOK_LOCATION}}` |
| Communication channels configured | `{{COMMS_OWNER}}` | `{{COMMS_STATUS}}` | `{{COMMS_CHANNEL}}` |
| Monitoring and alerting operational | `{{MONITORING_OWNER}}` | `{{MONITORING_STATUS}}` | `{{MONITORING_DASHBOARD}}` |
| IR team trained | `{{TRAINING_OWNER}}` | `{{TRAINING_STATUS}}` | `{{TRAINING_EVIDENCE}}` |
| Tools available | `{{TOOLS_OWNER}}` | `{{TOOLS_STATUS}}` | `{{TOOLS_LIST}}` |

## Phase 2 — Detection and Analysis

### Detection Sources

| Source | Tool | Alert Routing |
|---|---|---|
| `{{DETECTION_SOURCE_1}}` | `{{DETECTION_TOOL_1}}` | `{{ALERT_ROUTING_1}}` |
| `{{DETECTION_SOURCE_2}}` | `{{DETECTION_TOOL_2}}` | `{{ALERT_ROUTING_2}}` |

### Severity Classification

| Severity | Criteria | IC Required? | Comms Required? | Response SLA |
|---|---|---|---|---|
| SEV1 | `{{SEV1_CRITERIA}}` (e.g., complete service unavailability, data loss) | Yes | Yes — `{{SEV1_COMMS_SLA}}` | `{{SEV1_RESPONSE_SLA}}` |
| SEV2 | `{{SEV2_CRITERIA}}` (e.g., major degradation, key feature unavailable) | Yes | Yes — `{{SEV2_COMMS_SLA}}` | `{{SEV2_RESPONSE_SLA}}` |
| SEV3 | `{{SEV3_CRITERIA}}` (e.g., partial degradation, workaround available) | No | Optional | `{{SEV3_RESPONSE_SLA}}` |
| SEV4 | `{{SEV4_CRITERIA}}` (e.g., minor issue, no user impact) | No | No | `{{SEV4_RESPONSE_SLA}}` |

### Evidence Preservation

NIST SP 800-61r2 mandates evidence collection and preservation during Detection & Analysis. Evidence collected here supports root cause analysis, postmortems, and potential legal or regulatory proceedings.

| Evidence Source | Collection Method | Storage Location | Retention Period | Owner |
|---|---|---|---|---|
| Application logs | `{{LOG_COLLECTION_CMD}}` (e.g., `kubectl logs`, cloud log export) | `{{LOG_STORAGE_LOCATION}}` | `{{LOG_RETENTION}}` | `{{LOG_OWNER}}` |
| Infrastructure metrics | Snapshot from `{{METRICS_PLATFORM}}` | `{{METRICS_SNAPSHOT_LOCATION}}` | `{{METRICS_RETENTION}}` | `{{METRICS_OWNER}}` |
| Network traffic / traces | `{{TRACE_COLLECTION_METHOD}}` | `{{TRACE_STORAGE_LOCATION}}` | `{{TRACE_RETENTION}}` | `{{TRACE_OWNER}}` |
| Configuration state | `{{CONFIG_SNAPSHOT_CMD}}` | `{{CONFIG_STORAGE_LOCATION}}` | `{{CONFIG_RETENTION}}` | `{{CONFIG_OWNER}}` |
| `{{ADDITIONAL_EVIDENCE_SOURCE}}` | `{{ADDITIONAL_EVIDENCE_METHOD}}` | `{{ADDITIONAL_STORAGE}}` | `{{ADDITIONAL_RETENTION}}` | `{{ADDITIONAL_OWNER}}` |

Preservation rules: do NOT modify or delete any evidence source during active response. If containment requires disabling a component, snapshot its state first.

### Initial Triage Steps

1. Acknowledge alert in `{{ALERTING_TOOL}}`
2. Assess severity using classification table above
3. Declare incident and assign IC for SEV1/SEV2
4. Open war room in `{{WAR_ROOM_CHANNEL}}`
5. Start incident timeline at `{{TIMELINE_TEMPLATE_LINK}}`
6. Assign roles (see Roles section)

## Roles and Escalation Paths

| Role | Responsibilities | Primary Contact | Backup Contact |
|---|---|---|---|
| Incident Commander (IC) | Overall coordination, decision authority, declares resolution | `{{IC_PRIMARY}}` | `{{IC_BACKUP}}` |
| Operations Lead | Technical diagnosis and remediation | `{{OPS_LEAD_PRIMARY}}` | `{{OPS_LEAD_BACKUP}}` |
| Communications Lead | Stakeholder updates, internal/external messaging | `{{COMMS_LEAD_PRIMARY}}` | `{{COMMS_LEAD_BACKUP}}` |
| Subject Matter Expert | Domain-specific technical analysis | `{{SME_CONTACT}}` | `{{SME_BACKUP}}` |
| Executive Sponsor | Authorises major decisions (SEV1 only) | `{{EXECUTIVE_CONTACT}}` | `{{EXECUTIVE_BACKUP}}` |

Escalation path: On-call → IC → `{{MANAGER_CONTACT}}` → `{{EXECUTIVE_CONTACT}}`

## Phase 3 — Containment, Eradication, and Recovery

### Containment

Goal: limit impact without disrupting evidence collection.

| Action | Trigger | Command / Procedure | Owner |
|---|---|---|---|
| `{{CONTAINMENT_ACTION_1}}` | `{{CONTAINMENT_TRIGGER_1}}` | `{{CONTAINMENT_CMD_1}}` | `{{CONTAINMENT_OWNER_1}}` |
| `{{CONTAINMENT_ACTION_2}}` | `{{CONTAINMENT_TRIGGER_2}}` | `{{CONTAINMENT_CMD_2}}` | `{{CONTAINMENT_OWNER_2}}` |

### Eradication

Goal: remove the root cause.

1. `{{ERADICATION_STEP_1}}`
2. `{{ERADICATION_STEP_2}}`
3. Verify: `{{ERADICATION_VERIFICATION}}`

### Recovery

Goal: restore service to normal operational state.

1. `{{RECOVERY_STEP_1}}`
2. `{{RECOVERY_STEP_2}}`
3. Smoke test: `{{SMOKE_TEST_PROCEDURE}}`
4. Confirm SLO metrics returning to baseline: `{{SLO_DASHBOARD_LINK}}`
5. Declare resolution when: `{{RESOLUTION_CRITERIA}}`

Recovery target (RTO): `{{RTO}}`

## Phase 4 — Post-Incident Activity

| Activity | Owner | Deadline | Output |
|---|---|---|---|
| Incident report filed | IC | `{{INCIDENT_REPORT_DEADLINE}}` | `{{INCIDENT_REPORT_LINK}}` |
| Postmortem initiated (SEV1/SEV2) | IC | `{{POSTMORTEM_INITIATION_DEADLINE}}` | `{{POSTMORTEM_LINK}}` |
| Action items tracked | `{{ACTION_TRACKER_OWNER}}` | Per action due date | `{{ACTION_TRACKER_LINK}}` |
| SLO impact recorded | `{{SRE_OWNER}}` | Within `{{SLO_RECORDING_DEADLINE}}` | Error budget dashboard updated |

## Communication Templates

### Internal Update (during incident)

```
[INCIDENT UPDATE] {{SERVICE_NAME}} — SEV{{SEVERITY}} — {{STATUS}}
Time: {{TIMESTAMP_UTC}}
Impact: {{IMPACT_SUMMARY}}
Current status: {{CURRENT_STATUS}}
Next update: {{NEXT_UPDATE_TIME}}
IC: {{IC_NAME}}
```

### External Status Page Update

```
Investigating: We are investigating reports of {{EXTERNAL_IMPACT_DESCRIPTION}}.
Our team is actively working on a resolution. Next update: {{NEXT_UPDATE_TIME_UTC}}.
```

## Source Attribution

- Source manifests: operations__nist_cisa.md, operations__google_sre.md
- Primary source basis: NIST SP 800-61r3 and Google SRE incident management guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27

