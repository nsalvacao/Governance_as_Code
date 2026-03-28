# Gemini Automation Overview

This file is the provider-specific public note for Gemini-related automation patterns.

## Canonical policy

Follow the repository-wide rules in [`AI_AGENT_POLICY.md`](./AI_AGENT_POLICY.md).

## Repository stance

- Gemini automation is **not** currently active in the root workflow surface of this repository instance.
- Reusable Gemini workflow patterns are preserved in the library under [`artifacts/06_Platform_Delivery_Automation_AI_Operations/workflows/gemini/`](./artifacts/06_Platform_Delivery_Automation_AI_Operations/workflows/gemini/).
- Reusable Gemini prompt and command contracts are preserved under [`artifacts/06_Platform_Delivery_Automation_AI_Operations/templates/ai_automation/gemini/`](./artifacts/06_Platform_Delivery_Automation_AI_Operations/templates/ai_automation/gemini/).
- Downstream repositories may activate those patterns explicitly when they provide the required configuration, trust boundaries, and human review model.

## Notes

- The active root workflow surface of this repository is intentionally kept deterministic and minimal.
- Detailed runtime heuristics remain out of the public root surface.

## Source Attribution

- Source manifests: `governance__github_docs.md`, `ai_ops__openai_docs.md`
- Primary source basis: GitHub Actions governance patterns and public-safe AI automation guidance
- Alignment mode: `guided-synthesis`
- Reviewed on: 2026-03-28
