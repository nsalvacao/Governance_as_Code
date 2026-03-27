---
title: Business Impact Analysis Standard
artifact_type: standard
status: draft
visibility: public
classification: public
owner: "{{OWNER_NAME}}"
review_cadence: semiannually
applies_to: continuity planning
source_basis: NIST SP 800-34 Rev. 1, Google SRE Production Readiness
source_manifests: operations__nist_cisa.md, platform__aws_well_architected.md, operations__google_sre.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Purpose
Define the expected impact on people, finances, compliance, and reputation for each service so that recovery targets can be prioritized deterministically.

## BIA Structure
1. **Business function** – `{{BUSINESS_FUNCTION_NAME}}`
2. **Criticality level** – `{{CRITICALITY_LEVEL}}`
3. **Dependencies** – `{{DEPENDENCIES_LIST}}`
4. **Impact categories** – detail impact on users, revenue, operations, compliance, and brand.
5. **Recovery objectives** – define RTO (`{{RTO_HOURS}}`) and RPO (`{{RPO_MINUTES}}`).
6. **Contacts** – assign primary, secondary, and executive contacts with placeholders like `{{PRIMARY_CONTACT}}`.

## Automation Guidance
- Store the BIA in a structured registry for AI agents to reference when evaluating severity.
- Use the automation validator to ensure every BIA doc includes required metadata.

## Source Attribution
- Source manifests: `operations__nist_cisa.md`, `platform__aws_well_architected.md`, `operations__google_sre.md`
- Primary source basis: NIST SP 800-34 Rev. 1, AWS Operational Readiness, Google SRE Production Readiness Review
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
