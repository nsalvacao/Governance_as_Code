---
title: Model Monitoring / Drift Report
artifact_type: template
status: draft
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

## Monitoring summary

- Model or system: `{{SUBJECT}}`
- Observation window: `{{WINDOW}}`
- Owner: `{{OWNER}}`
- Status: `{{STATUS}}`

## Signals

| Signal | Threshold | Observation |
|---|---|---|
| `{{SIGNAL_NAME}}` | `{{THRESHOLD}}` | `{{OBSERVATION}}` |

## Source Attribution

- Source manifests: `platform__microsoft_learn.md`, `platform__aws_well_architected.md`
- Primary source basis: model monitoring and drift guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
