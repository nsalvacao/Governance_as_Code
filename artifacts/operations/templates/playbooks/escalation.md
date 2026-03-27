---
title: Escalation Playbook
artifact_type: template
status: draft
visibility: public
classification: public
owner: "{{OWNER_NAME}}"
review_cadence: quarterly
applies_to: escalation playbook
source_basis: NIST SP 800-61r3, Google SRE Incident Management Guide
source_manifests: operations__nist_cisa.md, operations__google_sre.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Escalation Criteria
- Severity threshold: `{{ESCALATION_SEVERITY}}`
- Service impact: `{{ESCALATION_IMPACT}}`
- Error budget breach: `{{ERROR_BUDGET_BREACH}}`
- Regulatory or safety flag: `{{REGULATORY_FLAG}}`

## Escalation Steps
1. Notify Incident Commander and Operations Lead via `{{ESCALATION_CHANNEL}}`.
2. Reference the incident report and timeline for context.
3. Activate extended support team (`{{EXTENDED_TEAM}}`) with designated ETA.
4. Confirm communication plan uses the incident communications template.
5. Log decision rationale and approvals in the escalation record.

## Source Attribution
- Source manifests: `operations__nist_cisa.md`, `operations__google_sre.md`
- Primary source basis: NIST SP 800-61r3, Google SRE Incident Management Guide
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
