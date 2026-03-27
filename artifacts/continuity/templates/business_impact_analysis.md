---
title: Business Impact Analysis Template
artifact_type: template
status: draft
visibility: public
classification: public
owner: "{{OWNER_NAME}}"
review_cadence: semiannually
applies_to: continuity planning
source_basis: NIST SP 800-34 Rev. 1
source_manifests: operations__nist_cisa.md
alignment_mode: guided-synthesis
updated: 2026-03-27
---

## Business Impact Analysis – `{{SERVICE_NAME}}`
- **Business function:** `{{BUSINESS_FUNCTION_NAME}}`
- **Criticality:** `{{CRITICALITY_LEVEL}}`
- **Primary contacts:** `{{PRIMARY_CONTACT}}`, `{{SECONDARY_CONTACT}}`
- **Executive sponsor:** `{{EXECUTIVE_SPONSOR}}`
- **Dependencies:** `{{DEPENDENCIES_LIST}}`
- **Recovery objective (RTO):** `{{RTO_HOURS}}`
- **Recovery objective (RPO):** `{{RPO_MINUTES}}`

### Impact Categories
| Category | Description | Impact | Tolerance |
|---|---|---|---|
| Users | `{{USER_IMPACT}}` | `{{USER_IMPACT_LEVEL}}` | `{{USER_TOLERANCE}}` |
| Revenue | `{{REVENUE_IMPACT}}` | `{{REVENUE_IMPACT_LEVEL}}` | `{{REVENUE_TOLERANCE}}` |
| Compliance | `{{COMPLIANCE_IMPACT}}` | `{{COMPLIANCE_IMPACT_LEVEL}}` | `{{COMPLIANCE_TOLERANCE}}` |
| Brand | `{{BRAND_IMPACT}}` | `{{BRAND_IMPACT_LEVEL}}` | `{{BRAND_TOLERANCE}}` |

### Notes
- Control dependencies with `{{CONTROL_MECHANISMS}}`.
- Document automation runbooks referenced by this BIA.

## Source Attribution
- Source manifests: `operations__nist_cisa.md`
- Primary source basis: NIST SP 800-34 Rev. 1
- Alignment mode: guided-synthesis
- Reviewed on: 2026-03-27
