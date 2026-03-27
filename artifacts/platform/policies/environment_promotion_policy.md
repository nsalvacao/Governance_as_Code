---
title: Environment Promotion Policy
artifact_type: policy
status: draft
visibility: public
classification: public
owner: platform-governance
review_cadence: quarterly
applies_to: repositories that promote changes across multiple environments
source_basis: GitHub environment and platform promotion guidance
source_manifests:
  - governance__github_docs.md
  - platform__microsoft_learn.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

# Environment Promotion Policy

## Rules

- Promote only after the required checks pass for the target environment.
- Use explicit environment names and promotion gates.
- Keep production promotion stricter than lower environments.
- Require human approval where risk, compliance, or blast radius justify it.
- Record the promotion path and the artifact version being promoted.

## Promotion metadata

- Source version: `{{SOURCE_VERSION}}`
- Target environment: `{{TARGET_ENVIRONMENT}}`
- Approval evidence: `{{APPROVAL_LINK}}`
- Rollback plan: `{{ROLLBACK_LINK}}`

## Source Attribution

- Source manifests: `governance__github_docs.md`, `platform__microsoft_learn.md`
- Primary source basis: GitHub environments and Microsoft promotion guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
