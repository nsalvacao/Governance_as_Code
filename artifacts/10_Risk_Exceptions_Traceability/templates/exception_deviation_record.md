---
title: Exception and Deviation Record Template
artifact_type: template
status: public
visibility: public
classification: public
owner: risk-platform
review_cadence: monthly
applies_to: approved exceptions and controlled policy deviations
source_basis: NIST control exception handling and Microsoft Learn governance guidance
source_manifests:
  - operations__nist_cisa.md
  - platform__microsoft_learn.md
alignment_mode: hybrid-synthesis
updated: 2026-03-30
---

## Exception Record

| Field | Value |
|---|---|
| Exception ID | `{{EXCEPTION_ID}}` (e.g., EX-2026-042) |
| Title | `{{EXCEPTION_TITLE}}` |
| Status | `{{EXCEPTION_STATUS}}` (Pending / Approved / Active / Expired / Closed) |
| Requested By | `{{REQUESTER}}` |
| Request Date | `{{REQUEST_DATE}}` |
| Approved By | `{{APPROVER}}` |
| Approval Date | `{{APPROVAL_DATE}}` |
| Effective Date | `{{EFFECTIVE_DATE}}` |
| Expiry Date | `{{EXPIRY_DATE}}` |
| Review Date | `{{REVIEW_DATE}}` |

## Policy / Control Deviation

| Field | Value |
|---|---|
| Policy / Control Affected | `{{POLICY_OR_CONTROL_ID}}` — `{{POLICY_OR_CONTROL_NAME}}` |
| Control Requirement | `{{CONTROL_REQUIREMENT}}` (what the policy normally requires) |
| Deviation Type | `{{DEVIATION_TYPE}}` (Temporary waiver / Permanent exception / Alternative implementation / Out-of-scope exclusion) |
| Affected System / Scope | `{{AFFECTED_SCOPE}}` |
| Affected Versions | `{{AFFECTED_VERSIONS}}` |

## Business Justification

<!-- Why is compliance with the standard not feasible or appropriate in this case? -->
`{{BUSINESS_JUSTIFICATION}}`

Reference: `{{JUSTIFICATION_EVIDENCE_LINK}}` (e.g., cost analysis, architectural constraint, vendor limitation)

## Risk Assessment

| Risk Dimension | Assessment |
|---|---|
| Risk Description | `{{RISK_DESCRIPTION}}` |
| Likelihood (1–5) | `{{LIKELIHOOD}}` |
| Impact (1–5) | `{{IMPACT}}` |
| Risk Score (L×I) | `{{RISK_SCORE}}` |
| Risk Category | `{{RISK_CATEGORY}}` (Strategic / Operational / Compliance / Financial / Reputational) |
| Risk Acceptance Authority | `{{RISK_ACCEPTANCE_AUTHORITY}}` |
| Linked Risk Register Entry | `{{RISK_REGISTER_LINK}}` |

## Compensating Controls

Controls implemented to reduce the risk introduced by this deviation:

| Control ID | Description | Owner | Verification Method | Verified? |
|---|---|---|---|---|
| `{{COMP_CONTROL_1_ID}}` | `{{COMP_CONTROL_1_DESC}}` | `{{COMP_CONTROL_1_OWNER}}` | `{{COMP_CONTROL_1_VERIFY}}` | `{{COMP_CONTROL_1_VERIFIED}}` |
| `{{COMP_CONTROL_2_ID}}` | `{{COMP_CONTROL_2_DESC}}` | `{{COMP_CONTROL_2_OWNER}}` | `{{COMP_CONTROL_2_VERIFY}}` | `{{COMP_CONTROL_2_VERIFIED}}` |

## Conditions and Obligations

Conditions that MUST be met for this exception to remain valid:

1. `{{CONDITION_1}}` — verified by `{{CONDITION_1_VERIFIER}}` by `{{CONDITION_1_DUE_DATE}}`
2. `{{CONDITION_2}}` — verified by `{{CONDITION_2_VERIFIER}}` by `{{CONDITION_2_DUE_DATE}}`

If any condition is not met, this exception becomes invalid and `{{EXCEPTION_REVOCATION_OWNER}}` must revoke approval.

## Renewal / Closure

| Field | Value |
|---|---|
| Renewal Allowed? | `{{RENEWAL_ALLOWED}}` (Yes / No / Conditional) |
| Renewal Requires | `{{RENEWAL_REQUIREMENTS}}` (e.g., full re-assessment, updated risk acceptance) |
| Closure Criteria | `{{CLOSURE_CRITERIA}}` (what must be true to close this exception) |
| Closed By | `{{CLOSED_BY}}` |
| Closure Date | `{{CLOSURE_DATE}}` |

## Source Attribution

- Source manifests: operations__nist_cisa.md, platform__microsoft_learn.md
- Primary source basis: NIST control exception handling and Microsoft Learn governance guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-30
