---
title: Incident Report Template
artifact_type: template
status: draft
visibility: public
classification: public
owner: "{{OWNER_NAME}}"
review_cadence: quarterly
applies_to: incident report
source_basis: Google SRE Incident Management Guide, NIST SP 800-61r3
source_manifests: operations__google_sre.md, operations__nist_cisa.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## {{INCIDENT_ID}} – Incident Report
- **Impact class:** `{{IMPACT_CLASS}}`
- **Severity level:** `{{SEVERITY_LEVEL}}`
- **Systems affected:** `{{SYSTEMS_AFFECTED}}`
- **Recovery target:** `{{RECOVERY_WINDOW_HOURS}}`
- **Incident commander:** `{{INCIDENT_COMMANDER}}`
- **Operations lead:** `{{OPERATIONS_LEAD}}`
- **Communications lead:** `{{COMMUNICATIONS_LEAD}}`

### Timeline Summary
| UTC time | Event | Owner |
|---|---|---|
| `{{TIMESTAMP}}` | `{{EVENT_DESCRIPTION}}` | `{{OWNED_BY}}` |

### Key Actions
- Detection: `{{DETECTION_METHOD}}`
- Initial containment: `{{CONTAINMENT_ACTIONS}}`
- Mitigation: `{{MITIGATION_ACTIONS}}`
- Recovery status: `{{RECOVERY_STATUS}}`

### Impact
- Customer impact: `{{CUSTOMER_IMPACT}}`
- Error budget impact: `{{ERROR_BUDGET_IMPACT}}`
- Business impact analysis reference: `{{BIA_URL}}`

### Next Steps
1. Follow-up action: `{{FOLLOW_UP_ACTION}}` (owner: `{{FOLLOW_UP_OWNER}}`)
2. Postmortem: `{{POSTMORTEM_LINK}}`
3. Lessons review: `{{LESSON_REVIEW_OWNER}}`

## Source Attribution
- Source manifests: `operations__google_sre.md`, `operations__nist_cisa.md`
- Primary source basis: Google SRE Incident Management Guide, NIST SP 800-61r3
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
