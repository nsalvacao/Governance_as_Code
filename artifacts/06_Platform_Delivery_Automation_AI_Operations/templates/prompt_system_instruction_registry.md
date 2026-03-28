---
title: Prompt / System Instruction Registry
artifact_type: template
status: public-draft
visibility: public
classification: public
owner: platform-governance
review_cadence: quarterly
applies_to: repositories that manage prompts or system instructions
source_basis: OpenAI prompt management and Microsoft AI guidance
source_manifests:
  - ai_ops__openai_docs.md
  - platform__microsoft_learn.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

# Prompt / System Instruction Registry

## Registry Entry Metadata

| Field | Value |
|---|---|
| Prompt ID | `{{PROMPT_ID}}` (e.g., PRO-2026-0042) |
| Prompt Name | `{{PROMPT_NAME}}` |
| Version | `{{PROMPT_VERSION}}` |
| Status | `{{PROMPT_STATUS}}` (Draft / Review / Active / Deprecated) |
| Owner | `{{OWNER}}` |
| Created | `{{CREATED_DATE}}` |
| Last Updated | `{{LAST_UPDATED}}` |
| Approved By | `{{APPROVER}}` |

## Model Target

| Field | Value |
|---|---|
| Primary Model | `{{PRIMARY_MODEL}}` (e.g., claude-3-5-sonnet, gpt-4o) |
| Compatible Models | `{{COMPATIBLE_MODELS}}` |
| Incompatible Models | `{{INCOMPATIBLE_MODELS}}` (models that produce unreliable results) |
| API Format | `{{API_FORMAT}}` (e.g., OpenAI Chat Completions, Anthropic Messages) |

## Prompt Configuration

| Parameter | Value | Notes |
|---|---|---|
| Temperature | `{{TEMPERATURE}}` | Controls randomness; 0 = deterministic |
| Top-p | `{{TOP_P}}` | Nucleus sampling threshold |
| Max tokens | `{{MAX_TOKENS}}` | Maximum output length |
| Stop sequences | `{{STOP_SEQUENCES}}` | |
| System prompt | Stored at `{{SYSTEM_PROMPT_LINK}}` | See below |

## System Prompt (or link to versioned file)

```
{{SYSTEM_PROMPT_INLINE_OR_LINK}}
```

Note: System prompts are stored in version-controlled files at `{{PROMPT_STORAGE_LOCATION}}`. Link here; do NOT store volatile prompt text directly in this record.

## User Prompt Template

```
{{USER_PROMPT_TEMPLATE}}
```

Variables used in template: `{{TEMPLATE_VARIABLES}}` (e.g., `{{USER_INPUT}}`, `{{CONTEXT}}`, `{{EXAMPLES}}`)

## Intended Use

**Primary use cases**: `{{PRIMARY_USE_CASES}}`

**Allowed environments**: `{{ALLOWED_ENVIRONMENTS}}` (e.g., production API, internal tooling, research only)

**Prohibited uses**: `{{PROHIBITED_USES}}`

## Safety and Guardrails

| Guardrail | Implemented? | Method |
|---|---|---|
| Input validation | `{{INPUT_VALIDATION_STATUS}}` | `{{INPUT_VALIDATION_METHOD}}` |
| Output filtering | `{{OUTPUT_FILTER_STATUS}}` | `{{OUTPUT_FILTER_METHOD}}` |
| PII detection | `{{PII_DETECTION_STATUS}}` | `{{PII_DETECTION_TOOL}}` |
| Harmful content detection | `{{HARM_DETECTION_STATUS}}` | `{{HARM_DETECTION_TOOL}}` |
| Prompt injection resistance | `{{INJECTION_RESISTANCE_STATUS}}` | `{{INJECTION_RESISTANCE_METHOD}}` |

Safety review: `{{SAFETY_REVIEW_LINK}}`

## Evaluation

| Metric | Threshold | Actual | Evaluation Suite |
|---|---|---|---|
| `{{EVAL_METRIC_1}}` | `{{EVAL_THRESHOLD_1}}` | `{{EVAL_ACTUAL_1}}` | `{{EVAL_SUITE_LINK}}` |
| Harmful output rate | ≤ `{{HARM_RATE_THRESHOLD}}`% | `{{HARM_RATE_ACTUAL}}`% | |

## Change Log

| Version | Date | Author | Summary of Changes |
|---|---|---|---|
| `{{VERSION_1}}` | `{{DATE_1}}` | `{{AUTHOR_1}}` | `{{CHANGES_1}}` |
| `{{VERSION_2}}` | `{{DATE_2}}` | `{{AUTHOR_2}}` | `{{CHANGES_2}}` |

## Source Attribution

- Source manifests: `ai_ops__openai_docs.md`, `platform__microsoft_learn.md`
- Primary source basis: prompt and system instruction management guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
