---
title: Operational Playbook
artifact_type: template
status: public-draft
visibility: public
classification: public
owner: "{{OWNER_NAME}}"
review_cadence: quarterly
applies_to: repeatable operational scenarios
source_basis: AWS operational guidance, NIST incident response guidance, Google SRE practices
source_manifests:
  - operations__nist_cisa.md
  - operations__google_sre.md
  - platform__aws_well_architected.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Purpose

Provide the generic structure for scenario-specific playbooks used in incident handling, triage, or recovery.

## Required sections

- Trigger or scenario
- Preconditions
- Step-by-step actions
- Validation and exit criteria
- Escalation or rollback

## Source Attribution

- Source manifests: operations__nist_cisa.md, operations__google_sre.md, platform__aws_well_architected.md
- Primary source basis: AWS operational guidance, NIST incident response guidance, Google SRE practices
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27

