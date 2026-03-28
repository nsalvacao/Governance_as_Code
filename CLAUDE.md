# Claude Code Public Guidance

This file is the provider-specific public note for Claude Code and similar coding agents.

## Canonical policy

Follow the repository-wide rules in [`AI_AGENT_POLICY.md`](./AI_AGENT_POLICY.md).

## Provider note

- treat the root repository files as the live instance and `artifacts/` as the reusable library;
- preserve traceability and source attribution in any public change;
- run `python3 scripts/validate_governance_artifacts.py` before proposing merge-ready work.

Detailed internal orchestration heuristics are intentionally not published here.

## Source Attribution

- Source manifests: `governance__github_docs.md`
- Primary source basis: GitHub Docs repository guidance and public contribution patterns
- Alignment mode: `guided-synthesis`
- Reviewed on: 2026-03-28
