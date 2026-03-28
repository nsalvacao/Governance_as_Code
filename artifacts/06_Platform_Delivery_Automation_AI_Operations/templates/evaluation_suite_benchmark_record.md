---
title: Evaluation Suite / Benchmark Record
artifact_type: template
status: public-draft
visibility: public
classification: public
owner: platform-governance
review_cadence: quarterly
applies_to: AI and model evaluation workflows
source_basis: OpenAI and Microsoft evaluation guidance
source_manifests:
  - ai_ops__openai_docs.md
  - platform__microsoft_learn.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

# Evaluation Suite / Benchmark Record

## Evaluation Suite Metadata

| Field | Value |
|---|---|
| Suite Name | `{{SUITE_NAME}}` |
| Suite Version | `{{SUITE_VERSION}}` |
| Owner | `{{OWNER}}` |
| Model / System Under Test | `{{SUBJECT}}` |
| Model Version | `{{MODEL_VERSION}}` |
| Evaluation Date | `{{EVALUATION_DATE}}` |
| Evaluator | `{{EVALUATOR}}` (human / automated / hybrid) |
| Run ID | `{{EVAL_RUN_ID}}` |

## Task Definition

| Field | Value |
|---|---|
| Task Type | `{{TASK_TYPE}}` (e.g., classification, generation, retrieval, ranking, safety) |
| Task Description | `{{TASK_DESCRIPTION}}` |
| Input Format | `{{INPUT_FORMAT}}` |
| Output Format | `{{OUTPUT_FORMAT}}` |
| Evaluation Prompt Template | `{{EVAL_PROMPT_TEMPLATE}}` (or link: `{{EVAL_PROMPT_LINK}}`) |

## Dataset

| Field | Value |
|---|---|
| Evaluation Dataset | `{{EVAL_DATASET_NAME}}` |
| Dataset Version | `{{EVAL_DATASET_VERSION}}` |
| Dataset Size | `{{EVAL_DATASET_SIZE}}` samples |
| Dataset Split | `{{EVAL_SPLIT}}` |
| Datasheet | `{{DATASET_RECORD_LINK}}` |

## Metrics and Thresholds

| Metric | Type | Baseline Score | Threshold | Actual Score | Pass? | Notes |
|---|---|---|---|---|---|---|
| `{{METRIC_1}}` | `{{METRIC_1_TYPE}}` (automated/human) | `{{BASELINE_SCORE_1}}` | `{{THRESHOLD_1}}` | `{{ACTUAL_SCORE_1}}` | `{{PASS_1}}` | `{{METRIC_1_NOTES}}` |
| `{{METRIC_2}}` | `{{METRIC_2_TYPE}}` | `{{BASELINE_SCORE_2}}` | `{{THRESHOLD_2}}` | `{{ACTUAL_SCORE_2}}` | `{{PASS_2}}` | `{{METRIC_2_NOTES}}` |
| `{{SAFETY_METRIC}}` | Human review | `{{SAFETY_BASELINE}}` | ≤ `{{SAFETY_THRESHOLD}}` harm rate | `{{SAFETY_ACTUAL}}` | `{{SAFETY_PASS}}` | |

Regression threshold: fail if any metric regresses by > `{{REGRESSION_THRESHOLD}}`% relative to baseline.

## Evaluation Methodology

| Property | Value |
|---|---|
| Sampling strategy | `{{SAMPLING_STRATEGY}}` |
| Confidence interval | `{{CONFIDENCE_INTERVAL}}` |
| Statistical test | `{{STATISTICAL_TEST}}` |
| Human rater instructions | `{{RATER_INSTRUCTIONS_LINK}}` |
| Inter-rater reliability | `{{IRR_METRIC}}` = `{{IRR_VALUE}}` |
| Judge model (if applicable) | `{{JUDGE_MODEL}}` at temperature `{{JUDGE_TEMPERATURE}}` |

## Results Summary

| Field | Value |
|---|---|
| Overall Pass / Fail | `{{OVERALL_RESULT}}` |
| Metrics passed | `{{METRICS_PASSED}}` / `{{TOTAL_METRICS}}` |
| Safety checks passed | `{{SAFETY_CHECKS_PASSED}}` |
| Regression detected | `{{REGRESSION_DETECTED}}` (Yes / No) |

## Evaluation Artifacts

| Artifact | Location |
|---|---|
| Raw results file | `{{RAW_RESULTS_LINK}}` |
| Evaluation script | `{{EVAL_SCRIPT_LINK}}` |
| Human annotation data | `{{ANNOTATION_DATA_LINK}}` |
| CI/CD integration | `{{CI_EVAL_WORKFLOW_LINK}}` |

## Source Attribution

- Source manifests: `ai_ops__openai_docs.md`, `platform__microsoft_learn.md`
- Primary source basis: evaluation and benchmark guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
