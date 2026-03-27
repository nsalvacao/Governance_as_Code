---
title: Trade-off Analysis Template
artifact_type: template
status: public-draft
visibility: public
classification: public
owner: architecture-platform
review_cadence: quarterly
applies_to: comparisons between viable architecture or delivery options
source_basis: AWS Well-Architected trade-off analysis practices; Microsoft Learn decision support guidance
source_manifests:
  - platform__aws_well_architected.md
  - platform__microsoft_learn.md
alignment_mode: direct-adaptation
updated: 2026-03-27
---

## Purpose

Record a structured comparison of options so that the selected path can be traced back to the factors that mattered most.

## Template

- **Decision context:** `{{CONTEXT}}`
- **Option A:** `{{OPTION_A}}`
- **Option B:** `{{OPTION_B}}`
- **Option C:** `{{OPTION_C}}`
- **Criteria:** `{{CRITERIA}}`
- **Scoring or comparison method:** `{{METHOD}}`
- **Selected option:** `{{SELECTED_OPTION}}`
- **Rationale:** `{{RATIONALE}}`

## Guidance

- Keep the comparison explicit enough for later review and automation.
- Include cost, operational risk, security, maintainability, and delivery impact where relevant.

## Source Attribution

- Source manifests: `platform__aws_well_architected.md`, `platform__microsoft_learn.md`
- Primary source basis: AWS trade-off analysis practices and Microsoft decision support guidance
- Alignment mode: direct-adaptation
- Reviewed on: 2026-03-27
