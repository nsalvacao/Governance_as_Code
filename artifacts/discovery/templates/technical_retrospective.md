---
title: Technical Retrospective Template
artifact_type: template
status: draft
visibility: public
classification: public
owner: governance@org
review_cadence: quarterly
applies_to: iteration and technical learning reviews
source_basis: Scrum Guide 2020 Sprint Retrospective + Norm Kerth Prime Directive
source_manifests:
  - method__scrum_guide.md
  - operations__google_sre.md
alignment_mode: guided-synthesis
updated: 2026-03-27
---

## Technical Retrospective — `{{PERIOD}}`

### Prime Directive

> "Regardless of what we discover, we understand and truly believe that everyone did the best job they could, given what they knew at the time, their skills and abilities, the resources available, and the situation at hand."
>
> — Norm Kerth, *Project Retrospectives: A Handbook for Team Reviews*

The Prime Directive must be read aloud or acknowledged at the start of every retrospective. It establishes psychological safety as the foundation for honest inspection.

---

### Sprint / Period Context

| Field | Value |
|---|---|
| Sprint / Period | `{{PERIOD}}` |
| Date of retrospective | `{{RETRO_DATE}}` |
| Facilitator | `{{FACILITATOR}}` |
| Attendees | `{{ATTENDEES}}` |

---

### What Went Well

Factual observations only — what actually happened that the team wants to protect or amplify.

| # | Observation |
|---|---|
| 1 | `{{POSITIVE_1}}` |
| 2 | `{{POSITIVE_2}}` |
| 3 | `{{POSITIVE_3}}` |

---

### What to Improve

Specific and actionable items. Avoid blame. Focus on processes, tools, and systemic issues rather than individuals.

| # | Improvement area |
|---|---|
| 1 | `{{IMPROVE_1}}` |
| 2 | `{{IMPROVE_2}}` |
| 3 | `{{IMPROVE_3}}` |

---

### Action Items

The Scrum Guide recommends the Scrum Team identifies the most impactful improvement to implement in the next Sprint. Each action item must have a clear owner and a verifiable success criterion.

| Action | Owner | Due date | Success criteria |
|---|---|---|---|
| `{{ACTION_1}}` | `{{OWNER_1}}` | `{{DUE_DATE_1}}` | `{{SUCCESS_CRITERIA_1}}` |
| `{{ACTION_2}}` | `{{OWNER_2}}` | `{{DUE_DATE_2}}` | `{{SUCCESS_CRITERIA_2}}` |

---

### Team Health Pulse (Optional)

Self-reported scores on a 1–5 scale. Use to track trends over time, not as a performance indicator. Scores are team property — do not report upward without team consent.

| Dimension | Score (1–5) |
|---|---|
| Energy | `{{ENERGY_SCORE_1_TO_5}}` |
| Collaboration | `{{COLLAB_SCORE}}` |
| Clarity | `{{CLARITY_SCORE}}` |

---

### Follow-up from Previous Retrospective

Track the fate of prior action items. Close the loop before opening new ones.

| Previous action | Status |
|---|---|
| `{{PREV_ACTION_1}}` | `{{PREV_STATUS_1}}` |
| `{{PREV_ACTION_2}}` | `{{PREV_STATUS_2}}` |

**Status values:** done / in-progress / dropped

If an action is dropped, record the reason to maintain transparency and avoid repeating the cycle.

## Source Attribution

- Source manifests: `method__scrum_guide.md`, `operations__google_sre.md`
- Primary source basis: Scrum Guide 2020 Sprint Retrospective + Norm Kerth Prime Directive (*Project Retrospectives*, 2001)
- Alignment mode: guided-synthesis
- Reviewed on: 2026-03-27
