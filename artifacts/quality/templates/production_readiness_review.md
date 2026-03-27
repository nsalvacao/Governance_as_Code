---
title: Production Readiness Review Template
artifact_type: template
status: public-draft
visibility: public
classification: public
owner: quality-platform
review_cadence: quarterly
applies_to: readiness checks before a change or service is treated as production-ready
source_basis: Google SRE production readiness practices; AWS Well-Architected operational readiness guidance
source_manifests:
  - operations__google_sre.md
  - platform__aws_well_architected.md
alignment_mode: direct-adaptation
updated: 2026-03-27
---

## Purpose

Capture the minimum evidence needed to decide whether a service or change can be operated safely.

## Template

- **Scope:** `{{SCOPE}}`
- **Owner:** `{{OWNER}}`
- **Readiness criteria:** `{{READINESS_CRITERIA}}`
- **Open risks:** `{{OPEN_RISKS}}`
- **Validation evidence:** `{{VALIDATION_EVIDENCE}}`
- **Decision:** `{{DECISION}}`

## Guidance

- Tie each criterion to an observable test or operational signal.
- Include rollback and support assumptions when relevant.

## Source Attribution

- Source manifests: `operations__google_sre.md`, `platform__aws_well_architected.md`
- Primary source basis: Google SRE production readiness practices and AWS operational readiness guidance
- Alignment mode: direct-adaptation
- Reviewed on: 2026-03-27
