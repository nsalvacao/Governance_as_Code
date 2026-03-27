---
title: SLO and Error Budget Policy
artifact_type: policy
status: public-draft
visibility: public
classification: public
owner: knowledge-platform
review_cadence: quarterly
applies_to: services that define reliability objectives and error budgets
source_basis: Google SRE service level objectives and error budget guidance
source_manifests:
  - operations__google_sre.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Policy Statement

Services that publish reliability commitments must define measurable SLOs and use error budgets to govern change decisions.

## Minimum requirements

- Define the service objective, measurement window, and accepted threshold.
- Make the error budget visible to owners and reviewers.
- State the escalation rule when the budget is consumed or trending toward exhaustion.
- Link the policy to review, release, and incident workflows.

## Guidance

- Use plain language for the business meaning of each objective.
- Keep the measurement method explicit enough for automation.
- Allow downstream repositories to instantiate service-specific thresholds through placeholders.

## Source Attribution

- Source manifests: operations__google_sre.md
- Primary source basis: Google SRE service level objectives and error budget guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
