---
title: AI Safety / Guardrail Policy
artifact_type: policy
status: draft
visibility: public
classification: public
owner: platform-governance
review_cadence: quarterly
applies_to: AI systems, prompts, evaluations, and model-serving workflows
source_basis: OpenAI and Microsoft AI safety guidance
source_manifests:
  - ai_ops__openai_docs.md
  - platform__microsoft_learn.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

# AI Safety / Guardrail Policy

## Rules

- Apply explicit safety checks to prompts, models, outputs, and workflows.
- Define prohibited or restricted use cases where applicable.
- Use evaluation and monitoring to detect regressions in safety behavior.
- Keep escalation and review paths visible for unsafe or unexpected outputs.
- Prefer least-privilege access for model operations, datasets, and prompt registries.

## Safety controls

- Prompt policy: `{{PROMPT_POLICY_LINK}}`
- Evaluation threshold: `{{EVALUATION_THRESHOLD}}`
- Human review: `{{HUMAN_REVIEW_RULE}}`
- Escalation path: `{{ESCALATION_PATH}}`

## Source Attribution

- Source manifests: `ai_ops__openai_docs.md`, `platform__microsoft_learn.md`
- Primary source basis: OpenAI and Microsoft AI safety guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
