---
title: Known Error Record
artifact_type: template
status: public-draft
visibility: public
classification: public
owner: "{{GOVERNANCE_OWNER}}"
review_cadence: quarterly
applies_to: diagnosed but unresolved errors and workarounds
source_basis: ITIL, NIST
source_manifests:
  - service_mgmt__itil.md
  - operations__nist_cisa.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

# Known Error Record

## Purpose

Record a diagnosed but unresolved error, its impact, and its workaround until a permanent fix is available (ITIL 4 Known Error Database — KEDB).

## Known Error Metadata

| Field | Value |
|---|---|
| Known Error ID | `{{KNOWN_ERROR_ID}}` (e.g., KE-2026-007) |
| Title | `{{KNOWN_ERROR_TITLE}}` |
| Status | `{{KNOWN_ERROR_STATUS}}` (Active / Workaround Available / Fix Scheduled / Resolved / Closed) |
| Discovery Date | `{{DISCOVERY_DATE}}` |
| Last Updated | `{{LAST_UPDATED}}` |
| Owner | `{{KNOWN_ERROR_OWNER}}` |
| Priority | `{{PRIORITY}}` (Critical / High / Medium / Low) |

## Affected Items

| Affected Service | Affected Component | Affected Versions | Impact Scope |
|---|---|---|---|
| `{{AFFECTED_SERVICE_1}}` | `{{AFFECTED_COMPONENT_1}}` | `{{AFFECTED_VERSIONS_1}}` | `{{IMPACT_SCOPE_1}}` |

## Error Description

**Symptoms** (what users/operators observe):
`{{ERROR_SYMPTOMS}}`

**Trigger conditions** (when/how the error manifests):
`{{TRIGGER_CONDITIONS}}`

**Frequency / Recurrence pattern**:
`{{RECURRENCE_PATTERN}}`

## Root Cause

**Root cause**: `{{ROOT_CAUSE}}`

**Supporting evidence**: `{{ROOT_CAUSE_EVIDENCE_LINK}}`

**Problem record reference**: `{{PROBLEM_RECORD_LINK}}`

**Contributing factors**: `{{CONTRIBUTING_FACTORS}}`

## Workaround

**Workaround available**: `{{WORKAROUND_AVAILABLE}}` (Yes / No / Partial)

**Workaround steps**:

1. `{{WORKAROUND_STEP_1}}`
2. `{{WORKAROUND_STEP_2}}`
3. `{{WORKAROUND_STEP_3}}`

**Workaround limitations**: `{{WORKAROUND_LIMITATIONS}}`

**Workaround effectiveness**: `{{WORKAROUND_EFFECTIVENESS}}` (Fully Effective / Partially Effective / Unreliable) — Effectiveness score: `{{WORKAROUND_EFFECTIVENESS_SCORE}}` (1 = barely usable, 5 = fully resolves impact). ITIL 4 KEDB requires effectiveness tracking to determine whether re-categorisation as a problem is needed.

**Workaround owner**: `{{WORKAROUND_OWNER}}`

## Permanent Fix

| Field | Value |
|---|---|
| Fix Status | `{{FIX_STATUS}}` (Under development / Scheduled / Deployed / No fix planned) |
| Fix Description | `{{FIX_DESCRIPTION}}` |
| Fix Target Date | `{{FIX_TARGET_DATE}}` |
| Change Record Reference | `{{CHANGE_RECORD_LINK}}` |
| Fix Deployed Date | `{{FIX_DEPLOYED_DATE}}` |

**Reason if no fix planned**: `{{NO_FIX_RATIONALE}}`

## Impact and Risk

**Business impact of leaving unresolved**: `{{BUSINESS_IMPACT_UNRESOLVED}}`

**Customer-visible impact**: `{{CUSTOMER_IMPACT}}`

**Error budget impact per occurrence**: `{{ERROR_BUDGET_IMPACT}}`

## Linked Records

| Record Type | ID / Link |
|---|---|
| Problem Record | `{{PROBLEM_RECORD_LINK}}` |
| Related Incidents | `{{LINKED_INCIDENTS}}` |
| Change Record (fix) | `{{CHANGE_RECORD_LINK}}` |
| SLA Impact | `{{SLA_IMPACT_REFERENCE}}` |

## Source Attribution

- Source manifests: `service_mgmt__itil.md`, `operations__nist_cisa.md`
- Primary source basis: ITIL known error management guidance and NIST incident learning practices
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
