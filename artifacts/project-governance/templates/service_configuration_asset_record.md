---
title: Service Configuration / Asset Record
artifact_type: template
status: draft
visibility: public
classification: public
owner: GOVERNANCE
review_cadence: quarterly
applies_to: service configuration and asset traceability
source_basis: ITIL
source_manifests:
  - service_mgmt__itil.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

# Service Configuration / Asset Record

## Purpose

Track the service components, dependencies, and managed assets that support the service.

## Fields

- configuration item or asset id
- name
- type
- owner
- environment
- dependency links
- status
- last reviewed

## Usage

1. Use a stable identifier for each configuration item.
2. Link the record to the service catalog and change history.
3. Keep asset relationships machine-readable when possible.

## Source Attribution

- Source manifests: `service_mgmt__itil.md`
- Primary source basis: ITIL configuration and asset management guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
