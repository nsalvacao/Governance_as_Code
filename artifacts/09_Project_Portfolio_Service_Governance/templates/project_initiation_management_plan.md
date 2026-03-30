---
title: Project Initiation / Management Plan
artifact_type: template
status: public
visibility: public
classification: public
owner: "{{GOVERNANCE_OWNER}}"
review_cadence: quarterly
applies_to: project baseline planning and governance setup
source_basis: PMI, PRINCE2
source_manifests:
  - project__pmi.md
  - project__prince2.md
alignment_mode: hybrid-synthesis
updated: 2026-03-30
---

# Project Initiation / Management Plan

## Purpose

Define the baseline for planning, controls, delivery approach, and governance, forming the contract between the project and its sponsoring organisation (PRINCE2 2023 Project Initiation Document + PMI Project Management Plan).

## Plan Metadata

| Field | Value |
|---|---|
| Project | `{{PROJECT_NAME}}` |
| Plan Version | `{{PLAN_VERSION}}` |
| Plan Author | `{{PM}}` |
| Date | `{{PLAN_DATE}}` |
| Approved By | `{{APPROVER}}` |
| Approval Date | `{{APPROVAL_DATE}}` |
| Cross-references | Charter: `{{CHARTER_LINK}}`, Business Case: `{{BC_LINK}}` |

## Delivery Approach

**Delivery methodology**: `{{DELIVERY_METHODOLOGY}}` (e.g., Scrum, Kanban, PRINCE2, hybrid)

**Delivery phases / stages**:

| Stage | Objectives | Key Deliverables | Start Date | End Date | Approval Gate |
|---|---|---|---|---|---|
| Initiation | `{{STAGE_1_OBJECTIVES}}` | `{{STAGE_1_DELIVERABLES}}` | `{{STAGE_1_START}}` | `{{STAGE_1_END}}` | `{{STAGE_1_GATE}}` |
| `{{STAGE_2}}` | `{{STAGE_2_OBJECTIVES}}` | `{{STAGE_2_DELIVERABLES}}` | `{{STAGE_2_START}}` | `{{STAGE_2_END}}` | `{{STAGE_2_GATE}}` |
| Closure | `{{CLOSURE_OBJECTIVES}}` | `{{CLOSURE_DELIVERABLES}}` | `{{CLOSURE_START}}` | `{{CLOSURE_END}}` | `{{CLOSURE_GATE}}` |

## Governance Cadence

| Review Type | Frequency | Owner | Output |
|---|---|---|---|
| Team stand-up | `{{STANDUP_CADENCE}}` | `{{PM}}` | Blocker log updated |
| Highlight report to sponsor | `{{HIGHLIGHT_CADENCE}}` | `{{PM}}` | Highlight report sent |
| Stage-end review | At each stage gate | `{{PROJECT_BOARD}}` | Stage authorization |
| Risk and issue review | `{{RISK_REVIEW_CADENCE}}` | `{{PM}}` | Risk register updated |
| Change control review | As needed | `{{CHANGE_AUTHORITY}}` | Change log updated |

## Planning Baselines

PRINCE2 2023 mandates six performance targets. All six must be baselined at project initiation. Omitting any baseline means the project board cannot authorise work or escalate exceptions for that dimension.

| Dimension | Baseline | Tolerance | Change Authority |
|---|---|---|---|
| Time | `{{TIME_BASELINE}}` | ± `{{TIME_TOLERANCE}}` | `{{TIME_CHANGE_AUTHORITY}}` |
| Cost | `{{COST_BASELINE}}` | ± `{{COST_TOLERANCE}}` | `{{COST_CHANGE_AUTHORITY}}` |
| Scope | `{{SCOPE_BASELINE}}` | `{{SCOPE_TOLERANCE}}` | `{{SCOPE_CHANGE_AUTHORITY}}` |
| Quality | `{{QUALITY_CRITERIA}}` | `{{QUALITY_TOLERANCE}}` | `{{QUALITY_AUTHORITY}}` |
| Benefits | `{{BENEFITS_BASELINE}}` — key metric: `{{BENEFITS_KEY_METRIC}}` | `{{BENEFITS_TOLERANCE}}` | `{{BENEFITS_AUTHORITY}}` |
| Risk | Risk appetite: `{{RISK_APPETITE_STATEMENT}}` | `{{RISK_TOLERANCE_THRESHOLD}}` | `{{RISK_AUTHORITY}}` |

## Risk and Issue Management

- Risk register location: `{{RISK_REGISTER_LINK}}`
- Issue log location: `{{ISSUE_LOG_LINK}}`
- Risk review owner: `{{RISK_REVIEW_OWNER}}`
- Escalation trigger: tolerance breach or risk score > `{{ESCALATION_RISK_THRESHOLD}}`
- Risk appetite: `{{RISK_APPETITE_STATEMENT}}`

## Quality Controls

| Control | Method | Owner | Frequency |
|---|---|---|---|
| Product quality review | `{{QUALITY_REVIEW_METHOD}}` | `{{QUALITY_REVIEWER}}` | Per deliverable |
| Process audit | `{{AUDIT_METHOD}}` | `{{AUDIT_OWNER}}` | `{{AUDIT_CADENCE}}` |
| Acceptance criteria verification | `{{ACCEPTANCE_METHOD}}` | `{{ACCEPTANCE_OWNER}}` | At stage end |

## Communication Plan Reference

See Communications Management Plan at `{{COMMS_PLAN_LINK}}` for the full stakeholder communication matrix.

## Change Control

Changes to this plan require:

1. Change request raised in `{{CHANGE_REQUEST_TOOL}}`
2. Impact assessment by `{{PM}}`
3. Approval by `{{CHANGE_AUTHORITY}}`
4. Baseline updated and version incremented

Changes outside tolerances require Exception Report to `{{PROJECT_BOARD}}`.

## Source Attribution

- Source manifests: `project__pmi.md`, `project__prince2.md`
- Primary source basis: PMI and PRINCE2 management planning guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-30
