---
title: Postmortem Template
artifact_type: template
status: public-draft
visibility: public
classification: public
owner: knowledge-platform
review_cadence: quarterly
applies_to: service-impacting incidents and significant failures
source_basis: Google SRE Book Chapter 15 blameless postmortem culture
source_manifests:
  - operations__google_sre.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Purpose

Capture a blameless operational review that explains what happened, what it affected, and what we will change. Focus on systems and processes — not individuals — to build a learning culture that improves reliability over time.

---

## Incident Summary

**Title:** {{INCIDENT_TITLE}}
**Date:** {{INCIDENT_DATE}}
**Duration:** {{DURATION}}
**Severity:** {{SEVERITY}}
**Affected services:** {{AFFECTED_SERVICES}}
**Author:** {{AUTHOR}}

Provide a 2–3 sentence executive summary of the incident. State what failed, when it was detected, and how it was resolved. This section is read by stakeholders who may not read further.

---

## Impact Summary

| Dimension | Value |
|---|---|
| Users affected | {{USER_IMPACT}} |
| Error rate at peak | {{ERROR_RATE}} |
| Revenue impact | {{REVENUE_IMPACT}} |
| SLO error budget consumed | {{BUDGET_CONSUMED}} |

Quantify impact wherever possible. If revenue impact is not applicable or unknown, mark as N/A with a brief explanation. SLO budget consumed links this incident to the service's error budget policy.

---

## Timeline

Chronological log of events from first signals to full resolution. Add rows as needed. Use UTC timestamps consistently.

| Timestamp (UTC) | Event | Who |
|---|---|---|
| {{TIMESTAMP_UTC}} | {{EVENT_DESCRIPTION}} | {{WHO}} |
| {{TIMESTAMP_UTC}} | {{EVENT_DESCRIPTION}} | {{WHO}} |
| {{TIMESTAMP_UTC}} | {{EVENT_DESCRIPTION}} | {{WHO}} |

Include: first alert or signal, escalation points, mitigations attempted, resolution, and all-clear declaration. Distinguish automated events from human actions.

---

## Root Cause

### Immediate cause

Describe the proximate technical trigger — the specific change, failure, or condition that directly caused the incident.

### Contributing factors

List conditions that amplified or allowed the immediate cause to produce impact. Each factor should be independently addressable.

- {{CONTRIBUTING_FACTOR_1}}
- {{CONTRIBUTING_FACTOR_2}}
- {{CONTRIBUTING_FACTOR_N}}

---

## Detection

**How detected:** {{DETECTION_METHOD}}
**Time to detect (TTD):** {{TTD}}

Describe how the incident was first identified — automated alert, customer report, or internal observation. Note any gaps between when the failure began and when it was detected, as these indicate monitoring blind spots.

---

## Response

**Time to respond (TTR):** {{TTR}}

Actions taken after detection, in order:

1. {{RESPONSE_ACTION_1}}
2. {{RESPONSE_ACTION_2}}
3. {{RESPONSE_ACTION_N}}

Describe the response process honestly, including actions that did not work. This information is critical for improving runbooks and on-call procedures.

---

## Resolution

**What fixed it:** {{FIX}}
**Time to resolve (TTRES):** {{TTRES}}

Describe the specific action that resolved the incident and restored normal service. Distinguish the mitigation (stopped the bleeding) from the fix (addressed the cause) if they were different steps.

---

## Action Items

Each action item must have a clear owner, priority, and due date. Action items without owners are not action items.

| Action | Owner | Priority | Due date |
|---|---|---|---|
| {{ACTION_1}} | {{OWNER}} | P1/P2/P3 | {{DUE_DATE}} |
| {{ACTION_2}} | {{OWNER}} | P1/P2/P3 | {{DUE_DATE}} |
| {{ACTION_N}} | {{OWNER}} | P1/P2/P3 | {{DUE_DATE}} |

P1 = critical, complete within 7 days; P2 = high, complete within 30 days; P3 = standard, complete within 90 days.

---

## Lessons Learned

### What went well

- {{WELL_1}}
- {{WELL_2}}
- {{WELL_N}}

### What to improve

- {{IMPROVE_1}}
- {{IMPROVE_2}}
- {{IMPROVE_N}}

Capture both strengths and gaps without assigning personal blame. The goal is to identify which systems, tools, processes, or team norms to reinforce or redesign. Blameless does not mean consequence-free — it means identifying systemic causes rather than attributing failure to individual error.

---

## Source Attribution

- Source manifests: operations__google_sre.md
- Primary source basis: Google SRE Book Chapter 15 blameless postmortem culture
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
