---
title: CI Workflow / Build Pipeline Record
artifact_type: template
status: public
visibility: public
classification: public
owner: platform-governance
review_cadence: quarterly
applies_to: repositories with automated build and validation workflows
source_basis: GitHub Actions workflow and build traceability guidance
source_manifests:
  - governance__github_docs.md
  - platform__microsoft_learn.md
alignment_mode: hybrid-synthesis
updated: 2026-03-30
---

# CI Workflow / Build Pipeline Record

## Pipeline Metadata

| Field | Value |
|---|---|
| Workflow Name | `{{WORKFLOW_NAME}}` |
| Workflow File | `.github/workflows/{{WORKFLOW_FILENAME}}.yml` |
| Build ID | `{{BUILD_ID}}` |
| Repository | `{{REPOSITORY}}` |
| Owner | `{{OWNER}}` |
| Record Date | `{{RECORD_DATE}}` |

## Trigger Configuration

| Trigger Event | Branches / Conditions | Notes |
|---|---|---|
| `{{TRIGGER_1}}` (e.g., `push`) | `{{TRIGGER_1_BRANCHES}}` | `{{TRIGGER_1_NOTES}}` |
| `{{TRIGGER_2}}` (e.g., `pull_request`) | `{{TRIGGER_2_BRANCHES}}` | `{{TRIGGER_2_NOTES}}` |
| `{{TRIGGER_3}}` (e.g., `workflow_dispatch`) | Manual | `{{TRIGGER_3_NOTES}}` |

Path filters: `{{PATH_FILTERS}}` (e.g., `artifacts/**`, `scripts/**`)

## Runner Configuration

| Property | Value |
|---|---|
| Runner type | `{{RUNNER_TYPE}}` (e.g., `ubuntu-latest`, self-hosted: `{{RUNNER_LABEL}}`) |
| Timeout | `{{JOB_TIMEOUT}}` minutes |
| Concurrency group | `{{CONCURRENCY_GROUP}}` |
| Cancel in-progress | `{{CANCEL_IN_PROGRESS}}` |

## Pipeline Steps

| Step # | Step Name | Purpose | Tool / Action | Expected Output | DORA Metric Gate |
|---|---|---|---|---|---|
| 1 | Checkout | Fetch source at `{{SOURCE_COMMIT}}` | `actions/checkout@{{CHECKOUT_VERSION}}` | Clean workspace | |
| 2 | `{{STEP_2_NAME}}` (e.g., Setup runtime) | `{{STEP_2_PURPOSE}}` | `{{STEP_2_ACTION}}` | `{{STEP_2_OUTPUT}}` | |
| 3 | Build | Compile / package source | `{{BUILD_COMMAND}}` | Artifact at `{{ARTIFACT_PATH}}` | |
| 4 | Unit tests | Verify unit-level behaviour | `{{UNIT_TEST_COMMAND}}` | `{{UNIT_TEST_REPORT}}` | Deployment frequency gate |
| 5 | Integration tests | `{{INTEGRATION_TEST_DESCRIPTION}}` | `{{INTEGRATION_TEST_COMMAND}}` | `{{INTEGRATION_TEST_REPORT}}` | |
| 6 | Static analysis / lint | `{{LINT_DESCRIPTION}}` | `{{LINT_COMMAND}}` | `{{LINT_REPORT}}` | |
| 7 | Security scan (SAST) | Identify vulnerable code patterns | `{{SAST_TOOL}}` | `{{SAST_REPORT_PATH}}` | |
| 8 | Dependency review | Check for vulnerable dependencies | `{{DEP_REVIEW_ACTION}}` | `{{DEP_REPORT_PATH}}` | |
| 9 | Artifact publish | Store build output for CD | `{{ARTIFACT_UPLOAD_ACTION}}` | `{{ARTIFACT_NAME}}` at `{{ARTIFACT_LOCATION}}` | |
| 10 | Governance validator | Enforce artifact standards | `python3 scripts/validate_governance_artifacts.py` | Exit 0 | |

## Outputs and Metrics

| Output | Value / Location |
|---|---|
| Build artifact | `{{ARTIFACT_PATH}}` |
| Test summary | `{{TEST_SUMMARY_LINK}}` |
| Coverage report | `{{COVERAGE_REPORT_LINK}}` |
| Security scan report | `{{SAST_REPORT_LINK}}` |
| Lead time for this build | `{{LEAD_TIME}}` (time from commit to pipeline completion) |
| Deployment eligibility | `{{DEPLOYMENT_ELIGIBILITY}}` (Pass / Fail / Conditional) |

## DORA Metrics Instrumentation

| Metric | Instrumented? | Data Source |
|---|---|---|
| Deployment frequency | `{{DF_INSTRUMENTED}}` | `{{DF_DATA_SOURCE}}` |
| Lead time for changes | `{{LT_INSTRUMENTED}}` | `{{LT_DATA_SOURCE}}` |
| Change failure rate | `{{CFR_INSTRUMENTED}}` | `{{CFR_DATA_SOURCE}}` |
| MTTR | `{{MTTR_INSTRUMENTED}}` | `{{MTTR_DATA_SOURCE}}` |

## Source Attribution

- Source manifests: `governance__github_docs.md`, `platform__microsoft_learn.md`
- Primary source basis: GitHub Actions and build traceability guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-30
