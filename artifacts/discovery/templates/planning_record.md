---
title: Planning Record Template
artifact_type: template
status: draft
visibility: public
classification: public
owner: governance@org
review_cadence: quarterly
applies_to: planning and cycle setup
source_basis: Scrum Guide 2020 Sprint Planning event
source_manifests:
  - method__scrum_guide.md
alignment_mode: direct-adaptation
updated: 2026-03-27
---

## Planning Record — Sprint `{{SPRINT_NUMBER}}`

Sprint Planning initiates the Sprint by laying out the work to be performed. The resulting plan is created collaboratively by the entire Scrum Team. This record captures all three topics addressed during Sprint Planning: Why is this Sprint valuable? What can be done? How will the work get done?

---

### Sprint Context

| Field | Value |
|---|---|
| Sprint number | `{{SPRINT_NUMBER}}` |
| Start date | `{{SPRINT_START}}` |
| End date | `{{SPRINT_END}}` |
| Team capacity | `{{TEAM_CAPACITY_POINTS}}` story points |

Capacity is the total effort the team can commit, accounting for holidays, planned absence, and known interruptions. It is the primary constraint for item selection.

---

### Sprint Goal

> `{{SPRINT_GOAL}}`

The Sprint Goal explains why this Sprint is valuable. It is proposed by the Product Owner and agreed upon by the entire Scrum Team. It is a single, coherent objective that gives the team flexibility while creating focus. If the work turns out to be different than expected, the team negotiates with the Product Owner about the scope without affecting the Sprint Goal.

---

### Sprint Backlog

Items selected from the Product Backlog to be delivered in this Sprint. Only items that can be done within capacity and that contribute to the Sprint Goal should appear here.

| Item ID | Title | Estimate (pts) | Assignee |
|---|---|---|---|
| `{{ITEM_ID_1}}` | `{{ITEM_TITLE_1}}` | `{{ESTIMATE_1}}` | `{{ASSIGNEE_1}}` |
| `{{ITEM_ID_2}}` | `{{ITEM_TITLE_2}}` | `{{ESTIMATE_2}}` | `{{ASSIGNEE_2}}` |

---

### How the Work Will Be Done

`{{TECHNICAL_APPROACH}}`

Describe the technical approach, architectural decisions, and any implementation strategy agreed upon during planning. This is not a full design doc — it is the team's shared understanding of the path forward. Include decisions about decomposition of stories into tasks where relevant.

---

### Dependencies and Risks

| # | Dependency / Risk | Owner | Mitigation |
|---|---|---|---|
| 1 | `{{DEPENDENCY_1}}` | `{{DEPENDENCY_OWNER_1}}` | `{{MITIGATION_1}}` |
| 2 | `{{DEPENDENCY_2}}` | `{{DEPENDENCY_OWNER_2}}` | `{{MITIGATION_2}}` |

Identify anything that could prevent the Sprint Goal from being achieved: external dependencies, unresolved technical unknowns, resource constraints, or blocked items.

---

### Definition of Done — Confirmation

The team confirms that the current Definition of Done applies to all Sprint Backlog items. No item is considered complete until it meets all criteria in the Definition of Done.

- [ ] DoD reviewed and agreed by the Scrum Team for this Sprint.
- [ ] All selected items are small enough to complete within the Sprint.
- [ ] Acceptance criteria are understood for each selected item.

---

### Velocity Reference (Last 3 Sprints)

| Sprint | Velocity (pts) |
|---|---|
| `{{SPRINT_N_MINUS_2}}` | `{{SPRINT_N_MINUS_2_VELOCITY}}` |
| `{{SPRINT_N_MINUS_1}}` | `{{SPRINT_N_MINUS_1_VELOCITY}}` |
| `{{SPRINT_N}}` | `{{SPRINT_N_VELOCITY}}` |

Velocity is used as a guide, not a commitment. Capacity calculation takes precedence over raw velocity. Track trends rather than targeting a specific number.

## Source Attribution

- Source manifests: `method__scrum_guide.md`
- Primary source basis: Scrum Guide 2020 — Sprint Planning event (three topics: Why, What, How)
- Alignment mode: direct-adaptation
- Reviewed on: 2026-03-27
