---
title: Dataset / Training Data Record
artifact_type: template
status: public-draft
visibility: public
classification: public
owner: platform-governance
review_cadence: quarterly
applies_to: repositories that train or evaluate models on data
source_basis: Microsoft and Google dataset lineage guidance
source_manifests:
  - platform__microsoft_learn.md
  - platform__aws_well_architected.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

# Dataset / Training Data Record

## Datasheet (Gebru et al. 2021 — Datasheets for Datasets)

### Motivation

| Question | Answer |
|---|---|
| Purpose | `{{DATASET_PURPOSE}}` — why was this dataset created? |
| Creator | `{{DATASET_CREATOR}}` |
| Funder / sponsor | `{{DATASET_FUNDER}}` |
| Dataset name | `{{DATASET_NAME}}` |
| Version | `{{DATASET_VERSION}}` |
| Owner | `{{OWNER}}` |
| Date created | `{{CREATION_DATE}}` |
| Status | `{{DATASET_STATUS}}` (Active / Frozen / Deprecated) |

### Composition

| Field | Value |
|---|---|
| Instances represent | `{{INSTANCE_DESCRIPTION}}` (e.g., text documents, images, tabular records) |
| Total instances | `{{TOTAL_INSTANCES}}` |
| Splits | Train: `{{TRAIN_SIZE}}` / Validation: `{{VAL_SIZE}}` / Test: `{{TEST_SIZE}}` |
| Feature count | `{{FEATURE_COUNT}}` |
| Label types | `{{LABEL_TYPES}}` |
| Missing data | `{{MISSING_DATA_DESCRIPTION}}` |
| Confidential data present | `{{CONFIDENTIAL_DATA}}` (Yes / No — if Yes: `{{CONFIDENTIAL_DATA_HANDLING}}`) |
| PII present | `{{PII_PRESENT}}` (Yes / No — if Yes: handled per `{{PII_POLICY_LINK}}`) |

### Collection Process

| Field | Value |
|---|---|
| Collection method | `{{COLLECTION_METHOD}}` (e.g., web scraping, sensors, human annotation, synthetic generation) |
| Collection window | `{{COLLECTION_WINDOW}}` |
| Source location(s) | `{{SOURCE_LOCATION}}` |
| Was consent obtained | `{{CONSENT_OBTAINED}}` (Yes / No / N/A — if N/A: `{{CONSENT_RATIONALE}}`) |
| Notification policy | `{{NOTIFICATION_POLICY}}` |
| Third-party data sources | `{{THIRD_PARTY_SOURCES}}` (Yes / No — if Yes: licenses at `{{LICENSE_LINKS}}`) |

### Preprocessing and Labelling

| Step | Description | Tool / Script |
|---|---|---|
| `{{PREPROCESSING_STEP_1}}` | `{{PREPROCESSING_DESC_1}}` | `{{PREPROCESSING_TOOL_1}}` |
| `{{PREPROCESSING_STEP_2}}` | `{{PREPROCESSING_DESC_2}}` | `{{PREPROCESSING_TOOL_2}}` |

Labelling method: `{{LABELLING_METHOD}}` (e.g., human annotation, programmatic, model-assisted)

Inter-annotator agreement: `{{IAA_METRIC}}` = `{{IAA_VALUE}}`

### Uses

**Appropriate uses**: `{{APPROPRIATE_USES}}`

**Uses that should be avoided**: `{{PROHIBITED_USES}}`

**Impact of misuse**: `{{MISUSE_IMPACT}}`

### Distribution

| Property | Value |
|---|---|
| License | `{{DATASET_LICENSE}}` |
| Distribution method | `{{DISTRIBUTION_METHOD}}` (internal only / open / restricted) |
| Access location | `{{ACCESS_LOCATION}}` |
| Access controls | `{{ACCESS_CONTROLS}}` |
| Export restrictions | `{{EXPORT_RESTRICTIONS}}` |

### Maintenance

| Property | Value |
|---|---|
| Maintained by | `{{MAINTAINER}}` |
| Update cadence | `{{UPDATE_CADENCE}}` |
| Known issues | `{{KNOWN_ISSUES}}` |
| Erratum | `{{ERRATUM_LINK}}` |
| Retention policy | `{{RETENTION_POLICY}}` |
| Deletion request contact | `{{DELETION_CONTACT}}` |

## Source Attribution

- Source manifests: `platform__microsoft_learn.md`, `platform__aws_well_architected.md`
- Primary source basis: dataset lineage guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
