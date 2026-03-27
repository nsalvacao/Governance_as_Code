---
title: GitOps Application / Environment Definition
artifact_type: template
status: draft
visibility: public
classification: public
owner: platform-governance
review_cadence: quarterly
applies_to: repositories that manage declarative applications or environments
source_basis: OpenGitOps, Flux, and Argo CD application definition guidance
source_manifests:
  - platform__gitops.md
alignment_mode: direct-adaptation
updated: 2026-03-27
---

# GitOps Application / Environment Definition

## Desired state

- Application name: `{{APPLICATION_NAME}}`
- Environment: `{{ENVIRONMENT_NAME}}`
- Source repo: `{{SOURCE_REPO}}`
- Path or chart: `{{SOURCE_PATH}}`
- Sync policy: `{{SYNC_POLICY}}`

## Parameters

| Parameter | Value |
|---|---|
| `{{PARAMETER_NAME}}` | `{{PARAMETER_VALUE}}` |

## Source Attribution

- Source manifests: `platform__gitops.md`
- Primary source basis: OpenGitOps, Flux, and Argo CD application definition guidance
- Alignment mode: direct-adaptation
- Reviewed on: 2026-03-27
