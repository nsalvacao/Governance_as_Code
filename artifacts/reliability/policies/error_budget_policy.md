---
title: Error Budget Policy
artifact_type: policy
status: public-draft
visibility: public
classification: public
owner: reliability-platform
review_cadence: semiannual
applies_to: services with defined SLOs
source_basis: Google SRE Example Error Budget Policy
source_manifests: operations__google_sre.md
alignment_mode: direct-adaptation
updated: 2026-03-27
---

## Objective

Keep reliability commitments explicit, keep response deterministic, and avoid politicizing SLA breaches.

## Key rules

- `SLO`: `{{SLO_NAME}}` measured by `{{SLO_METRIC}}`.
- `Error budget`: `{{ERROR_BUDGET_LIMIT}}` per `{{MEASUREMENT_PERIOD}}`.
- `SLO miss policy`: escalation to `{{ESCALATION_TIER}}` when `{{ERROR_BUDGET_CONSUMED}}` exceeds `{{THRESHOLD}}`.
- `Outage policy`: declare outage when impact triggers `{{OUTAGE_CRITERIA}}`.

## Response lifecycle

1. Monitor dashboards; automate alerts via `{{MONITORING_TOOL}}`.
2. Notify `{{RESPONSE_TEAM}}` when error budget crosses `{{CROSSOVER_POINT}}`.
3. Pause releases or trigger freeze with `{{RELEASE_CONTROL}}` if necessary.
4. Document mitigations in a postmortem using the family defined in this wave.

## Source Attribution

- Source manifests: `operations__google_sre.md`
- Primary source basis: Google SRE Example Error Budget Policy
- Alignment mode: direct-adaptation
- Reviewed on: 2026-03-27
