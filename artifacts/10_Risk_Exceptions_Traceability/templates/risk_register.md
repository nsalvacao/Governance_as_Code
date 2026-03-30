---
title: Risk Register Template
artifact_type: template
status: public
visibility: public
classification: public
owner: "{{RISK_OWNER}}"
review_cadence: monthly
applies_to: project, service, and governance risks
source_basis: NIST risk management guidance and Microsoft Learn governance practices
source_manifests:
  - operations__nist_cisa.md
  - platform__microsoft_learn.md
alignment_mode: hybrid-synthesis
updated: 2026-03-30
---

## Risk Appetite Statement

ISO 31000:2018 Clause 5.3 requires the organisation to define and communicate its risk appetite before risks are assessed. Without a declared appetite, treatment decisions lack a consistent reference point.

| Risk Category | Appetite Level | Maximum Acceptable Score | Rationale |
|---|---|---|---|
| Strategic | `{{STR_APPETITE}}` (Zero / Low / Medium / High) | `{{STR_MAX_SCORE}}` | `{{STR_APPETITE_RATIONALE}}` |
| Operational | `{{OPS_APPETITE}}` | `{{OPS_MAX_SCORE}}` | `{{OPS_APPETITE_RATIONALE}}` |
| Security | `{{SEC_APPETITE}}` | `{{SEC_MAX_SCORE}}` | `{{SEC_APPETITE_RATIONALE}}` |
| Compliance | `{{COM_APPETITE}}` | `{{COM_MAX_SCORE}}` | `{{COM_APPETITE_RATIONALE}}` |
| Financial | `{{FIN_APPETITE}}` | `{{FIN_MAX_SCORE}}` | `{{FIN_APPETITE_RATIONALE}}` |
| Technical | `{{TEC_APPETITE}}` | `{{TEC_MAX_SCORE}}` | `{{TEC_APPETITE_RATIONALE}}` |

Approved by: `{{RISK_APPETITE_APPROVER}}` — Date: `{{RISK_APPETITE_APPROVED_DATE}}`

Any risk with a residual score exceeding its category's maximum acceptable score requires escalation to `{{RISK_ESCALATION_AUTHORITY}}`.

## Register Metadata

| Field | Value |
|---|---|
| Register Owner | `{{REGISTER_OWNER}}` |
| Scope | `{{RISK_REGISTER_SCOPE}}` (e.g., project name, service name, programme) |
| Risk Framework | ISO 31000:2018 + NIST RMF (SP 800-37 Rev.2) |
| Review Cadence | `{{REVIEW_CADENCE}}` |
| Last Reviewed | `{{LAST_REVIEWED_DATE}}` |
| Next Review | `{{NEXT_REVIEW_DATE}}` |

## Risk Register

| Risk ID | Category | Description | Likelihood (1–5) | Impact (1–5) | Risk Score | Inherent Risk Level | Treatment Strategy | Mitigation / Control | Residual Likelihood | Residual Impact | Residual Score | Status | Owner | Review Date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `{{RISK_ID_1}}` | `{{CATEGORY_1}}` | `{{DESCRIPTION_1}}` | `{{L_1}}` | `{{I_1}}` | `{{RISK_SCORE_1}}` | `{{INHERENT_LEVEL_1}}` | `{{TREATMENT_1}}` | `{{MITIGATION_1}}` | `{{RL_1}}` | `{{RI_1}}` | `{{RS_1}}` | `{{STATUS_1}}` | `{{OWNER_1}}` | `{{REVIEW_1}}` |
| `{{RISK_ID_2}}` | `{{CATEGORY_2}}` | `{{DESCRIPTION_2}}` | `{{L_2}}` | `{{I_2}}` | `{{RISK_SCORE_2}}` | `{{INHERENT_LEVEL_2}}` | `{{TREATMENT_2}}` | `{{MITIGATION_2}}` | `{{RL_2}}` | `{{RI_2}}` | `{{RS_2}}` | `{{STATUS_2}}` | `{{OWNER_2}}` | `{{REVIEW_2}}` |

## Scoring Scales

### Likelihood Scale

| Score | Label | Description |
|---|---|---|
| 1 | Rare | May occur only in exceptional circumstances (<10% probability) |
| 2 | Unlikely | Could occur at some time (10–30%) |
| 3 | Possible | Might occur at some time (30–50%) |
| 4 | Likely | Will probably occur in most circumstances (50–70%) |
| 5 | Almost Certain | Expected to occur in most circumstances (>70%) |

### Impact Scale

| Score | Label | Description |
|---|---|---|
| 1 | Insignificant | Negligible business impact |
| 2 | Minor | Limited impact; resolved quickly with minimal cost |
| 3 | Moderate | Significant but manageable impact; requires escalation |
| 4 | Major | Serious impact on objectives, reputation, or financials |
| 5 | Catastrophic | Existential risk; regulatory breach; major financial loss |

### Risk Level Matrix

| Score Range | Level | Colour | Required Response |
|---|---|---|---|
| 1–4 | Low | Green | Accept; monitor |
| 5–9 | Medium | Yellow | Mitigate; owner accountability |
| 10–16 | High | Orange | Active mitigation plan; monthly review |
| 17–25 | Critical | Red | Immediate escalation to `{{CRITICAL_RISK_ESCALATION}}`; weekly review |

## Treatment Strategies

| Strategy | When to Use |
|---|---|
| **Accept** | Risk score ≤ `{{ACCEPT_THRESHOLD}}`; residual risk within appetite |
| **Mitigate** | Reduce likelihood or impact via control; preferred for medium/high risks |
| **Transfer** | Shift risk to third party (insurance, contract); appropriate for financial risks |
| **Avoid** | Eliminate the activity that creates the risk; used when mitigation cost > impact |

## Risk Categories

| Code | Category | Examples |
|---|---|---|
| STR | Strategic | Business model, competitive, regulatory change |
| OPS | Operational | Process failure, supply chain, third-party dependency |
| SEC | Security | Data breach, insider threat, vulnerability exploitation |
| COM | Compliance | Regulatory violation, contractual breach, audit finding |
| FIN | Financial | Budget overrun, cost variance, fraud |
| TEC | Technical | Architecture failure, scalability, tech debt |
| REP | Reputational | Brand damage, public incident, negative press |

## Source Attribution

- Source manifests: operations__nist_cisa.md, platform__microsoft_learn.md
- Primary source basis: NIST risk management guidance and Microsoft Learn governance practices
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-30
