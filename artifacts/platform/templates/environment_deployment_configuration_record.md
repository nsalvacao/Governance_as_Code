---
title: Environment / Deployment Configuration Record
artifact_type: template
status: draft
visibility: public
classification: public
owner: platform-governance
review_cadence: quarterly
applies_to: repositories that configure deployable environments
source_basis: GitHub environment variables and GitOps configuration guidance
source_manifests:
  - governance__github_docs.md
  - platform__gitops.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

# Environment / Deployment Configuration Record

## Configuration

- Environment name: `{{ENVIRONMENT_NAME}}`
- Deployment target: `{{DEPLOYMENT_TARGET}}`
- Variables source: `{{VARIABLE_SOURCE}}`
- Secrets reference: `{{SECRETS_REFERENCE}}`
- Owner: `{{OWNER}}`

## Controlled values

| Key | Value source | Notes |
|---|---|---|
| `{{CONFIG_KEY}}` | `{{VALUE_SOURCE}}` | `{{NOTES}}` |

## Source Attribution

- Source manifests: `governance__github_docs.md`, `platform__gitops.md`
- Primary source basis: GitHub environment and GitOps configuration guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
