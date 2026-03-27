---
title: Threat Model Template
artifact_type: template
status: public-draft
visibility: public
classification: public
owner: architecture-platform
review_cadence: quarterly
applies_to: systems or changes that require explicit security threat analysis
source_basis: Microsoft Learn threat modeling guidance; NIST security assessment concepts
source_manifests:
  - platform__microsoft_learn.md
  - operations__nist_cisa.md
alignment_mode: direct-adaptation
updated: 2026-03-27
---

## Purpose

Describe the trust boundaries, threats, and mitigations relevant to a design in a way that can be reviewed and reused.

## Template

- **System or change:** `{{SYSTEM_OR_CHANGE}}`
- **Assets:** `{{ASSETS}}`
- **Trust boundaries:** `{{TRUST_BOUNDARIES}}`
- **Threats identified:** `{{THREATS}}`
- **Mitigations:** `{{MITIGATIONS}}`
- **Residual risk:** `{{RESIDUAL_RISK}}`

## Guidance

- Capture threats at the level needed for action, not at the level of speculative detail.
- Link to security requirements and architecture decisions where relevant.

## Source Attribution

- Source manifests: `platform__microsoft_learn.md`, `operations__nist_cisa.md`
- Primary source basis: Microsoft threat modeling guidance and NIST security assessment concepts
- Alignment mode: direct-adaptation
- Reviewed on: 2026-03-27
