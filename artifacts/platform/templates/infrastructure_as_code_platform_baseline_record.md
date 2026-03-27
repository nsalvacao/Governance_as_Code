---
title: Infrastructure as Code / Platform Baseline Record
artifact_type: template
status: draft
visibility: public
classification: public
owner: platform-governance
review_cadence: quarterly
applies_to: repositories with declarative infrastructure or platform baselines
source_basis: OpenGitOps, AWS Well-Architected, and Microsoft platform baseline guidance
source_manifests:
  - platform__gitops.md
  - platform__aws_well_architected.md
  - platform__microsoft_learn.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

# Infrastructure as Code / Platform Baseline Record

## Baseline summary

- Baseline name: `{{BASELINE_NAME}}`
- Scope: `{{SCOPE}}`
- Owner: `{{OWNER}}`
- Revision: `{{REVISION}}`
- Linked repository source: `{{SOURCE_REPO}}`

## Components

| Component | Desired state | Evidence |
|---|---|---|
| `{{COMPONENT_NAME}}` | `{{DESIRED_STATE}}` | `{{EVIDENCE_LINK}}` |

## Source Attribution

- Source manifests: `platform__gitops.md`, `platform__aws_well_architected.md`, `platform__microsoft_learn.md`
- Primary source basis: declarative infrastructure and platform baseline guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
