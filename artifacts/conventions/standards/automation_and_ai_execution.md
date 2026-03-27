---
title: Automation and AI Execution
artifact_type: normative
status: draft
visibility: public
classification: public-redacted
owner: governance@org
review_cadence: quarterly
applies_to: repositories using automation hooks or AI agents
source_basis: documentation__diataxis, platform__aws_well_architected, platform__microsoft_learn, ai_ops__openai_docs
source_manifests: documentation__diataxis.md, platform__aws_well_architected.md, platform__microsoft_learn.md, ai_ops__openai_docs.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

# Automation and AI Execution

This document is a reusable library standard. It governs how downstream repositories should describe and operate automation and AI-assisted flows when they instantiate assets from this repository.

## Intent

Ensure deterministic, GitHub-native automation and AI agent execution by documenting triggers, parameters, and guardrails for each governance artifact.

## Automation signals

- Every automation mix must describe:
  - Triggering event (e.g., `workflow_dispatch`, `issue_comment`, `pull_request`).
  - Input parameters (`{{UPPER_SNAKE_CASE}}`) and defaults.
  - Expected outputs (e.g., validation comment, checklist update).
  - Downstream actions (e.g., `{{GOVERNANCE_VALIDATION_WORKFLOW}}`).

- Link automation descriptions to `artifacts/conventions/templates/partials/source_attribution.md` so attribution travels with results.
- Preface platform-native scripts (Actions, Python, etc.) with “Deterministic step:” statements summarizing the deterministic inputs and outputs.

## AI agents

- Document the surface that agents may read or write, such as:
  - Frontmatter schema hooking (`artifacts/conventions/schemas/frontmatter.schema.json`).
  - `source_manifests` and `alignment_mode` fields for verification.
- Provide guidance for how agents should interpret placeholders, e.g., “Replace `{{PROJECT_NAME}}` before instantiating the template.”
- State the fallback behavior when AI detects missing data (e.g., “If `{{SERVICE_AREA}}` is unknown, tag as `requires human` and stop before committing changes”).
- Outline the verification obligation (e.g., “Agents must run `python scripts/validate_governance_artifacts.py` locally before merging; `.github/workflows/validate-governance-artifacts.yml` enforces the same checks in CI”).

## Selective applicability

- Call out automation and AI rules only for repositories where the workflow is enabled (`{{AUTOMATION_ENABLED}}` flag).
- Documents can note optional parameters and gating fields that downstream repos can flip.

## Source Attribution

- Source manifests: documentation__diataxis.md, platform__aws_well_architected.md, platform__microsoft_learn.md, ai_ops__openai_docs.md
- Primary source basis: Diataxis editorial model, AWS/Microsoft automation guidance, OpenAI AI ops guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
