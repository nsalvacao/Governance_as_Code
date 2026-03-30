---
title: Post-Implementation Review Template
artifact_type: template
status: public
visibility: public
classification: public
owner: "{{DELIVERY_OWNER}}"
review_cadence: quarterly
applies_to: post-release and implementation review
source_basis: GOV.UK PIR structure and ITIL 4 continual improvement practice
source_manifests:
  - operations__nist_cisa.md
  - governance__github_docs.md
alignment_mode: guided-synthesis
updated: 2026-03-30
---

## Post-Implementation Review - `{{CHANGE_ID}}`

Conduct this review within the window defined in the change record (typically 5–10 business days after implementation for normal changes; within 2 business days for emergency changes and rollbacks). The PIR is a structured learning exercise, not a blame exercise. All findings must be converted into tracked action items.

---

### 1. PIR Context

| Field | Value |
|---|---|
| Change ID | `{{CHANGE_ID}}` |
| Change title | `{{CHANGE_TITLE}}` |
| Implementation date | `{{IMPLEMENTATION_DATE}}` |
| Review date | `{{REVIEW_DATE}}` |
| Facilitator | `{{FACILITATOR}}` |
| Participants | `{{PARTICIPANTS}}` |
| Review type | [standard / emergency / rollback] |

The facilitator should be someone not directly involved in the implementation to ensure impartiality. Participants must include the implementer(s), the change owner, and a representative from the affected service team.

---

### 2. Objectives vs Outcomes

Map every stated objective from the change record to its actual result. Identify and explain all variances.

| Objective | Planned result | Actual result | Variance analysis |
|---|---|---|---|
| `{{OBJECTIVE_1}}` | `{{PLANNED_RESULT_1}}` | `{{ACTUAL_RESULT_1}}` | `{{VARIANCE_1}}` |
| `{{OBJECTIVE_2}}` | `{{PLANNED_RESULT_2}}` | `{{ACTUAL_RESULT_2}}` | `{{VARIANCE_2}}` |
| `{{OBJECTIVE_N}}` | `{{PLANNED_RESULT_N}}` | `{{ACTUAL_RESULT_N}}` | `{{VARIANCE_N}}` |

A variance of "none" is a valid and expected outcome. Positive variances (exceeded expectations) are as informative as negative ones — record what contributed to the better-than-expected result.

---

### 3. Implementation Quality

Assess delivery quality across the three dimensions used in the GOV.UK PIR framework. For any "no" answer, provide the reason and the delta.

| Dimension | Assessment | Reason / delta (if not fully met) |
|---|---|---|
| On time | [yes / no / partial] — planned: `{{PLANNED_END}}`, actual: `{{ACTUAL_END}}` | `{{TIME_DELTA_REASON}}` |
| On scope | [yes / no / partial] — scope changes: `{{SCOPE_CHANGES}}` | `{{SCOPE_DELTA_REASON}}` |
| Quality gates met | [yes / no / partial] — gates missed: `{{QUALITY_GATES_MISSED}}` | `{{QUALITY_DELTA_REASON}}` |

---

### 4. Issues Encountered

Document every issue encountered during or immediately after implementation, regardless of severity.

| Issue | Impact | Resolution | Recurrence risk |
|---|---|---|---|
| `{{ISSUE_1}}` | `{{ISSUE_IMPACT_1}}` | `{{RESOLUTION_1}}` | [low / medium / high] |
| `{{ISSUE_2}}` | `{{ISSUE_IMPACT_2}}` | `{{RESOLUTION_2}}` | [low / medium / high] |
| `{{ISSUE_N}}` | `{{ISSUE_IMPACT_N}}` | `{{RESOLUTION_N}}` | [low / medium / high] |

For each issue with medium or high recurrence risk, a corresponding action item is mandatory in section 7.

---

### 5. Benefits Realized

Compare the benefits expected in the business justification (from the change record) against what was actually observed.

**Expected benefits:**
`{{EXPECTED_BENEFITS}}`

**Actual benefit realization:**
`{{BENEFIT_REALIZATION}}`

**Measurement method:**
`{{MEASUREMENT_METHOD}}`

**Measurement date / next measurement date:**
`{{MEASUREMENT_DATE}}` / `{{NEXT_MEASUREMENT_DATE}}`

If benefits are not yet measurable (e.g. cost savings that accrue over time), define the measurement plan and schedule. Benefits should be reviewed at the next relevant cadence.

---

### 6. Lessons Learned

Capture specific, actionable lessons. Avoid generic statements — tie each lesson to an observable event from this implementation.

#### What worked well

| Lesson | Evidence | Recommend for future |
|---|---|---|
| `{{LESSON_POSITIVE_1}}` | `{{LESSON_EVIDENCE_1}}` | [yes / no] |
| `{{LESSON_POSITIVE_2}}` | `{{LESSON_EVIDENCE_2}}` | [yes / no] |
| `{{LESSON_POSITIVE_N}}` | `{{LESSON_EVIDENCE_N}}` | [yes / no] |

#### What to improve

| Lesson | Evidence | Priority |
|---|---|---|
| `{{LESSON_IMPROVE_1}}` | `{{LESSON_IMPROVE_EVIDENCE_1}}` | [low / medium / high] |
| `{{LESSON_IMPROVE_2}}` | `{{LESSON_IMPROVE_EVIDENCE_2}}` | [low / medium / high] |
| `{{LESSON_IMPROVE_N}}` | `{{LESSON_IMPROVE_EVIDENCE_N}}` | [low / medium / high] |

Lessons with "recommend for future: yes" must be propagated to the relevant process or template documentation by the assigned action owner.

---

### 7. Action Items

Capture every action item raised during the PIR. Each action must have a single owner and a concrete due date. Track these in the project management system.

| Action | Owner | Due date | Priority | Status |
|---|---|---|---|---|
| `{{ACTION_1}}` | `{{OWNER_1}}` | `{{DUE_DATE_1}}` | [low / medium / high] | [open] |
| `{{ACTION_2}}` | `{{OWNER_2}}` | `{{DUE_DATE_2}}` | [low / medium / high] | [open] |
| `{{ACTION_N}}` | `{{OWNER_N}}` | `{{DUE_DATE_N}}` | [low / medium / high] | [open] |

Action items from the PIR must be reviewed at the next relevant team cadence. High-priority items must have a confirmed owner and due date before the PIR is closed.

---

### 8. PIR Sign-Off

| Role | Name | Sign-off date |
|---|---|---|
| Facilitator | `{{FACILITATOR}}` | `{{FACILITATOR_SIGN_OFF_DATE}}` |
| Change owner | `{{CHANGE_OWNER}}` | `{{CHANGE_OWNER_SIGN_OFF_DATE}}` |
| Service owner | `{{SERVICE_OWNER}}` | `{{SERVICE_OWNER_SIGN_OFF_DATE}}` |

**PIR status:** [open / closed]
**Closed by:** `{{PIR_CLOSED_BY}}`
**Closure date:** `{{PIR_CLOSURE_DATE}}`

The PIR is not closed until all high-priority action items have owners and due dates assigned, and all participants have provided sign-off.

---

## Source Attribution

- Source manifests: `operations__nist_cisa.md`, `governance__github_docs.md`
- Primary source basis: GOV.UK PIR structure and ITIL 4 continual improvement practice
- Alignment mode: guided-synthesis
- Reviewed on: 2026-03-30
