---
title: Model Release / Serving Record
artifact_type: template
status: public
visibility: public
classification: public
owner: platform-governance
review_cadence: quarterly
applies_to: repositories that release or serve AI models
source_basis: Microsoft and Google model serving guidance
source_manifests:
  - platform__microsoft_learn.md
  - platform__aws_well_architected.md
alignment_mode: hybrid-synthesis
updated: 2026-03-30
---

# Model Release / Serving Record

## Release Metadata

| Field | Value |
|---|---|
| Model Name | `{{MODEL_NAME}}` |
| Model Version | `{{MODEL_VERSION}}` |
| Release ID | `{{RELEASE_ID}}` |
| Serving Environment | `{{SERVING_ENVIRONMENT}}` |
| Release Owner | `{{OWNER}}` |
| Release Date | `{{RELEASE_DATE}}` |
| Status | `{{STATUS}}` (Staged / Active / Shadow / Canary / Deprecated) |
| Approver | `{{APPROVER}}` |

## Pre-Release Checks

| Check | Required | Status | Evidence |
|---|---|---|---|
| Evaluation suite passed | Yes | `{{EVAL_STATUS}}` | `{{EVAL_LINK}}` |
| Model card complete | Yes | `{{MODEL_CARD_STATUS}}` | `{{MODEL_CARD_LINK}}` |
| Safety guardrail review | Yes | `{{SAFETY_STATUS}}` | `{{SAFETY_REVIEW_LINK}}` |
| Production readiness review | Yes | `{{PRR_STATUS}}` | `{{PRR_LINK}}` |
| Dataset compliance verified | Yes | `{{DATASET_COMPLIANCE_STATUS}}` | `{{DATASET_RECORD_LINK}}` |
| A/B test / shadow mode results | `{{AB_TEST_REQUIRED}}` | `{{AB_TEST_STATUS}}` | `{{AB_TEST_LINK}}` |

## Serving Configuration

| Property | Value |
|---|---|
| Endpoint URL | `{{ENDPOINT}}` |
| Model server | `{{MODEL_SERVER}}` (e.g., TorchServe, Triton, vLLM, `{{CUSTOM_SERVER}}`) |
| Serving framework | `{{SERVING_FRAMEWORK}}` |
| Instance type | `{{INSTANCE_TYPE}}` |
| Min instances | `{{MIN_INSTANCES}}` |
| Max instances | `{{MAX_INSTANCES}}` |
| Scaling trigger | `{{SCALING_TRIGGER}}` (e.g., CPU > `{{CPU_THRESHOLD}}`%, requests > `{{RPS_THRESHOLD}}` RPS) |
| Concurrency limit | `{{CONCURRENCY_LIMIT}}` |
| Timeout | `{{SERVING_TIMEOUT}}` ms |

## Traffic Management

| Traffic Split | Model Version | Percentage | Notes |
|---|---|---|---|
| Production | `{{PROD_MODEL_VERSION}}` | `{{PROD_PCT}}`% | Current champion |
| Canary / Shadow | `{{CANARY_MODEL_VERSION}}` | `{{CANARY_PCT}}`% | `{{CANARY_NOTES}}` |

Traffic routing mechanism: `{{TRAFFIC_ROUTING_MECHANISM}}` (e.g., Istio weight, feature flag, A/B service)

## SLO Targets

| Metric | Target | Alert Threshold |
|---|---|---|
| Prediction latency P50 | ≤ `{{LATENCY_P50_TARGET}}` ms | `{{LATENCY_P50_ALERT}}` ms |
| Prediction latency P99 | ≤ `{{LATENCY_P99_TARGET}}` ms | `{{LATENCY_P99_ALERT}}` ms |
| Availability | ≥ `{{AVAILABILITY_TARGET}}`% | < `{{AVAILABILITY_ALERT}}`% |
| Error rate | ≤ `{{ERROR_RATE_TARGET}}`% | > `{{ERROR_RATE_ALERT}}`% |
| Model quality metric | `{{QUALITY_METRIC}}` ≥ `{{QUALITY_TARGET}}` | < `{{QUALITY_ALERT}}` |

## Rollback Plan

| Field | Value |
|---|---|
| Rollback Trigger | `{{ROLLBACK_TRIGGER}}` (automatic on SLO breach / manual) |
| Previous Stable Version | `{{PREVIOUS_VERSION}}` |
| Rollback Mechanism | `{{ROLLBACK_MECHANISM}}` |
| Rollback SLA | `{{ROLLBACK_SLA}}` |
| Rollback Owner | `{{ROLLBACK_OWNER}}` |

## Monitoring

| Signal | Tool | Alert Destination |
|---|---|---|
| Prediction drift | `{{DRIFT_TOOL}}` | `{{DRIFT_ALERT_DEST}}` |
| Serving latency | `{{LATENCY_TOOL}}` | `{{LATENCY_ALERT_DEST}}` |
| Error rate | `{{ERROR_RATE_TOOL}}` | `{{ERROR_RATE_ALERT_DEST}}` |
| Feature distribution | `{{FEATURE_MONITOR_TOOL}}` | `{{FEATURE_ALERT_DEST}}` |

Drift report cadence: `{{DRIFT_REPORT_CADENCE}}` — template at `artifacts/06_Platform_Delivery_Automation_AI_Operations/templates/model_monitoring_drift_report.md`

## Source Attribution

- Source manifests: `platform__microsoft_learn.md`, `platform__aws_well_architected.md`
- Primary source basis: model serving guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-30
