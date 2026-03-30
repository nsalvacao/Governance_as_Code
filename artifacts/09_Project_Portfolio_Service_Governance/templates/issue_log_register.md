---
title: Issue Log / Issue Register
artifact_type: template
status: public
visibility: public
classification: public
owner: GOVERNANCE
review_cadence: quarterly
applies_to: project issues requiring tracking and resolution
source_basis: PMI, PRINCE2
source_manifests:
  - project__pmi.md
  - project__prince2.md
alignment_mode: hybrid-synthesis
updated: 2026-03-30
---

# Issue Log / Issue Register

## Purpose

Track issues requiring action, decision, or escalation, maintaining a single record per issue through its lifecycle (PMI PMBOK 7th Edition Issue Log + PRINCE2 2023 Issue Register).

## Register Metadata

| Field | Value |
|---|---|
| Project | `{{PROJECT_NAME}}` |
| Register Owner | `{{REGISTER_OWNER}}` |
| Last Updated | `{{LAST_UPDATED}}` |
| Next Review | `{{NEXT_REVIEW_DATE}}` |

## Issue Register

| Issue ID | Date Raised | Category | Description | Impact | Priority | Owner | Status | Resolution / Decision | Resolution Date | Related Items |
|---|---|---|---|---|---|---|---|---|---|---|
| `{{ISSUE_ID_1}}` | `{{DATE_RAISED_1}}` | `{{CATEGORY_1}}` | `{{DESCRIPTION_1}}` | `{{IMPACT_1}}` | `{{PRIORITY_1}}` | `{{OWNER_1}}` | `{{STATUS_1}}` | `{{RESOLUTION_1}}` | `{{RESOLUTION_DATE_1}}` | `{{RELATED_1}}` |
| `{{ISSUE_ID_2}}` | `{{DATE_RAISED_2}}` | `{{CATEGORY_2}}` | `{{DESCRIPTION_2}}` | `{{IMPACT_2}}` | `{{PRIORITY_2}}` | `{{OWNER_2}}` | `{{STATUS_2}}` | `{{RESOLUTION_2}}` | `{{RESOLUTION_DATE_2}}` | `{{RELATED_2}}` |

## Issue Categories

| Code | Category | Escalation Path |
|---|---|---|
| SCOPE | Scope change or creep | Change Control Board |
| TIME | Schedule impact | Project Manager → Sponsor if tolerance breached |
| COST | Budget impact | Project Manager → Sponsor if tolerance breached |
| QUAL | Quality non-compliance | `{{QUALITY_AUTHORITY}}` |
| RISK | Risk materialised as issue | Risk Manager |
| TECH | Technical blocker | `{{TECH_AUTHORITY}}` |
| TEAM | Resource or team issue | `{{RESOURCE_AUTHORITY}}` |
| STKHLD | Stakeholder conflict | Project Manager |
| EXT | External dependency | `{{EXTERNAL_LIAISON}}` |

## Priority Levels

| Priority | Description | Response SLA | Escalation |
|---|---|---|---|
| P1 — Critical | Threatens project objectives or delivery | `{{P1_SLA}}` | Immediate escalation to `{{SPONSOR}}` |
| P2 — High | Significant impact; tolerance at risk | `{{P2_SLA}}` | Escalate to `{{SENIOR_MANAGER}}` |
| P3 — Medium | Manageable; within tolerances | `{{P3_SLA}}` | PM discretion |
| P4 — Low | Minor; no tolerance impact | `{{P4_SLA}}` | Log and monitor |

## Status Definitions

| Status | Description |
|---|---|
| Open | Logged; awaiting assignment or action |
| In Progress | Owner actively working on resolution |
| Escalated | Referred to higher authority for decision |
| Resolved | Issue closed; outcome recorded |
| Deferred | Agreed to defer resolution to later stage / project |
| Closed | No further action required |

## Distinction from Risks and Changes

- **Issue**: A problem that HAS materialised and requires action now.
- **Risk**: A potential problem that has NOT yet occurred — track in the Risk Register.
- **Change Request**: A proposed scope, time, or cost change — track in the Change Log.

## Source Attribution

- Source manifests: `project__pmi.md`, `project__prince2.md`
- Primary source basis: PMI and PRINCE2 issue management guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-30
