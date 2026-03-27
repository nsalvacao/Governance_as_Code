---
title: CI Workflow / Build Pipeline Record
artifact_type: template
status: draft
visibility: public
classification: public
owner: platform-governance
review_cadence: quarterly
applies_to: repositories with automated build and validation workflows
source_basis: GitHub Actions workflow and build traceability guidance
source_manifests:
  - governance__github_docs.md
  - platform__microsoft_learn.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

# CI Workflow / Build Pipeline Record

## Pipeline summary

- Workflow name: `{{WORKFLOW_NAME}}`
- Trigger: `{{TRIGGER}}`
- Branches: `{{BRANCHES}}`
- Owner: `{{OWNER}}`
- Build identity: `{{BUILD_ID}}`

## Steps

| Step | Purpose | Evidence |
|---|---|---|
| `{{STEP_NAME}}` | `{{STEP_PURPOSE}}` | `{{STEP_EVIDENCE}}` |

## Outputs

- Artifact path: `{{ARTIFACT_PATH}}`
- Test summary: `{{TEST_SUMMARY}}`
- Deployment eligibility: `{{DEPLOYMENT_ELIGIBILITY}}`

## Source Attribution

- Source manifests: `governance__github_docs.md`, `platform__microsoft_learn.md`
- Primary source basis: GitHub Actions and build traceability guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
