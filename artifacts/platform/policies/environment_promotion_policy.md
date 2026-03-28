---
title: Environment Promotion Policy
artifact_type: policy
status: draft
visibility: public
classification: public
owner: platform-governance
review_cadence: quarterly
applies_to: repositories that promote changes across multiple environments
source_basis: GitHub environment and platform promotion guidance
source_manifests:
  - governance__github_docs.md
  - platform__microsoft_learn.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

# Environment Promotion Policy

## Policy Purpose

This policy defines the rules and gates that govern how a versioned artifact moves from one deployment environment to the next. It applies progressive delivery principles: promotion is earned, not assumed. Every stage must satisfy its gate criteria before the artifact advances.

## Environment Stages

Define all environment stages in the promotion chain. Each stage must have an explicit purpose and declared promotion criteria.

| Stage | Name | Purpose | Promotion Criteria |
|---|---|---|---|
| 1 | `{{STAGE_1}}` | Development validation — fast feedback for developers | `{{PROMO_CRITERIA_1}}` |
| 2 | `{{STAGE_2}}` | Integration and regression testing | `{{PROMO_CRITERIA_2}}` |
| N | `{{STAGE_N}}` | Declare additional stages as required by the project | `{{PROMO_CRITERIA_N}}` |

## Promotion Pipeline

The canonical promotion path is:

```
dev → {{STAGING_ENV}} → {{CANARY_ENV}} → {{PRODUCTION_ENV}}
```

Skipping stages is prohibited except under a documented emergency procedure. Each hop must be traceable to a pull request or approved promotion event.

## Promotion Gate Criteria

### Automated Gates

The following checks must pass automatically before a promotion can proceed. Failing an automated gate blocks promotion without exception.

- `{{AUTO_GATE_1}}` (e.g., all CI tests pass, coverage threshold met)
- `{{AUTO_GATE_2}}` (e.g., security scan result below severity threshold)
- `{{AUTO_GATE_N}}` (add gates as required per stage)

### Manual Approval Gates

Manual approval by a designated reviewer is required before promotion to `{{MANUAL_GATE_ENV}}`. Configure this as a GitHub Actions environment protection rule with named required reviewers.

- Approval must be recorded in the promotion audit log.
- Approver must not be the same person who authored the change (four-eyes principle).

## Rollback Policy

Every promotion must have a tested rollback path.

- Automatic rollback is triggered by: `{{AUTO_ROLLBACK_TRIGGER}}` (e.g., health check failures ≥ threshold, error rate spike, deployment timeout).
- Rollback must complete within: `{{ROLLBACK_TIMEOUT}}` (e.g., `5m`, `15m`).
- If automatic rollback fails, the on-call engineer is paged and a manual rollback procedure is initiated.

## Environment Parity Requirements

Environments positioned as production-like (staging, canary, production) must maintain parity in the following dimensions to prevent drift masking bugs.

- Parity requirements: `{{PARITY_REQUIREMENTS}}` (e.g., same container base images, same infrastructure tier, equivalent network topology, mirrored secrets rotation schedule).
- Parity gaps must be documented as known exceptions with an associated risk acceptance.

## Configuration Drift Prevention

Drift between environment configurations must be detected and remediated.

- Drift prevention tool: `{{DRIFT_PREVENTION_TOOL}}` (e.g., Flux reconciler, Argo CD sync, Terraform plan diff in CI).
- Detected drift must trigger an alert and a remediation PR within the SLA defined in the GitOps policy.

## Promotion Audit Log

Every promotion event must be recorded for traceability and compliance.

- Audit log location: `{{AUDIT_LOG_LOCATION}}` (e.g., GitHub Actions run history, a dedicated audit table, a SIEM integration).
- Each log entry must capture: artifact version, source stage, target stage, gate results, approver identity, and timestamp.

## Source Attribution

- Source manifests: `governance__github_docs.md`, `platform__microsoft_learn.md`
- Primary source basis: GitHub environments and Microsoft promotion guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
