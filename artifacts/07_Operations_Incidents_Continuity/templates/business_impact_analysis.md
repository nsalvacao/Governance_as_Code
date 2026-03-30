---
title: Business Impact Analysis Template
artifact_type: template
status: public
visibility: public
classification: public
owner: "{{OWNER_NAME}}"
review_cadence: semiannually
applies_to: continuity planning
source_basis: NIST SP 800-34 Rev. 1
source_manifests: operations__nist_cisa.md
alignment_mode: guided-synthesis
updated: 2026-03-30
---

## System Identification

Identify the system under analysis. All fields are mandatory; incomplete identification blocks must not be used to set contractual recovery commitments.

- **System name:** `{{SYSTEM_NAME}}`
- **System owner:** `{{SYSTEM_OWNER}}`
- **System classification:** `{{SYSTEM_CLASSIFICATION}}`
- **System description:** `{{SYSTEM_DESCRIPTION}}`
- **System tier:** `{{SYSTEM_TIER}}`
- **Primary contacts:** `{{PRIMARY_CONTACT}}`, `{{SECONDARY_CONTACT}}`
- **Executive sponsor:** `{{EXECUTIVE_SPONSOR}}`
- **BIA completed by:** `{{BIA_AUTHOR}}`
- **BIA completion date:** `{{BIA_DATE}}`
- **Next review date:** `{{NEXT_REVIEW_DATE}}`

## Mission-Critical Functions

List every business function performed by or dependent on this system. Assign a unique Function ID and set recovery objectives for each. Priority values: 1 = must restore first, 2 = restore after priority 1 functions, 3 = restore when resources allow.

| Function ID | Function Description | Supporting Resources | RTO | RPO | MTD | Priority |
|---|---|---|---|---|---|---|
| `{{FUNCTION_ID}}` | `{{FUNCTION_DESCRIPTION}}` | `{{SUPPORTING_RESOURCES}}` | `{{RTO}}` | `{{RPO}}` | `{{MTD}}` | `{{PRIORITY_LEVEL}}` |

Add one row per mission-critical function. RTO must be less than or equal to MTD. RPO is expressed as maximum data age at recovery (e.g., 4 hours). MTD is the absolute outer bound beyond which the disruption becomes unacceptable.

## Function-to-Function Dependency Map

NIST SP 800-34 Rev.1 requires mapping inter-function dependencies to ensure recovery sequencing accounts for cascading failures. If Function A depends on Function B, Function A's RTO must be ≥ Function B's RTO — otherwise the recovery target is unachievable.

| Dependent Function ID | Depends On (Function ID) | Dependency Type | RTO Impact | Recovery Sequence Note |
|---|---|---|---|---|
| `{{DEPENDENT_FUNCTION_ID}}` | `{{REQUIRED_FUNCTION_ID}}` | `{{DEPENDENCY_TYPE}}` (hard / soft / optional) | `{{RTO_IMPACT}}` (e.g., +2h if {{REQUIRED_FUNCTION_ID}} not restored first) | `{{RECOVERY_SEQUENCE_NOTE}}` |

Verify: for each dependent function, confirm its RTO ≥ the RTO of all functions it depends on. Flag any inversion as a planning risk.

## Resource Dependencies Matrix

Map each key resource to the functions it supports. This matrix is used during recovery to determine the minimum resource set needed to restore each priority tier.

| Resource Name | Resource Type | Functions Supported | Owner | SPOF (Y/N) | Notes |
|---|---|---|---|---|---|
| `{{RESOURCE_NAME}}` | `{{RESOURCE_TYPE}}` | `{{FUNCTIONS_SUPPORTED}}` | `{{RESOURCE_OWNER}}` | `{{SPOF_FLAG}}` | `{{RESOURCE_NOTES}}` |

Resource types include: application, database, infrastructure, network, personnel, facility, third-party service. Flag single points of failure with `{{SPOF_FLAG}}`.

## Outage Impact Assessment

For each plausible outage scenario, quantify the impact across four categories. Use this section to justify the RTO, RPO, and MTD values assigned above.

| Outage Scenario | Duration | Financial Impact | Operational Impact | Reputational Impact | Regulatory Impact |
|---|---|---|---|---|---|
| `{{OUTAGE_SCENARIO}}` | `{{OUTAGE_DURATION}}` | `{{FINANCIAL_IMPACT}}` | `{{OPERATIONAL_IMPACT}}` | `{{REPUTATIONAL_IMPACT}}` | `{{REGULATORY_IMPACT}}` |

Financial impact should be expressed as estimated loss per hour or per incident. Regulatory impact must reference specific obligations (e.g., `{{REGULATORY_REFERENCE}}`).

## Recovery Priorities

Translate the function priority rankings into a sequenced recovery plan. For each priority level, identify the minimum resources required to begin recovery operations.

| Priority Level | Function | Minimum Resources Required | Recovery Team Lead |
|---|---|---|---|
| `{{PRIORITY_LEVEL}}` | `{{FUNCTION_DESCRIPTION}}` | `{{MINIMUM_RESOURCES}}` | `{{RECOVERY_TEAM_LEAD}}` |

This table drives the recovery phase of the contingency plan. Ensure minimum resource requirements are achievable with the resources available at the alternate processing site `{{ALT_SITE}}`.

## BIA Approval

The BIA is considered complete when all sections are populated, recovery objectives are approved by the system owner, and the document has been reviewed by the contingency planning coordinator.

- **Prepared by:** `{{BIA_AUTHOR}}`
- **Reviewed by:** `{{BIA_REVIEWER}}`
- **Approved by:** `{{BIA_APPROVER}}`
- **Approval date:** `{{BIA_DATE}}`
- **Next scheduled review:** `{{NEXT_REVIEW_DATE}}`

## Source Attribution

- Source manifests: `operations__nist_cisa.md`
- Primary source basis: NIST SP 800-34 Rev. 1 section 2.2 BIA template
- Alignment mode: guided-synthesis
- Reviewed on: 2026-03-30
