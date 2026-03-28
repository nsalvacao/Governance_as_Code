---
title: Incident Coordination Playbook
artifact_type: template
status: draft
visibility: public
classification: public
owner: "{{OWNER_NAME}}"
review_cadence: quarterly
applies_to: coordination playbook
source_basis: Google SRE Incident Management Guide
source_manifests:
  - operations__google_sre.md
  - operations__nist_cisa.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Playbook Metadata

| Field | Value |
|---|---|
| Playbook ID | `{{PLAYBOOK_ID}}` |
| Service | `{{SERVICE_NAME}}` |
| Severity | `{{SEVERITY}}` (SEV1 / SEV2 / Any) |
| Owner | `{{PLAYBOOK_OWNER}}` |
| Last Reviewed | `{{LAST_REVIEWED}}` |

## Trigger

| Field | Value |
|---|---|
| Detected by | `{{DETECTION_SYSTEM}}` |
| Incident ID | `{{INCIDENT_ID}}` |
| Alert / Signal | `{{ALERT_DESCRIPTION}}` |
| Impact class | `{{IMPACT_CLASS}}` |
| Severity declared | `{{SEVERITY}}` |

## Step 1 — Declare and Convene

1. Acknowledge alert in `{{ALERTING_TOOL}}` — assign to yourself
2. Declare incident in `{{INCIDENT_MANAGEMENT_TOOL}}` with title: `{{INCIDENT_TITLE_FORMAT}}`
3. Open war room: `{{WAR_ROOM_CHANNEL}}`
4. Post initial status: `[INCIDENT DECLARED] {{SERVICE_NAME}} — {{SEVERITY}} — {{INITIAL_IMPACT}} — IC: {{INCIDENT_COMMANDER}}`
5. Start timeline: `{{TIMELINE_TEMPLATE_LINK}}`

## Coordination Roles

| Role | Current Assignee | Responsibility |
|---|---|---|
| Incident Commander (IC) | `{{INCIDENT_COMMANDER}}` | Overall coordination, decision authority, external comms gate |
| Operations Lead | `{{OPERATIONS_LEAD}}` | Technical diagnosis and remediation; runs runbooks |
| Communications Lead | `{{COMMUNICATIONS_LEAD}}` | Stakeholder updates every `{{COMMS_CADENCE}}`; status page |
| SME | `{{SME_CONTACT}}` | Domain-specific analysis for `{{SYSTEMS_AFFECTED}}` |

## Step 2 — Assess and Scope

1. Validate alert against live instrumentation: `{{MONITORING_DASHBOARD_LINK}}`
2. Confirm affected systems: `{{SYSTEMS_AFFECTED}}`
3. Estimate blast radius: `{{BLAST_RADIUS_ASSESSMENT_GUIDE}}`
4. Update severity classification if scope has changed
5. Notify `{{STAKEHOLDER_LIST}}` per communication plan

## Step 3 — Coordinate Diagnosis and Remediation

1. Assign runbooks per affected system:

| System | Runbook | Assigned To |
|---|---|---|
| `{{SYSTEM_1}}` | `{{RUNBOOK_1_LINK}}` | `{{OPERATIONS_LEAD}}` |
| `{{SYSTEM_2}}` | `{{RUNBOOK_2_LINK}}` | `{{SME_CONTACT}}` |

2. Surface hypotheses in war room; document in timeline
3. Apply mitigation when identified; record step in timeline with evidence
4. Verify mitigation via: `{{VERIFICATION_PROCEDURE}}`

## Step 4 — Escalation

Escalate when:
- Impact scope expands beyond `{{ESCALATION_TRIGGER}}`
- No mitigation identified within `{{ESCALATION_TIMEOUT}}`
- Customer-visible SLA breach confirmed

Escalation path: `{{OPERATIONS_LEAD}}` → `{{INCIDENT_COMMANDER}}` → `{{MANAGER_CONTACT}}` → `{{EXECUTIVE_CONTACT}}`

## Step 5 — Resolution and Handoff

1. Confirm resolution criteria met: `{{RESOLUTION_CRITERIA}}`
2. Declare resolution in `{{INCIDENT_MANAGEMENT_TOOL}}`
3. Post resolution message: `[RESOLVED] {{SERVICE_NAME}} — {{RESOLUTION_SUMMARY}}`
4. Assign postmortem to IC: `{{POSTMORTEM_TEMPLATE_LINK}}`
5. Hand off action items to `{{ACTION_TRACKER}}`

## Communications Cadence

| Severity | Internal Update | External Update | Escalation Notify |
|---|---|---|---|
| SEV1 | Every `{{SEV1_INTERNAL_CADENCE}}` | Every `{{SEV1_EXTERNAL_CADENCE}}` | Immediate |
| SEV2 | Every `{{SEV2_INTERNAL_CADENCE}}` | Every `{{SEV2_EXTERNAL_CADENCE}}` | Within `{{SEV2_ESCALATION_SLA}}` |

## Source Attribution
- Source manifests: `operations__google_sre.md`, `operations__nist_cisa.md`
- Primary source basis: Google SRE Incident Management Guide
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
