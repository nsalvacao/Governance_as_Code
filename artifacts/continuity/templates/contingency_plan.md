---
title: Contingency Plan Template
artifact_type: template
status: draft
visibility: public
classification: public
owner: "{{OWNER_NAME}}"
review_cadence: semiannually
applies_to: contingency execution
source_basis: NIST SP 800-34 Rev. 1
source_manifests: operations__nist_cisa.md
alignment_mode: guided-synthesis
updated: 2026-03-27
---

## Plan Overview

Identify the system and plan version. This section is the authoritative reference block for the plan and must be updated on every revision.

- **System name:** `{{SYSTEM_NAME}}`
- **System classification:** `{{SYSTEM_CLASSIFICATION}}`
- **Plan type:** `{{PLAN_TYPE}}` (BCP / ISCP / COOP / DRP / CIRP)
- **Plan version:** `{{PLAN_VERSION}}`
- **Plan date:** `{{PLAN_DATE}}`
- **Activation authority:** `{{ACTIVATION_AUTHORITY}}`
- **BIA reference:** `{{BIA_LINK}}`
- **Plan owner:** `{{OWNER_NAME}}`

## Supporting Information

Provide the context needed to understand and execute the plan. This section must be read by all recovery team members before any activation.

### Purpose and Scope

This plan describes the procedures for recovering `{{SYSTEM_NAME}}` following a disruption. The scope covers `{{SCOPE_STATEMENT}}`. Out-of-scope items are listed in `{{OUT_OF_SCOPE_REF}}`.

### Applicable Laws and Regulations

List all legal, regulatory, and contractual obligations that govern recovery timelines and data handling: `{{REGULATORY_REQUIREMENTS}}`.

### Assumptions

The plan is built on the following assumptions; if any assumption is invalid at activation time, the activation authority must assess the impact before proceeding:

- `{{ASSUMPTION_1}}`
- `{{ASSUMPTION_2}}`
- `{{ASSUMPTION_N}}`

## Notification and Activation Phase

This phase begins when a potential disruption is detected and ends with a formal activation decision. Follow the steps in order; do not skip the damage assessment step.

### Detection Criteria

The plan may be activated when one or more of the following conditions are met: `{{DETECTION_CRITERIA}}`. Detection may originate from automated monitoring, user reports, or third-party notification.

### Notification Contacts

Notify all contacts in the table below using the listed channels. Primary contact must be reached before notifying secondary contacts.

| Contact Name | Role | Phone | Email | Notification Order |
|---|---|---|---|---|
| `{{CONTACT_NAME}}` | `{{ROLE}}` | `{{PHONE}}` | `{{EMAIL}}` | `{{NOTIFICATION_ORDER}}` |

### Damage Assessment Procedure

Before activating the plan, the activation authority must assess the scope and severity of the disruption. Complete the damage assessment checklist at `{{DAMAGE_ASSESSMENT_CHECKLIST}}` and document findings in `{{DAMAGE_ASSESSMENT_RECORD}}`. The activation decision must be made within `{{ACTIVATION_DECISION_WINDOW}}` of initial detection.

## Recovery Phase

This phase begins with formal plan activation and ends when the system meets the minimum service threshold defined in the BIA. All recovery actions must be logged with timestamps.

### Recovery Objectives

Recovery must meet or exceed the following objectives derived from the BIA:

- **Recovery Time Objective (RTO):** `{{RTO}}`
- **Recovery Point Objective (RPO):** `{{RPO}}`
- **Maximum Tolerable Downtime (MTD):** `{{MTD}}`

### Recovery Team Roles

| Recovery Team Role | Assigned Personnel | Responsibilities | Backup Personnel |
|---|---|---|---|
| `{{RECOVERY_TEAM_ROLE}}` | `{{ASSIGNED_PERSONNEL}}` | `{{RESPONSIBILITIES}}` | `{{BACKUP_PERSONNEL}}` |

### Alternative Processing Site

If primary facilities are unavailable, recovery operations will be conducted at the alternate processing site `{{ALT_SITE}}`. Access procedures, infrastructure availability, and data synchronization state at the alternate site are documented in `{{ALT_SITE_PROCEDURES}}`.

### Recovery Procedures by Priority Tier

Execute recovery procedures in priority order as defined in the BIA. Do not proceed to a lower-priority tier until minimum acceptable service is restored for all higher-priority functions.

**Priority 1 — Mission-critical functions:**
`{{PRIORITY_1_RECOVERY_STEPS}}`

**Priority 2 — Essential functions:**
`{{PRIORITY_2_RECOVERY_STEPS}}`

**Priority 3 — Supporting functions:**
`{{PRIORITY_3_RECOVERY_STEPS}}`

## Reconstitution Phase

This phase begins when minimum acceptable service is restored and ends when the system is fully operational and all alternate arrangements are deactivated.

### Validation Criteria

The system is considered fully restored when all of the following validation criteria are met: `{{VALIDATION_CRITERIA}}`. Validation must be performed by `{{VALIDATION_TEAM}}` and documented in `{{VALIDATION_RECORD}}`.

### Notification of Restoration

Upon successful validation, notify all stakeholders using the contacts table in the Notification and Activation Phase. Issue a restoration notice to `{{RESTORATION_NOTIFICATION_LIST}}` within `{{RESTORATION_NOTIFICATION_WINDOW}}` of validation completion.

### Lessons Captured

After every activation, the recovery team must complete a lessons-learned review within `{{LESSONS_LEARNED_WINDOW}}`. Document findings in `{{LESSONS_LEARNED_RECORD}}` and create corrective action items for any gaps identified. Significant findings must trigger a BIA review.

## Appendices

### Appendix A — Contact List

Full contact list for all personnel referenced in this plan: `{{CONTACT_LIST_REF}}`.

### Appendix B — Equipment Inventory

| Equipment Item | Location | Owner | Recovery Priority |
|---|---|---|---|
| `{{EQUIPMENT_ITEM}}` | `{{EQUIPMENT_LOCATION}}` | `{{EQUIPMENT_OWNER}}` | `{{EQUIPMENT_PRIORITY}}` |

### Appendix C — Software and Data Backup Procedures

Document all backup procedures, schedules, retention policies, and restoration steps. Backup procedures must align with the RPO defined in the BIA.

| System / Dataset | Backup Type | Frequency | Retention | Restoration Procedure |
|---|---|---|---|---|
| `{{BACKUP_SYSTEM}}` | `{{BACKUP_TYPE}}` | `{{BACKUP_FREQUENCY}}` | `{{BACKUP_RETENTION}}` | `{{BACKUP_PROCEDURE}}` |

## Source Attribution

- Source manifests: `operations__nist_cisa.md`
- Primary source basis: NIST SP 800-34 Rev. 1 full plan structure
- Alignment mode: guided-synthesis
- Reviewed on: 2026-03-27
