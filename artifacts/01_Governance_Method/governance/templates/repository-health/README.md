---
title: "{{REPOSITORY_TITLE}}"
artifact_type: template
status: public
visibility: public
classification: public
owner: "{{REPOSITORY_OWNER}}"
review_cadence: "{{REVIEW_CADENCE}}"
applies_to: repositories adopting the governance baseline
source_basis: GitHub Docs + Open Source Guides
source_manifests: governance__github_docs.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

[![Status](https://img.shields.io/badge/status-{{STATUS_BADGE}}-2563eb)]({{PRIMARY_DOC_URL}})
[![Validation](https://img.shields.io/badge/validation-{{VALIDATION_BADGE}}-15803d)]({{VALIDATION_DOC_URL}})
[![Visibility](https://img.shields.io/badge/visibility-{{VISIBILITY_BADGE}}-475569)]({{MAP_URL}})

# {{REPOSITORY_TITLE}}

{{ONE_SENTENCE_SUMMARY}}

## What this repository is

- {{WHAT_IT_IS_1}}
- {{WHAT_IT_IS_2}}
- {{WHAT_IT_IS_3}}

## Why now

{{WHY_NOW}}

## Repository model

| Layer | Purpose | Location |
|---|---|---|
| Repository instance | Concrete files for this repository | {{INSTANCE_PATHS}} |
| Reusable library | Templates, schemas, scripts, workflows, and standards | {{LIBRARY_PATHS}} |
| Private working material | Drafts and non-public context | {{PRIVATE_PATHS}} |

## Key features

| Feature | Present? | Notes |
|---|---|---|
| Deterministic validation | {{VALIDATION_STATUS}} | {{VALIDATION_NOTES}} |
| Reusable templates | {{TEMPLATE_STATUS}} | {{TEMPLATE_NOTES}} |
| Schemas | {{SCHEMA_STATUS}} | {{SCHEMA_NOTES}} |
| Workflows | {{WORKFLOW_STATUS}} | {{WORKFLOW_NOTES}} |

## Navigation

- Primary governance doc: {{PRIMARY_GOVERNANCE_DOC}}
- Contribution guide: {{CONTRIBUTING_DOC}}
- Public document map: {{MAP_DOC}}
- Artifact library index: {{ARTIFACT_LIBRARY_DOC}}

## Contribution

- Explain where contributors should edit instance files versus reusable assets.
- State how validation runs locally and in CI.
- Link the relevant GitHub-native intake surfaces.

## Source Attribution

- Source manifests: {{SOURCE_MANIFESTS}}
- Primary source basis: {{PRIMARY_SOURCE_BASIS}}
- Alignment mode: {{ALIGNMENT_MODE}}
- Reviewed on: {{REVIEWED_ON}}
