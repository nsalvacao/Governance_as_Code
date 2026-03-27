---
title: MLOps / GenAIOps Policy
artifact_type: policy
status: draft
visibility: public
classification: public
owner: platform-governance
review_cadence: quarterly
applies_to: repositories that build, evaluate, deploy, or monitor models or prompts
source_basis: Microsoft Learn and Google Cloud model operations guidance
source_manifests:
  - platform__microsoft_learn.md
  - platform__aws_well_architected.md
  - ai_ops__openai_docs.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

# MLOps / GenAIOps Policy

## Rules

- Track model, dataset, prompt, and evaluation assets as versioned artifacts.
- Require repeatable evaluation before release or promotion.
- Preserve lineage from source data to serving configuration.
- Separate experimentation from approved production assets.
- Define explicit safety and governance checks for AI-assisted workflows.

## Required controls

| Control | Expectation |
|---|---|
| Registry | Versioned and owned |
| Evaluation | Repeatable and comparable |
| Release | Traceable and approval-aware |
| Monitoring | Drift, quality, and safety signals |
| Safety | Guardrails and escalation paths |

## Source Attribution

- Source manifests: `platform__microsoft_learn.md`, `platform__aws_well_architected.md`, `ai_ops__openai_docs.md`
- Primary source basis: cloud model operations guidance and AI operations guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
