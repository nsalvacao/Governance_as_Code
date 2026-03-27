---
title: Model Registry Record
artifact_type: template
status: draft
visibility: public
classification: public
owner: platform-governance
review_cadence: quarterly
applies_to: repositories that register models or model-like AI assets
source_basis: Microsoft and Google model registry guidance
source_manifests:
  - platform__microsoft_learn.md
  - platform__aws_well_architected.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

# Model Registry Record

## Model details

- Model name: `{{MODEL_NAME}}`
- Version: `{{MODEL_VERSION}}`
- Owner: `{{OWNER}}`
- Purpose: `{{PURPOSE}}`
- Status: `{{STATUS}}`

## Lineage

| Field | Value |
|---|---|
| Training source | `{{TRAINING_SOURCE}}` |
| Evaluation link | `{{EVALUATION_LINK}}` |
| Deployment link | `{{DEPLOYMENT_LINK}}` |

## Source Attribution

- Source manifests: `platform__microsoft_learn.md`, `platform__aws_well_architected.md`
- Primary source basis: model registry and lineage guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
