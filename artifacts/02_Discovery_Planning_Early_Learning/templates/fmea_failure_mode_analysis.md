---
title: FMEA / Failure Mode Analysis Template
artifact_type: template
status: public-draft
visibility: public
classification: public
owner: "{{GOVERNANCE_OWNER}}"
review_cadence: quarterly
applies_to: failure mode analysis and mitigation planning
source_basis: IEC 60812:2018 FMEA standard + SAE J1739 Design FMEA methodology
source_manifests:
  - platform__microsoft_learn.md
  - operations__nist_cisa.md
alignment_mode: guided-synthesis
updated: 2026-03-27
---

## FMEA — `{{SYSTEM_OR_PROCESS_NAME}}`

A Failure Mode and Effects Analysis (FMEA) is a systematic, proactive technique for identifying how a system or process can fail and assessing the impact of each failure. This template follows IEC 60812:2018 and SAE J1739. The primary output is the Risk Priority Number (RPN = Severity × Occurrence × Detection), which drives prioritisation of corrective actions.

---

### System / Process Context

| Field | Value |
|---|---|
| System or process | `{{SYSTEM_OR_PROCESS}}` |
| Scope | `{{SCOPE}}` |
| Analysis date | `{{ANALYSIS_DATE}}` |
| Lead analyst | `{{LEAD_ANALYST}}` |
| Review date | `{{REVIEW_DATE}}` |

Define the boundary of the analysis. Out-of-scope elements should be listed explicitly to prevent ambiguity. FMEA is a living document — update it whenever the system changes or a new failure mode is discovered.

---

### FMEA Table

**Scoring scale (per IEC 60812 / SAE J1739):**
- **Severity (S):** 1 (no effect) → 10 (catastrophic, safety/compliance impact)
- **Occurrence (O):** 1 (extremely unlikely) → 10 (almost certain)
- **Detection (D):** 1 (almost certain to detect before impact) → 10 (cannot detect)
- **RPN = S × O × D** (range: 1–1000; higher = greater risk)

IEC 60812 requires "Action Taken" and "Completion Status" columns to close the corrective action loop — without them, the FMEA is open-ended and cannot demonstrate that recommended actions were implemented and verified.

| Item ID | Function | Failure Mode | Effect | S | Cause | O | Current Controls | D | RPN | Recommended Action | Action Owner | Target Date | Action Taken | Completion Status | Revised RPN |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FM-01 | `{{FUNCTION_1}}` | `{{FAILURE_MODE_1}}` | `{{EFFECT_1}}` | `{{S_1}}` | `{{CAUSE_1}}` | `{{O_1}}` | `{{CONTROLS_1}}` | `{{D_1}}` | `{{RPN_1}}` | `{{ACTION_1}}` | `{{OWNER_1}}` | `{{TARGET_DATE_1}}` | `{{ACTION_TAKEN_1}}` | `{{COMPLETION_STATUS_1}}` (Open / In Progress / Completed / Verified) | `{{REVISED_RPN_1}}` |
| FM-02 | `{{FUNCTION_2}}` | `{{FAILURE_MODE_2}}` | `{{EFFECT_2}}` | `{{S_2}}` | `{{CAUSE_2}}` | `{{O_2}}` | `{{CONTROLS_2}}` | `{{D_2}}` | `{{RPN_2}}` | `{{ACTION_2}}` | `{{OWNER_2}}` | `{{TARGET_DATE_2}}` | `{{ACTION_TAKEN_2}}` | `{{COMPLETION_STATUS_2}}` | `{{REVISED_RPN_2}}` |

---

### RPN Thresholds

| Risk level | RPN range | Required action |
|---|---|---|
| High | > `{{HIGH_RPN_THRESHOLD}}` | Mandatory corrective action before release |
| Medium | > `{{MED_RPN_THRESHOLD}}` | Corrective action planned and tracked |
| Low | ≤ `{{MED_RPN_THRESHOLD}}` | Monitor; accept with documented rationale |

Set thresholds based on system criticality and organisational risk tolerance. Common defaults: High > 200, Medium > 100 — adjust to context.

---

### Review Rules

- Recalculate RPN when the system changes, a new control is added, or an action is completed.
- Escalate high-RPN items into the backlog or decision log with a tracked owner.
- Connect each recommended action to a backlog item, risk register entry, or ADR.
- Re-review the full FMEA at the stated review date or after any significant incident.

## Source Attribution

- Source manifests: `platform__microsoft_learn.md`, `operations__nist_cisa.md`
- Primary source basis: IEC 60812:2018 (Failure modes and effects analysis) + SAE J1739 (Design FMEA methodology)
- Alignment mode: guided-synthesis
- Reviewed on: 2026-03-27
