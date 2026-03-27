---
title: Postmortem Template
artifact_type: template
status: public-draft
visibility: public
classification: public
owner: reliability-platform
review_cadence: quarterly
applies_to: incidents requiring service review
source_basis: Google SRE Postmortem Culture workbook
source_manifests: operations__google_sre.md
alignment_mode: direct-adaptation
updated: 2026-03-27
---

## Incident summary

- **Incident name:** `{{INCIDENT_NAME}}`
- **Date:** `{{INCIDENT_DATE}}`
- **Duration:** `{{DURATION}}`
- **Services impacted:** `{{SERVICE_LIST}}`

## Timeline

Follow the documented steps from detection through recovery; include timestamps and references to recorded evidence.

1. `{{EVENT}}`
2. `{{EVENT}}`

## Impact

- Customer-facing impact: `{{CUSTOMER_IMPACT}}`
- Operator impact: `{{OPERATOR_IMPACT}}`
- Error budget impact: `{{ERROR_BUDGET_IMPACT}}`

## Root causes

Describe the minimal set of systemic, process, and tooling factors that led to the incident and cite the supporting evidence.

## Remediation

- Short-term mitigation: `{{MITIGATION}}`
- Long-term fix: `{{LONG_TERM_FIX}}`
- Owner: `{{OWNER}}`
- Due date: `{{DUE_DATE}}`

## Recognition

Highlight what kept the incident from being worse and what to repeat.

## Source Attribution

- Source manifests: `operations__google_sre.md`
- Primary source basis: Google SRE Postmortem Culture workbook
- Alignment mode: direct-adaptation
- Reviewed on: 2026-03-27
