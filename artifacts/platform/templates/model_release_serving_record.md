---
title: Model Release / Serving Record
artifact_type: template
status: draft
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
updated: 2026-03-27
---

# Model Release / Serving Record

## Release summary

- Model: `{{MODEL_NAME}}`
- Version: `{{MODEL_VERSION}}`
- Serving environment: `{{SERVING_ENVIRONMENT}}`
- Release owner: `{{OWNER}}`
- Release status: `{{STATUS}}`

## Serving details

| Field | Value |
|---|---|
| Endpoint | `{{ENDPOINT}}` |
| Scaling policy | `{{SCALING_POLICY}}` |
| Rollback path | `{{ROLLBACK_PATH}}` |

## Source Attribution

- Source manifests: `platform__microsoft_learn.md`, `platform__aws_well_architected.md`
- Primary source basis: model serving guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
