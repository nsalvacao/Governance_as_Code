---
title: Problem Management Policy
artifact_type: policy
status: public-draft
visibility: public
classification: public
owner: GOVERNANCE
review_cadence: quarterly
applies_to: recurring problem analysis and prevention of incident recurrence
source_basis: ITIL, NIST, Google SRE
source_manifests:
  - service_mgmt__itil.md
  - operations__nist_cisa.md
  - operations__google_sre.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

# Problem Management Policy

This policy defines how recurring problems are identified, prioritized, diagnosed, and tracked to closure following ITIL 4 Problem Management practice.

## Problem Management Lifecycle

ITIL 4 distinguishes three types of problem management activity:

| Type | Trigger | Goal |
|---|---|---|
| **Reactive** | Incident recurrence or major incident trigger | Identify root cause, prevent recurrence |
| **Proactive** | Trend analysis, capacity review, change risk | Identify problems before incidents occur |
| **Error control** | Known error exists without permanent fix | Manage workarounds, monitor for fix opportunity |

## Problem Record Lifecycle

```
Identified → Under Investigation → Root Cause Known → Known Error → Resolved → Closed
```

| Status | Description | Owner |
|---|---|---|
| Identified | Problem logged; cause unknown | `{{PROBLEM_MANAGER}}` |
| Under Investigation | RCA in progress | `{{RCA_OWNER}}` |
| Root Cause Known | Cause identified; fix not yet deployed | `{{PROBLEM_OWNER}}` |
| Known Error | Workaround available; permanent fix scheduled | `{{KEDB_OWNER}}` |
| Resolved | Permanent fix deployed; monitoring for recurrence | `{{PROBLEM_OWNER}}` |
| Closed | No further recurrence in `{{MONITORING_PERIOD}}`; record archived | `{{PROBLEM_MANAGER}}` |

## Problem Identification Triggers

A problem record MUST be created when:

- The same failure mode causes `{{RECURRENCE_THRESHOLD}}` or more incidents within `{{RECURRENCE_WINDOW}}`
- A major incident (SEV1/SEV2) occurs — reactive problem record mandatory within `{{MAJOR_INCIDENT_PROBLEM_SLA}}`
- Proactive analysis identifies a pattern in trend data or capacity metrics
- A change or release introduces a defect that is not immediately fixable

## Required Fields per Problem Record

| Field | Description |
|---|---|
| Problem ID | `{{PROBLEM_ID}}` — unique, immutable |
| Title | `{{PROBLEM_TITLE}}` — concise, symptom-focused |
| Affected Service(s) | `{{AFFECTED_SERVICES}}` |
| Impact | `{{PROBLEM_IMPACT}}` (users affected, error budget impact) |
| Recurrence Pattern | `{{RECURRENCE_PATTERN}}` (frequency, conditions) |
| Suspected / Confirmed Cause | `{{ROOT_CAUSE}}` — separate symptoms from causes |
| Workaround | `{{WORKAROUND}}` — or "none available" |
| Permanent Fix | `{{PERMANENT_FIX}}` — or "under investigation" with `{{FIX_TARGET_DATE}}` |
| Linked Incidents | `{{LINKED_INCIDENT_IDS}}` |
| Known Error Record | `{{KEDB_RECORD_LINK}}` (if applicable) |
| Owner | `{{PROBLEM_OWNER}}` |
| Review Date | `{{REVIEW_DATE}}` |

## RCA Methods

Use one or more of the following methods:

- **5 Whys**: drill down iteratively — ask "why?" at least 5 times
- **Fishbone (Ishikawa)**: categorise causes by: People, Process, Technology, Environment, Measurement
- **Fault Tree Analysis**: for complex, multi-cause failures
- **Timeline reconstruction**: correlate incident timeline with change and event logs

## Escalation Rules

| Condition | Escalation | SLA |
|---|---|---|
| Problem open > `{{PROBLEM_OPEN_SLA}}` with no root cause | Escalate to `{{TECH_ESCALATION_CONTACT}}` | Within `{{ESCALATION_SLA}}` |
| Known error without permanent fix > `{{KNOWN_ERROR_MAX_DURATION}}` | Review with `{{SERVICE_OWNER}}` | Monthly |
| Problem causes SLA breach | Notify `{{SLM_OWNER}}` | Immediate |

## Automation Guidance

- Problem IDs follow the pattern `PROB-{{YEAR}}-{{SEQUENCE}}` for consistent agent grouping.
- Recurrence status and fix deployment date are machine-readable fields.
- Link problem records to postmortems in `{{POSTMORTEM_REPOSITORY}}` via `{{LINK_FIELD}}`.

## Source Attribution

- Source manifests: `service_mgmt__itil.md`, `operations__nist_cisa.md`, `operations__google_sre.md`
- Primary source basis: ITIL problem management guidance plus NIST and Google SRE operational learning practices
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
