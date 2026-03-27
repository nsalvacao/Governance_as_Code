---
title: Artifact / Build Provenance Record
artifact_type: template
status: draft
visibility: public
classification: public
owner: platform-governance
review_cadence: quarterly
applies_to: repositories that need build and artifact traceability
source_basis: GitHub artifact provenance and build traceability guidance
source_manifests:
  - governance__github_docs.md
  - platform__microsoft_learn.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

# Artifact / Build Provenance Record

## Provenance

- Artifact name: `{{ARTIFACT_NAME}}`
- Build source: `{{BUILD_SOURCE}}`
- Commit or version: `{{VERSION_REF}}`
- Workflow run: `{{WORKFLOW_RUN}}`
- Digest or signature: `{{DIGEST}}`

## Traceability

| Link type | Reference |
|---|---|
| Source commit | `{{SOURCE_COMMIT}}` |
| Build workflow | `{{BUILD_WORKFLOW}}` |
| Release artifact | `{{RELEASE_ARTIFACT}}` |

## Source Attribution

- Source manifests: `governance__github_docs.md`, `platform__microsoft_learn.md`
- Primary source basis: GitHub artifact provenance guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
