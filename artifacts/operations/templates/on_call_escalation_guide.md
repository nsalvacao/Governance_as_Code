---
title: On-call and Escalation Guide
artifact_type: template
status: public-draft
visibility: public
classification: public
owner: "{{OWNER_NAME}}"
review_cadence: quarterly
applies_to: on-call response and escalation routing
source_basis: Google SRE Workbook on-call chapter and NIST escalation conventions
source_manifests:
  - operations__google_sre.md
  - operations__nist_cisa.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Purpose

Provide the reusable structure for on-call responsibilities, escalation paths, and handoff expectations. Every on-call engineer must be able to follow this guide without prior context.

---

## On-Call Setup

**Rotation schedule:** `{{ROTATION_SCHEDULE}}`

**Tools required:**

| # | Tool |
|---|------|
| 1 | `{{ONCALL_TOOL_1}}` |
| 2 | `{{ONCALL_TOOL_2}}` |
| N | `{{ONCALL_TOOLS}}` |

Verify tool access and alert routing at the start of each on-call shift. An engineer who cannot access the monitoring system or runbook repository is not ready for on-call.

---

## Alert Triage

When an alert fires, apply the following triage sequence:

| Alert name | Severity assessment | Runbook |
|-----------|---------------------|---------|
| `{{ALERT_NAME_1}}` | `{{SEVERITY_ASSESSMENT_1}}` | `{{RUNBOOK_LINK_1}}` |
| `{{ALERT_NAME_2}}` | `{{SEVERITY_ASSESSMENT_2}}` | `{{RUNBOOK_LINK_2}}` |
| `{{ALERT_NAME_N}}` | `{{SEVERITY_ASSESSMENT_N}}` | `{{RUNBOOK_LINK_N}}` |

Open the linked runbook immediately on alert receipt. Do not begin ad-hoc debugging before checking whether a runbook already covers the scenario.

---

## Escalation Matrix

Escalate in tier order. Do not skip levels unless the incident is catastrophic (data loss, security breach).

| Level | Role | Contact | Availability | How to reach |
|-------|------|---------|-------------|-------------|
| L1 | `{{L1_ROLE}}` — first responder | `{{L1_CONTACT}}` | Primary on-call hours | `{{L1_REACH_METHOD}}` |
| L2 | `{{L2_ROLE}}` — after `{{L1_ESCALATION_TIME}}` unresolved | `{{L2_CONTACT}}` | `{{L2_AVAILABILITY}}` | `{{L2_REACH_METHOD}}` |
| L3 | `{{L3_ROLE}}` — management escalation | `{{L3_CONTACT}}` | `{{L3_AVAILABILITY}}` | `{{L3_REACH_METHOD}}` |

Document the time you escalated and to whom in the incident record. This creates an auditable escalation trail and prevents simultaneous escalation confusion.

---

## Sleep Protection Rules

Do not page for SEV < `{{NO_PAGE_SEVERITY}}` outside paging hours `{{PAGING_HOURS}}`.

**After-hours paging criteria:**
- Customer data is at risk
- Service is fully unavailable
- Automated recovery has failed and human action is required within `{{SLEEP_PROTECTION_THRESHOLD}}` minutes

Respect sleep protection rules. An exhausted on-call engineer makes errors. If a low-severity alert fires after hours, log it and address it at the start of business.

---

## Toil Tracking

Log all toil in `{{TOIL_LOG}}`.

**Toil entry fields:** alert name | time spent | whether it was automatable | ticket reference

Track toil systematically. Every recurring manual intervention that could be automated should be filed as a toil-reduction ticket. Review toil logs monthly to prioritize automation work.

---

## Handoff Checklist

Complete this checklist at every shift handoff. Both outgoing and incoming engineers must acknowledge.

| Item | Status |
|------|--------|
| Open incidents | `{{OPEN_INCIDENT_1}}`, `{{OPEN_INCIDENT_N}}` |
| Pending actions | `{{PENDING_ACTION_1}}`, `{{PENDING_ACTION_N}}` |
| Known issues | `{{KNOWN_ISSUE_1}}`, `{{KNOWN_ISSUE_N}}` |
| Monitoring anomalies | `{{MONITORING_ANOMALY}}` |
| Upcoming high-risk events | `{{HIGH_RISK_EVENT}}` |

A handoff without a checklist is not a handoff. Incomplete handoffs are the leading cause of incidents being dropped between shifts.

---

## Source Attribution

- Source manifests: operations__google_sre.md, operations__nist_cisa.md
- Primary source basis: Google SRE Workbook on-call chapter and NIST escalation conventions
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
