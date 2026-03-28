---
title: Workflow Definition
artifact_type: standard
status: public-draft
visibility: public
classification: public
owner: "{{OWNER_NAME}}"
review_cadence: quarterly
applies_to: delivery workflow definition
source_basis: GitHub Actions workflow conventions; DORA small-batch delivery principles; GitHub Docs and Scrum Guide workflow conventions
source_manifests:
  - governance__github_docs.md
  - method__scrum_guide.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Workflow Definition Scope

This document defines the structure, quality gates, and operational expectations for a single automated workflow. One workflow definition document corresponds to one named workflow. Use this template to make the workflow intent, triggers, and failure behavior explicit so downstream consumers and operators can run, maintain, and extend it without ambiguity.

## Workflow Metadata

| Field | Value |
|---|---|
| Workflow name | `{{WORKFLOW_NAME}}` |
| Trigger event | `{{TRIGGER_EVENT}}` (e.g., `push`, `pull_request`, `schedule`, `workflow_dispatch`) |
| Target environment | `{{TARGET_ENVIRONMENT}}` (e.g., `staging`, `production`, `ci`) |
| Owner | `{{OWNER_NAME}}` |
| Review cadence | `{{REVIEW_CADENCE}}` |

## Workflow Steps

Define each step in the workflow. Every step must specify its action, expected inputs, expected outputs, and behavior on failure.

| Step | Action | Inputs | Outputs | On Failure |
|---|---|---|---|---|
| `{{N}}` | `{{ACTION}}` | `{{INPUTS}}` | `{{OUTPUTS}}` | `{{ON_FAILURE}}` |
| `{{N+1}}` | `{{ACTION}}` | `{{INPUTS}}` | `{{OUTPUTS}}` | `{{ON_FAILURE}}` |

Add rows as needed. Steps should be independently understandable; avoid implicit dependencies between non-adjacent steps.

## Quality Gates

Quality gates are blocking checkpoints within the workflow. A workflow run must not proceed to deployment or merge if any blocking gate fails.

| Gate Name | Criterion | Blocking |
|---|---|---|
| `{{GATE_NAME}}` | `{{CRITERION}}` | `{{YES_OR_NO}}` |
| `{{GATE_NAME}}` | `{{CRITERION}}` | `{{YES_OR_NO}}` |

Non-blocking gates produce warnings and are recorded in the run summary but do not halt execution.

## DORA Small-Batch Principles

This workflow should be designed to support DORA's small-batch delivery model:

- Each workflow run must produce an independently deployable artifact or outcome. Avoid bundling unrelated changes into a single run.
- Keep batch size at or below `{{MAX_BATCH_SIZE}}` (e.g., one feature, one fix, one configuration change per run).
- Prefer frequent, small runs over infrequent, large ones. Smaller batches reduce blast radius and improve mean time to restore (MTTR).
- Workflow duration should stay within `{{MAX_DURATION}}` to maintain developer flow; runs exceeding this threshold trigger a review of step efficiency.

## Workflow Health Metrics

Monitor these metrics to detect degradation before it becomes an incident:

| Metric | Target |
|---|---|
| Run frequency | `{{EXPECTED_FREQUENCY}}` (e.g., `>= 5 runs/day`) |
| Maximum allowed duration | `{{MAX_DURATION}}` (e.g., `<= 10 minutes`) |
| Success rate threshold | `{{SUCCESS_RATE_THRESHOLD}}` (e.g., `>= 95%`) |

Alerts for breached thresholds are sent to `{{NOTIFICATION_CHANNEL}}`.

## Failure Handling and Notification

- On step failure, the workflow must emit a structured error message identifying the failed step, the exit code, and the last log line.
- Blocking gate failures halt the workflow and notify `{{NOTIFICATION_CHANNEL}}` immediately.
- Non-blocking failures are summarized in the run report and reviewed at the next `{{REVIEW_CADENCE}}` cycle.
- Flaky steps (intermittent failures without code changes) must be triaged within `{{FLAKY_TRIAGE_SLA}}` and either fixed or explicitly marked as known-flaky with a tracking issue.

## Source Attribution

- Source manifests: governance__github_docs.md, method__scrum_guide.md
- Primary source basis: GitHub Actions workflow conventions; DORA small-batch delivery principles; GitHub Docs and Scrum Guide
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
