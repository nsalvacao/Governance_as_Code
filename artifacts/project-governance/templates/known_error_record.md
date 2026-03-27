---
title: Known Error Record
artifact_type: template
status: draft
visibility: public
classification: public
owner: GOVERNANCE
review_cadence: quarterly
applies_to: diagnosed but unresolved errors and workarounds
source_basis: ITIL, NIST
source_manifests:
  - service_mgmt__itil.md
  - operations__nist_cisa.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

# Known Error Record

## Purpose

Record a known error, its impact, and its workaround until a permanent fix is available.

## Fields

- known error id
- affected service or asset
- description
- workaround
- root cause reference
- owner
- status

## Usage

1. Link the record to the associated problem and incident history.
2. Keep the workaround visible even if the permanent fix is pending.
3. Update the record when the error state changes.

## Source Attribution

- Source manifests: `service_mgmt__itil.md`, `operations__nist_cisa.md`
- Primary source basis: ITIL known error management guidance and NIST incident learning practices
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
