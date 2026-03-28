---
title: Metrics and Review Cadence Standard
artifact_type: standard
status: public-draft
visibility: public
classification: public
owner: risk-platform
review_cadence: quarterly
applies_to: governance metrics, risks, exceptions, and operational reviews
source_basis: Google SRE review cadence and Scrum inspection guidance
source_manifests:
  - operations__google_sre.md
  - governance__github_docs.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Purpose

Define the review cadence for reliability, deployment, quality, and risk metrics so governance stays current and trends drive decisions (Google SRE review practices + Scrum Guide 2020 inspection principle).

## Review Types and Cadences

### Sprint / Iteration Review (Frequency: `{{SPRINT_CADENCE}}`)

| Metric Category | Metric | Owner | Threshold / Target | Action if Breached |
|---|---|---|---|---|
| Deployment | Deployment frequency | `{{DEPLOY_METRIC_OWNER}}` | `{{DEPLOY_FREQ_TARGET}}` | Review pipeline blockers |
| Deployment | Lead time for changes | `{{DEPLOY_METRIC_OWNER}}` | ≤ `{{LEAD_TIME_TARGET}}` | Investigate bottlenecks |
| Quality | Test pass rate | `{{QA_METRIC_OWNER}}` | ≥ `{{TEST_PASS_THRESHOLD}}`% | Halt if < `{{TEST_FAIL_THRESHOLD}}`% |
| Quality | Defect escape rate | `{{QA_METRIC_OWNER}}` | ≤ `{{DEFECT_ESCAPE_TARGET}}`% | Root cause analysis |

### Monthly Review (Frequency: Monthly)

| Metric Category | Metric | Owner | Threshold / Target | Action if Breached |
|---|---|---|---|---|
| Reliability | SLO compliance | `{{SRE_METRIC_OWNER}}` | ≥ `{{SLO_TARGET}}`% | Trigger error budget review |
| Reliability | Error budget consumed | `{{SRE_METRIC_OWNER}}` | ≤ `{{MONTHLY_BUDGET_CONSUMPTION}}`% | Freeze releases if > `{{FREEZE_THRESHOLD}}`% |
| Reliability | MTTR (mean time to recover) | `{{OPS_METRIC_OWNER}}` | ≤ `{{MTTR_TARGET}}` | Review incident playbooks |
| Reliability | Change failure rate | `{{DEPLOY_METRIC_OWNER}}` | ≤ `{{CHANGE_FAIL_RATE_TARGET}}`% | Review change management process |
| Risk | Open P1/P2 risks | `{{RISK_METRIC_OWNER}}` | 0 unmitigated P1 | Immediate escalation |
| Risk | Exception expiry | `{{COMPLIANCE_METRIC_OWNER}}` | 0 expired exceptions | Renew or remediate |

### Quarterly Review (Frequency: Quarterly)

| Metric Category | Metric | Owner | Threshold / Target | Action if Breached |
|---|---|---|---|---|
| SLO | SLO target validity | `{{SLO_REVIEW_OWNER}}` | Aligned with current product commitments | Renegotiate SLO |
| Reliability | Toil percentage | `{{SRE_TOIL_OWNER}}` | ≤ `{{TOIL_TARGET}}`% of eng time | Automation investment required |
| Security | Open CVEs (critical/high) | `{{SECURITY_METRIC_OWNER}}` | 0 critical, ≤ `{{HIGH_CVE_LIMIT}}` high | Patch sprint or exception |
| Risk | Risk register age | `{{RISK_REGISTER_OWNER}}` | No item > `{{MAX_RISK_AGE}}` days without review | Force review or close |
| Governance | Artifact staleness | `{{GOVERNANCE_METRIC_OWNER}}` | No artifact > `{{STALE_THRESHOLD}}` days past review date | Trigger review workflow |
| Governance | ADR coverage | `{{ARCHITECTURE_METRIC_OWNER}}` | `{{ADR_COVERAGE_TARGET}}`% of significant decisions | Backfill missing ADRs |

### Annual Review (Frequency: Annual)

| Review | Owner | Output |
|---|---|---|
| SLO renegotiation | `{{SLO_NEGOTIATION_OWNER}}` | Updated SLO targets with stakeholder sign-off |
| Risk appetite review | `{{RISK_COMMITTEE}}` | Revised risk tolerance thresholds |
| Compliance audit | `{{COMPLIANCE_AUDITOR}}` | Audit report + corrective action register |
| Metric taxonomy review | `{{METRICS_CURATOR}}` | Pruned/updated metric list |

## Review Output Requirements

Every review MUST produce one of:

1. **Confirm** — metrics within targets; no action required; record date and reviewer
2. **Mitigate** — metrics breached; action item created with owner `{{ACTION_OWNER}}` and due date `{{ACTION_DUE_DATE}}`
3. **Escalate** — metrics breached and mitigation insufficient; escalate to `{{ESCALATION_CONTACT}}`

Reviews with no output are invalid. Record outcomes in `{{REVIEW_OUTCOME_LOCATION}}`.

## Source Attribution

- Source manifests: operations__google_sre.md, governance__github_docs.md
- Primary source basis: Google SRE review cadence and Scrum inspection guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
