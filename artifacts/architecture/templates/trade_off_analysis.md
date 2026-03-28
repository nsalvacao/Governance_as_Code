---
title: Trade-off Analysis Template
artifact_type: template
status: public-draft
visibility: public
classification: public
owner: architecture-platform
review_cadence: quarterly
applies_to: comparisons between viable architecture or delivery options
source_basis: AWS Well-Architected trade-off analysis practices; Microsoft Learn decision support guidance
source_manifests:
  - platform__aws_well_architected.md
  - platform__microsoft_learn.md
alignment_mode: direct-adaptation
updated: 2026-03-27
---

## Purpose

Record a structured comparison of options so that the selected path can be traced back to the factors that mattered most. This template uses a weighted-criteria matrix approach to make implicit trade-offs explicit and auditable.

## Template

---

### Analysis metadata

- **Analysis ID:** `{{ANALYSIS_ID}}`
- **Date:** `{{ANALYSIS_DATE}}`
- **Author:** `{{AUTHOR}}`
- **Related ADR:** `ADR-{{ADR_REFERENCE}}`
- **Related design rationale:** `{{RATIONALE_ID}}`
- **Status:** `{{STATUS}}` (draft | accepted | superseded)

---

### 1. Decision context

Describe the specific decision that requires structured evaluation: `{{DECISION_CONTEXT}}`. State the trigger, the system or component affected, and the deadline or forcing function if one exists. This section should make clear why a structured analysis was necessary rather than a simple preference vote.

### 2. Evaluation criteria

List the criteria used to compare options. Each criterion must have a weight that reflects its relative importance. Weights should sum to 1.0 across all criteria.

| Criterion | Description | Weight |
|---|---|---|
| `{{CRITERION_NAME}}` | `{{CRITERION_DESCRIPTION}}` | `{{WEIGHT_0_TO_1}}` |

Guidance on criteria selection: include at least one criterion from each relevant AWS Well-Architected pillar (security, reliability, operational excellence, performance efficiency, cost optimization, sustainability). Remove pillars that are genuinely not applicable and document the reason.

### 3. Options matrix

Score each option against each criterion on a scale of 1 (poor fit) to 5 (excellent fit). Multiply each score by the criterion weight to get the weighted score. Sum weighted scores for each option to produce a weighted total.

| Option | `{{CRITERION_NAME}}` (×`{{WEIGHT_0_TO_1}}`) | … | Weighted total |
|---|---|---|---|
| `{{OPTION_NAME}}` | `{{SCORE}}` | … | `{{WEIGHTED_TOTAL}}` |

Add a row for each option and a column for each criterion. At least two options and two criteria are required for a valid analysis.

**Scoring notes:**
- `{{SCORING_NOTE}}` — explain any score that might not be obvious to a future reviewer.

### 4. Sensitivity analysis

State whether the recommendation changes if any single criterion weight is adjusted by ±20%. This tests whether the recommendation is robust or depends on a particular weighting choice.

- **Robust:** the recommendation holds across all single-criterion weight variations of ±20%: `{{ROBUST_YES_NO}}`
- **Sensitive criteria:** if the recommendation is not robust, list the criteria where a weight change flips the result: `{{SENSITIVE_CRITERIA}}`
- **Implication:** `{{SENSITIVITY_IMPLICATION}}`

### 5. Recommendation

State the recommended option: `{{RECOMMENDED_OPTION}}`.

**Justification:** Explain why the highest-scoring option is recommended, referencing the weighted total and any qualitative factors that the matrix does not capture. If the recommended option is not the highest scorer, explain the override reason.

**Conditions:** `{{CONDITIONS}}` — list any conditions that must hold for the recommendation to remain valid (e.g. cost assumptions, availability of a technology, regulatory status).

### 6. Dissenting views

Record any significant disagreement with the recommendation. This section is mandatory if the analysis was contested.

`{{DISSENT_IF_ANY}}`

If no dissent was recorded, state: "No dissent recorded." Do not leave this section blank.

---

## Guidance

- Keep the comparison explicit enough for later review and automation.
- Include cost, operational risk, security, maintainability, and delivery impact where relevant.
- Scores must be assigned before the recommendation is stated — do not reverse-engineer scores to justify a predetermined choice.
- Link the final recommendation to an ADR so the decision is durable.

## Source Attribution

- Source manifests: `platform__aws_well_architected.md`, `platform__microsoft_learn.md`
- Primary source basis: AWS Well-Architected trade-off analysis practices; Microsoft Learn decision support guidance
- Alignment mode: direct-adaptation
- Reviewed on: 2026-03-27
