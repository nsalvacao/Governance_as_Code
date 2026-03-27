---
title: Incident Communications Playbook
artifact_type: template
status: draft
visibility: public
classification: public
owner: "{{OWNER_NAME}}"
review_cadence: quarterly
applies_to: communications playbook
source_basis: Google SRE Incident Management Guide
source_manifests:
  - operations__google_sre.md
  - operations__nist_cisa.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Notification Targets
- Internal mailing list: `{{INTERNAL_CHANNEL}}`
- Executive briefing channel: `{{EXECUTIVE_CHANNEL}}`
- Customer-facing status page: `{{CUSTOMER_STATUS_PAGE}}`

## Communication Cadence
1. Initial statement within `{{INITIAL_COMM_WINDOW}}` after incident detection.
2. Follow-ups every `{{UPDATE_INTERVAL_MINUTES}}` until the incident is resolved.
3. Final recovery announcement once `{{RECOVERY_TARGET}}` is met.

## Message Template
- Summary: `{{INCIDENT_SUMMARY}}`
- Impact: `{{CUSTOMER_IMPACT}}`
- Recovery status: `{{RECOVERY_PROGRESS}}`
- Next steps: `{{NEXT_STEPS}}`

## Source Attribution
- Source manifests: `operations__google_sre.md`, `operations__nist_cisa.md`
- Primary source basis: Google SRE Incident Management Guide
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
