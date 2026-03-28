---
title: Business Case / Value Case
artifact_type: template
status: public-draft
visibility: public
classification: public
owner: "{{GOVERNANCE_OWNER}}"
review_cadence: quarterly
applies_to: initiative justification and value framing
source_basis: PMI, PRINCE2
source_manifests:
  - project__pmi.md
  - project__prince2.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

# Business Case / Value Case

## Purpose

Capture why the initiative should exist, what value it creates, and what cost or risk it introduces (PRINCE2 2023 Business Case + PMI Benefits Realization Management).

## Business Case Summary

| Field | Value |
|---|---|
| Initiative Name | `{{INITIATIVE_NAME}}` |
| Business Case ID | `{{BUSINESS_CASE_ID}}` |
| Prepared By | `{{BUSINESS_CASE_AUTHOR}}` |
| Date | `{{BUSINESS_CASE_DATE}}` |
| Version | `{{BUSINESS_CASE_VERSION}}` |
| Decision Status | `{{DECISION_STATUS}}` (Draft / Approved / Superseded / Closed) |
| Sponsor | `{{SPONSOR}}` |

## Reasons and Problem Statement

**Problem or opportunity**: `{{PROBLEM_OR_OPPORTUNITY}}`

**Why now**: `{{URGENCY_RATIONALE}}`

**Options considered**:

| Option | Description | Pros | Cons | Cost Estimate | Recommended? |
|---|---|---|---|---|---|
| Do nothing | `{{DO_NOTHING_DESC}}` | `{{DO_NOTHING_PROS}}` | `{{DO_NOTHING_CONS}}` | `{{DO_NOTHING_COST}}` | No |
| `{{OPTION_1}}` | `{{OPTION_1_DESC}}` | `{{OPTION_1_PROS}}` | `{{OPTION_1_CONS}}` | `{{OPTION_1_COST}}` | `{{OPTION_1_RECOMMENDED}}` |
| `{{OPTION_2}}` | `{{OPTION_2_DESC}}` | `{{OPTION_2_PROS}}` | `{{OPTION_2_CONS}}` | `{{OPTION_2_COST}}` | `{{OPTION_2_RECOMMENDED}}` |

**Recommended option**: `{{RECOMMENDED_OPTION}}` — rationale: `{{RECOMMENDATION_RATIONALE}}`

## Expected Benefits

| Benefit ID | Benefit Description | Benefit Metric | Baseline | Target | Realization Date | Benefit Owner |
|---|---|---|---|---|---|---|
| `{{BENEFIT_ID_1}}` | `{{BENEFIT_DESC_1}}` | `{{BENEFIT_METRIC_1}}` | `{{BASELINE_1}}` | `{{TARGET_1}}` | `{{REALIZATION_DATE_1}}` | `{{BENEFIT_OWNER_1}}` |
| `{{BENEFIT_ID_2}}` | `{{BENEFIT_DESC_2}}` | `{{BENEFIT_METRIC_2}}` | `{{BASELINE_2}}` | `{{TARGET_2}}` | `{{REALIZATION_DATE_2}}` | `{{BENEFIT_OWNER_2}}` |

Benefit type: `{{BENEFIT_TYPE}}` (Financial / Operational / Strategic / Social / Risk reduction)

## Expected Dis-benefits

PRINCE2 2023 mandates dis-benefits alongside benefits for a balanced business case. Dis-benefits are measurable negative outcomes that result from this initiative — not risks, but expected and accepted negative consequences (e.g., transition disruption, temporary productivity loss, decommissioning costs).

| Dis-benefit ID | Description | Metric | Baseline | Expected Value | Timeframe | Owner |
|---|---|---|---|---|---|---|
| `{{DISBENEFIT_ID_1}}` | `{{DISBENEFIT_DESC_1}}` | `{{DISBENEFIT_METRIC_1}}` | `{{DISBENEFIT_BASELINE_1}}` | `{{DISBENEFIT_VALUE_1}}` | `{{DISBENEFIT_TIMEFRAME_1}}` | `{{DISBENEFIT_OWNER_1}}` |
| `{{DISBENEFIT_ID_2}}` | `{{DISBENEFIT_DESC_2}}` | `{{DISBENEFIT_METRIC_2}}` | `{{DISBENEFIT_BASELINE_2}}` | `{{DISBENEFIT_VALUE_2}}` | `{{DISBENEFIT_TIMEFRAME_2}}` | `{{DISBENEFIT_OWNER_2}}` |

## Timescale

PRINCE2 2023 requires an explicit timescale section separate from the investment appraisal.

| Milestone | Target Date | Notes |
|---|---|---|
| Project start | `{{PROJECT_START_DATE}}` | |
| First benefit realisation | `{{FIRST_BENEFIT_DATE}}` | `{{FIRST_BENEFIT_NOTES}}` |
| Full benefits realisation | `{{FULL_BENEFITS_DATE}}` | `{{FULL_BENEFITS_NOTES}}` |
| Project close | `{{PROJECT_CLOSE_DATE}}` | |

Overall duration: `{{PROJECT_DURATION}}`

## Investment Appraisal

| Item | Amount | Notes |
|---|---|---|
| Development cost | `{{DEVELOPMENT_COST}}` | `{{DEVELOPMENT_COST_NOTES}}` |
| Infrastructure cost | `{{INFRA_COST}}` | `{{INFRA_COST_NOTES}}` |
| Ongoing operational cost | `{{OPEX}}` / year | `{{OPEX_NOTES}}` |
| **Total cost (Year 1)** | `{{TOTAL_COST_Y1}}` | |
| **Total cost (3-year)** | `{{TOTAL_COST_3Y}}` | |
| **Expected NPV** | `{{NPV}}` | Discount rate: `{{DISCOUNT_RATE}}`% |
| **Expected ROI** | `{{ROI}}`% | Payback period: `{{PAYBACK_PERIOD}}` |
| **Break-even** | `{{BREAK_EVEN_DATE}}` | |

## Key Risks

| Risk | Likelihood | Impact | Mitigation | Effect on Business Case |
|---|---|---|---|---|
| `{{BC_RISK_1}}` | `{{BC_RISK_1_L}}` | `{{BC_RISK_1_I}}` | `{{BC_RISK_1_MITIGATION}}` | `{{BC_RISK_1_EFFECT}}` |
| `{{BC_RISK_2}}` | `{{BC_RISK_2_L}}` | `{{BC_RISK_2_I}}` | `{{BC_RISK_2_MITIGATION}}` | `{{BC_RISK_2_EFFECT}}` |

## Key Assumptions

| Assumption | Owner | Risk if Wrong | Validation Method |
|---|---|---|---|
| `{{BC_ASSUMPTION_1}}` | `{{BC_ASSUMPTION_1_OWNER}}` | `{{BC_ASSUMPTION_1_RISK}}` | `{{BC_ASSUMPTION_1_VALIDATION}}` |

## Approval

| Decision | Approver | Date | Conditions |
|---|---|---|---|
| Approved to proceed | `{{APPROVER}}` | `{{APPROVAL_DATE}}` | `{{APPROVAL_CONDITIONS}}` |

## Source Attribution

- Source manifests: `project__pmi.md`, `project__prince2.md`
- Primary source basis: PMI and PRINCE2 business justification guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
