---
title: Status / Highlight Report
artifact_type: template
status: public
visibility: public
classification: public
owner: GOVERNANCE
review_cadence: quarterly
applies_to: project progress reporting
source_basis: PRINCE2, PMI
source_manifests:
  - project__prince2.md
  - project__pmi.md
alignment_mode: hybrid-synthesis
updated: 2026-03-30
---

# Status / Highlight Report

## Purpose

Provide a periodic, concise view of project progress, health, and deviations from plan for the project board or sponsor (PRINCE2 2023 Highlight Report).

## Report Metadata

| Field | Value |
|---|---|
| Project | `{{PROJECT_NAME}}` |
| Report ID | `{{REPORT_ID}}` |
| Reporting Period | `{{PERIOD_START}}` to `{{PERIOD_END}}` |
| Report Date | `{{REPORT_DATE}}` |
| Prepared By | `{{PM}}` |
| Submitted To | `{{PROJECT_BOARD}}` / `{{SPONSOR}}` |

## Overall Status

| Dimension | Status | RAG | Notes |
|---|---|---|---|
| Overall | `{{OVERALL_STATUS}}` | `{{OVERALL_RAG}}` | |
| Time | `{{TIME_STATUS}}` | `{{TIME_RAG}}` | Forecast completion: `{{FORECAST_COMPLETION}}` |
| Cost | `{{COST_STATUS}}` | `{{COST_RAG}}` | Spend to date: `{{SPEND_TO_DATE}}` / Budget: `{{BUDGET}}` |
| Scope | `{{SCOPE_STATUS}}` | `{{SCOPE_RAG}}` | |
| Quality | `{{QUALITY_STATUS}}` | `{{QUALITY_RAG}}` | |
| Benefits | `{{BENEFITS_STATUS}}` | `{{BENEFITS_RAG}}` | |

RAG: 🟢 Green (on track) / 🟡 Amber (at risk / monitor) / 🔴 Red (exception / action required)

## Work Accomplished This Period

| Work Package / Deliverable | Status | Notes |
|---|---|---|
| `{{WP_1}}` | `{{WP_1_STATUS}}` | `{{WP_1_NOTES}}` |
| `{{WP_2}}` | `{{WP_2_STATUS}}` | `{{WP_2_NOTES}}` |

## Work Planned for Next Period

| Work Package / Deliverable | Target Completion | Owner |
|---|---|---|
| `{{NEXT_WP_1}}` | `{{NEXT_WP_1_DATE}}` | `{{NEXT_WP_1_OWNER}}` |
| `{{NEXT_WP_2}}` | `{{NEXT_WP_2_DATE}}` | `{{NEXT_WP_2_OWNER}}` |

## Key Milestones

| Milestone | Planned Date | Forecast Date | Status |
|---|---|---|---|
| `{{MILESTONE_1}}` | `{{MILESTONE_1_PLANNED}}` | `{{MILESTONE_1_FORECAST}}` | `{{MILESTONE_1_STATUS}}` |

## Risks (Top `{{TOP_N_RISKS}}`)

| Risk ID | Description | Probability | Impact | RAG | Owner | Action |
|---|---|---|---|---|---|---|
| `{{RISK_ID_1}}` | `{{RISK_DESC_1}}` | `{{RISK_PROB_1}}` | `{{RISK_IMPACT_1}}` | `{{RISK_RAG_1}}` | `{{RISK_OWNER_1}}` | `{{RISK_ACTION_1}}` |

## Issues

| Issue ID | Description | Priority | Owner | Status | Resolution |
|---|---|---|---|---|---|
| `{{ISSUE_ID_1}}` | `{{ISSUE_DESC_1}}` | `{{ISSUE_PRIORITY_1}}` | `{{ISSUE_OWNER_1}}` | `{{ISSUE_STATUS_1}}` | `{{ISSUE_RESOLUTION_1}}` |

## Exceptions and Tolerance Breaches

_If tolerances are being breached or are forecast to breach, an Exception Report must be raised separately._

`{{EXCEPTION_SUMMARY}}` — Exception Report: `{{EXCEPTION_REPORT_LINK}}` (if applicable)

## Decisions Required

| Decision | Required By | Owner | Options |
|---|---|---|---|
| `{{DECISION_1}}` | `{{DECISION_1_DEADLINE}}` | `{{DECISION_1_OWNER}}` | `{{DECISION_1_OPTIONS}}` |

## Next Scheduled Report

`{{NEXT_REPORT_DATE}}`

## Source Attribution

- Source manifests: `project__prince2.md`, `project__pmi.md`
- Primary source basis: PRINCE2 and PMI reporting guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-30
