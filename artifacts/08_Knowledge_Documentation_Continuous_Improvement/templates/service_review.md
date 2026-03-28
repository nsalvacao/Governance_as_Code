---
title: Service Review Template
artifact_type: template
status: public-draft
visibility: public
classification: public
owner: knowledge-platform
review_cadence: quarterly
applies_to: service health, reliability, and operational improvement reviews
source_basis: Google SRE Workbook quarterly reliability review practices
source_manifests:
  - operations__google_sre.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Purpose

Review service health and operational trends so that reliability work stays visible, quantified, and actionable. This review is the primary mechanism for surfacing whether a service is meeting its reliability commitments and whether engineering investment is keeping pace with growth.

---

## Service Context

**Service name:** {{SERVICE_NAME}}
**Review period:** {{REVIEW_PERIOD}}
**Reviewer:** {{REVIEWER}}

Scope this review to a single service or a tightly coupled service group. If multiple reviewers contributed, list all. The reviewer is accountable for the accuracy of the data presented.

---

## SLO Performance

Report actual SLO achievement against target for the review period. Include trend direction to show whether reliability is improving, stable, or degrading.

| SLO | Target | Actual | Trend |
|---|---|---|---|
| {{SLO_1}} | {{TARGET}} | {{ACTUAL}} | ↑ / ↓ / → |
| {{SLO_2}} | {{TARGET}} | {{ACTUAL}} | ↑ / ↓ / → |
| {{SLO_N}} | {{TARGET}} | {{ACTUAL}} | ↑ / ↓ / → |

For each SLO that missed target, provide a one-sentence explanation. Trend direction (↑ improving, ↓ degrading, → stable) must be based on data, not intuition.

---

## Error Budget Status

**Budget available:** {{BUDGET_PCT}}%
**Consumed this period:** {{CONSUMED_PCT}}%
**Burn rate:** {{BURN_RATE}}×

Summarize error budget health. If budget is below the freeze threshold defined in the SLO policy, note which reliability actions were or are being taken. If budget was fully consumed, explain what triggered the freeze and how budget was recovered.

---

## Top Incidents This Period

| Incident | Date | Duration | User impact | RCA completed |
|---|---|---|---|---|
| {{INCIDENT_1}} | {{DATE}} | {{DURATION}} | {{IMPACT}} | yes / no |
| {{INCIDENT_2}} | {{DATE}} | {{DURATION}} | {{IMPACT}} | yes / no |
| {{INCIDENT_N}} | {{DATE}} | {{DURATION}} | {{IMPACT}} | yes / no |

List all incidents that consumed meaningful error budget or required escalation. Link to postmortem documents where available. Flag any incidents where RCA is not yet complete with a target completion date.

---

## Toil Metrics

**Toil as % of engineer time:** {{TOIL_PCT}}%

Toil is repetitive operational work that is automatable, tactical, and does not produce lasting value. The SRE target is to keep toil below 50% of engineering time.

**Top toil sources:**
- {{TOIL_SOURCE_1}}
- {{TOIL_SOURCE_2}}
- {{TOIL_SOURCE_N}}

**Toil reduction actions in progress:**
- {{TOIL_ACTION}}

If toil exceeds 50%, this section must include a concrete plan with owners and timelines to bring it below threshold.

---

## Reliability Improvements

Progress on reliability investments made during this period. Link to ADRs, runbooks, or other artifacts where applicable.

| Improvement | Impact | Status |
|---|---|---|
| {{IMPROVEMENT_1}} | {{IMPACT}} | planned / in-progress / done |
| {{IMPROVEMENT_2}} | {{IMPACT}} | planned / in-progress / done |
| {{IMPROVEMENT_N}} | {{IMPACT}} | planned / in-progress / done |

---

## Capacity and Scaling

**Current load:** {{CURRENT_LOAD}}
**Projected load (next period):** {{PROJECTED_LOAD}}
**Capacity headroom:** {{HEADROOM}}

Summarize current resource utilization and growth projections. Flag any dimension where headroom is below 30% and note the plan to address it before it becomes an incident.

---

## Action Items for Next Period

| Action | Owner | Due | Priority |
|---|---|---|---|
| {{ACTION_1}} | {{OWNER}} | {{DUE}} | P1/P2/P3 |
| {{ACTION_2}} | {{OWNER}} | {{DUE}} | P1/P2/P3 |
| {{ACTION_N}} | {{OWNER}} | {{DUE}} | P1/P2/P3 |

Every action item must have an owner. Actions carried over from the previous review period must be explicitly marked as such and their delay explained. P1 = critical, complete within 7 days; P2 = high, complete within 30 days; P3 = standard, complete within 90 days.

---

## Source Attribution

- Source manifests: operations__google_sre.md
- Primary source basis: Google SRE Workbook quarterly reliability review practices
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
