---
title: Change Record Template
artifact_type: template
status: draft
visibility: public
classification: public
owner: delivery@org
review_cadence: quarterly
applies_to: change control and implementation tracking
source_basis: ITIL 4 Change Enablement practice
source_manifests:
  - operations__nist_cisa.md
  - platform__aws_well_architected.md
alignment_mode: guided-synthesis
updated: 2026-03-27
---

## Change Record - `{{CHANGE_ID}}`

Record every proposed change using this template. Complete all sections before submitting to the Change Authority for approval. ITIL 4 Change Enablement distinguishes three change types — ensure the correct type is selected as it governs the approval path.

---

### 1. Change Identification

| Field | Value |
|---|---|
| Change ID | `{{CHANGE_ID}}` |
| Change title | `{{CHANGE_TITLE}}` |
| Requester | `{{REQUESTER}}` |
| Request date | `{{REQUEST_DATE}}` |
| Affected service / system | `{{AFFECTED_SERVICE}}` |

Populate `{{CHANGE_ID}}` using your organisation's change numbering scheme (e.g. CHG-YYYY-NNNN). The requester is the person or team originating the need, not necessarily the implementer.

---

### 2. Change Type

**Selected type:** `{{CHANGE_TYPE}}`

| Type | Definition | Approval path |
|---|---|---|
| Standard | Pre-authorised, low-risk, repeatable change with an established procedure | No CAB review required; follows pre-approved template |
| Normal | Scheduled change that must follow the full assessment and authorisation process | CAB review required |
| Emergency | Urgent change to restore service or prevent a critical failure; fast-track approval | Emergency CAB or designated authority; post-implementation review mandatory |

Select the type that reflects the risk and urgency of this change. Emergency changes must be documented retrospectively in full if time constraints prevent pre-approval.

---

### 3. Change Description and Business Justification

**Description:**
`{{CHANGE_DESCRIPTION}}`

**Business justification:**
`{{BUSINESS_JUSTIFICATION}}`

Describe what will change (scope, components affected) and why the change is needed. The justification must link the change to a business need, risk mitigation, or compliance requirement. Avoid technical jargon here — this section is read by the Change Authority.

---

### 4. Risk Assessment

| Dimension | Assessment |
|---|---|
| Risk level | `{{RISK_LEVEL}}` — [low / medium / high] |
| Impact assessment | `{{IMPACT_ASSESSMENT}}` |
| Probability of failure | `{{PROBABILITY}}` — [low / medium / high] |
| Affected users / services | `{{AFFECTED_SCOPE}}` |

Assess impact (breadth and severity if the change fails or has unintended consequences) and probability (likelihood of failure or unexpected outcome). Risk level is the combined judgment of both dimensions. Document mitigations in the implementation plan.

---

### 5. Implementation Plan

**Pre-implementation steps:**

1. `{{IMPLEMENTATION_STEP_1}}`
2. `{{IMPLEMENTATION_STEP_2}}`
3. `{{IMPLEMENTATION_STEP_N}}`

**Rollback trigger:**
`{{ROLLBACK_TRIGGER}}`

Each step must be atomic and verifiable. Define the rollback trigger as a specific, observable condition (e.g. error rate exceeds 5%, health check fails) that unambiguously initiates the backout procedure. Reference the rollback plan document.

**Rollback plan reference:** `{{ROLLBACK_PLAN_REFERENCE}}`

---

### 6. Change Authority and CAB Review

| Field | Value |
|---|---|
| Change Authority | `{{CHANGE_AUTHORITY}}` |
| CAB review required | [yes / no] |
| CAB review date | `{{CAB_REVIEW_DATE}}` |
| CAB decision | `{{CAB_DECISION}}` |
| Approver sign-off | `{{APPROVER_SIGN_OFF}}` |
| Approval date | `{{APPROVAL_DATE}}` |

The Change Authority is the individual or body empowered to authorise this change. For standard changes this may be delegated to the service owner; for normal and emergency changes the CAB or emergency CAB must record a decision.

---

### 7. Implementation Window

| Field | Value |
|---|---|
| Scheduled start | `{{IMPLEMENTATION_WINDOW_START}}` |
| Scheduled end | `{{IMPLEMENTATION_WINDOW_END}}` |
| Maintenance window (if applicable) | `{{MAINTENANCE_WINDOW}}` |
| On-call contact | `{{ON_CALL_CONTACT}}` |

The implementation window must fall within any agreed maintenance windows for the affected service. Confirm on-call coverage before proceeding.

---

### 8. Post-Implementation Verification

**Verification criteria:**
`{{VERIFICATION_CRITERIA}}`

| Verification step | Expected result | Actual result | Verified by |
|---|---|---|---|
| `{{VERIFICATION_STEP_1}}` | `{{EXPECTED_RESULT_1}}` | `{{ACTUAL_RESULT_1}}` | `{{VERIFIER_1}}` |
| `{{VERIFICATION_STEP_2}}` | `{{EXPECTED_RESULT_2}}` | `{{ACTUAL_RESULT_2}}` | `{{VERIFIER_2}}` |

Document specific, measurable criteria that confirm the change was successful. Verification must occur within the implementation window before closing the change record.

---

### 9. Change Status Lifecycle

Track progress through the ITIL 4 Change Enablement lifecycle stages:

| Stage | Date | Updated by | Notes |
|---|---|---|---|
| Draft | `{{DRAFT_DATE}}` | `{{DRAFT_BY}}` | Initial record created |
| Submitted | `{{SUBMITTED_DATE}}` | `{{SUBMITTED_BY}}` | Submitted for assessment |
| Approved | `{{APPROVED_DATE}}` | `{{APPROVED_BY}}` | Authorised by Change Authority |
| Implemented | `{{IMPLEMENTED_DATE}}` | `{{IMPLEMENTED_BY}}` | Change applied to environment |
| Closed | `{{CLOSED_DATE}}` | `{{CLOSED_BY}}` | Verification complete; record closed |

A change record must not be closed until post-implementation verification criteria are met and, for emergency changes, the mandatory PIR is completed.

---

### 10. Traceability

- Related release plan: `{{RELEASE_PLAN_LINK}}`
- Related rollback plan: `{{ROLLBACK_PLAN_LINK}}`
- Related validation evidence: `{{VALIDATION_LINKS}}`
- PIR reference: `{{PIR_REFERENCE}}`

---

## Source Attribution

- Source manifests: `operations__nist_cisa.md`, `platform__aws_well_architected.md`
- Primary source basis: ITIL 4 Change Enablement practice
- Alignment mode: guided-synthesis
- Reviewed on: 2026-03-27
