---
title: Design Rationale Template
artifact_type: template
status: public-draft
visibility: public
classification: public
owner: architecture-platform
review_cadence: quarterly
applies_to: records that preserve the reasoning behind a design choice
source_basis: Microsoft Learn architecture rationale guidance; AWS Well-Architected trade-off practices
source_manifests:
  - platform__microsoft_learn.md
  - platform__aws_well_architected.md
alignment_mode: direct-adaptation
updated: 2026-03-27
---

## Purpose

Capture the reasoning behind a design choice in a form that is reusable, reviewable, and easy to connect to the surrounding decision record.

## Template

- **Problem:** `{{PROBLEM}}`
- **Constraints:** `{{CONSTRAINTS}}`
- **Alternatives considered:** `{{ALTERNATIVES}}`
- **Why this option:** `{{RATIONALE}}`
- **Trade-offs accepted:** `{{TRADE_OFFS}}`
- **Follow-up checks:** `{{FOLLOW_UP_CHECKS}}`

## Guidance

- Keep the reasoning factual and concise.
- Separate assumptions from evidence.
- Link to any ADR, review, or benchmark that influenced the choice.

## Source Attribution

- Source manifests: `platform__microsoft_learn.md`, `platform__aws_well_architected.md`
- Primary source basis: Microsoft architecture rationale guidance and AWS trade-off practices
- Alignment mode: direct-adaptation
- Reviewed on: 2026-03-27
