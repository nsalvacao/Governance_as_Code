---
title: Test Strategy and Verification Policy
artifact_type: standard
status: public-draft
visibility: public
classification: public
owner: quality-platform
review_cadence: quarterly
applies_to: validation strategy, verification expectations, and quality gates
source_basis: Microsoft Learn testing guidance; Google SRE verification and reliability practices
source_manifests:
  - platform__microsoft_learn.md
  - operations__google_sre.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Purpose

Define how a repository should verify changes and what evidence is sufficient to accept them.

## Policy

- Require automated validation for the artifact library and repository-instance files.
- Prefer repeatable checks that can run locally and in CI.
- Treat manual verification as supplementary unless automation is impossible.
- Record the testing scope, method, and outcome in the change artifact.

## Canonical relationship

- The implementation-level validator lives in `artifacts/conventions/scripts/validate_governance_artifacts.py`.
- This standard explains the verification model that the validator supports.

## Source Attribution

- Source manifests: `platform__microsoft_learn.md`, `operations__google_sre.md`
- Primary source basis: Microsoft testing guidance and Google SRE verification practices
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
