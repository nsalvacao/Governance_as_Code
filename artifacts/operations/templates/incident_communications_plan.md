---
title: Incident Communications Plan
artifact_type: template
status: public-draft
visibility: public
classification: public
owner: "{{OWNER_NAME}}"
review_cadence: quarterly
applies_to: incident communication during operational events
source_basis: Google SRE incident communication guidance and NIST incident response guidance
source_manifests:
  - operations__google_sre.md
  - operations__nist_cisa.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Communications Context

Fill in the fields below at incident declaration. The Communications Lead owns this document for the duration of the incident.

- **Incident ID:** `{{INCIDENT_ID}}`
- **Severity:** `{{SEVERITY}}`
- **Declared at (UTC):** `{{DECLARATION_TIME}}`
- **Communications Lead:** `{{COMMS_LEAD_NAME}}`
- **IC:** `{{IC_NAME}}`
- **Update interval:** `{{UPDATE_INTERVAL}}`

## Stakeholder Matrix

Identify all audiences at declaration time. Add rows as new stakeholders are identified. The message owner is responsible for each communication — the IC does not need to draft every message.

| Stakeholder Group | Channel | Frequency | Message Owner | First Notification Trigger |
|-------------------|---------|-----------|---------------|---------------------------|
| `{{STAKEHOLDER_GROUP_1}}` | `{{CHANNEL_1}}` | `{{FREQUENCY_1}}` | `{{MSG_OWNER_1}}` | `{{FIRST_TRIGGER_1}}` |
| `{{STAKEHOLDER_GROUP_2}}` | `{{CHANNEL_2}}` | `{{FREQUENCY_2}}` | `{{MSG_OWNER_2}}` | `{{FIRST_TRIGGER_2}}` |
| `{{STAKEHOLDER_GROUP_N}}` | `{{CHANNEL_N}}` | `{{FREQUENCY_N}}` | `{{MSG_OWNER_N}}` | `{{FIRST_TRIGGER_N}}` |

Typical stakeholder groups include: engineering on-call, engineering leadership, customer support, executive team, affected customers, status page subscribers, `{{ADDITIONAL_STAKEHOLDER_GROUP}}`.

## Communication Templates

Use the templates below verbatim where possible. Customize only the bracketed fields. Templates keep message style consistent and reduce drafting time under pressure.

### Initial Notification Template

Send within `{{INITIAL_NOTIFICATION_SLA}}` of incident declaration. Purpose: tell stakeholders what is known now, not what might happen.

```
{{INITIAL_NOTIFICATION_TEMPLATE}}

Subject: [{{SEVERITY}}] Service incident affecting {{AFFECTED_SERVICE}}

We are investigating an issue affecting {{AFFECTED_SERVICE}}.

What happened: {{WHAT_HAPPENED}}
Impact: {{CUSTOMER_IMPACT_DESCRIPTION}}
What we are doing: {{CURRENT_ACTIONS}}
Next update in: {{UPDATE_INTERVAL}}

Incident ID: {{INCIDENT_ID}}
```

### Status Update Template

Send at every `{{UPDATE_INTERVAL}}` interval, even if there is nothing new to report. Silence increases customer anxiety and internal escalations.

```
{{UPDATE_TEMPLATE}}

Subject: [UPDATE {{UPDATE_NUMBER}}] {{SEVERITY}} incident affecting {{AFFECTED_SERVICE}}

Current status: {{CURRENT_STATUS}}
Actions taken since last update: {{ACTIONS_TAKEN}}
Next steps: {{NEXT_STEPS}}
Next update: {{NEXT_UPDATE_TIME_UTC}}

Incident ID: {{INCIDENT_ID}}
```

### Resolution Notification Template

Send when the IC declares the incident resolved. Include enough detail that customers can assess whether they need to take action.

```
{{RESOLUTION_TEMPLATE}}

Subject: [RESOLVED] Service incident affecting {{AFFECTED_SERVICE}}

The incident affecting {{AFFECTED_SERVICE}} has been resolved as of {{RESOLUTION_TIME_UTC}}.

What happened: {{WHAT_HAPPENED_SUMMARY}}
Root cause summary: {{ROOT_CAUSE_SUMMARY}}
Resolution: {{RESOLUTION_DESCRIPTION}}
Duration: {{INCIDENT_DURATION}}
Follow-up: {{FOLLOW_UP_DESCRIPTION}}

We apologize for the impact. A full incident report will be available at {{REPORT_LINK}} within {{REPORT_PUBLICATION_SLA}}.

Incident ID: {{INCIDENT_ID}}
```

### Escalation Notification Template

Use when the incident scope or severity increases and new stakeholders must be notified or the update cadence must change.

```
Subject: [ESCALATED to {{NEW_SEVERITY}}] Incident {{INCIDENT_ID}} — {{AFFECTED_SERVICE}}

This incident has been escalated from {{PREVIOUS_SEVERITY}} to {{NEW_SEVERITY}}.

Reason for escalation: {{ESCALATION_REASON}}
Current impact: {{CURRENT_IMPACT}}
Actions in progress: {{CURRENT_ACTIONS}}
IC: {{IC_NAME}}
Next update in: {{UPDATE_INTERVAL}}
```

## Approval Rules

Before sending any external communication, verify:

1. IC has reviewed and approved the message content.
2. Legal review required if: security breach, data exposure, or regulatory notification obligation (`{{LEGAL_REVIEW_TRIGGER}}`).
3. Executive notification required for: SEV1 and any SEV2 with external customer impact (`{{EXEC_NOTIFICATION_TRIGGER}}`).

Internal updates (engineering team, on-call) do not require approval — send as soon as available.

## Escalation and Handoff

If the Communications Lead must hand off during an active incident:

1. Brief the incoming lead on: messages already sent, last update time, next scheduled update, any pending approvals.
2. Log the handoff in the communication log with timestamp and both lead names.
3. Notify the IC of the handoff.

## Communication Log

Record every communication sent during the incident. This log is required for the incident report and postmortem.

| Timestamp (UTC) | Channel | Message Summary | Sent By | Approved By |
|-----------------|---------|-----------------|---------|-------------|
| `{{TS_1}}` | `{{CHANNEL_LOG_1}}` | `{{MESSAGE_SUMMARY_1}}` | `{{SENDER_1}}` | `{{APPROVER_1}}` |
| `{{TS_2}}` | `{{CHANNEL_LOG_2}}` | `{{MESSAGE_SUMMARY_2}}` | `{{SENDER_2}}` | `{{APPROVER_2}}` |
| `{{TS_N}}` | `{{CHANNEL_LOG_N}}` | `{{MESSAGE_SUMMARY_N}}` | `{{SENDER_N}}` | `{{APPROVER_N}}` |

## Source Attribution

- Source manifests: operations__google_sre.md, operations__nist_cisa.md
- Primary source basis: Google SRE communication guidance and NIST incident response guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
