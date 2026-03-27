---
title: Artifact Library Index
artifact_type: normative
status: public
visibility: public
classification: public
owner: GOVERNANCE
review_cadence: quarterly
applies_to: repositories consuming reusable governance assets
source_basis: Repository structural decisions and the public document map
source_manifests: governance__github_docs.md, documentation__diataxis.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

# Artifact Library

`artifacts/` is the reusable library of this repository. Everything here is intended to be instantiated, adapted, or referenced by downstream repositories according to applicability.

## Structure rule

The library is organised by **dimension first** and **artifact type second**:

- `artifacts/<dimension>/standards/`
- `artifacts/<dimension>/policies/`
- `artifacts/<dimension>/templates/`
- `artifacts/<dimension>/schemas/`
- `artifacts/<dimension>/scripts/`
- `artifacts/<dimension>/workflows/`

Not every dimension needs every artifact type.

## Current dimensions

| Dimension | Purpose |
|---|---|
| `conventions` | Cross-cutting metadata, attribution, automation, and validation rules |
| `governance` | Decision architecture, repository-health templates, GitHub-native templates, and governance schemas |
| `reliability` | Error budgets, postmortems, and production readiness |
| `operations` | Incident policy, incident records, and playbooks |
| `continuity` | Business impact analysis and contingency planning |

## Instance versus template

- Files in the repository root and `/.github/` are the live instance for this repository.
- Files in `artifacts/` are reusable source assets.
- If a document class exists in both places, the root version is the concrete instance and the `artifacts/` version is the reusable template or standard.

## Source Attribution

- Source manifests: governance__github_docs.md, documentation__diataxis.md
- Primary source basis: GitHub Docs, Diataxis, and the repository's accepted structural decisions
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
