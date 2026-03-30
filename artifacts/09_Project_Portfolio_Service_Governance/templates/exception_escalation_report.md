---
title: Exception / Escalation Report
artifact_type: template
status: public
visibility: public
classification: public
owner: GOVERNANCE
review_cadence: quarterly
applies_to: tolerance breaches and escalations
source_basis: PRINCE2
source_manifests:
  - project__prince2.md
alignment_mode: hybrid-synthesis
updated: 2026-03-30
---

# Exception / Escalation Report

## Purpose

Document a forecast or actual deviation from agreed tolerances and request a decision from the appropriate authority (PRINCE2 2023 Exception Report).

## Report Metadata

| Field | Value |
|---|---|
| Exception Report ID | `{{EXCEPTION_REPORT_ID}}` |
| Project | `{{PROJECT_NAME}}` |
| Stage / Work Package | `{{STAGE_OR_WP}}` |
| Reported By | `{{REPORTER}}` (Project Manager) |
| Report Date | `{{REPORT_DATE}}` |
| Decision Required By | `{{DECISION_DEADLINE}}` |
| Escalated To | `{{ESCALATION_AUTHORITY}}` (e.g., Sponsor / Project Board) |

## Exception Type and Description

**Exception Type**: `{{EXCEPTION_TYPE}}`

| Type | Options |
|---|---|
| Scope | Change or reduction to agreed scope |
| Time | Forecast completion outside tolerance: `{{TIME_TOLERANCE}}` |
| Cost | Forecast spend outside tolerance: `{{COST_TOLERANCE}}` |
| Quality | Deliverable below agreed quality criteria |
| Benefits | Forecast benefits below threshold |
| Risk | Risk exposure exceeds agreed risk tolerance |

**Description**: `{{EXCEPTION_DESCRIPTION}}`

**What caused the exception**: `{{EXCEPTION_CAUSE}}`

**Evidence**: `{{EVIDENCE_LINK}}`

## Current Situation

| Dimension | Agreed Baseline | Current Forecast | Variance | Tolerance | Tolerance Breached? |
|---|---|---|---|---|---|
| Time | `{{BASELINE_COMPLETION}}` | `{{FORECAST_COMPLETION}}` | `{{TIME_VARIANCE}}` | ± `{{TIME_TOLERANCE}}` | `{{TIME_BREACH}}` |
| Cost | `{{BASELINE_COST}}` | `{{FORECAST_COST}}` | `{{COST_VARIANCE}}` | ± `{{COST_TOLERANCE}}` | `{{COST_BREACH}}` |
| Scope | `{{BASELINE_SCOPE}}` | `{{FORECAST_SCOPE}}` | `{{SCOPE_VARIANCE}}` | `{{SCOPE_TOLERANCE}}` | `{{SCOPE_BREACH}}` |

## Impact Assessment

**Customer / Business Impact**: `{{BUSINESS_IMPACT}}`

**Knock-on effects**: `{{KNOCK_ON_EFFECTS}}`

**Affected stakeholders**: `{{AFFECTED_STAKEHOLDERS}}`

## Options

| Option | Description | Cost Impact | Time Impact | Scope Impact | Risk | Benefit |
|---|---|---|---|---|---|---|
| Option 1 | `{{OPTION_1_DESC}}` | `{{OPTION_1_COST}}` | `{{OPTION_1_TIME}}` | `{{OPTION_1_SCOPE}}` | `{{OPTION_1_RISK}}` | `{{OPTION_1_BENEFIT}}` |
| Option 2 | `{{OPTION_2_DESC}}` | `{{OPTION_2_COST}}` | `{{OPTION_2_TIME}}` | `{{OPTION_2_SCOPE}}` | `{{OPTION_2_RISK}}` | `{{OPTION_2_BENEFIT}}` |
| Option 3 — Close project | `{{CLOSE_DESC}}` | `{{CLOSE_COST}}` | N/A | N/A | `{{CLOSE_RISK}}` | `{{CLOSE_BENEFIT}}` |

## Recommendation

**Recommended option**: `{{RECOMMENDED_OPTION}}`

**Rationale**: `{{RECOMMENDATION_RATIONALE}}`

**Next steps if approved**: `{{NEXT_STEPS}}`

## Decision

| Decision | Made By | Date | Conditions |
|---|---|---|---|
| `{{DECISION}}` | `{{DECISION_MAKER}}` | `{{DECISION_DATE}}` | `{{DECISION_CONDITIONS}}` |

## Source Attribution

- Source manifests: `project__prince2.md`
- Primary source basis: PRINCE2 exception management guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-30
