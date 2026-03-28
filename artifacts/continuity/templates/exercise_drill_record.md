---
title: Exercise and Drill Record
artifact_type: template
status: public-draft
visibility: public
classification: public
owner: "{{OWNER_NAME}}"
review_cadence: annual
applies_to: continuity and incident response exercises
source_basis: NIST SP 800-34 Rev. 1, ISO 22301:2019
source_manifests:
  - operations__nist_cisa.md
  - operations__google_sre.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Exercise Identification

Uniquely identify the exercise. This block is required for all exercise types and must be completed before the exercise begins.

- **Exercise ID:** `{{EXERCISE_ID}}`
- **Exercise date:** `{{EXERCISE_DATE}}`
- **Exercise type:** `{{EXERCISE_TYPE}}` (tabletop / functional / full-scale)
- **Plan(s) exercised:** `{{PLANS_EXERCISED}}`
- **System(s) in scope:** `{{SYSTEMS_IN_SCOPE}}`
- **Exercise facilitator:** `{{EXERCISE_FACILITATOR}}`
- **Exercise location:** `{{EXERCISE_LOCATION}}`
- **Duration:** `{{EXERCISE_DURATION}}`

## Scope and Objectives

Define what the exercise will test and what success looks like. Objectives must be measurable and mapped to specific plan sections or BIA recovery targets.

**Scope statement:** `{{SCOPE_STATEMENT}}`

| Objective ID | Objective Description | Success Criteria | Plan Section |
|---|---|---|---|
| `{{OBJECTIVE_ID}}` | `{{OBJECTIVE_N}}` | `{{SUCCESS_CRITERIA}}` | `{{PLAN_SECTION_REF}}` |

Each objective should test a specific plan capability (e.g., activation speed, communication procedures, alternate site readiness). Align at least one objective to the RTO and RPO targets from the BIA.

## Participants

Record all personnel who participated in the exercise. Attendance is required for all personnel with recovery team roles assigned in the contingency plan.

| Participant Name | Role | Organization | Attendance Status |
|---|---|---|---|
| `{{PARTICIPANT_NAME}}` | `{{ROLE}}` | `{{ORGANIZATION}}` | `{{ATTENDANCE_STATUS}}` |

Note any key absences and whether a backup participant covered the role. Unexcused absences must be escalated to `{{ESCALATION_CONTACT}}`.

## Scenario Description

Describe the exercise scenario in sufficient detail for a reader who was not present to understand what was simulated. The scenario must be realistic, based on plausible threat conditions, and calibrated to the exercise type.

**Scenario summary:** `{{SCENARIO}}`

**Inject timeline:** List any injects used to evolve the scenario during the exercise.

| Inject ID | Time | Inject Description | Intended Test |
|---|---|---|---|
| `{{INJECT_ID}}` | `{{INJECT_TIME}}` | `{{INJECT_DESCRIPTION}}` | `{{INTENDED_TEST}}` |

## Exercise Timeline

Record the actual sequence of events during the exercise. This log is used for post-exercise analysis and as evidence for audit purposes.

| Phase Name | Start Time | End Time | Activities | Facilitator Notes |
|---|---|---|---|---|
| `{{PHASE_NAME}}` | `{{START_TIME}}` | `{{END_TIME}}` | `{{ACTIVITIES}}` | `{{FACILITATOR_NOTES}}` |

Phases typically include: preparation, scenario briefing, execution, hot wash, and close-out. Record actual times against planned times to assess exercise schedule performance.

## Observations and Findings

Record observations made during the exercise. Every observation must be categorized as a strength or an improvement area, and improvement observations must have a severity rating.

| Observation ID | Description | Category | Severity | Plan Section Affected |
|---|---|---|---|---|
| `{{OBSERVATION_N}}` | `{{OBSERVATION_DESCRIPTION}}` | `{{CATEGORY}}` (strength / improvement) | `{{SEVERITY}}` (high / medium / low) | `{{PLAN_SECTION_REF}}` |

Strengths should be documented to reinforce good practices. Improvement observations with high severity must generate corrective actions. Do not suppress observations to protect plan reputation.

## Corrective Actions

For every improvement observation with a severity of medium or higher, create a corrective action item. Track each item to closure through the plan maintenance process.

| Action ID | Observation Reference | Action Description | Owner | Due Date | Status |
|---|---|---|---|---|---|
| `{{ACTION_N}}` | `{{OBSERVATION_REF}}` | `{{ACTION_DESCRIPTION}}` | `{{OWNER}}` | `{{DUE_DATE}}` | `{{ACTION_STATUS}}` |

Corrective actions must be reviewed at the next scheduled plan review. High-severity actions that affect RTO or RPO targets must trigger a BIA review within `{{BIA_REVIEW_WINDOW}}`.

## Exercise Evaluation Summary

Provide an overall assessment of exercise performance against the stated objectives. This summary is the primary input to the next exercise planning cycle.

- **Overall result:** `{{OVERALL_RESULT}}` (objectives met / partially met / not met)
- **RTO target met:** `{{RTO_MET}}` (yes / no / not tested)
- **RPO target met:** `{{RPO_MET}}` (yes / no / not tested)
- **Key strengths:** `{{KEY_STRENGTHS}}`
- **Priority improvement areas:** `{{PRIORITY_IMPROVEMENTS}}`
- **Plan update required:** `{{PLAN_UPDATE_REQUIRED}}` (yes / no)
- **BIA review required:** `{{BIA_REVIEW_REQUIRED}}` (yes / no)

## Next Scheduled Exercise

Document the next exercise to maintain continuity of the testing programme. The next exercise type and scope should be informed by findings from this exercise.

- **Next exercise date:** `{{NEXT_EXERCISE_DATE}}`
- **Planned exercise type:** `{{NEXT_EXERCISE_TYPE}}`
- **Planned scope:** `{{NEXT_EXERCISE_SCOPE}}`
- **Responsible planner:** `{{NEXT_EXERCISE_PLANNER}}`

## Source Attribution

- Source manifests: `operations__nist_cisa.md`, `operations__google_sre.md`
- Primary source basis: NIST SP 800-34 Rev. 1 section 3.5, ISO 22301:2019 section 8.5
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
