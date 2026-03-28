---
title: Root Cause Analysis Template
artifact_type: template
status: public-draft
visibility: public
classification: public
owner: knowledge-platform
review_cadence: quarterly
applies_to: incidents, defects, and recurring operational failures
source_basis: NIST SP 800-61 incident analysis combined with 5 Whys and Ishikawa causal methods
source_manifests:
  - operations__nist_cisa.md
  - operations__google_sre.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Purpose

Document the causal chain behind a failure so that analysis leads to durable improvement, not just a label. A good RCA identifies the root cause and the systemic conditions that allowed it, then maps each to a verifiable corrective action.

---

## Incident Context

**Incident ID:** {{INCIDENT_ID}}
**Date:** {{DATE}}
**RCA facilitator:** {{FACILITATOR}}

Reference the postmortem or incident record that triggered this RCA. The facilitator is responsible for keeping the analysis blameless and structurally complete.

---

## Problem Statement

{{PROBLEM_STATEMENT}}

State what happened, when, where, and what the impact was. The problem statement must be falsifiable — precise enough that a corrective action can be evaluated against it. Avoid vague language such as "the system was slow."

---

## 5 Whys Analysis

Start from the observed problem and ask "Why?" iteratively until reaching a root cause that is actionable. Shallow analysis stops at symptoms; rigorous analysis reaches systemic or design-level causes.

| Step | Question | Answer |
|---|---|---|
| Why 1 | {{WHY_1}} | {{BECAUSE_1}} |
| Why 2 | {{WHY_2}} | {{BECAUSE_2}} |
| Why 3 | {{WHY_3}} | {{BECAUSE_3}} |
| Why 4 | {{WHY_4}} | {{BECAUSE_4}} |
| Why 5 | {{WHY_5}} | {{ROOT_CAUSE}} |

If the root cause is reached before Why 5, stop at that step. If five levels are insufficient, continue until the cause is actionable. Document your stopping criteria.

---

## Ishikawa (Fishbone) Cause Categories

Organize contributing causes by category to ensure the analysis covers all relevant dimensions. Not every category will apply to every incident.

| Category | Contributing cause |
|---|---|
| People | {{PEOPLE_CAUSE}} |
| Process | {{PROCESS_CAUSE}} |
| Technology | {{TECH_CAUSE}} |
| Environment | {{ENV_CAUSE}} |

For each populated cell, note whether the cause is confirmed (evidence exists) or hypothesized (inference from available data). Hypotheses should be validated before closing corrective actions.

---

## Root Cause Statement

{{ROOT_CAUSE_STATEMENT}}

Write a single concise statement that captures the fundamental cause. This statement should be specific enough to guide a corrective action and general enough to prevent recurrence, not just the specific instance.

---

## Contributing Factors

Conditions that amplified the impact or increased the likelihood of the root cause manifesting. Each contributing factor is independently worth addressing.

- {{CONTRIBUTING_FACTOR_1}}
- {{CONTRIBUTING_FACTOR_2}}
- {{CONTRIBUTING_FACTOR_N}}

---

## Systemic Factors

Conditions in the broader system — architecture, process, culture, or tooling — that made this failure mode possible. Systemic factors are the targets for long-term reliability improvement.

- {{SYSTEMIC_FACTOR_1}}
- {{SYSTEMIC_FACTOR_2}}
- {{SYSTEMIC_FACTOR_N}}

---

## Corrective Actions

Map each action to the root cause, a contributing factor, or a systemic factor. Actions without this mapping are not corrective — they are tasks.

| Action | Type | Owner | Due |
|---|---|---|---|
| {{ACTION_1}} | preventive / corrective / detective | {{OWNER}} | {{DUE}} |
| {{ACTION_2}} | preventive / corrective / detective | {{OWNER}} | {{DUE}} |
| {{ACTION_N}} | preventive / corrective / detective | {{OWNER}} | {{DUE}} |

Types: **preventive** = stops recurrence; **corrective** = repairs current damage; **detective** = improves ability to detect faster next time.

---

## Verification Criteria

{{VERIFICATION}}

Describe how we will confirm that the root cause has been addressed. Verification criteria must be measurable and observable — for example, a metric threshold, a test result, or an audit finding — not a subjective judgment.

---

## Source Attribution

- Source manifests: operations__nist_cisa.md, operations__google_sre.md
- Primary source basis: NIST SP 800-61 incident analysis combined with 5 Whys and Ishikawa causal methods
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
