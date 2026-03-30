---
title: Release Plan / Rollout Plan Template
artifact_type: template
status: public
visibility: public
classification: public
owner: "{{DELIVERY_OWNER}}"
review_cadence: quarterly
applies_to: release planning and rollout execution
source_basis: DORA four key metrics and SRE Workbook progressive delivery
source_manifests:
  - operations__google_sre.md
  - governance__github_docs.md
alignment_mode: guided-synthesis
updated: 2026-03-30
---

## Release Plan - `{{RELEASE_ID}}`

This template combines DORA metrics baseline with SRE Workbook progressive delivery practices. Complete every section before the release window opens. Gate owners must sign off at each phase boundary.

---

### 1. Release Context

| Field | Value |
|---|---|
| Release ID | `{{RELEASE_ID}}` |
| Version | `{{VERSION}}` |
| Target environment | `{{TARGET_ENVIRONMENT}}` |
| Release owner | `{{RELEASE_OWNER}}` |
| Planned release date | `{{PLANNED_RELEASE_DATE}}` |
| Related change record | `{{CHANGE_RECORD_ID}}` |

The release ID links this plan to the change record, rollback plan, and post-implementation review. Target environment must be explicit (e.g. production-us-east-1, staging) — avoid ambiguous names.

---

### 2. DORA Baseline

Record DORA four key metrics as measured immediately before this release. Use these as the baseline for post-release comparison to detect regressions in engineering performance.

| Metric | Baseline value | Target / acceptable threshold |
|---|---|---|
| Deployment frequency | `{{DEPLOY_FREQUENCY}}` | `{{DEPLOY_FREQUENCY_TARGET}}` |
| Lead time for changes | `{{LEAD_TIME}}` | `{{LEAD_TIME_TARGET}}` |
| Mean time to restore (MTTR) | `{{MTTR}}` | `{{MTTR_TARGET}}` |
| Change failure rate | `{{CHANGE_FAIL_RATE}}` | `{{CHANGE_FAIL_RATE_TARGET}}` |

If baseline data is unavailable, state "not yet measured" and capture actuals post-release to establish the baseline. Elite performers target: deployment frequency multiple/day, lead time < 1 hour, MTTR < 1 hour, change failure rate 0–15%.

---

### 3. Rollout Strategy

**Selected strategy:** `{{ROLLOUT_STRATEGY}}`

| Strategy | Description | When to use |
|---|---|---|
| Canary | Route a small traffic percentage to the new version; expand on success | High-risk changes; large user bases |
| Blue-green | Maintain two identical environments; switch traffic atomically | Zero-downtime releases; easy rollback |
| Rolling | Replace instances incrementally; old and new versions coexist briefly | Stateless services; gradual exposure |
| Feature flag | Deploy code to all; enable progressively via feature toggles | Decoupled deploy and release; A/B testing |

Describe any hybrid approach in `{{ROLLOUT_STRATEGY_NOTES}}`. Feature flag deployments must reference the flag management system and list all flags being toggled.

---

### 4. Rollout Phases

Define each gate. The gate owner must explicitly approve progression before traffic is increased. Do not advance phases automatically.

| Phase | Traffic % | Duration | Success criteria | Gate owner |
|---|---|---|---|---|
| Phase 1 | `{{TRAFFIC_PCT_1}}` | `{{PHASE_DURATION_1}}` | `{{SUCCESS_CRITERIA_1}}` | `{{GATE_OWNER_1}}` |
| Phase 2 | `{{TRAFFIC_PCT_2}}` | `{{PHASE_DURATION_2}}` | `{{SUCCESS_CRITERIA_2}}` | `{{GATE_OWNER_2}}` |
| Phase 3 | `{{TRAFFIC_PCT_3}}` | `{{PHASE_DURATION_3}}` | `{{SUCCESS_CRITERIA_3}}` | `{{GATE_OWNER_3}}` |
| Full rollout | 100% | `{{PHASE_DURATION_FULL}}` | `{{SUCCESS_CRITERIA_FULL}}` | `{{GATE_OWNER_FULL}}` |

Success criteria must be objective and measurable (e.g. p99 latency < 200 ms, error rate < 0.1%, zero critical alerts). Phase durations must be long enough to collect statistically meaningful signal for the metric being monitored.

---

### 5. Monitoring During Rollout

List every metric and alert threshold that must be watched during rollout. On-call must have dashboard access before the release window opens.

| Metric | Alert threshold | Dashboard / tool |
|---|---|---|
| `{{METRIC_1}}` | `{{THRESHOLD_1}}` | `{{DASHBOARD_1}}` |
| `{{METRIC_2}}` | `{{THRESHOLD_2}}` | `{{DASHBOARD_2}}` |
| `{{METRIC_N}}` | `{{THRESHOLD_N}}` | `{{DASHBOARD_N}}` |

**On-call contact:** `{{ON_CALL_CONTACT}}`
**Alerting runbook:** `{{ALERTING_RUNBOOK_LINK}}`

---

### 6. Go / No-Go Decision Criteria

**Go criteria (all must be met to proceed with or advance a phase):**
`{{GO_CRITERIA}}`

| Criterion | Owner | Status before release |
|---|---|---|
| `{{GO_CRITERION_1}}` | `{{GO_CRITERION_OWNER_1}}` | [pending / confirmed] |
| `{{GO_CRITERION_2}}` | `{{GO_CRITERION_OWNER_2}}` | [pending / confirmed] |
| `{{GO_CRITERION_N}}` | `{{GO_CRITERION_OWNER_N}}` | [pending / confirmed] |

**No-go triggers (any one is sufficient to halt or roll back):**
- `{{NO_GO_TRIGGER_1}}`
- `{{NO_GO_TRIGGER_2}}`

Document the decision and the decision-maker in the change record when a go/no-go call is made.

---

### 7. Communication Plan

Notify stakeholders at each milestone. Use the change communication template for message content.

| Milestone | Audience | Channel | Timing | Owner |
|---|---|---|---|---|
| Release start | `{{STAKEHOLDER_1}}` | `{{CHANNEL_1}}` | `{{MILESTONE_TIMING_1}}` | `{{COMMS_OWNER_1}}` |
| Phase gate reached | `{{STAKEHOLDER_2}}` | `{{CHANNEL_2}}` | `{{MILESTONE_TIMING_2}}` | `{{COMMS_OWNER_2}}` |
| Full rollout complete | `{{STAKEHOLDER_3}}` | `{{CHANNEL_3}}` | `{{MILESTONE_TIMING_3}}` | `{{COMMS_OWNER_3}}` |
| Rollback initiated | `{{STAKEHOLDER_4}}` | `{{CHANNEL_4}}` | Immediately | `{{COMMS_OWNER_4}}` |

---

### 8. Rollback Plan

**Rollback trigger:** `{{ROLLBACK_TRIGGER}}`

The rollback trigger must be an objective, observable condition. On detection, the gate owner or on-call engineer initiates rollback without requiring additional approval.

**Rollback plan reference:** `{{ROLLBACK_PLAN_REFERENCE}}`

Ensure the rollback plan has been reviewed and the rollback procedure tested before the release window opens.

---

## Source Attribution

- Source manifests: `operations__google_sre.md`, `governance__github_docs.md`
- Primary source basis: DORA four key metrics and SRE Workbook progressive delivery
- Alignment mode: guided-synthesis
- Reviewed on: 2026-03-30
