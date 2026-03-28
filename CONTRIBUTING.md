---
title: Contribution Guidelines
artifact_type: policy
status: public
visibility: public
classification: public
owner: repository-maintainer
review_cadence: quarterly
applies_to: this repository
source_basis: GitHub Docs + Open Source Guides
source_manifests:
  - governance__github_docs.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

# Contribution Guidelines

Contributions to this repository must respect one core distinction:

- root files and `/.github/` are the concrete instance of this repository;
- reusable assets belong under `artifacts/`.

## Before you start

1. Check [`decision_log.md`](./decision_log.md) and the [`Public Document Map`](./README.md#public-document-map) section in the README for the current rules and target corpus.
2. Decide whether your change affects the repository instance or the reusable artifact library.
3. Run `python scripts/validate_governance_artifacts.py` locally before opening a pull request.

## Editing rules

- Edit `artifacts/` when the change should be reusable by downstream repositories.
- Edit the repository root or `/.github/` only when the behavior of **this** repository should change.
- Do not introduce unresolved placeholders into root instance files.
- Keep source attribution intact and update it when the governing source basis changes.

## Pull request expectations

1. Use [`.github/PULL_REQUEST_TEMPLATE.md`](./.github/PULL_REQUEST_TEMPLATE.md).
2. Explain whether the change affects the repository instance, the reusable library, or both.
3. Describe any follow-up required for downstream repositories.
4. Merge only after validation passes.

## Source Attribution

- Source manifests: [`governance__github_docs.md`](./sources/manifests/governance__github_docs.md)
- Primary source basis: GitHub Docs + Open Source Guides
- Alignment mode: `hybrid-synthesis`
- Reviewed on: 2026-03-27
