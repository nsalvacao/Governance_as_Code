---
title: CI/CD Policy
artifact_type: policy
status: draft
visibility: public
classification: public
owner: platform-governance
review_cadence: quarterly
applies_to: repositories using build, test, release, or deployment automation
source_basis: DORA State of DevOps Research (Accelerate book) + GitHub Actions
source_manifests:
  - governance__github_docs.md
  - platform__microsoft_learn.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

# CI/CD Policy

## Policy Purpose and Scope

This policy defines how automated build, test, release, and deployment flows must behave in repositories that opt into the platform library. It is grounded in the DORA four key metrics (Accelerate) and GitHub Actions platform controls. All pipelines must be deterministic, observable, and reversible.

## DORA Performance Targets as Policy Gates

DORA four key metrics are treated as enforceable policy gates. Teams must declare their tier and configure their pipelines to meet or exceed the corresponding targets.

| Metric | Placeholder | Elite | High | Medium | Low |
|---|---|---|---|---|---|
| Deployment Frequency | `{{TARGET_DEPLOY_FREQ}}` | On-demand (multiple/day) | Weekly | Monthly | 6-monthly |
| Lead Time for Changes | `{{TARGET_LEAD_TIME}}` | < 1 hour | < 1 week | 1–6 months | > 6 months |
| Mean Time to Restore (MTTR) | `{{TARGET_MTTR}}` | < 1 hour | < 1 day | < 1 week | > 6 months |
| Change Failure Rate | `{{TARGET_CFR}}` | 0–15% | 16–30% | 16–30% | 16–30% |

Declare the target tier for this repository as `{{DORA_TARGET_TIER}}`. Pipeline configuration must satisfy the targets for that tier.

## CI Requirements

Every commit must trigger CI automatically — no manual dispatch for standard validation flows.

- All automated tests must pass before a branch is eligible for merge.
- Security scanning is required on every CI run using `{{SECURITY_SCAN_TOOL}}` (e.g., CodeQL, Trivy, Snyk). Failures at severity `{{SCAN_FAIL_THRESHOLD}}` block merge.
- Linting and static analysis must run as mandatory CI steps.
- CI must run in an isolated, ephemeral environment; no shared mutable state between runs.

## CD Requirements

Continuous Delivery applies to the target environment declared as `{{CD_TARGET_ENV}}`.

- Automated deployment to `{{CD_TARGET_ENV}}` is triggered on merge to the primary branch.
- A manual approval gate is required before deployment to `{{MANUAL_GATE_ENV}}` (typically production). Configure this as a GitHub Actions environment protection rule.
- Deployment must be atomic and support rollback within `{{ROLLBACK_TIMEOUT}}` of a failed health check.

## Branch Protection Rules

Branch protection must be configured on the default branch and any release branches.

- Required status checks before merge: `{{REQUIRED_CHECK_1}}`, `{{REQUIRED_CHECK_2}}`, `{{REQUIRED_CHECK_N}}` (enumerate all checks that must pass).
- Minimum required reviewers: `{{MIN_REVIEWERS}}` (recommend ≥ 1 for standard branches, ≥ 2 for release branches).
- Dismiss stale reviews on new commits: enabled.
- Require signed commits where the team has signing infrastructure in place.

## Pipeline Failure Handling

Pipeline failures must be surfaced and tracked, not silently ignored.

- Failures must generate an alert to `{{PIPELINE_ALERT_CHANNEL}}` (e.g., Slack channel, email group, PagerDuty service).
- Maximum automatic retries for transient failures: `{{MAX_RETRIES}}` (recommend ≤ 3; beyond this, manual investigation is required).
- Flaky tests must be tracked and resolved within the sprint; flakiness rate must stay below `{{FLAKINESS_THRESHOLD}}`.

## Artifact Retention Policy

Built artifacts must be retained according to the following schedule.

- Retention period: `{{ARTIFACT_RETENTION}}` (e.g., 30 days for PR artifacts, 90 days for release artifacts, indefinite for signed production releases).
- Artifacts linked to a production deployment must not be purged while that deployment is active.
- Artifact digests must be recorded in the build provenance record (see `artifact_build_provenance_record.md`).

## Source Attribution

- Source manifests: `governance__github_docs.md`, `platform__microsoft_learn.md`
- Primary source basis: DORA State of DevOps Research (Accelerate book) + GitHub Actions
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
