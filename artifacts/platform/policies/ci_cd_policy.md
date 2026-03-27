---
title: CI/CD Policy
artifact_type: policy
status: draft
visibility: public
classification: public
owner: platform-governance
review_cadence: quarterly
applies_to: repositories using build, test, release, or deployment automation
source_basis: GitHub Actions and platform deployment guidance
source_manifests:
  - governance__github_docs.md
  - platform__microsoft_learn.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

# CI/CD Policy

## Scope

This policy defines how automated build, test, release, and deployment flows should behave in repositories that opt into the platform library.

## Rules

- Prefer deterministic, repeatable workflows.
- Keep promotion steps explicit and reviewable.
- Separate validation from deployment where practical.
- Require traceable approvals, environment controls, and rollback paths for production changes.
- Use repository variables, environments, and secrets for runtime differences instead of hard-coded values.

## Required controls

| Control | Expectation |
|---|---|
| Build | Repeatable and scriptable |
| Test | Automated before promotion |
| Release | Observable and traceable |
| Deployment | Environment-aware and reversible |
| Auditability | Pipeline run, commit, and artifact linkage |

## Source Attribution

- Source manifests: `governance__github_docs.md`, `platform__microsoft_learn.md`
- Primary source basis: GitHub Actions and Microsoft deployment guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
