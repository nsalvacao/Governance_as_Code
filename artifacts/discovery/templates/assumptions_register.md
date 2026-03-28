---
title: Assumptions Register Template
artifact_type: template
status: draft
visibility: public
classification: public
owner: governance@org
review_cadence: quarterly
applies_to: planning and uncertainty management
source_basis: Assumption-based planning (PMI PMBOK) + Lean Startup validated learning
source_manifests:
  - platform__microsoft_learn.md
alignment_mode: guided-synthesis
updated: 2026-03-27
---

## Assumptions Register — `{{SCOPE_NAME}}`

An Assumptions Register makes implicit beliefs explicit so they can be tested. Every assumption is a risk until validated. This register is owned by the team and reviewed continuously — not only at project start. Assumptions that are invalidated must trigger a reassessment of the decisions that depended on them.

---

### Context

`{{ASSUMPTION_CONTEXT}}`

Describe the initiative, product, or decision context for which these assumptions are being tracked. Include the planning horizon and the decision-making stage (e.g., pre-discovery, post-spike, pre-launch).

---

### Assumptions Table

| ID | Assumption | Category | Owner | Confidence | Validation method | Validated | Risk if wrong |
|---|---|---|---|---|---|---|---|
| A-01 | `{{ASSUMPTION_1}}` | `{{CATEGORY_1}}` | `{{OWNER_1}}` | `{{CONFIDENCE_1}}` | `{{VALIDATION_METHOD_1}}` | `{{VALIDATED_1}}` | `{{RISK_1}}` |
| A-02 | `{{ASSUMPTION_2}}` | `{{CATEGORY_2}}` | `{{OWNER_2}}` | `{{CONFIDENCE_2}}` | `{{VALIDATION_METHOD_2}}` | `{{VALIDATED_2}}` | `{{RISK_2}}` |

**Category values:** Technical / Business / User / Market

**Confidence values:** High / Medium / Low

**Validated values:** yes / no / partial

---

### Assumption Validation Log

Record the outcome of each validation effort. Update this log as experiments, interviews, and data analysis complete. Each entry closes the loop on a specific assumption.

| Assumption ID | Test conducted | Result | Date | Action taken |
|---|---|---|---|---|
| `{{ASSUMPTION_ID_1}}` | `{{TEST_1}}` | `{{RESULT_1}}` | `{{DATE_1}}` | `{{ACTION_1}}` |
| `{{ASSUMPTION_ID_2}}` | `{{TEST_2}}` | `{{RESULT_2}}` | `{{DATE_2}}` | `{{ACTION_2}}` |

---

### Critical Assumptions

The top `{{N}}` assumptions whose invalidity would cause the project to fail, be cancelled, or require a fundamental pivot. These must be validated first, before significant investment is committed.

1. `{{CRITICAL_ASSUMPTION_1}}` — risk: `{{CRITICAL_RISK_1}}`
2. `{{CRITICAL_ASSUMPTION_2}}` — risk: `{{CRITICAL_RISK_2}}`

Prioritise critical assumption validation above feature delivery. An unvalidated critical assumption is the highest-risk item in any backlog.

---

### Rules

- Keep assumptions explicit until evidence either confirms or removes them.
- Escalate assumptions with low confidence or high impact.
- Tie each assumption to a decision, experiment, or backlog item.
- An assumption that cannot be validated is a constraint — treat it as such.

## Source Attribution

- Source manifests: `platform__microsoft_learn.md`
- Primary source basis: Assumption-based planning (PMI PMBOK 7th edition) + Lean Startup validated learning (Ries, 2011)
- Alignment mode: guided-synthesis
- Reviewed on: 2026-03-27
