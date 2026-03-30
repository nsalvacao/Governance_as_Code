---
title: Stakeholder Register
artifact_type: template
status: public
visibility: public
classification: public
owner: GOVERNANCE
review_cadence: quarterly
applies_to: stakeholder identification and engagement planning
source_basis: PMI
source_manifests:
  - project__pmi.md
alignment_mode: hybrid-synthesis
updated: 2026-03-30
---

# Stakeholder Register

## Purpose

Track the people or groups that influence, sponsor, use, or review the project, enabling systematic engagement planning (PMI PMBOK 7th Edition Stakeholder Register).

## Register Metadata

| Field | Value |
|---|---|
| Project | `{{PROJECT_NAME}}` |
| Register Owner | `{{REGISTER_OWNER}}` |
| Last Updated | `{{LAST_UPDATED}}` |
| Next Review | `{{NEXT_REVIEW_DATE}}` |

## Stakeholder Register

| ID | Stakeholder | Organisation | Role | Interest in Project | Influence Level | Power Level | Engagement Level (Current) | Engagement Level (Desired) | Communication Needs | Owner |
|---|---|---|---|---|---|---|---|---|---|---|
| `{{SH_ID_1}}` | `{{SH_NAME_1}}` | `{{SH_ORG_1}}` | `{{SH_ROLE_1}}` | `{{SH_INTEREST_1}}` | `{{SH_INFLUENCE_1}}` | `{{SH_POWER_1}}` | `{{SH_ENG_CURRENT_1}}` | `{{SH_ENG_DESIRED_1}}` | `{{SH_COMMS_1}}` | `{{SH_OWNER_1}}` |
| `{{SH_ID_2}}` | `{{SH_NAME_2}}` | `{{SH_ORG_2}}` | `{{SH_ROLE_2}}` | `{{SH_INTEREST_2}}` | `{{SH_INFLUENCE_2}}` | `{{SH_POWER_2}}` | `{{SH_ENG_CURRENT_2}}` | `{{SH_ENG_DESIRED_2}}` | `{{SH_COMMS_2}}` | `{{SH_OWNER_2}}` |

## Influence and Power Scales

| Level | Influence Description | Power Description |
|---|---|---|
| High | Can significantly shape project direction or decisions | Can approve or veto major decisions |
| Medium | Can affect specific aspects of scope or approach | Can influence decisions through formal channels |
| Low | Has limited ability to affect the project | Advisory role; no formal decision authority |

## Engagement Level Categories (PMI)

| Level | Description |
|---|---|
| Unaware | Unaware of the project and its impacts |
| Resistant | Aware but opposed to the project |
| Neutral | Aware but neither supportive nor resistant |
| Supportive | Aware and supportive of the project |
| Leading | Actively engaged in ensuring project success |

## Power / Interest Grid

Quadrant mapping for prioritisation:

| | Low Interest | High Interest |
|---|---|---|
| **High Power** | Keep satisfied: `{{KEEP_SATISFIED_STAKEHOLDERS}}` | Manage closely: `{{MANAGE_CLOSELY_STAKEHOLDERS}}` |
| **Low Power** | Monitor: `{{MONITOR_STAKEHOLDERS}}` | Keep informed: `{{KEEP_INFORMED_STAKEHOLDERS}}` |

## Cross-References

| Document | Link |
|---|---|
| Communications Management Plan | `{{COMMS_PLAN_LINK}}` |
| Project Charter | `{{CHARTER_LINK}}` |

## Source Attribution

- Source manifests: `project__pmi.md`
- Primary source basis: PMI stakeholder management guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-30
