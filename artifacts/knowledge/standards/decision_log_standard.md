---
title: Decision Log Standard
artifact_type: standard
status: public-draft
visibility: public
classification: public
owner: knowledge-platform
review_cadence: quarterly
applies_to: public decision logs used by this repository and downstream repositories
source_basis: GitHub Docs decision record practices and repository governance conventions
source_manifests:
  - governance__github_docs.md
  - platform__aws_well_architected.md
  - platform__microsoft_learn.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Purpose

Define how a public decision log is structured so that it remains readable, traceable, and easy to automate.

## Rules

- Each entry must have a stable identifier.
- Each accepted decision should record status, context, and source basis.
- Public wording should avoid private rationale and sensitive context.
- The log should link to the authoritative repository instance when one exists.

## Guidance

- Keep the log concise and cumulative.
- Use the log for organizational decisions; reserve detailed analysis for linked artifacts.
- Treat the public log as the canonical public surface and the repository instance as its live embodiment.

## Source Attribution

- Source manifests: governance__github_docs.md, platform__aws_well_architected.md, platform__microsoft_learn.md
- Primary source basis: GitHub Docs decision record practices and repository governance conventions
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
