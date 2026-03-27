---
title: Service Level Policy
artifact_type: policy
status: draft
visibility: public
classification: public
owner: GOVERNANCE
review_cadence: quarterly
applies_to: service level targets, commitments, and review expectations
source_basis: PMI, PRINCE2, ITIL
source_manifests:
  - project__pmi.md
  - project__prince2.md
  - service_mgmt__itil.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

# Service Level Policy

This policy defines how service level commitments are named, approved, reviewed, and adjusted.

## Required elements

- service name
- service owner
- customer or consumer group
- target metrics and thresholds
- review cadence
- exception handling path

## Operating rules

1. Use one policy per service family or portfolio when the targets differ materially.
2. Keep thresholds measurable and reviewable.
3. Link each service level commitment to the owning service catalog entry.
4. Record approved exceptions explicitly rather than hiding them in narrative notes.

## Automation guidance

- Prefer structured fields over prose so AI agents can compare service levels consistently.
- Store the policy in a location that can be referenced from dashboards, catalogs, and review reports.

## Source Attribution

- Source manifests: `project__pmi.md`, `project__prince2.md`, `service_mgmt__itil.md`
- Primary source basis: PMI, PRINCE2, and ITIL service governance guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
