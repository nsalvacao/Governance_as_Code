---
title: Communications Management Plan
artifact_type: template
status: public
visibility: public
classification: public
owner: GOVERNANCE
review_cadence: quarterly
applies_to: planned project communications
source_basis: PMI
source_manifests:
  - project__pmi.md
alignment_mode: hybrid-synthesis
updated: 2026-03-30
---

# Communications Management Plan

## Purpose

Define who needs information, what they need, when they need it, and how it is delivered (PMI PMBOK 7th Edition Chapter 10 Communications Management).

## Plan Metadata

| Field | Value |
|---|---|
| Project | `{{PROJECT_NAME}}` |
| Plan Owner | `{{COMMS_PLAN_OWNER}}` |
| Version | `{{COMMS_PLAN_VERSION}}` |
| Last Updated | `{{LAST_UPDATED}}` |

## Communications Matrix

| ID | Audience | Purpose | Message / Content | Cadence | Channel | Format | Owner | Escalation Route | Notes |
|---|---|---|---|---|---|---|---|---|---|
| C01 | `{{AUDIENCE_1}}` | Status update | Progress vs. plan, risks, blockers | `{{CADENCE_1}}` | `{{CHANNEL_1}}` | `{{FORMAT_1}}` | `{{OWNER_1}}` | `{{ESCALATION_1}}` | `{{NOTES_1}}` |
| C02 | `{{AUDIENCE_2}}` | Risk / issue escalation | Tolerance breach, decisions required | As needed | `{{ESCALATION_CHANNEL}}` | Exception Report | `{{PM}}` | `{{SPONSOR}}` | Triggered by tolerance breach |
| C03 | `{{AUDIENCE_3}}` | Milestone communication | Achievement, next phase | At each milestone | `{{MILESTONE_CHANNEL}}` | Email + meeting | `{{PM}}` | `{{SPONSOR}}` | |
| C04 | `{{AUDIENCE_4}}` | Change communication | Approved changes, impact | Within `{{CHANGE_COMMS_SLA}}` of approval | `{{CHANGE_CHANNEL}}` | `{{CHANGE_FORMAT}}` | `{{CHANGE_COMMS_OWNER}}` | | |

## Communication Channels

| Channel | Purpose | Access | Owner |
|---|---|---|---|
| `{{CHANNEL_TOOL_1}}` (e.g., Slack `#{{CHANNEL_NAME}}`) | Day-to-day team communication | `{{ACCESS_1}}` | `{{CHANNEL_OWNER_1}}` |
| `{{EMAIL_LIST}}` | Formal stakeholder updates | `{{ACCESS_2}}` | `{{CHANNEL_OWNER_2}}` |
| `{{MEETING_CADENCE}}` (e.g., weekly stand-up) | Synchronous coordination | `{{MEETING_ACCESS}}` | `{{MEETING_FACILITATOR}}` |
| `{{DOCUMENT_REPOSITORY}}` | Document sharing and archiving | `{{DOC_REPO_ACCESS}}` | `{{DOC_REPO_OWNER}}` |

## Escalation Communication

Escalation is triggered when:
- Forecast tolerance breach in time, cost, or scope
- SEV1/SEV2 incident impacting the project
- Sponsor decision required within `{{DECISION_SLA}}`

Escalation path: `{{PM}}` → `{{SENIOR_MANAGER}}` → `{{SPONSOR}}` → `{{GOVERNING_BOARD}}`

Response SLA: `{{ESCALATION_RESPONSE_SLA}}`

## Glossary and Constraints

| Constraint | Value |
|---|---|
| Language | `{{COMMUNICATION_LANGUAGE}}` |
| Confidentiality level | `{{CONFIDENTIALITY_LEVEL}}` |
| Distribution restrictions | `{{DISTRIBUTION_RESTRICTIONS}}` |
| Record retention | `{{COMMS_RETENTION_PERIOD}}` |

## Cross-References

| Document | Link |
|---|---|
| Stakeholder Register | `{{STAKEHOLDER_REGISTER_LINK}}` |
| Project Charter | `{{CHARTER_LINK}}` |
| Exception / Escalation Report template | `{{ESCALATION_REPORT_LINK}}` |

## Source Attribution

- Source manifests: `project__pmi.md`
- Primary source basis: PMI communications planning guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-30
