---
title: Security Requirements Record Template
artifact_type: template
status: public-draft
visibility: public
classification: public
owner: architecture-platform
review_cadence: quarterly
applies_to: design and delivery security requirements that must be tracked explicitly
source_basis: Microsoft Learn security requirements guidance; NIST control-oriented documentation practices
source_manifests:
  - platform__microsoft_learn.md
  - operations__nist_cisa.md
alignment_mode: direct-adaptation
updated: 2026-03-27
---

## Purpose

Record security requirements in a form that can be traced to the design, implementation, and validation work that satisfies them.

## Template

- **Requirement ID:** `{{REQUIREMENT_ID}}`
- **Requirement statement:** `{{REQUIREMENT_STATEMENT}}`
- **Risk addressed:** `{{RISK_ADDRESSED}}`
- **Owner:** `{{OWNER}}`
- **Implementation note:** `{{IMPLEMENTATION_NOTE}}`
- **Validation method:** `{{VALIDATION_METHOD}}`
- **Status:** `{{STATUS}}`

## Guidance

- Keep requirements specific, testable, and linked to the threat model or architecture record.
- Use the same identifier across downstream implementation and review artifacts.

## Source Attribution

- Source manifests: `platform__microsoft_learn.md`, `operations__nist_cisa.md`
- Primary source basis: Microsoft security requirements guidance and NIST control-oriented documentation practices
- Alignment mode: direct-adaptation
- Reviewed on: 2026-03-27
