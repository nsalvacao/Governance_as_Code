---
title: Model Registry Record
artifact_type: template
status: public
visibility: public
classification: public
owner: "{{PLATFORM_OWNER}}"
review_cadence: quarterly
applies_to: repositories that register models or model-like AI assets
source_basis: Microsoft and Google model registry guidance
source_manifests:
  - platform__microsoft_learn.md
  - platform__aws_well_architected.md
alignment_mode: hybrid-synthesis
updated: 2026-03-30
---

# Model Registry Record

## Model Card (Google Model Card 2.0 — Gebru et al. 2019/2022)

### Model Details

| Field | Value |
|---|---|
| Model Name | `{{MODEL_NAME}}` |
| Model Version | `{{MODEL_VERSION}}` |
| Model ID | `{{MODEL_ID}}` |
| Model Type | `{{MODEL_TYPE}}` (e.g., classification / regression / generative / embedding) |
| Architecture | `{{MODEL_ARCHITECTURE}}` (e.g., transformer, CNN, gradient boosting) |
| Framework | `{{ML_FRAMEWORK}}` (e.g., PyTorch `{{FRAMEWORK_VERSION}}`, scikit-learn) |
| Owner | `{{OWNER}}` |
| Status | `{{STATUS}}` (Experimental / Staging / Production / Deprecated) |
| Created | `{{CREATED_DATE}}` |
| Last Updated | `{{LAST_UPDATED}}` |
| Registry Location | `{{REGISTRY_LOCATION}}` |

### Intended Use

**Primary intended uses**: `{{PRIMARY_USE_CASES}}`

**Primary intended users**: `{{INTENDED_USERS}}`

**Out-of-scope use cases**: `{{OUT_OF_SCOPE_USES}}`

### Factors and Sensitive Attributes

Relevant factors that affect model performance:

| Factor | Description | Evaluation Coverage |
|---|---|---|
| `{{FACTOR_1}}` (e.g., demographic subgroup) | `{{FACTOR_1_DESC}}` | `{{FACTOR_1_COVERAGE}}` |
| `{{FACTOR_2}}` (e.g., geographic region) | `{{FACTOR_2_DESC}}` | `{{FACTOR_2_COVERAGE}}` |

### Metrics

| Metric | Evaluation Dataset | Threshold | Current Value | Pass? |
|---|---|---|---|---|
| `{{METRIC_1}}` (e.g., F1 score) | `{{EVAL_DATASET_1}}` | ≥ `{{THRESHOLD_1}}` | `{{VALUE_1}}` | `{{PASS_1}}` |
| `{{METRIC_2}}` (e.g., AUC-ROC) | `{{EVAL_DATASET_2}}` | ≥ `{{THRESHOLD_2}}` | `{{VALUE_2}}` | `{{PASS_2}}` |
| `{{FAIRNESS_METRIC}}` (e.g., equalized odds) | `{{FAIRNESS_DATASET}}` | `{{FAIRNESS_THRESHOLD}}` | `{{FAIRNESS_VALUE}}` | `{{FAIRNESS_PASS}}` |

### Evaluation Data

| Dataset | Split | Size | Date Range | Notes |
|---|---|---|---|---|
| `{{EVAL_DATASET_NAME}}` | `{{EVAL_SPLIT}}` | `{{EVAL_SIZE}}` | `{{EVAL_DATE_RANGE}}` | `{{EVAL_NOTES}}` |

Evaluation data differs from training data: `{{EVAL_TRAIN_DIFFERENCE}}`

### Training Data

| Dataset | Version | Size | Date Range | Datasheet |
|---|---|---|---|---|
| `{{TRAINING_DATASET_NAME}}` | `{{TRAINING_DATASET_VERSION}}` | `{{TRAINING_SIZE}}` | `{{TRAINING_DATE_RANGE}}` | `{{DATASET_RECORD_LINK}}` |

### Quantitative Analyses

Performance by subgroup (disaggregated evaluation):

| Subgroup | `{{METRIC_1}}` | `{{METRIC_2}}` | Notes |
|---|---|---|---|
| `{{SUBGROUP_1}}` | `{{SG1_M1}}` | `{{SG1_M2}}` | `{{SG1_NOTES}}` |
| `{{SUBGROUP_2}}` | `{{SG2_M1}}` | `{{SG2_M2}}` | `{{SG2_NOTES}}` |

### Ethical Considerations

- **Risks identified**: `{{ETHICAL_RISKS}}`
- **Mitigation strategies**: `{{MITIGATION_STRATEGIES}}`
- **Recommended safeguards**: `{{RECOMMENDED_SAFEGUARDS}}`
- **Use NOT recommended for**: `{{PROHIBITED_USES}}`

### Known Limitations

Model Card 2.0 (Gebru et al.) requires explicit documentation of known limitations. This section is non-optional: undisclosed limitations create fairness, safety, and compliance risk for downstream consumers of this model.

| Limitation ID | Description | Affected Inputs / Conditions | Severity | Mitigation / Workaround | Status |
|---|---|---|---|---|---|
| `{{LIMITATION_ID_1}}` | `{{LIMITATION_DESC_1}}` | `{{LIMITATION_CONDITION_1}}` | `{{LIMITATION_SEVERITY_1}}` (High / Medium / Low) | `{{LIMITATION_MITIGATION_1}}` | `{{LIMITATION_STATUS_1}}` (Known / Under investigation / Accepted) |
| `{{LIMITATION_ID_2}}` | `{{LIMITATION_DESC_2}}` | `{{LIMITATION_CONDITION_2}}` | `{{LIMITATION_SEVERITY_2}}` | `{{LIMITATION_MITIGATION_2}}` | `{{LIMITATION_STATUS_2}}` |

Common limitation categories to consider: distributional shift (model trained on data that doesn't represent deployment context), edge cases (inputs where model fails silently), demographic performance gaps (subgroup underperformance), language/locale gaps, temporal decay (model trained on stale data).

## Lineage and Traceability

| Field | Value |
|---|---|
| Training run ID | `{{TRAINING_RUN_ID}}` |
| Training data version | `{{TRAINING_DATASET_VERSION}}` |
| Training code commit | `{{TRAINING_CODE_COMMIT}}` |
| Training compute | `{{TRAINING_COMPUTE}}` |
| Evaluation suite | `{{EVALUATION_LINK}}` |
| Serving configuration | `{{DEPLOYMENT_LINK}}` |
| Experiment tracker | `{{EXPERIMENT_TRACKER_LINK}}` |

## Source Attribution

- Source manifests: `platform__microsoft_learn.md`, `platform__aws_well_architected.md`
- Primary source basis: model registry and lineage guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-30
