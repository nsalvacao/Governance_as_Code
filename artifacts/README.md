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
source_manifests:
  - governance__github_docs.md
  - documentation__diataxis.md
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
| `01_Governance_Method` | Cross-cutting governance method, conventions, repository health, GitHub-native templates, and decision architecture |
| `02_Discovery_Planning_Early_Learning` | Discovery, planning, experimentation, retrospectives, and early learning records |
| `03_Architecture_Security_Decision` | Architecture decision support, review, threat modeling, and security reasoning |
| `04_Quality_Review_Control` | Review controls, ownership, support, and verification surfaces |
| `05_Delivery_Change_Readiness` | Delivery planning, change management, rollout, rollback, and post-implementation review |
| `06_Platform_Delivery_Automation_AI_Operations` | CI/CD, GitOps, environment governance, platform baselines, and AI operations |
| `07_Operations_Incidents_Continuity` | Service facts, incident response, operational playbooks, runbooks, procedures, continuity, and drills |
| `08_Knowledge_Documentation_Continuous_Improvement` | Post-incident learning, documentation governance, and continuous improvement |
| `09_Project_Portfolio_Service_Governance` | Project, portfolio, service governance, and ITSM-adjacent reusable records |
| `10_Risk_Exceptions_Traceability` | Risk, exceptions, auditability, vulnerability records, and governance review cadence |

## Instance versus template

- Files in the repository root and `/.github/` are the live instance for this repository.
- Files in `artifacts/` are reusable source assets.
- If a document class exists in both places, the root version is the concrete instance and the `artifacts/` version is the reusable template or standard.

## Catalog model

The public README indexes both:

- canonical artifacts, which anchor each document class in the main tables;
- supporting artifacts, which appear in supporting tables inside the same collapsible dimension sections.

This keeps the README as the single public catalog while preserving a distinction between primary anchors and secondary reusable assets.

## Source Attribution

- Source manifests: [`governance__github_docs.md`](../sources/manifests/governance__github_docs.md), [`documentation__diataxis.md`](../sources/manifests/documentation__diataxis.md)
- Primary source basis: GitHub Docs, Diataxis, and the repository's accepted structural decisions
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
