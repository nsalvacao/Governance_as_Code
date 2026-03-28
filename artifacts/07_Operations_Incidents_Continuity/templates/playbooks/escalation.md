---
title: Escalation Playbook
artifact_type: template
status: public-draft
visibility: public
classification: public
owner: "{{OWNER_NAME}}"
review_cadence: quarterly
applies_to: escalation playbook
source_basis: NIST SP 800-61r3, Google SRE Incident Management Guide
source_manifests: operations__nist_cisa.md, operations__google_sre.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Purpose

Define when and how to escalate an incident to the next tier. Use this playbook when the current responder cannot resolve the incident within the defined threshold, when severity is upgraded, or when the Incident Commander is unavailable.

---

## Trigger

Activate this playbook when any of the following conditions is met:

- Incident unresolved after `{{TIME_THRESHOLD}}`
- Severity upgraded to SEV ≤ `{{ESCALATION_SEVERITY_THRESHOLD}}`
- Incident Commander unavailable or unreachable
- Trigger condition: `{{ESCALATION_TRIGGER}}`

Do not wait until the time threshold has fully elapsed before preparing the escalation. Begin preparing the escalation script and gathering state summary at the midpoint of the threshold window.

---

## Escalation Tiers

| Tier | Role | Contact | Availability | How to reach |
|------|------|---------|-------------|-------------|
| 1 | `{{ROLE_T1}}` | `{{CONTACT_T1}}` | `{{AVAILABILITY_T1}}` | `{{REACH_METHOD_T1}}` |
| 2 | `{{ROLE_T2}}` | `{{CONTACT_T2}}` | `{{AVAILABILITY_T2}}` | `{{REACH_METHOD_T2}}` |
| 3 | `{{ROLE_T3}}` | `{{CONTACT_T3}}` | `{{AVAILABILITY_T3}}` | `{{REACH_METHOD_T3}}` |

Escalate in tier order. Do not skip tiers except in cases of catastrophic impact (data loss, security breach, regulatory exposure).

---

## Pre-Escalation Checklist

Complete all items before escalating. Incomplete escalations waste the time of the next tier.

- [ ] Incident Commander is designated: `{{IC_NAME}}`
- [ ] Impact has been assessed and severity is set: `{{CURRENT_SEVERITY}}`
- [ ] Initial diagnosis steps have been attempted
- [ ] Relevant runbook has been executed to the point of failure
- [ ] Current state summary is prepared (see Escalation Script below)

---

## Escalation Script

Use this structure when contacting the escalation target. Adapt to voice, chat, or page as appropriate.

> "This is `{{IC_NAME}}` escalating incident `{{INCIDENT_ID}}`. Here is the current state: `{{STATE_SUMMARY}}`. We have tried: `{{ATTEMPTED_ACTIONS}}`. We need help with: `{{HELP_NEEDED}}`. The incident channel is `{{ESCALATION_CHANNEL}}`."

Keep the script concise. The escalation target will ask follow-up questions. Do not front-load all details — lead with what is needed.

---

## Handoff Protocol

When transferring IC responsibility to the incoming responder:

| Item | Outgoing IC provides |
|------|---------------------|
| State summary | `{{STATE_SUMMARY}}` |
| Open actions | `{{OPEN_ACTIONS}}` |
| Decisions made | `{{DECISIONS_MADE}}` |
| Active communication channels | `{{ACTIVE_CHANNELS}}` |
| Next planned action | `{{NEXT_ACTION}}` |

The incoming IC must verbally confirm they have received and understood the handoff before the outgoing IC leaves the incident. Document the handoff time and both names in the incident record.

---

## Escalation Log

| Time | From | To | Reason | Outcome |
|------|------|----|--------|---------|
| `{{ESCALATION_TIME_1}}` | `{{FROM_1}}` | `{{TO_1}}` | `{{REASON_1}}` | `{{OUTCOME_1}}` |

Maintain a log entry for every escalation action. This log is required input for the post-incident review.

---

## Source Attribution

- Source manifests: `operations__nist_cisa.md`, `operations__google_sre.md`
- Primary source basis: NIST SP 800-61r3, Google SRE Incident Management Guide
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
