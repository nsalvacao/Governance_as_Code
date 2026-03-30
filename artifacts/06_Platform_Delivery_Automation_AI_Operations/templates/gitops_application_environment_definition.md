---
title: GitOps Application / Environment Definition
artifact_type: template
status: public
visibility: public
classification: public
owner: platform-governance
review_cadence: quarterly
applies_to: repositories that manage declarative applications or environments
source_basis: OpenGitOps, Flux, and Argo CD application definition guidance
source_manifests:
  - platform__gitops.md
alignment_mode: direct-adaptation
updated: 2026-03-30
---

# GitOps Application / Environment Definition

## Definition Metadata

| Field | Value |
|---|---|
| Application Name | `{{APPLICATION_NAME}}` |
| Environment | `{{ENVIRONMENT_NAME}}` |
| GitOps Controller | `{{GITOPS_CONTROLLER}}` (Flux CD / Argo CD / `{{OTHER_CONTROLLER}}`) |
| Definition Version | `{{DEFINITION_VERSION}}` |
| Owner | `{{OWNER}}` |
| Last Updated | `{{LAST_UPDATED}}` |

## OpenGitOps Principles Compliance

This definition implements the four OpenGitOps v1.0 principles:

| Principle | Implementation |
|---|---|
| **Declarative** | All desired state declared in `{{STATE_MANIFEST_PATH}}` |
| **Versioned and immutable** | State stored in `{{SOURCE_REPO}}` branch `{{SOURCE_BRANCH}}` at commit `{{PINNED_COMMIT}}` |
| **Pulled automatically** | `{{GITOPS_CONTROLLER}}` polls `{{POLL_INTERVAL}}` or uses webhook trigger |
| **Continuously reconciled** | Drift detected and corrected within `{{RECONCILIATION_INTERVAL}}` |

## Source Configuration

| Property | Value |
|---|---|
| Source Repository | `{{SOURCE_REPO}}` |
| Branch / Tag | `{{SOURCE_BRANCH}}` |
| Path / Chart | `{{SOURCE_PATH}}` |
| Revision Policy | `{{REVISION_POLICY}}` (pin to tag / follow branch / semver range: `{{SEMVER_RANGE}}`) |

## Sync Policy

| Property | Value |
|---|---|
| Sync Mode | `{{SYNC_MODE}}` (Automated / Manual) |
| Self-heal | `{{SELF_HEAL}}` (enabled / disabled) |
| Prune | `{{PRUNE}}` (remove resources not in source: enabled / disabled) |
| Force apply | `{{FORCE_APPLY}}` |
| Retry on failure | `{{RETRY_POLICY}}` (e.g., backoff: 5s, 60s, max 3 attempts) |
| Sync windows (allowed) | `{{SYNC_WINDOWS}}` (e.g., Mon–Fri 06:00–22:00 UTC) |

## Health Checks

| Resource | Health Rule | Pass Criteria |
|---|---|---|
| `{{RESOURCE_1}}` (e.g., Deployment) | `{{HEALTH_RULE_1}}` | `{{HEALTH_PASS_1}}` (e.g., all pods ready, rollout complete) |
| `{{RESOURCE_2}}` (e.g., Service) | `{{HEALTH_RULE_2}}` | `{{HEALTH_PASS_2}}` |

## Parameters and Overrides

| Parameter | Value | Override Source |
|---|---|---|
| `{{PARAM_1_NAME}}` | `{{PARAM_1_VALUE}}` | `{{PARAM_1_SOURCE}}` (inline / ConfigMap / Secret / Helm values) |
| `{{PARAM_2_NAME}}` | `{{PARAM_2_VALUE}}` | `{{PARAM_2_SOURCE}}` |

## Notification and Alerting

| Event | Notification Channel | Recipient |
|---|---|---|
| Sync failure | `{{SYNC_FAIL_CHANNEL}}` | `{{SYNC_FAIL_RECIPIENT}}` |
| Health degraded | `{{HEALTH_ALERT_CHANNEL}}` | `{{HEALTH_ALERT_RECIPIENT}}` |
| Drift detected | `{{DRIFT_CHANNEL}}` | `{{DRIFT_RECIPIENT}}` |
| Sync succeeded | `{{SYNC_SUCCESS_CHANNEL}}` | `{{SYNC_SUCCESS_RECIPIENT}}` |

## Access and Security

| Property | Value |
|---|---|
| Deployment identity | `{{DEPLOYMENT_SERVICE_ACCOUNT}}` |
| RBAC permissions | `{{RBAC_PERMISSIONS}}` |
| Image pull secret | `{{IMAGE_PULL_SECRET}}` |
| Network policy | `{{NETWORK_POLICY}}` |

## Source Attribution

- Source manifests: `platform__gitops.md`
- Primary source basis: OpenGitOps, Flux, and Argo CD application definition guidance
- Alignment mode: direct-adaptation
- Reviewed on: 2026-03-30
