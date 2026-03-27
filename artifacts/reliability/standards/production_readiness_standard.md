---
title: Production Readiness Standard
artifact_type: policy
status: public-draft
visibility: public
classification: public
owner: reliability-platform
review_cadence: semiannual
applies_to: releases carrying new services or significant changes
source_basis: Google SRE Production Readiness Review & AWS Operational Readiness guidance
source_manifests: operations__google_sre.md platform__aws_well_architected.md platform__microsoft_learn.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Purpose

Ensure new releases can be operated reliably by embedding readiness checks into delivery workflows and enabling AI-assisted verification where feasible.

## Readiness pillars

1. `Service understanding`: documented `{{SERVICE_DESCRIPTION}}`, dependencies, and owner contact.
2. `Observability`: meters, dashboards, alerting `{{OBSERVABILITY_COVERAGE}}`, and runbook links.
3. `Automation`: deployment, rollback, and recovery steps expressed as reproducible workflows.
4. `Support readiness`: on-call roster, escalation path, and knowledge transfer artifacts.

## Evidence requirements

- Attach evidence links to `{{RUNBOOK_URL}}`, `{{DASHBOARD_URL}}`, and `{{TEST_REPORT}}`.
- Confirm AI/automation probes (GitHub Action, pipeline, script) validate steps automatically before sign-off.
- Include `{{SAFETY_CHECK}}` or checklist output for critical guardrails.

## Process notes

- Collate readiness artifacts into the production readiness review template.
- Reject readiness if any pillar is unverified, and schedule remediation prior to release gating.
- Use placeholders for tool-specific commands so downstream repos can plug in `{{DEPLOY_COMMAND}}`, `{{ROLLBACK_COMMAND}}`, and `{{OBSERVE_COMMAND}}`.

## Source Attribution

- Source manifests: `operations__google_sre.md`, `platform__aws_well_architected.md`, `platform__microsoft_learn.md`
- Primary source basis: Google SRE Production Readiness Review, AWS ORR, Microsoft Learn deployment guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
