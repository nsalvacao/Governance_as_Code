---
title: Documentation Architecture and Information Model
artifact_type: standard
status: public-draft
visibility: public
classification: public
owner: knowledge-platform
review_cadence: semiannual
applies_to: documentation corpora and reusable governance libraries
source_basis: Diataxis documentation structure guidance and GitHub Docs repository governance practices
source_manifests:
  - documentation__diataxis.md
  - governance__github_docs.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Purpose

Define how the document corpus is organized, related, and navigated so that future documents remain consistent and discoverable.

## Core model

- `Normative`: policies, standards, and rules that govern behavior.
- `Instantiable`: templates and records that downstream repositories fill in.
- `Evidence`: records that capture facts, outcomes, and traceability.
- `Reference`: stable explanatory material and knowledge base content.

## Rules

- Every document class should have one clear primary artifact.
- Related artifacts should link back to the primary artifact and the governing standard.
- Names should be stable, human-readable, and obvious from the catalog.
- The information model should make reuse and automation easy without hiding provenance.

## Source Attribution

- Source manifests: documentation__diataxis.md, governance__github_docs.md
- Primary source basis: Diataxis documentation structure guidance and GitHub Docs repository governance practices
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
