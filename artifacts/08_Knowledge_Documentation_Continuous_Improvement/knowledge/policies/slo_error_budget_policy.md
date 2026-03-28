---
title: SLO and Error Budget Policy
artifact_type: policy
status: public-draft
visibility: public
classification: public
owner: knowledge-platform
review_cadence: quarterly
applies_to: services that define reliability objectives and error budgets
source_basis: Google SRE Book Chapter 6 Service Level Objectives
source_manifests:
  - operations__google_sre.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Policy Statement

Services that publish reliability commitments must define measurable SLOs, make their error budgets visible, and use budget consumption to govern change velocity and incident response decisions.

---

## SLI Definition

**Metric type:** request-based / window-based _(select one)_
**SLI formula:** {{SLI_FORMULA}}
**Measurement window:** {{MEASUREMENT_WINDOW}}

An SLI (Service Level Indicator) is a quantitative measure of a specific aspect of service behavior. Define the formula precisely enough for automated measurement. Example: `(successful_requests / total_requests) * 100` over a 30-day rolling window.

---

## SLO Target

**SLO:** {{SLO_TARGET}}

The SLO is the target value for the SLI. Express as a percentage (e.g., 99.9%). The target must reflect the actual reliability users need — not the maximum achievable, not an aspirational number. Overly tight SLOs consume error budget on routine operations; overly loose SLOs fail users silently.

---

## Error Budget Calculation

**Error budget:** 1 − SLO = {{ERROR_BUDGET_PCT}} of requests or time allowed to fail per measurement window.

Example: a 99.9% SLO on a 30-day window yields 43.8 minutes of allowed downtime or 0.1% of requests allowed to fail. Document the calculation explicitly so all stakeholders share the same baseline.

---

## Error Budget Consumption Tracking

**Current consumption:** {{CURRENT_CONSUMPTION}}
**Tracking dashboard:** {{DASHBOARD_LINK}}

Consumption must be visible to service owners, on-call engineers, and product managers at all times. The dashboard link is mandatory — invisible budgets cannot drive behavior change.

---

## Burn Rate Alerts

Burn rate measures how fast the error budget is being consumed relative to the normal rate (1× = exactly on track to exhaust by end of window).

| Alert type | Burn rate threshold | Window | Action |
|---|---|---|---|
| Fast burn | {{FAST_BURN_RATE}}× | {{FAST_BURN_WINDOW}} | Page on-call immediately |
| Slow burn | {{SLOW_BURN_RATE}}× | {{SLOW_BURN_WINDOW}} | Create ticket, review within 24 h |

Typical starting values: fast burn at 14.4× over 1 hour (consumes 2% of monthly budget); slow burn at 3× over 6 hours. Tune thresholds based on service criticality.

---

## Error Budget Freeze Policy

When remaining error budget falls below **{{FREEZE_THRESHOLD}}%** of the measurement window:

1. Freeze all new feature releases and non-critical changes.
2. Redirect engineering capacity to reliability work.
3. Require explicit approval from the service owner to resume feature work.
4. Document the freeze period and the actions taken to recover budget.

The freeze threshold is a circuit breaker, not a punishment. It protects users while signaling that the service needs reliability investment before absorbing more change risk.

---

## Error Budget Review Cadence

**Review cadence:** {{REVIEW_CADENCE}}

At each review, assess: current budget consumption, burn rate trend, recent incidents affecting budget, and whether the SLO target remains calibrated to user needs. Adjust SLO targets through the governance process, not unilaterally.

---

## Error Budget Reset

**Reset period:** {{RESET_PERIOD}}

At the end of each reset period, the error budget returns to its full value. Use the reset as an opportunity to review the measurement window and SLO target, not just restart the counter.

---

## Source Attribution

- Source manifests: operations__google_sre.md
- Primary source basis: Google SRE Book Chapter 6 Service Level Objectives
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
