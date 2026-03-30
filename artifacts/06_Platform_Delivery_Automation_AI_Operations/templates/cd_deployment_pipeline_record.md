---
title: CD / Deployment Pipeline Record
artifact_type: template
status: public
visibility: public
classification: public
owner: platform-governance
review_cadence: quarterly
applies_to: repositories with automated deployment or promotion flows
source_basis: GitHub and Microsoft deployment automation guidance
source_manifests:
  - governance__github_docs.md
  - platform__microsoft_learn.md
alignment_mode: hybrid-synthesis
updated: 2026-03-30
---

# CD / Deployment Pipeline Record

## Deployment Metadata

| Field | Value |
|---|---|
| Deployment Name | `{{DEPLOYMENT_NAME}}` |
| Deployment ID | `{{DEPLOYMENT_ID}}` |
| Source Version / Tag | `{{SOURCE_VERSION}}` |
| Source Commit | `{{SOURCE_COMMIT}}` |
| Build ID | `{{BUILD_ID}}` |
| Pipeline Run | `{{WORKFLOW_RUN_LINK}}` |
| Repository | `{{REPOSITORY}}` |
| Trigger | `{{DEPLOYMENT_TRIGGER}}` (manual / automated promotion / schedule) |
| Initiated By | `{{INITIATED_BY}}` |
| Record Date | `{{RECORD_DATE}}` |

## Deployment Targets (Progressive Delivery — DORA / SRE Workbook)

| Stage | Environment | Promotion Criteria | Rollback Trigger | Approver |
|---|---|---|---|---|
| 1 | `{{STAGE_1_ENV}}` (e.g., dev) | `{{STAGE_1_PROMOTION_CRITERIA}}` | `{{STAGE_1_ROLLBACK_TRIGGER}}` | Auto |
| 2 | `{{STAGE_2_ENV}}` (e.g., staging) | `{{STAGE_2_PROMOTION_CRITERIA}}` | `{{STAGE_2_ROLLBACK_TRIGGER}}` | `{{STAGE_2_APPROVER}}` |
| 3 | `{{STAGE_3_ENV}}` (e.g., canary `{{CANARY_PCT}}`%) | Error rate ≤ `{{CANARY_ERROR_THRESHOLD}}`, latency ≤ `{{CANARY_LATENCY_THRESHOLD}}` for `{{CANARY_BAKE_TIME}}` | Any threshold breach | `{{CANARY_APPROVER}}` |
| 4 | `{{STAGE_4_ENV}}` (production — 100%) | Canary stable; approver sign-off | `{{PRODUCTION_ROLLBACK_TRIGGER}}` | `{{PRODUCTION_APPROVER}}` |

## Health Gates

Gates that MUST pass before promotion to next stage:

| Gate | Check | Pass Criteria | Fail Action |
|---|---|---|---|
| Smoke tests | `{{SMOKE_TEST_COMMAND}}` | All pass | Block promotion |
| Error rate | `{{ERROR_RATE_QUERY}}` | ≤ `{{ERROR_RATE_THRESHOLD}}`% | Block; alert `{{OPS_CONTACT}}` |
| Latency (P99) | `{{LATENCY_QUERY}}` | ≤ `{{LATENCY_THRESHOLD}}` ms | Block; alert `{{OPS_CONTACT}}` |
| Dependency health | `{{DEPENDENCY_HEALTH_CHECK}}` | All dependencies responsive | Block |
| Security scan | `{{SECURITY_GATE_CHECK}}` | No new critical/high | Block |

## Rollout Configuration

| Property | Value |
|---|---|
| Rollout Strategy | `{{ROLLOUT_STRATEGY}}` (Blue-Green / Canary / Rolling / Recreate) |
| Canary Increment | `{{CANARY_INCREMENT}}`% traffic every `{{CANARY_STEP_DURATION}}` |
| Max Unavailable | `{{MAX_UNAVAILABLE}}` |
| Max Surge | `{{MAX_SURGE}}` |
| Bake Time | `{{BAKE_TIME}}` at each canary step |

## Rollback Plan

| Field | Value |
|---|---|
| Rollback Trigger | `{{ROLLBACK_TRIGGER}}` (automatic on health gate failure / manual) |
| Rollback Mechanism | `{{ROLLBACK_MECHANISM}}` (redeploy previous version / GitOps revert / feature flag) |
| Previous Stable Version | `{{PREVIOUS_STABLE_VERSION}}` |
| Rollback SLA | `{{ROLLBACK_SLA}}` (target time to complete rollback) |
| Rollback Owner | `{{ROLLBACK_OWNER}}` |
| Post-rollback validation | `{{POST_ROLLBACK_VALIDATION}}` |

## Deployment Evidence

| Item | Link / Value |
|---|---|
| CI build artifact | `{{RELEASE_ARTIFACT_LINK}}` |
| SLSA provenance | `{{PROVENANCE_LINK}}` |
| Deployment workflow run | `{{WORKFLOW_RUN_LINK}}` |
| Post-deploy smoke test | `{{SMOKE_TEST_RESULTS_LINK}}` |
| Deployment duration | `{{DEPLOYMENT_DURATION}}` |
| DORA: Lead time for this change | `{{LEAD_TIME}}` |

## Final Status

| Field | Value |
|---|---|
| Deployment Status | `{{STATUS}}` (Success / Partial / Failed / Rolled Back) |
| Production deployed at | `{{PRODUCTION_DEPLOY_TIME}}` |
| Approver sign-off | `{{APPROVER}}` on `{{APPROVAL_DATE}}` |
| Change failure? | `{{CHANGE_FAILURE}}` (Yes / No) — if Yes, file incident `{{INCIDENT_LINK}}` |

## Source Attribution

- Source manifests: `governance__github_docs.md`, `platform__microsoft_learn.md`
- Primary source basis: GitHub and Microsoft deployment automation guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-30
