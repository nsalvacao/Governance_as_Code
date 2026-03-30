---
title: Error Budget Policy
artifact_type: policy
status: public
visibility: public
classification: public
owner: reliability-platform
review_cadence: semiannual
applies_to: services with defined SLOs
source_basis: Google SRE Example Error Budget Policy
source_manifests: operations__google_sre.md
alignment_mode: direct-adaptation
updated: 2026-03-30
---

## Objective

Keep reliability commitments explicit, responses deterministic, and SLO negotiations grounded in data (Google SRE Book Ch.6).

## SLI and SLO Definitions

| Service | SLI Definition | SLI Type | SLO Target | Measurement Window |
|---|---|---|---|---|
| `{{SERVICE_NAME}}` | `{{SLI_DEFINITION}}` (e.g., proportion of HTTP requests returning 2xx in < 500 ms) | Request-based | `{{SLO_TARGET}}`% (e.g., 99.9%) | `{{MEASUREMENT_WINDOW}}` (e.g., rolling 28 days) |

Error Budget = 1 − SLO = `{{ERROR_BUDGET_PERCENT}}`% of requests/time allowed to fail per window.

For `{{SLO_TARGET}}`% SLO over 28 days: error budget = `{{ERROR_BUDGET_MINUTES}}` minutes of downtime.

## Burn Rate Alerts

Multi-window, multi-burn-rate alerting (Google SRE Workbook Ch.5):

| Alert Name | Burn Rate Threshold | Short Window | Long Window | Severity | Paging? |
|---|---|---|---|---|---|
| `{{SERVICE_NAME}}`-critical | `{{FAST_BURN_RATE}}`× (e.g., 14.4×) | 5 minutes | 1 hour | SEV1 | Yes — immediate page |
| `{{SERVICE_NAME}}`-high | `{{SLOW_BURN_RATE}}`× (e.g., 6×) | 30 minutes | 6 hours | SEV2 | Yes — business hours |
| `{{SERVICE_NAME}}`-warning | `{{WARNING_BURN_RATE}}`× (e.g., 1×) | 6 hours | 3 days | SEV3 | No — ticket only |

At `{{FAST_BURN_RATE}}`× burn rate: `{{FAST_BURN_BUDGET_HOURS}}` hours until budget exhausted.

## Error Budget Consumption Policy

| Budget Consumed | Response Required | Freeze Releases? |
|---|---|---|
| 0–50% | Normal operations, monitor | No |
| 50–75% | Engineering review with `{{RELIABILITY_LEAD}}` | No — but flag to engineering manager |
| 75–100% | Incident review; prioritise reliability work over features | No new risky releases |
| > 100% (exhausted) | Reliability freeze activated; only reliability-improving changes merge | **Yes** — freeze all non-reliability work |

Reliability freeze activated by: `{{FREEZE_AUTHORITY}}` (e.g., SRE lead or service owner).
Freeze lifted by: `{{FREEZE_LIFT_CRITERIA}}` (e.g., budget recovers to ≥ 25% with 7-day stable trend).

## Feature Release Gate

When error budget is below `{{FEATURE_GATE_THRESHOLD}}`% (e.g., 25%):

- Product Manager `{{PM_CONTACT}}` and Engineering Lead `{{ENG_LEAD_CONTACT}}` must jointly approve new feature releases.
- Release is only permitted if the change is expected to improve or not affect reliability.
- All releases during budget-below-threshold periods are logged in `{{RELEASE_LOG_LOCATION}}`.

## Postmortem Trigger

A postmortem MUST be filed when:

- Any single incident consumes more than `{{POSTMORTEM_TRIGGER_BUDGET_PCT}}`% of the monthly error budget
- Error budget is exhausted at any point in the measurement window
- A SEV1 or SEV2 incident occurs regardless of budget consumption

Postmortem deadline: `{{POSTMORTEM_DEADLINE}}` business days after incident resolution.

## Review Cadence

| Review Type | Frequency | Owner | Agenda |
|---|---|---|---|
| Error budget dashboard | Weekly | `{{WEEKLY_REVIEWER}}` | Check burn rate trend, upcoming release risk |
| SLO review | `{{SLO_REVIEW_CADENCE}}` (e.g., monthly) | `{{SLO_REVIEW_OWNER}}` | SLO target validation, SLI query accuracy |
| SLO renegotiation | Annually | `{{SLO_NEGOTIATION_OWNER}}` | Adjust targets based on business + technical evidence |

## Source Attribution

- Source manifests: `operations__google_sre.md`
- Primary source basis: Google SRE Example Error Budget Policy
- Alignment mode: direct-adaptation
- Reviewed on: 2026-03-30
