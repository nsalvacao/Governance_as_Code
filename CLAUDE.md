# Claude Code Public Guidance

This file is the public contribution guide for Claude Code and similar coding agents working in this repository.

## Purpose

- preserve the boundary between the repository instance and the reusable artifact library;
- keep changes publication-safe and attributable;
- run deterministic validation before proposing merge.

## Public rules

1. Treat root files and `/.github/` as the concrete behavior of this repository.
2. Treat `artifacts/` as the reusable library for downstream repositories.
3. Keep source attribution intact in Markdown, YAML, and workflow-facing assets.
4. Use `python3 scripts/validate_governance_artifacts.py` before proposing changes.
5. Prefer small, auditable changes over broad undocumented rewrites.

## Notes

- Detailed internal orchestration and execution heuristics are intentionally not published in this file.
- The public source of truth for repository behavior remains `README.md`, `decision_log.md`, `GOVERNANCE.md`, and the deterministic validator.

## Source Attribution

- Source manifests: `governance__github_docs.md`
- Primary source basis: GitHub Docs repository guidance and public contribution patterns
- Alignment mode: `guided-synthesis`
- Reviewed on: 2026-03-28
