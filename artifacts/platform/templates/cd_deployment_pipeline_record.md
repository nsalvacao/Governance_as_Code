---
title: CD / Deployment Pipeline Record
artifact_type: template
status: draft
visibility: public
classification: public
owner: platform-governance
review_cadence: quarterly
applies_to: repositories with automated deployment or promotion flows
source_basis: GitHub and Microsoft deployment automation guidance
source_manifests:
  - governance__github_docs.md
  - platform__microsoft_learn.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

# CD / Deployment Pipeline Record

## Deployment summary

- Deployment name: `{{DEPLOYMENT_NAME}}`
- Source version: `{{SOURCE_VERSION}}`
- Target environment: `{{TARGET_ENVIRONMENT}}`
- Approver: `{{APPROVER}}`
- Deployment status: `{{STATUS}}`

## Rollout and rollback

- Rollout strategy: `{{ROLLOUT_STRATEGY}}`
- Health gates: `{{HEALTH_GATES}}`
- Rollback path: `{{ROLLBACK_PATH}}`

## Evidence

- Workflow run: `{{WORKFLOW_RUN_LINK}}`
- Release artifact: `{{RELEASE_ARTIFACT_LINK}}`

## Source Attribution

- Source manifests: `governance__github_docs.md`, `platform__microsoft_learn.md`
- Primary source basis: GitHub and Microsoft deployment automation guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
