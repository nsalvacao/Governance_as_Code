---
title: Production Readiness Review Template
artifact_type: template
status: public-draft
visibility: public
classification: public
owner: reliability-platform
review_cadence: semiannual
applies_to: production launches and major updates
source_basis: Google SRE Production Readiness Review / AWS ORR combined
source_manifests: operations__google_sre.md platform__aws_well_architected.md platform__microsoft_learn.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Service context

- **Service name:** `{{SERVICE_NAME}}`
- **Team:** `{{SERVICE_OWNER}}`
- **Release window:** `{{RELEASE_WINDOW}}`

## Pillar review

### Observability

- Dashboards: `{{DASHBOARD_URL}}`
- Alerting: `{{ALERTING_CHANNEL}}`
- Runbooks: `{{RUNBOOK_URL}}`

### Automation & Deployment

- Deployment workflow: `{{DEPLOY_COMMAND}}`
- Rollback steps: `{{ROLLBACK_COMMAND}}`
- Canary or gate: `{{CANARY_CRITERIA}}`

### Reliability & Support

- SLO description: `{{SLO}}`
- Error budget status: `{{ERROR_BUDGET_STATUS}}`
- On-call acknowledgments: `{{ON_CALL_ACK}}`

### Safety & Guardrails

- Safety checks executed: `{{SAFETY_CHECK_LIST}}`
- Approval status: `{{APPROVAL_STATUS}}`
- Automated validation (GitHub Action/pipeline): `{{CI_REPORT}}`

## Review outcome

- Status (pass/conditional/reject): `{{DECISION}}`
- Required actions: `{{ACTIONS}}`
- Owner: `{{ACTION_OWNER}}`
- Completion date: `{{DUE_DATE}}`

## Source Attribution

- Source manifests: `operations__google_sre.md`, `platform__aws_well_architected.md`, `platform__microsoft_learn.md`
- Primary source basis: Google SRE PRR, AWS ORR, Microsoft deployment guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
