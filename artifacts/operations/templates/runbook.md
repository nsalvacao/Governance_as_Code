---
title: Runbook
artifact_type: template
status: public-draft
visibility: public
classification: public
owner: "{{OWNER_NAME}}"
review_cadence: quarterly
applies_to: repeatable operational procedures
source_basis: AWS operational guidance and Google SRE runbook practices
source_manifests:
  - operations__google_sre.md
  - platform__aws_well_architected.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Purpose

Provide the reusable structure for step-by-step operational execution that can be followed by humans and automation.

## Required sections

- Purpose and trigger
- Preconditions
- Steps
- Validation
- Rollback or recovery

## Source Attribution

- Source manifests: operations__google_sre.md, platform__aws_well_architected.md
- Primary source basis: AWS operational guidance and Google SRE runbook practices
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27

