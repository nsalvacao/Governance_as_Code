---
title: Model Monitoring / Drift Report
artifact_type: template
status: public-draft
visibility: public
classification: public
owner: platform-governance
review_cadence: quarterly
applies_to: repositories that monitor deployed models or AI systems
source_basis: Microsoft and Google model monitoring guidance
source_manifests:
  - platform__microsoft_learn.md
  - platform__aws_well_architected.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

# Model Monitoring / Drift Report

## Report Metadata

| Field | Value |
|---|---|
| Model / System | `{{SUBJECT}}` |
| Model Version | `{{MODEL_VERSION}}` |
| Observation Window | `{{WINDOW_START}}` to `{{WINDOW_END}}` |
| Report Date | `{{REPORT_DATE}}` |
| Owner | `{{OWNER}}` |
| Status | `{{STATUS}}` (No drift / Drift warning / Drift alert / Model replaced) |

## Data Drift Analysis

Data drift occurs when the distribution of input data shifts relative to the reference (training) distribution.

| Feature | Reference Distribution | Current Distribution | Drift Metric | Drift Score | Threshold | Alert? |
|---|---|---|---|---|---|---|
| `{{FEATURE_1}}` | `{{FEATURE_1_REF_DIST}}` | `{{FEATURE_1_CURRENT_DIST}}` | `{{FEATURE_1_METRIC}}` (PSI / KS / KL) | `{{FEATURE_1_SCORE}}` | `{{DRIFT_THRESHOLD}}` | `{{FEATURE_1_ALERT}}` |
| `{{FEATURE_2}}` | `{{FEATURE_2_REF_DIST}}` | `{{FEATURE_2_CURRENT_DIST}}` | `{{FEATURE_2_METRIC}}` | `{{FEATURE_2_SCORE}}` | `{{DRIFT_THRESHOLD}}` | `{{FEATURE_2_ALERT}}` |

**PSI interpretation**: 0–0.1: no drift; 0.1–0.2: moderate drift (investigate); >0.2: severe drift (retrain)

Overall data drift score: `{{OVERALL_DATA_DRIFT_SCORE}}` — `{{OVERALL_DATA_DRIFT_INTERPRETATION}}`

## Concept Drift / Prediction Quality

Concept drift occurs when the relationship between inputs and outputs changes.

| Metric | Reference Value | Current Value | Change | Threshold | Alert? |
|---|---|---|---|---|---|
| `{{PREDICTION_METRIC_1}}` (e.g., accuracy) | `{{REF_PRED_1}}` | `{{CURR_PRED_1}}` | `{{CHANGE_PRED_1}}` | Δ ≤ `{{PRED_DRIFT_THRESHOLD_1}}` | `{{PRED_ALERT_1}}` |
| `{{PREDICTION_METRIC_2}}` (e.g., F1 score) | `{{REF_PRED_2}}` | `{{CURR_PRED_2}}` | `{{CHANGE_PRED_2}}` | Δ ≤ `{{PRED_DRIFT_THRESHOLD_2}}` | `{{PRED_ALERT_2}}` |
| Prediction distribution | `{{REF_PRED_DIST}}` | `{{CURR_PRED_DIST}}` | PSI: `{{PRED_PSI}}` | > `{{DRIFT_THRESHOLD}}` | `{{PRED_DIST_ALERT}}` |

## Model Performance (with ground truth, if available)

| Metric | Reference | Current | Acceptable Range | Status |
|---|---|---|---|---|
| `{{PERF_METRIC_1}}` | `{{REF_PERF_1}}` | `{{CURR_PERF_1}}` | `{{PERF_RANGE_1}}` | `{{PERF_STATUS_1}}` |
| `{{PERF_METRIC_2}}` | `{{REF_PERF_2}}` | `{{CURR_PERF_2}}` | `{{PERF_RANGE_2}}` | `{{PERF_STATUS_2}}` |

Ground truth lag: `{{GROUND_TRUTH_LAG}}` (delay between prediction and label availability)

## Serving Performance Signals

| Signal | Threshold | Observation | Alert? |
|---|---|---|---|
| Prediction latency P99 | ≤ `{{LATENCY_THRESHOLD}}` ms | `{{LATENCY_OBSERVATION}}` ms | `{{LATENCY_ALERT}}` |
| Error rate | ≤ `{{ERROR_RATE_THRESHOLD}}`% | `{{ERROR_RATE_OBSERVATION}}`% | `{{ERROR_RATE_ALERT}}` |
| Throughput | ≥ `{{THROUGHPUT_THRESHOLD}}` RPS | `{{THROUGHPUT_OBSERVATION}}` RPS | `{{THROUGHPUT_ALERT}}` |
| `{{CUSTOM_SIGNAL_1}}` | `{{CUSTOM_THRESHOLD_1}}` | `{{CUSTOM_OBSERVATION_1}}` | `{{CUSTOM_ALERT_1}}` |

## Recommended Actions

| Condition | Recommended Action | Owner | Trigger |
|---|---|---|---|
| PSI > 0.2 on `{{N_FEATURES}}` features | Investigate data pipeline; schedule retraining | `{{DATA_OWNER}}` | Automated |
| Performance regression > `{{PERF_REGRESSION_THRESHOLD}}`% | Retrain with recent data; compare with challenger model | `{{MODEL_OWNER}}` | Alert |
| Serving error rate > `{{ERROR_RATE_THRESHOLD}}`% | Roll back to `{{PREVIOUS_VERSION}}`; open incident | `{{OPS_OWNER}}` | Automated rollback |

## Current Recommendation

**Action**: `{{RECOMMENDED_ACTION}}` (No action / Investigate / Schedule retraining / Emergency rollback)

**Rationale**: `{{ACTION_RATIONALE}}`

**Owner**: `{{ACTION_OWNER}}`

**Due by**: `{{ACTION_DUE_DATE}}`

## Source Attribution

- Source manifests: `platform__microsoft_learn.md`, `platform__aws_well_architected.md`
- Primary source basis: model monitoring and drift guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
