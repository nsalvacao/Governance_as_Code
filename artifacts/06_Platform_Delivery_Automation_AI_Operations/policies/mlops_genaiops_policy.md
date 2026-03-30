---
title: MLOps / GenAIOps Policy
artifact_type: policy
status: public
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
updated: 2026-03-30
---

# MLOps / GenAIOps Policy

## Scope

This policy applies to all repositories that build, evaluate, deploy, or monitor:

- Classical ML models (supervised, unsupervised, reinforcement learning)
- Generative AI models (LLMs, diffusion, multimodal)
- AI-assisted workflows where model output influences production decisions
- Prompt templates and system instructions used in production

## MLOps Maturity Levels (Microsoft MLOps Maturity Model)

| Level | Characteristics | Gate to Progress |
|---|---|---|
| 0 — Manual | Experiments in notebooks; no tracking; manual deployment | `{{L0_TO_L1_GATE}}` |
| 1 — ML Pipelines | Automated training; model registry; manual deployment | `{{L1_TO_L2_GATE}}` |
| 2 — Automated Training + Deployment | CI/CD triggers retraining; automated promotion; monitoring | `{{L2_TO_L3_GATE}}` |
| 3 — Full MLOps | Continuous training, deployment, and monitoring; closed-loop feedback | Ongoing |

Current maturity target: **Level `{{TARGET_MATURITY_LEVEL}}`**

## Asset Lifecycle Requirements

### Model Assets

| Stage | Requirements | Approval |
|---|---|---|
| Experimentation | Logged in `{{EXPERIMENT_TRACKER}}`; dataset version recorded | None — research only |
| Staging | Evaluation suite passed; model card complete; registry entry created | `{{STAGING_APPROVER}}` |
| Production | PRR complete; safety review passed; serving SLO defined | `{{PRODUCTION_APPROVER}}` |
| Deprecated | Serving traffic = 0; monitoring disabled; registry status updated | `{{DEPRECATION_APPROVER}}` |

### Dataset Assets

- All training and evaluation datasets MUST have a Datasheet record (see `artifacts/06_Platform_Delivery_Automation_AI_Operations/templates/dataset_training_data_record.md`)
- Dataset version used for each model training run MUST be pinned and logged in `{{LINEAGE_TRACKER}}`
- PII and sensitive data MUST be identified, documented, and handled per `{{DATA_GOVERNANCE_POLICY}}`

### Prompt / System Instruction Assets

- All production prompts MUST be registered in the Prompt Registry (see `artifacts/06_Platform_Delivery_Automation_AI_Operations/templates/prompt_system_instruction_registry.md`)
- Prompt changes follow the same change management process as code changes
- Prompt evaluation is required before promotion; results logged in `{{PROMPT_EVAL_TRACKER}}`

## Required Controls

| Control | Requirement | Verification |
|---|---|---|
| Model Registry | Every production model version registered with model card | `{{REGISTRY_VERIFICATION}}` |
| Evaluation | Evaluation suite run before each promotion; metrics compared to `{{BASELINE_SOURCE}}` | `{{EVAL_VERIFICATION}}` |
| Lineage | Source data → training → model → serving chain traceable end-to-end | `{{LINEAGE_VERIFICATION}}` |
| Continuous Training | Retraining triggered by: data drift PSI > `{{DRIFT_TRIGGER_THRESHOLD}}`, schedule `{{RETRAINING_SCHEDULE}}`, or performance regression | `{{RETRAINING_VERIFICATION}}` |
| Monitoring | Data drift, concept drift, prediction quality, and latency monitored post-deployment | `{{MONITORING_VERIFICATION}}` |
| Safety | AI safety guardrails applied per `artifacts/06_Platform_Delivery_Automation_AI_Operations/policies/ai_safety_guardrail_policy.md` | `{{SAFETY_VERIFICATION}}` |

## Experiment and Production Separation

- Experimentation occurs in `{{EXPERIMENT_ENVIRONMENT}}` only — never in production namespaces
- Promotion to staging requires: `{{STAGING_PROMOTION_CRITERIA}}`
- Promotion to production requires: `{{PRODUCTION_PROMOTION_CRITERIA}}`
- Emergency rollback SLA: `{{EMERGENCY_ROLLBACK_SLA}}`

## Governance Cadences

| Review | Frequency | Owner | Output |
|---|---|---|---|
| Model performance review | `{{MODEL_REVIEW_CADENCE}}` | `{{MODEL_REVIEW_OWNER}}` | Drift report + action items |
| Dataset freshness review | `{{DATASET_REVIEW_CADENCE}}` | `{{DATA_OWNER}}` | Retraining trigger or confirmation |
| Safety guardrail review | `{{SAFETY_REVIEW_CADENCE}}` | `{{SAFETY_OFFICER}}` | Guardrail effectiveness report |
| Policy review | Quarterly | `{{POLICY_OWNER}}` | Updated policy version |

## Source Attribution

- Source manifests: `platform__microsoft_learn.md`, `platform__aws_well_architected.md`, `ai_ops__openai_docs.md`
- Primary source basis: cloud model operations guidance and AI operations guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-30
