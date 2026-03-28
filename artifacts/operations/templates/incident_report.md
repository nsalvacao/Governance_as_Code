---
title: Incident Report Template
artifact_type: template
status: draft
visibility: public
classification: public
owner: "{{OWNER_NAME}}"
review_cadence: quarterly
applies_to: incident report
source_basis: Google SRE Incident Management Guide, NIST SP 800-61r3
source_manifests: operations__google_sre.md, operations__nist_cisa.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Incident Identification

Complete this section at declaration time. Update as facts change; do not wait until closure.

- **Incident ID:** `{{INCIDENT_ID}}`
- **Title:** `{{INCIDENT_TITLE}}`
- **Date declared (UTC):** `{{DATE}}`
- **Date resolved (UTC):** `{{RESOLUTION_DATE}}`
- **Severity:** `{{SEVERITY}}`
- **Impact class:** `{{IMPACT_CLASS}}`
- **Systems affected:** `{{SERVICE_1}}`, `{{SERVICE_2}}`, `{{SERVICE_N}}`
- **Recovery target:** `{{RECOVERY_WINDOW_HOURS}}`
- **Incident Commander:** `{{INCIDENT_COMMANDER}}`
- **Operations Lead:** `{{OPERATIONS_LEAD}}`
- **Communications Lead:** `{{COMMUNICATIONS_LEAD}}`

## Executive Summary

Write a 5-minute read of the incident. This section is read by executives and non-technical stakeholders who need context without detail. Cover: what happened, who was affected, how long it lasted, and what is being done to prevent recurrence.

`{{EXECUTIVE_SUMMARY}}`

## Impact

Quantify the impact as precisely as possible. Estimates are acceptable if exact figures are unavailable; note the basis for any estimate.

- **Users affected:** `{{USERS_AFFECTED}}`
- **Duration:** `{{DURATION}}`
- **Services impacted:** `{{SERVICE_1}}`, `{{SERVICE_N}}`
- **SLO impact:** `{{SLO_IMPACT}}` — describe which SLOs were breached and by how much.
- **Customer impact:** `{{CUSTOMER_IMPACT}}`
- **Error budget impact:** `{{ERROR_BUDGET_IMPACT}}`
- **Business impact analysis reference:** `{{BIA_URL}}`

## Timeline

Record events in chronological UTC order. Include every significant action, decision, and observation. Link to the full incident timeline document for granular detail.

| Timestamp (UTC) | Event | Actor |
|-----------------|-------|-------|
| `{{TS_UTC_1}}` | `{{EVENT_1}}` | `{{ACTOR_1}}` |
| `{{TS_UTC_2}}` | `{{EVENT_2}}` | `{{ACTOR_2}}` |
| `{{TS_UTC_N}}` | `{{EVENT_N}}` | `{{ACTOR_N}}` |

For the full event-by-event record, see the incident timeline: `{{TIMELINE_LINK}}`.

## Root Cause

State the root cause in one or two sentences. If a full RCA is available, link to it. The root cause must be specific enough to drive a corrective action — "human error" is not an acceptable root cause statement.

`{{ROOT_CAUSE}}`

Full RCA link (if available): `{{RCA_LINK}}`

## Contributing Factors

List conditions that allowed the root cause to have its full impact. Contributing factors are not root causes — they are gaps in defenses that should be addressed independently.

- `{{CONTRIBUTING_FACTOR_1}}`
- `{{CONTRIBUTING_FACTOR_2}}`
- `{{CONTRIBUTING_FACTOR_N}}`

## Key Actions

- **Detection method:** `{{DETECTION_METHOD}}`
- **Initial containment:** `{{CONTAINMENT_ACTIONS}}`
- **Mitigation:** `{{MITIGATION_ACTIONS}}`
- **Recovery status:** `{{RECOVERY_STATUS}}`

## Resolution

Describe what was done to resolve the incident and restore normal service. Include any temporary mitigations that remain in place and when they will be replaced with permanent fixes.

`{{RESOLUTION_DESCRIPTION}}`

## Detection and Response Metrics

These metrics feed MTTR tracking and SLO reporting. Report in minutes unless otherwise noted.

- **Time to Detect (TTD):** `{{TTD}}` — from incident start to first alert or human detection
- **Time to Respond (TTR):** `{{TTR}}` — from detection to first responder engaged
- **Time to Resolve:** `{{TIME_TO_RESOLVE}}` — from declaration to resolution
- **MTTR contribution:** document this incident's contribution to the rolling MTTR metric at `{{MTTR_DASHBOARD_LINK}}`

## Action Items

Track all follow-up work here. Each action item must have an owner and due date before the incident is closed. High-priority items must be linked to a tracking issue.

| Action | Owner | Due Date | Priority | Tracking Link |
|--------|-------|----------|----------|---------------|
| `{{ACTION_1}}` | `{{OWNER_1}}` | `{{DUE_1}}` | `{{PRIORITY_1}}` | `{{TRACKING_1}}` |
| `{{ACTION_2}}` | `{{OWNER_2}}` | `{{DUE_2}}` | `{{PRIORITY_2}}` | `{{TRACKING_2}}` |
| `{{ACTION_N}}` | `{{OWNER_N}}` | `{{DUE_N}}` | `{{PRIORITY_N}}` | `{{TRACKING_N}}` |

## Next Steps

1. Follow-up action: `{{FOLLOW_UP_ACTION}}` (owner: `{{FOLLOW_UP_OWNER}}`)
2. Postmortem: `{{POSTMORTEM_LINK}}`
3. Lessons review: `{{LESSON_REVIEW_OWNER}}`

## Source Attribution

- Source manifests: `operations__google_sre.md`, `operations__nist_cisa.md`
- Primary source basis: Google SRE Incident Management Guide, NIST SP 800-61r3
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
