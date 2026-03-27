---
title: Incident Coordination Playbook
artifact_type: template
status: draft
visibility: public
classification: public
owner: "{{OWNER_NAME}}"
review_cadence: quarterly
applies_to: coordination playbook
source_basis: Google SRE Incident Management Guide
source_manifests:
  - operations__google_sre.md
  - operations__nist_cisa.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Trigger
- Detected by: `{{DETECTION_SYSTEM}}`
- Incident ID: `{{INCIDENT_ID}}`
- Impact class: `{{IMPACT_CLASS}}`

## Coordination Roles
- Incident Commander: `{{INCIDENT_COMMANDER}}`
- Operations Lead: `{{OPERATIONS_LEAD}}`
- Communications Lead: `{{COMMUNICATIONS_LEAD}}`

## Coordination Activities
1. Establish communication bridge (`{{COMM_CHANNEL}}`) and share `{{STAKEHOLDER_LIST}}`.
2. Confirm runbook execution for each affected `{{SYSTEMS_AFFECTED}}`.
3. Validate alerts vs. instrumentation data before declaring status.
4. Synchronize with escalation path when `{{ESCALATION_THRESHOLD}}` is met.
5. Record actions in the incident report and timeline templates.

## Source Attribution
- Source manifests: `operations__google_sre.md`, `operations__nist_cisa.md`
- Primary source basis: Google SRE Incident Management Guide
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
