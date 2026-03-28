---
title: Incident Timeline Template
artifact_type: template
status: draft
visibility: public
classification: public
owner: "{{OWNER_NAME}}"
review_cadence: quarterly
applies_to: timeline
source_basis: Google SRE Incident Management Guide
source_manifests: operations__google_sre.md
alignment_mode: guided-synthesis
updated: 2026-03-27
---

## Timeline Metadata

| Field | Value |
|---|---|
| Incident ID | `{{INCIDENT_ID}}` |
| Incident Name | `{{INCIDENT_NAME}}` |
| Severity | `{{SEVERITY}}` |
| Timeline Author | `{{TIMELINE_AUTHOR}}` |
| Last Updated | `{{LAST_UPDATED_UTC}}` (UTC) |

## Required Anchor Events

Every incident timeline MUST record the following anchor events when they occur:

| Anchor | Time (UTC) | Actor | Evidence |
|---|---|---|---|
| First signal (alert fired / user report) | `{{T_FIRST_SIGNAL}}` | `{{FIRST_SIGNAL_SOURCE}}` | `{{FIRST_SIGNAL_LINK}}` |
| On-call notified | `{{T_NOTIFICATION}}` | `{{NOTIFIER}}` | `{{NOTIFICATION_EVIDENCE}}` |
| Incident declared | `{{T_DECLARED}}` | `{{DECLARER}}` | `{{DECLARATION_LINK}}` |
| IC assigned | `{{T_IC_ASSIGNED}}` | `{{IC_NAME}}` | |
| Impact scoped | `{{T_IMPACT_SCOPED}}` | `{{IC_NAME}}` | `{{SCOPE_EVIDENCE}}` |
| Mitigation applied | `{{T_MITIGATION}}` | `{{MITIGATION_OWNER}}` | `{{MITIGATION_EVIDENCE}}` |
| Service restored | `{{T_RESTORED}}` | `{{IC_NAME}}` | `{{RESTORATION_EVIDENCE}}` |
| Incident resolved | `{{T_RESOLVED}}` | `{{IC_NAME}}` | |
| Postmortem opened | `{{T_POSTMORTEM}}` | `{{IC_NAME}}` | `{{POSTMORTEM_LINK}}` |

## Full Chronological Log

All times in UTC. Minimum granularity: 5 minutes during active response.

| UTC Timestamp | Actor / Role | Event | Evidence Link | Notes |
|---|---|---|---|---|
| `{{TIMESTAMP_1}}` | `{{ACTOR_1}}` | `{{EVENT_DESCRIPTION_1}}` | `{{EVIDENCE_LINK_1}}` | `{{CONTEXT_1}}` |
| `{{TIMESTAMP_2}}` | `{{ACTOR_2}}` | `{{EVENT_DESCRIPTION_2}}` | `{{EVIDENCE_LINK_2}}` | `{{CONTEXT_2}}` |
| `{{TIMESTAMP_3}}` | `{{ACTOR_3}}` | `{{EVENT_DESCRIPTION_3}}` | `{{EVIDENCE_LINK_3}}` | `{{CONTEXT_3}}` |

## Timeline Conventions

- **Actor / Role**: use the role name (e.g., "IC", "Ops Lead") rather than personal names where possible — postmortems are blameless
- **Evidence links**: link to log query, alert URL, dashboard snapshot, or Slack message — do NOT paraphrase telemetry
- **Notes**: capture decision rationale and hypotheses, not just actions
- Actors map to roles defined in `artifacts/01_Governance_Method/operations/policies/incident_management_policy.md`

## Time-to-Resolution Metrics

| Metric | Value |
|---|---|
| Time to detect (TTD) | `{{T_FIRST_SIGNAL}}` → `{{T_DECLARED}}` = `{{TTD}}` |
| Time to acknowledge (TTA) | Alert fired → on-call acknowledged = `{{TTA}}` |
| Time to mitigate (TTM) | `{{T_DECLARED}}` → `{{T_MITIGATION}}` = `{{TTM}}` |
| Time to resolve (MTTR) | `{{T_DECLARED}}` → `{{T_RESOLVED}}` = `{{MTTR}}` |

## Source Attribution
- Source manifests: `operations__google_sre.md`
- Primary source basis: Google SRE Incident Management Guide, Incident Management: Key to Restore Operations
- Alignment mode: guided-synthesis
- Reviewed on: 2026-03-27
