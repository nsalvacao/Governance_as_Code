---
title: Source Attribution Standard
artifact_type: normative
status: draft
visibility: public
classification: public
owner: governance@org
review_cadence: quarterly
applies_to: all governance artifacts
source_basis: documentation__diataxis, governance__github_docs
source_manifests: documentation__diataxis.md, governance__github_docs.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

# Source Attribution Standard

## Purpose

This standard explains how to record provenance for every public artifact so that humans and AI agents can trace design decisions back to the original sources.

## Attribution block

- End each document with a `## Source Attribution` section.
- Include the following items using `{{UPPER_SNAKE_CASE}}` placeholders:
  - `Source manifests`: list filenames (e.g., `documentation__diataxis.md`).
  - `Primary source basis`: brief description of the dominant source family.
  - `Alignment mode`: choose one of `direct-adaptation`, `guided-synthesis`, `hybrid-synthesis`, or `native-platform-binding`.
  - `Reviewed on`: ISO date (e.g., `2026-03-27`).

- In frontmatter, prefer a YAML list for `source_manifests`; use a single string only when backfilling older documents.
- When referencing multiple manifests, order them by authority and note the specific sections that influenced the artifact.
- Include notes for deterministic automation (e.g., “Tied to `validate-governance-artifacts` workflow”) if automation was part of the creation.

## Template usage

- Use `artifacts/conventions/templates/partials/source_attribution.md` as the canonical snippet to append to artifacts.
- Inject the snippet post-generation so automation agents can leave the attribution block untouched while updating metadata or content.

## Automation verification

- Workflows and scripts may read the `source_manifests` and `alignment_mode` frontmatter fields to ensure compliance before publishing.
- Verifier agents confirm the attribution block matches the metadata contract and the `source_manifests` list.

## Source Attribution

- Source manifests: documentation__diataxis.md, governance__github_docs.md
- Primary source basis: Diataxis editorial model plus GitHub governance templates
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
