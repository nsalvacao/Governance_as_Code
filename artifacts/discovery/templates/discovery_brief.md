---
title: Discovery Brief Template
artifact_type: template
status: draft
visibility: public
classification: public
owner: governance@org
review_cadence: quarterly
applies_to: discovery and problem framing
source_basis: Dual-track discovery — Teresa Torres / Jeff Patton continuous discovery
source_manifests:
  - method__scrum_guide.md
  - governance__github_docs.md
alignment_mode: guided-synthesis
updated: 2026-03-27
---

## Discovery Brief — `{{INITIATIVE_NAME}}`

A Discovery Brief frames the problem before any solution is considered. It captures the user problem, supporting evidence, and the learning questions the team must answer before committing to a solution path. It is not a requirements document — it is a structured hypothesis about where value exists.

---

### Problem Statement

> `{{PROBLEM_STATEMENT}}`

Describe the user problem in the user's terms, not in terms of a desired feature or solution. A good problem statement answers: who experiences this, what they are trying to do, and where they get stuck. Do not include solution language here.

---

### Who Experiences This Problem

| Field | Value |
|---|---|
| User segment | `{{USER_SEGMENT}}` |
| Context | `{{CONTEXT}}` |

Identify the specific type of user and the situation in which the problem occurs. "All users" is not a valid segment — narrow it to the group for whom this problem is most acute.

---

### Evidence of the Problem

| Data source | Evidence |
|---|---|
| `{{DATA_SOURCE_1}}` | `{{EVIDENCE_1}}` |
| `{{DATA_SOURCE_2}}` | `{{EVIDENCE_2}}` |

List the concrete signals that confirm this problem exists: support tickets, usability session observations, analytics data, survey responses, or interview quotes. Quantity and quality of evidence should be proportional to the investment being considered.

---

### Why Solve Now

| Field | Value |
|---|---|
| Business opportunity | `{{BUSINESS_OPPORTUNITY}}` |
| Urgency | `{{URGENCY}}` |

Explain the cost of delay and the opportunity being addressed. This section justifies prioritization over other problems in the backlog.

---

### Success Metrics

Define measurable outcomes that would confirm the problem is solved. Separate from output metrics (features shipped).

| Metric | Baseline | Target | Timeframe |
|---|---|---|---|
| `{{METRIC_1}}` | `{{BASELINE_1}}` | `{{TARGET_1}}` | `{{TIMEFRAME_1}}` |
| `{{METRIC_2}}` | `{{BASELINE_2}}` | `{{TARGET_2}}` | `{{TIMEFRAME_2}}` |

---

### Learning Questions

What must the team learn to confirm they are solving the right problem? Each question should be answerable through research, experiment, or data — not by assumption.

1. `{{LEARNING_QUESTION_1}}`
2. `{{LEARNING_QUESTION_2}}`
3. `{{LEARNING_QUESTION_3}}`

---

### Constraints

1. `{{CONSTRAINT_1}}`
2. `{{CONSTRAINT_2}}`

List known constraints: technical, legal, regulatory, organisational, or timeline-based. Constraints narrow the solution space before ideation begins.

---

### Out of Scope

`{{OUT_OF_SCOPE}}`

Explicitly state what this brief does not cover. This prevents scope creep and helps future readers understand deliberate exclusions.

---

### Next Steps

The smallest useful follow-up action that will reduce uncertainty.

1. `{{NEXT_STEP_1}}`
2. `{{NEXT_STEP_2}}`

## Source Attribution

- Source manifests: `method__scrum_guide.md`, `governance__github_docs.md`
- Primary source basis: Dual-track discovery (Teresa Torres, *Continuous Discovery Habits*, 2021; Jeff Patton, *User Story Mapping*, 2014)
- Alignment mode: guided-synthesis
- Reviewed on: 2026-03-27
