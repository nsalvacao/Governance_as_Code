---
title: Postmortem Standard
artifact_type: policy
status: public-draft
visibility: public
classification: public
owner: reliability-platform
review_cadence: quarterly
applies_to: all critical services
source_basis: Google SRE Incident Management Guide & Postmortem Culture
source_manifests: operations__google_sre.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Purpose

Define what a postmortem must capture so that we treat failures as learning opportunities without exposing sensitive decision processes.

## When to run

- `{{TRIGGER}}`: service-impacting incident where recovery took longer than `{{MTTR_THRESHOLD}}` or where customer commitment degrade.
- `{{RESPONSE_OWNER}}` should ensure the postmortem is filed within `{{POSTMORTEM_WINDOW}}`.

## Evidence fields

- `Timeline`: brief chronological entries (supporting documentation may live in incident bucket).
- `Impact`: measurable customer/operator impact, using available SLO/outage data.
- `Root causes`: minimal set of contributing factors (technical, process, tooling, human).
- `Remediation`: actions, owners, and due dates.
- `Recognition`: what worked well or positive deviations worth repeating.

## Writing guidance

- Write in plain English, avoid conjecture, and reference logs/graphs where possible.
- Quote SLO dashboards or telemetry records when calling out impact.
- Coordinate with `{{TOOLS_TEAM}}` to ensure sensitive data is redacted before sharing publicly.

## Source Attribution

- Source manifests: `operations__google_sre.md`
- Primary source basis: Google SRE Incident Management Guide & Postmortem Culture
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
