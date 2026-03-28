---
title: Postmortem Template
artifact_type: template
status: public-draft
visibility: public
classification: public
owner: reliability-platform
review_cadence: quarterly
applies_to: incidents requiring service review
source_basis: Google SRE Postmortem Culture workbook
source_manifests: operations__google_sre.md
alignment_mode: direct-adaptation
updated: 2026-03-27
---

## Incident Metadata

| Field | Value |
|---|---|
| Incident ID | `{{INCIDENT_ID}}` |
| Incident Name | `{{INCIDENT_NAME}}` |
| Severity | `{{SEVERITY}}` (SEV1 / SEV2 / SEV3 / SEV4) |
| Start Time (UTC) | `{{START_TIME_UTC}}` |
| End Time (UTC) | `{{END_TIME_UTC}}` |
| Duration | `{{DURATION}}` |
| Services Impacted | `{{SERVICE_LIST}}` |
| Incident Commander | `{{INCIDENT_COMMANDER}}` |
| Communications Lead | `{{COMMS_LEAD}}` |
| Postmortem Author | `{{POSTMORTEM_AUTHOR}}` |
| Postmortem Date | `{{POSTMORTEM_DATE}}` |

## Executive Summary

<!-- ≤ 5 sentences: what happened, customer impact, contributing factor, resolution, follow-up action -->
`{{EXECUTIVE_SUMMARY}}`

## Impact

| Metric | Value |
|---|---|
| Users affected | `{{USERS_AFFECTED}}` |
| Error budget consumed (this incident) | `{{BUDGET_CONSUMED}}`% of `{{MEASUREMENT_WINDOW}}` budget |
| Cumulative error budget this period | `{{CUMULATIVE_BUDGET_CONSUMED}}`% |
| Customer-facing errors | `{{CUSTOMER_ERROR_COUNT}}` (rate: `{{ERROR_RATE}}`) |
| Revenue impact (if known) | `{{REVENUE_IMPACT}}` |
| SLA breach | `{{SLA_BREACH}}` (Yes / No / Pending review) |

## Timeline

All times UTC. Link each entry to evidence (log query, alert, graph, or message).

| Time (UTC) | Event | Evidence |
|---|---|---|
| `{{T_FIRST_SIGNAL}}` | First signal detected: `{{FIRST_SIGNAL_DESCRIPTION}}` | `{{FIRST_SIGNAL_EVIDENCE_LINK}}` |
| `{{T_NOTIFICATION}}` | On-call `{{ON_CALL_PERSON}}` notified via `{{NOTIFICATION_CHANNEL}}` | `{{NOTIFICATION_EVIDENCE_LINK}}` |
| `{{T_IC_DECLARED}}` | Incident Commander `{{INCIDENT_COMMANDER}}` declared | `{{IC_DECLARATION_LINK}}` |
| `{{T_IMPACT_SCOPED}}` | Impact scope established: `{{IMPACT_SCOPE_SUMMARY}}` | `{{SCOPE_EVIDENCE_LINK}}` |
| `{{T_MITIGATION_APPLIED}}` | Mitigation applied: `{{MITIGATION_DESCRIPTION}}` | `{{MITIGATION_EVIDENCE_LINK}}` |
| `{{T_SERVICE_RESTORED}}` | Service fully restored | `{{RESTORATION_EVIDENCE_LINK}}` |
| `{{T_POSTMORTEM_OPENED}}` | Postmortem opened | `{{POSTMORTEM_TICKET_LINK}}` |

## Root Cause Analysis

**Immediate cause** (the proximate trigger):
`{{IMMEDIATE_CAUSE}}`

**Causal chain** (why the immediate cause was possible):
1. `{{CAUSAL_FACTOR_1}}`
2. `{{CAUSAL_FACTOR_2}}`
3. `{{CAUSAL_FACTOR_3}}`

## Contributing Factors

| Category | Factor | Evidence |
|---|---|---|
| Technical | `{{TECHNICAL_FACTOR}}` | `{{TECHNICAL_EVIDENCE_LINK}}` |
| Process | `{{PROCESS_FACTOR}}` | `{{PROCESS_EVIDENCE_LINK}}` |
| Tooling | `{{TOOLING_FACTOR}}` | `{{TOOLING_EVIDENCE_LINK}}` |
| Monitoring | `{{MONITORING_GAP}}` | `{{MONITORING_EVIDENCE_LINK}}` |

## What Went Well

<!-- Describe actions that limited blast radius or accelerated recovery -->
- `{{POSITIVE_OBSERVATION_1}}`
- `{{POSITIVE_OBSERVATION_2}}`

## Action Items

| ID | Action | Owner | Due Date | Priority | Tracker |
|---|---|---|---|---|---|
| `{{ACTION_ID_1}}` | `{{ACTION_DESCRIPTION_1}}` | `{{ACTION_OWNER_1}}` | `{{ACTION_DUE_1}}` | `{{ACTION_PRIORITY_1}}` | `{{ACTION_TRACKER_LINK_1}}` |
| `{{ACTION_ID_2}}` | `{{ACTION_DESCRIPTION_2}}` | `{{ACTION_OWNER_2}}` | `{{ACTION_DUE_2}}` | `{{ACTION_PRIORITY_2}}` | `{{ACTION_TRACKER_LINK_2}}` |

Action items are tracked in `{{ACTION_TRACKER_LOCATION}}` and reviewed at `{{REVIEW_CADENCE}}`.

## Lessons Learned

<!-- Non-obvious insights not already captured as action items -->
- `{{LESSON_1}}`
- `{{LESSON_2}}`

## Source Attribution

- Source manifests: `operations__google_sre.md`
- Primary source basis: Google SRE Postmortem Culture workbook
- Alignment mode: direct-adaptation
- Reviewed on: 2026-03-27
