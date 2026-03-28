---
title: Benefits Review / Benefits Realization Record
artifact_type: template
status: public-draft
visibility: public
classification: public
owner: GOVERNANCE
review_cadence: quarterly
applies_to: benefit tracking and realization review
source_basis: PMI, PRINCE2
source_manifests:
  - project__pmi.md
  - project__prince2.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

# Benefits Review / Benefits Realization Record

## Purpose

Track whether expected benefits were achieved and sustained, providing traceability from the original business case to realized value (PMI Benefits Realization Management + PRINCE2 2023 Benefits Review).

## Record Metadata

| Field | Value |
|---|---|
| Record ID | `{{BENEFITS_RECORD_ID}}` |
| Project / Programme | `{{PROJECT_NAME}}` |
| Business Case Reference | `{{BUSINESS_CASE_LINK}}` |
| Record Owner | `{{BENEFITS_OWNER}}` |
| Review Date | `{{REVIEW_DATE}}` |
| Next Review | `{{NEXT_REVIEW_DATE}}` |

## Benefits Register

| Benefit ID | Benefit Description | Benefit Type | Baseline Value | Target Value | Actual Value | Variance | Realization Status | Benefit Owner | Measurement Method | Review Date | Follow-up Action |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `{{BENEFIT_ID_1}}` | `{{BENEFIT_DESC_1}}` | `{{BENEFIT_TYPE_1}}` | `{{BASELINE_1}}` | `{{TARGET_1}}` | `{{ACTUAL_1}}` | `{{VARIANCE_1}}` | `{{STATUS_1}}` | `{{OWNER_1}}` | `{{METHOD_1}}` | `{{REVIEW_DATE_1}}` | `{{ACTION_1}}` |
| `{{BENEFIT_ID_2}}` | `{{BENEFIT_DESC_2}}` | `{{BENEFIT_TYPE_2}}` | `{{BASELINE_2}}` | `{{TARGET_2}}` | `{{ACTUAL_2}}` | `{{VARIANCE_2}}` | `{{STATUS_2}}` | `{{OWNER_2}}` | `{{METHOD_2}}` | `{{REVIEW_DATE_2}}` | `{{ACTION_2}}` |

## Benefit Types

| Code | Type | Description |
|---|---|---|
| FIN | Financial | Revenue increase, cost reduction, ROI |
| OPS | Operational | Efficiency gain, process improvement, throughput |
| STR | Strategic | Market position, competitive advantage, capability |
| RIS | Risk reduction | Lower probability or impact of known risks |
| REG | Regulatory / compliance | Meeting legal or regulatory obligations |
| SOC | Social / reputational | Brand value, community impact, employee satisfaction |

## Realization Status Definitions

| Status | Description |
|---|---|
| Planned | Benefit expected but not yet measurable |
| On track | Measurement trend consistent with target |
| Partially realized | Benefit achieved below target — `{{PARTIAL_THRESHOLD}}`% of target |
| Fully realized | Target met or exceeded |
| Not realized | Target not met and recovery is not forecast |
| Superseded | Benefit replaced by a revised or more relevant outcome |

## Consolidated View

| Summary Metric | Value |
|---|---|
| Total benefits targeted (NPV) | `{{TOTAL_TARGETED_NPV}}` |
| Total benefits realized to date (NPV) | `{{TOTAL_REALIZED_NPV}}` |
| % of benefits realized | `{{PCT_REALIZED}}`% |
| Benefits on track | `{{ON_TRACK_COUNT}}` |
| Benefits at risk | `{{AT_RISK_COUNT}}` |
| Benefits not realized | `{{NOT_REALIZED_COUNT}}` |

## Recommendations

`{{BENEFITS_REVIEW_RECOMMENDATIONS}}`

**Decision required**: `{{DECISION_REQUIRED}}` (e.g., extend programme, re-baseline, close)

## Source Attribution

- Source manifests: `project__pmi.md`, `project__prince2.md`
- Primary source basis: PMI and PRINCE2 benefits realization guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
