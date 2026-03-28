---
title: Test Strategy and Verification Policy
artifact_type: standard
status: public-draft
visibility: public
classification: public
owner: quality-platform
review_cadence: quarterly
applies_to: validation strategy, verification expectations, and quality gates
source_basis: Microsoft Learn testing guidance; Google SRE verification and reliability practices
source_manifests:
  - platform__microsoft_learn.md
  - operations__google_sre.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Purpose

Define test levels, test types, coverage targets, and exit criteria to ensure verification is systematic and risk-based (ISTQB CTFL 2023 v4.0).

## Test Objectives

1. Verify all functional requirements are met against `{{ACCEPTANCE_CRITERIA_SOURCE}}`
2. Validate non-functional quality attributes (performance, security, reliability)
3. Detect defects early to reduce cost of correction
4. Provide confidence to stakeholders that `{{SYSTEM_OR_SERVICE_NAME}}` is fit for release

## Test Levels

| Level | Scope | Entry Criteria | Exit Criteria | Owner |
|---|---|---|---|---|
| Unit | Individual functions/modules | Code complete, static analysis clean | `{{UNIT_COVERAGE_THRESHOLD}}`% line/branch coverage, all unit tests pass | `{{DEV_TEAM}}` |
| Integration | Module interactions, APIs, data flows | Unit tests pass, integration environment available | Integration test suite passes, no P1/P2 defects open | `{{DEV_TEAM}}` |
| System | End-to-end functional behaviour | Integration tests pass, staging environment available | All functional test cases pass, performance baseline met | `{{QA_TEAM}}` |
| Acceptance | Business value, user stories, regulatory | System tests pass, UAT environment available | `{{UAT_PASS_RATE}}`% user stories accepted, sponsor sign-off | `{{PRODUCT_OWNER}}` |

## Test Types

| Type | What It Verifies | Automation Level | Tool/Approach |
|---|---|---|---|
| Functional | Features meet specified behaviour | `{{FUNCTIONAL_AUTOMATION_LEVEL}}` | `{{FUNCTIONAL_TEST_TOOL}}` |
| Non-functional (performance) | Throughput ≥ `{{THROUGHPUT_TARGET}}`, latency ≤ `{{LATENCY_TARGET}}` | Automated | `{{PERF_TEST_TOOL}}` |
| Security (DAST/SAST) | OWASP Top 10 categories, dependency vulnerabilities | Automated in CI | `{{SAST_TOOL}}`, `{{DAST_TOOL}}` |
| Regression | No previously passing test now fails | Fully automated | Part of CI pipeline |
| Exploratory | Unscripted risk-based discovery | Manual | `{{EXPLORATORY_SESSION_TIMEBOXES}}` sessions |
| Accessibility | WCAG `{{WCAG_LEVEL}}` compliance | Semi-automated | `{{ACCESSIBILITY_TOOL}}` |

## Coverage Targets

| Artefact | Metric | Target | Blocking? |
|---|---|---|---|
| Unit tests | Line coverage | `{{UNIT_COVERAGE_THRESHOLD}}`% | Yes — build fails below threshold |
| Integration tests | API endpoint coverage | `{{INTEGRATION_COVERAGE_THRESHOLD}}`% | Yes |
| Security scan | Critical/High CVEs | 0 unresolved | Yes |
| Performance | P99 latency | ≤ `{{P99_LATENCY_TARGET}}` ms | Yes for production |

## Exit Criteria (Release Gate)

A build is releasable when ALL of the following are true:

- [ ] All test levels completed and exit criteria met
- [ ] Coverage targets satisfied for `{{BRANCH_NAME}}`
- [ ] Zero open P1 defects; P2 defects have accepted workaround or deferred per `{{DEFERRAL_POLICY}}`
- [ ] Security scan output reviewed and cleared by `{{SECURITY_REVIEWER}}`
- [ ] Performance baseline recorded at `{{PERFORMANCE_BASELINE_DATE}}`
- [ ] Test evidence recorded in `{{TEST_EVIDENCE_LOCATION}}`

## Defect Classification

| Priority | Description | Resolution SLA |
|---|---|---|
| P1 — Critical | Data loss, security breach, service unavailable | `{{P1_SLA}}` |
| P2 — High | Major feature broken, no workaround | `{{P2_SLA}}` |
| P3 — Medium | Feature degraded, workaround available | `{{P3_SLA}}` |
| P4 — Low | Cosmetic or edge-case issue | `{{P4_SLA}}` |

## Canonical Relationship

- The implementation-level validator lives in `artifacts/01_Governance_Method/conventions/scripts/validate_governance_artifacts.py`.
- This standard explains the verification model that the validator supports.

## Source Attribution

- Source manifests: `platform__microsoft_learn.md`, `operations__google_sre.md`
- Primary source basis: Microsoft testing guidance and Google SRE verification practices
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
