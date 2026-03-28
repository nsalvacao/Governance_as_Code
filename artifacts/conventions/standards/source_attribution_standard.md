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

Source attribution serves three functions: **traceability** (linking every artifact to the authoritative source it was derived from), **credibility** (making the reasoning behind design choices auditable), and **downstream reuse** (enabling consumers to verify provenance before adopting an artifact). Without attribution, artifacts become disconnected from their origin and cannot be reliably updated when their source evolves.

## Required Fields in `## Source Attribution` Section

Every artifact must end with a `## Source Attribution` section containing the following fields. Fields marked as required must not be omitted even when the value is a placeholder.

| Field | Required | Description |
|---|---|---|
| `Source manifests` | Yes | Comma-separated list of source manifest filenames (e.g., `documentation__diataxis.md`). At least one manifest must be listed. |
| `Primary source basis` | Yes | A brief human-readable description of the dominant source family (e.g., "Diataxis framework (Daniele Procida)"). |
| `Alignment mode` | Yes | One of the four defined alignment modes (see section below). |
| `Reviewed on` | Yes | ISO date of the most recent review (`YYYY-MM-DD`). |

The section header must be exactly `## Source Attribution` — no variation in capitalization or punctuation. Automated validation checks for this exact string.

## Alignment Modes Defined

The `alignment_mode` field communicates how closely the artifact follows its source basis. Choose the mode that most accurately describes the relationship.

| Mode | Definition |
|---|---|
| `direct-adaptation` | Minimal deviation from the source. The artifact structure, terminology, and content closely follow the source with only minor adjustments for platform conventions. |
| `guided-synthesis` | Synthesized from one primary source with meaningful additions, omissions, or reorganization. The source provides the framework; the artifact adds interpretation. |
| `hybrid-synthesis` | Synthesized from two or more sources that have been actively reconciled. No single source is dominant. |
| `native-platform-binding` | Follows the platform-native specification exactly (e.g., GitHub Actions workflow syntax, JSON Schema draft). The source is the platform specification itself. |

When the correct mode is ambiguous between `guided-synthesis` and `hybrid-synthesis`, use `hybrid-synthesis` if two or more source manifests are listed.

## Source Manifests Naming Convention

Source manifest filenames follow the pattern: `{{DOMAIN}}__{{SOURCE_NAME}}.md`

- `{{DOMAIN}}` identifies the knowledge domain (e.g., `documentation`, `governance`, `platform`, `operations`, `method`).
- `{{SOURCE_NAME}}` identifies the specific source (e.g., `diataxis`, `github_docs`, `scrum_guide`).
- The double underscore `__` is a deliberate separator that distinguishes domain from source name and makes filenames machine-parseable.
- Examples: `documentation__diataxis.md`, `governance__github_docs.md`, `method__scrum_guide.md`

Source manifest files reside in the manifests directory at `{{MANIFESTS_DIRECTORY}}`. Each manifest describes a source family, its version or edition, key concepts adopted, and the artifacts that reference it.

## Update Triggers

The Source Attribution section must be updated when:

- The primary source basis changes (e.g., a newer edition of a specification replaces the previous one).
- The artifact is reviewed and confirmed accurate; update `Reviewed on` to the review date even if no content changes.
- The alignment mode changes because the artifact's relationship to its source has shifted.
- A new source manifest is added or an existing one is renamed.

Do not update `Reviewed on` as a formatting or housekeeping change; it must reflect a genuine review of the artifact's content and accuracy.

## Using the Partial Template

Use `artifacts/conventions/templates/partials/source_attribution.md` as the canonical snippet. Append it to new artifacts at creation time and update the placeholder values. Automation agents may inject the snippet and leave the attribution block untouched while updating other sections.

## Validation Method

The governance validator (`scripts/validate_governance_artifacts.py`) checks for the presence of `## Source Attribution` in every artifact under `artifacts/`. It does not validate the content of the attribution block. Additional validation may be added to check that:

- `source_manifests` listed in frontmatter match those listed in the `## Source Attribution` section.
- `alignment_mode` in frontmatter matches the value in the `## Source Attribution` section.
- `Reviewed on` date is not older than the artifact's `review_cadence` period.

Automation is tied to `{{GOVERNANCE_VALIDATION_WORKFLOW}}` which runs on every pull request touching `artifacts/`.

## Source Attribution

- Source manifests: documentation__diataxis.md, governance__github_docs.md
- Primary source basis: Diataxis editorial model plus GitHub governance templates
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
