---
title: Project Charter / Project Brief
artifact_type: template
status: public-draft
visibility: public
classification: public
owner: "{{GOVERNANCE_OWNER}}"
review_cadence: quarterly
applies_to: project authorization and scope framing
source_basis: PMI, PRINCE2
source_manifests:
  - project__pmi.md
  - project__prince2.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

# Project Charter / Project Brief

## Purpose

Formally authorize the project, define its scope, and identify the accountable owner (PMI PMBOK 7th Edition + PRINCE2 2023 Project Brief).

## Project Identification

| Field | Value |
|---|---|
| Project Name | `{{PROJECT_NAME}}` |
| Project ID | `{{PROJECT_ID}}` |
| Programme / Portfolio | `{{PROGRAMME_NAME}}` |
| Charter Version | `{{CHARTER_VERSION}}` |
| Charter Date | `{{CHARTER_DATE}}` |

## Authorization

| Role | Name | Signature | Date |
|---|---|---|---|
| Sponsor (Executive) | `{{SPONSOR}}` | | `{{SPONSOR_SIGN_DATE}}` |
| Project Manager / Owner | `{{PROJECT_MANAGER}}` | | `{{PM_SIGN_DATE}}` |
| Senior User | `{{SENIOR_USER}}` | | `{{SENIOR_USER_SIGN_DATE}}` |
| Senior Supplier | `{{SENIOR_SUPPLIER}}` | | `{{SENIOR_SUPPLIER_SIGN_DATE}}` |

## Purpose and Strategic Alignment

**Problem or opportunity**: `{{PROBLEM_OR_OPPORTUNITY}}`

**Strategic alignment**: `{{STRATEGIC_ALIGNMENT}}` — links to `{{STRATEGY_DOC_REFERENCE}}`

**Project justification**: `{{PROJECT_JUSTIFICATION}}`

## Objectives and Success Criteria

| Objective | Success Criterion | Measurement Method | Target Date |
|---|---|---|---|
| `{{OBJECTIVE_1}}` | `{{SUCCESS_CRITERION_1}}` | `{{MEASUREMENT_1}}` | `{{TARGET_DATE_1}}` |
| `{{OBJECTIVE_2}}` | `{{SUCCESS_CRITERION_2}}` | `{{MEASUREMENT_2}}` | `{{TARGET_DATE_2}}` |

## High-Level Requirements

PMBOK 7 requires high-level requirements in the charter to establish scope boundaries and drive later detailed requirements work. These are not detailed specifications — they are the non-negotiable conditions the project must satisfy.

| Req ID | Requirement Description | Category | Priority | Source |
|---|---|---|---|---|
| `{{REQ_ID_1}}` | `{{REQ_DESCRIPTION_1}}` | `{{REQ_CATEGORY_1}}` (Functional / Non-functional / Regulatory / Quality) | `{{REQ_PRIORITY_1}}` (Must / Should / Could) | `{{REQ_SOURCE_1}}` |
| `{{REQ_ID_2}}` | `{{REQ_DESCRIPTION_2}}` | `{{REQ_CATEGORY_2}}` | `{{REQ_PRIORITY_2}}` | `{{REQ_SOURCE_2}}` |

Detailed requirements: `{{REQUIREMENTS_DOCUMENT_LINK}}`

## Scope

**In scope**:
- `{{IN_SCOPE_ITEM_1}}`
- `{{IN_SCOPE_ITEM_2}}`

**Out of scope** (explicit exclusions):
- `{{OUT_OF_SCOPE_ITEM_1}}`
- `{{OUT_OF_SCOPE_ITEM_2}}`

## Constraints and Assumptions

| Type | Description | Owner |
|---|---|---|
| Constraint (time) | `{{TIME_CONSTRAINT}}` | `{{CONSTRAINT_OWNER}}` |
| Constraint (cost) | Budget not to exceed `{{BUDGET_LIMIT}}` | `{{BUDGET_OWNER}}` |
| Constraint (quality) | `{{QUALITY_CONSTRAINT}}` | `{{QUALITY_OWNER}}` |
| Assumption | `{{ASSUMPTION_1}}` — see Assumptions Register | `{{ASSUMPTION_OWNER_1}}` |

## High-Level Milestones

| Milestone | Target Date | Owner | Tolerance |
|---|---|---|---|
| Project initiation complete | `{{INITIATION_DATE}}` | `{{PM}}` | `{{INITIATION_TOLERANCE}}` |
| `{{MILESTONE_1}}` | `{{MILESTONE_1_DATE}}` | `{{MILESTONE_1_OWNER}}` | `{{MILESTONE_1_TOLERANCE}}` |
| `{{MILESTONE_2}}` | `{{MILESTONE_2_DATE}}` | `{{MILESTONE_2_OWNER}}` | `{{MILESTONE_2_TOLERANCE}}` |
| Project closure | `{{CLOSURE_DATE}}` | `{{PM}}` | `{{CLOSURE_TOLERANCE}}` |

## Tolerances (PRINCE2 2023)

| Dimension | Tolerance | Escalation Trigger |
|---|---|---|
| Time | ± `{{TIME_TOLERANCE}}` | Forecast breach → Exception Report |
| Cost | ± `{{COST_TOLERANCE}}` | Forecast breach → Exception Report |
| Scope | `{{SCOPE_TOLERANCE}}` | Change beyond this → Change Request |
| Quality | `{{QUALITY_TOLERANCE}}` | Below this → Exception Report |
| Risk | `{{RISK_TOLERANCE}}` | Exceeds → Escalate to `{{SPONSOR}}` |
| Benefits | `{{BENEFITS_TOLERANCE}}` | Below this → Benefits Review |

## Key Risks Summary

PMBOK 7 requires a risks summary in the charter so that authorising bodies understand the risk profile at sign-off. List the top 3–5 risks; full details in the Risk Register.

| Risk ID | Risk Description | Probability | Impact | Mitigation Owner |
|---|---|---|---|---|
| `{{RISK_ID_1}}` | `{{RISK_DESCRIPTION_1}}` | `{{RISK_PROB_1}}` (H/M/L) | `{{RISK_IMPACT_1}}` (H/M/L) | `{{RISK_OWNER_1}}` |
| `{{RISK_ID_2}}` | `{{RISK_DESCRIPTION_2}}` | `{{RISK_PROB_2}}` | `{{RISK_IMPACT_2}}` | `{{RISK_OWNER_2}}` |

Risk tolerance: `{{RISK_TOLERANCE_STATEMENT}}`

Full Risk Register: `{{RISK_REGISTER_LINK}}`

## Key Stakeholders

See Stakeholder Register at `{{STAKEHOLDER_REGISTER_LINK}}`.

| Stakeholder | Role | Interest | Influence |
|---|---|---|---|
| `{{STAKEHOLDER_1}}` | `{{STAKEHOLDER_1_ROLE}}` | `{{STAKEHOLDER_1_INTEREST}}` | `{{STAKEHOLDER_1_INFLUENCE}}` |

## Cross-References

| Document | Link |
|---|---|
| Business Case | `{{BUSINESS_CASE_LINK}}` |
| Project Initiation / Management Plan | `{{PID_LINK}}` |
| Stakeholder Register | `{{STAKEHOLDER_REGISTER_LINK}}` |
| Risk Register | `{{RISK_REGISTER_LINK}}` |

## Source Attribution

- Source manifests: `project__pmi.md`, `project__prince2.md`
- Primary source basis: PMI and PRINCE2 initiation guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
