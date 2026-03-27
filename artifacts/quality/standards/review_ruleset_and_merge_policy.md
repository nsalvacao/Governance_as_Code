---
title: Review Ruleset and Merge Policy
artifact_type: standard
status: public-draft
visibility: public
classification: public
owner: quality-platform
review_cadence: quarterly
applies_to: pull request review, merge rules, and exception handling
source_basis: GitHub Docs branch protection and rulesets guidance
source_manifests:
  - governance__github_docs.md
alignment_mode: direct-adaptation
updated: 2026-03-27
---

## Purpose

Define the quality gates that must pass before a change can merge.

## Policy

- Require at least one meaningful review for material changes.
- Require status checks for the repository validator and any domain-specific checks.
- Prefer small, reviewable pull requests.
- Document approved exceptions explicitly and keep them time-bound.

## Canonical relationship

- The GitHub-native enforcement surface is represented by the reusable assets under `artifacts/governance/templates/github-native/`.
- This standard is the quality-layer policy that explains why the rules exist and how they are applied.

## Source Attribution

- Source manifests: `governance__github_docs.md`
- Primary source basis: GitHub Docs branch protection and rulesets guidance
- Alignment mode: direct-adaptation
- Reviewed on: 2026-03-27
