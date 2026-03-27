---
title: Root Cause Analysis Template
artifact_type: template
status: public-draft
visibility: public
classification: public
owner: knowledge-platform
review_cadence: quarterly
applies_to: incidents, defects, and recurring operational failures
source_basis: NIST incident analysis and Google SRE learning guidance
source_manifests:
  - operations__nist_cisa.md
  - operations__google_sre.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Purpose

Document the causal chain behind a failure so that the analysis leads to durable improvement, not just a label.

## Required sections

- Problem statement
- Direct cause
- Contributing causes
- Systemic causes
- Evidence reviewed
- Corrective actions
- Verification plan

## Guidance

- Favor specific causal statements over broad blame language.
- Separate evidence from inference.
- Identify the smallest actionable set of causes that explains the outcome.

## Source Attribution

- Source manifests: operations__nist_cisa.md, operations__google_sre.md
- Primary source basis: NIST incident analysis practices and Google SRE learning guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
