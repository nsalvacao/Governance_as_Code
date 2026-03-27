---
title: Service Recovery Playbook
artifact_type: template
status: draft
visibility: public
classification: public
owner: "{{OWNER_NAME}}"
review_cadence: quarterly
applies_to: recovery playbook
source_basis: NIST SP 800-61r3, Google SRE
source_manifests: operations__nist_cisa.md, operations__google_sre.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Recovery Objectives
- Recovery target: `{{RECOVERY_TARGET}}`
- Max allowable downtime: `{{MAX_DOWNTIME_MINUTES}}`
- Systems prioritized: `{{SYSTEMS_PRIORITIZED}}`

## Recovery Steps
1. Execute containment runbook for each `{{SYSTEM}}`.
2. Coordinate data restoration or failover via automation scripts referenced in the `automation_and_ai_execution` guidance.
3. Test functionality against `{{VALIDATION_CHECKS}}`.
4. Reconcile incidents with `{{ERROR_BUDGET_TRACKING}}` and update the postmortem.

## Recovery Confirmation
- Recovery owner: `{{RECOVERY_OWNER}}`
- Validation proof: `{{VALIDATION_ARTIFACT_URL}}`
- Documentation reference: `{{INCIDENT_REPORT_URL}}`

## Source Attribution
- Source manifests: `operations__nist_cisa.md`, `operations__google_sre.md`
- Primary source basis: NIST SP 800-61r3, Google SRE Incident Management Guide
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
