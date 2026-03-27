---
title: Architecture Decision Record Standard
artifact_type: standard
status: public-draft
visibility: public
classification: public
owner: architecture-platform
review_cadence: quarterly
applies_to: architecture decisions that require durable justification and review
source_basis: AWS Well-Architected decision practices; Microsoft Learn architecture review guidance; GitHub Docs governance norms
source_manifests:
  - platform__aws_well_architected.md
  - platform__microsoft_learn.md
  - governance__github_docs.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Purpose

This standard defines the architecture-layer entry point for recording durable decisions that shape system design, platform choices, and delivery constraints.

## Canonical relationship

- The detailed ADR body lives in the reusable template at `artifacts/governance/templates/architecture_decision_record.md`.
- The governance-layer ADR standard at `artifacts/governance/standards/adr_standard.md` defines the broader decision policy.
- This artifact exists so the architecture dimension has a clear, public canonical primary artifact for the catalog.

## Required structure

- Use a stable identifier for each ADR.
- Capture context, decision, consequences, validation, and review notes.
- Keep the rationale explicit enough for later automation and review.
- Prefer parameterized placeholders when the ADR is intended for instantiation by downstream repositories.

## Automation guidance

- Link each ADR to the decision log when the outcome is accepted.
- Keep the artifact stable once accepted; superseding decisions should produce a new record.

## Source Attribution

- Source manifests: `platform__aws_well_architected.md`, `platform__microsoft_learn.md`, `governance__github_docs.md`
- Primary source basis: AWS and Microsoft architecture decision practices plus GitHub governance norms
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
