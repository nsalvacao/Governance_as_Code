---
title: Rollback / Backout Plan Template
artifact_type: template
status: draft
visibility: public
classification: public
owner: "{{DELIVERY_OWNER}}"
review_cadence: quarterly
applies_to: rollback planning and recovery
source_basis: SRE Workbook rollback and recovery practices
source_manifests:
  - operations__google_sre.md
  - platform__microsoft_learn.md
alignment_mode: guided-synthesis
updated: 2026-03-27
---

## Rollback Plan - `{{CHANGE_REFERENCE}}`

Prepare this plan before the implementation window opens. The rollback procedure must be reviewed and, where possible, tested in a non-production environment. Every step must be executable without requiring the original implementer to be present.

---

### 1. Rollback Context

| Field | Value |
|---|---|
| Change reference | `{{CHANGE_REFERENCE}}` |
| Release / version | `{{VERSION}}` |
| Rollback owner | `{{ROLLBACK_OWNER}}` |
| Backup / restore responsible | `{{BACKUP_OWNER}}` |
| Environment | `{{ENVIRONMENT}}` |
| Rollback plan reviewed date | `{{REVIEW_DATE}}` |

The rollback owner has the authority and responsibility to initiate and oversee the rollback without requiring additional approval once a trigger condition is met.

---

### 2. Rollback Triggers

#### Automatic triggers
Conditions that must trigger an automated rollback (e.g. via deployment pipeline health gates):

- `{{AUTO_TRIGGER_CONDITION_1}}`
- `{{AUTO_TRIGGER_CONDITION_2}}`
- `{{AUTO_TRIGGER_CONDITION_N}}`

Automatic triggers should be configured in the deployment pipeline where possible, with observable alerting that notifies the rollback owner immediately on activation.

#### Manual triggers
Conditions that require the rollback owner to make a judgment call and initiate rollback manually:

- `{{MANUAL_TRIGGER_CONDITION_1}}`
- `{{MANUAL_TRIGGER_CONDITION_2}}`
- `{{MANUAL_TRIGGER_CONDITION_N}}`

For manual triggers, document the decision and the decision-maker in the change record.

---

### 3. Pre-Rollback Verification

Complete all items before initiating rollback to avoid compounding the incident.

| Check | Required | Status |
|---|---|---|
| Backup confirmed at `{{BACKUP_LOCATION}}` | yes | [pending / confirmed] |
| Rollback procedure previously tested | [yes / no] | `{{TEST_DATE}}` |
| Rollback owner notified and available | yes | [pending / confirmed] |
| Stakeholders notified of rollback intention | yes | [pending / confirmed] |
| Data migration reversibility confirmed | `{{DATA_MIGRATION_REVERSIBLE}}` | [pending / confirmed / N-A] |

If the rollback procedure has not been tested, flag this as a risk in the change record and assign a post-incident action to remedy the gap.

---

### 4. Rollback Procedure

Execute steps in order. Do not skip steps. Record the actual outcome of each step.

| Step | Command / Action | Expected output | Verification | Status |
|---|---|---|---|---|
| `{{ROLLBACK_STEP_1}}` | `{{ACTION_1}}` | `{{EXPECTED_OUTPUT_1}}` | `{{VERIFICATION_1}}` | [pending / done / failed] |
| `{{ROLLBACK_STEP_2}}` | `{{ACTION_2}}` | `{{EXPECTED_OUTPUT_2}}` | `{{VERIFICATION_2}}` | [pending / done / failed] |
| `{{ROLLBACK_STEP_N}}` | `{{ACTION_N}}` | `{{EXPECTED_OUTPUT_N}}` | `{{VERIFICATION_N}}` | [pending / done / failed] |

If any step fails, stop and escalate to `{{ESCALATION_CONTACT}}` before proceeding. Do not attempt to continue the rollback sequence after an unexpected failure without guidance.

---

### 5. Post-Rollback Verification

Confirm that the system has returned to a known-good state before declaring the rollback complete.

**System health checks:**

| Health check | Expected state | Actual state | Verified by |
|---|---|---|---|
| `{{HEALTH_CHECK_1}}` | `{{HEALTH_STATE_1}}` | `{{ACTUAL_STATE_1}}` | `{{VERIFIER_1}}` |
| `{{HEALTH_CHECK_2}}` | `{{HEALTH_STATE_2}}` | `{{ACTUAL_STATE_2}}` | `{{VERIFIER_2}}` |
| `{{HEALTH_CHECK_N}}` | `{{HEALTH_STATE_N}}` | `{{ACTUAL_STATE_N}}` | `{{VERIFIER_N}}` |

**Data integrity checks:**

| Integrity check | Expected result | Actual result | Verified by |
|---|---|---|---|
| `{{INTEGRITY_CHECK_1}}` | `{{INTEGRITY_EXPECTED_1}}` | `{{INTEGRITY_ACTUAL_1}}` | `{{INTEGRITY_VERIFIER_1}}` |
| `{{INTEGRITY_CHECK_2}}` | `{{INTEGRITY_EXPECTED_2}}` | `{{INTEGRITY_ACTUAL_2}}` | `{{INTEGRITY_VERIFIER_2}}` |

Health checks and data integrity checks must be run and verified by someone other than the person who executed the rollback steps where possible.

---

### 6. Stakeholder Notification

Notify all listed stakeholders at both trigger points — when the rollback is initiated and when it is completed.

| Stakeholder / group | Channel | Notify at | Responsible |
|---|---|---|---|
| `{{STAKEHOLDER_1}}` | `{{CHANNEL_1}}` | Rollback initiated | `{{NOTIFY_OWNER_1}}` |
| `{{STAKEHOLDER_2}}` | `{{CHANNEL_2}}` | Rollback completed | `{{NOTIFY_OWNER_2}}` |
| `{{STAKEHOLDER_3}}` | `{{CHANNEL_3}}` | `{{NOTIFY_TIMING_3}}` | `{{NOTIFY_OWNER_3}}` |

Use the change communication template for message content. Notifications must include: what happened, current system state, and next steps.

---

### 7. Rollback Completion Criteria

**Completion criteria:**
`{{COMPLETION_CRITERIA}}`

The rollback is not complete until all completion criteria are verified and recorded. Update the change record status to reflect the rollback outcome.

**Rollback completed by:** `{{ROLLBACK_COMPLETED_BY}}`
**Rollback completed at:** `{{ROLLBACK_COMPLETED_AT}}`

---

### 8. Post-Rollback Review

A post-rollback review must be initiated within `{{PIR_TRIGGER_WINDOW}}` of rollback completion. The review uses the Post-Implementation Review template and must address:

- Root cause of the rollback trigger
- Effectiveness of the rollback procedure
- Changes required to prevent recurrence
- Whether the rollback plan requires updating

**PIR owner:** `{{PIR_OWNER}}`
**PIR scheduled date:** `{{PIR_SCHEDULED_DATE}}`
**PIR reference:** `{{PIR_REFERENCE}}`

---

## Source Attribution

- Source manifests: `operations__google_sre.md`, `platform__microsoft_learn.md`
- Primary source basis: SRE Workbook rollback and recovery practices
- Alignment mode: guided-synthesis
- Reviewed on: 2026-03-27
