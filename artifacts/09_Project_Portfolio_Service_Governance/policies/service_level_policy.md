---
title: Service Level Policy
artifact_type: policy
status: public-draft
visibility: public
classification: public
owner: GOVERNANCE
review_cadence: quarterly
applies_to: service level targets, commitments, and review expectations
source_basis: PMI, PRINCE2, ITIL
source_manifests:
  - project__pmi.md
  - project__prince2.md
  - service_mgmt__itil.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

# Service Level Policy

This policy defines how service level commitments are structured, approved, reviewed, and enforced following ITIL 4 Service Level Management (SLM) practice.

## Service Level Agreement (SLA) Structure

An SLA is the agreement between the service provider and the customer defining the expected level of service.

| Agreement Type | Between | Purpose |
|---|---|---|
| SLA (Service Level Agreement) | Provider and Customer/Consumer | Customer-facing commitments |
| OLA (Operational Level Agreement) | Provider and Internal Team | Internal support targets |
| UC (Underpinning Contract) | Provider and Supplier | Third-party commitments |

## Required SLA Elements

Each SLA or equivalent agreement MUST define:

| Element | Guidance |
|---|---|
| Service Name | `{{SERVICE_NAME}}` — as it appears in the Service Catalog |
| Service Scope | `{{SERVICE_SCOPE}}` — what is and is not included |
| Service Owner | `{{SERVICE_OWNER}}` |
| Consumer Group | `{{CONSUMER_GROUP}}` |
| SLA Reference | `{{SLA_ID}}` |
| Effective Date | `{{EFFECTIVE_DATE}}` |
| Review Date | `{{REVIEW_DATE}}` |
| Approval | `{{SLA_APPROVER}}` |

## Service Level Targets

| KPI Name | Measurement Method | Target | Measurement Window | Reporting Cadence | Consequence of Breach |
|---|---|---|---|---|---|
| `{{KPI_NAME_1}}` (e.g., Availability) | `{{KPI_METHOD_1}}` | `{{KPI_TARGET_1}}`% | `{{KPI_WINDOW_1}}` | `{{REPORTING_CADENCE_1}}` | `{{BREACH_CONSEQUENCE_1}}` |
| `{{KPI_NAME_2}}` (e.g., Incident Response SLA) | `{{KPI_METHOD_2}}` | `{{KPI_TARGET_2}}` | `{{KPI_WINDOW_2}}` | `{{REPORTING_CADENCE_2}}` | `{{BREACH_CONSEQUENCE_2}}` |
| `{{KPI_NAME_3}}` (e.g., Request Fulfillment SLA) | `{{KPI_METHOD_3}}` | `{{KPI_TARGET_3}}` | `{{KPI_WINDOW_3}}` | `{{REPORTING_CADENCE_3}}` | `{{BREACH_CONSEQUENCE_3}}` |

## Review Cadence

| Review Type | Frequency | Owner | Output |
|---|---|---|---|
| Service Level Report | `{{SLR_CADENCE}}` (e.g., monthly) | `{{SLR_OWNER}}` | Published SLR with KPI performance |
| SLA Review Meeting | `{{SLA_REVIEW_CADENCE}}` | `{{SLA_REVIEW_OWNER}}` | Exception log, SLA adjustment decisions |
| Annual SLA Renegotiation | Annual | `{{SLA_NEGOTIATION_OWNER}}` | Updated SLA targets signed by `{{APPROVER}}` |

## Exception Handling

SLA exceptions must be:

1. Raised as exception records in `{{EXCEPTION_LOG_LOCATION}}`
2. Approved by `{{EXCEPTION_AUTHORITY}}`
3. Time-limited to `{{MAX_EXCEPTION_DURATION}}`
4. Linked to a remediation plan with target date `{{REMEDIATION_DATE}}`

Approved exceptions that persist beyond `{{EXCEPTION_REVIEW_PERIOD}}` trigger SLA renegotiation.

## Automation Guidance

- SLA targets are stored as structured YAML/JSON fields at `{{SLA_STRUCTURED_DATA_LOCATION}}` for dashboard integration.
- Breach detection is automated via `{{MONITORING_TOOL}}` with alert routing to `{{SLA_BREACH_ALERT_DESTINATION}}`.
- Monthly SLR generation is automated by `{{SLR_AUTOMATION_TOOL}}`.

## Source Attribution

- Source manifests: `project__pmi.md`, `project__prince2.md`, `service_mgmt__itil.md`
- Primary source basis: PMI, PRINCE2, and ITIL service governance guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
