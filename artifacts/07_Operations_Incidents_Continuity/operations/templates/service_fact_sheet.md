---
title: Service Fact Sheet
artifact_type: template
status: public-draft
visibility: public
classification: public
owner: "{{OWNER_NAME}}"
review_cadence: quarterly
applies_to: service documentation and operational handoff
source_basis: Google SRE service documentation guidance and AWS service operating model guidance
source_manifests:
  - operations__google_sre.md
  - platform__aws_well_architected.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Purpose

Summarize the service in a concise, scannable format so on-call engineers, new team members, and incident responders can quickly understand ownership, dependencies, and operational context (Google SRE service documentation).

## Service Identity

| Field | Value |
|---|---|
| Service Name | `{{SERVICE_NAME}}` |
| Service ID | `{{SERVICE_ID}}` |
| Description | `{{SERVICE_DESCRIPTION}}` |
| Service Tier | `{{SERVICE_TIER}}` (Tier 1 — critical / Tier 2 — important / Tier 3 — internal) |
| Team | `{{TEAM_NAME}}` |
| Slack Channel | `{{SLACK_CHANNEL}}` |
| Service Catalog Entry | `{{SERVICE_CATALOG_LINK}}` |
| Last Updated | `{{LAST_UPDATED}}` |

## Owners and Contacts

| Role | Name / Team | Contact |
|---|---|---|
| Service Owner | `{{SERVICE_OWNER}}` | `{{SERVICE_OWNER_CONTACT}}` |
| Tech Lead | `{{TECH_LEAD}}` | `{{TECH_LEAD_CONTACT}}` |
| Primary On-call | `{{PRIMARY_ONCALL}}` | Via `{{ONCALL_TOOL}}` |
| Secondary On-call | `{{SECONDARY_ONCALL}}` | Via `{{ONCALL_TOOL}}` |
| Escalation Manager | `{{ESCALATION_MANAGER}}` | `{{ESCALATION_MANAGER_CONTACT}}` |
| Security Contact | `{{SECURITY_CONTACT}}` | `{{SECURITY_CONTACT_EMAIL}}` |

## SLOs and Error Budget

| SLI | SLO Target | Measurement Window | Current Status |
|---|---|---|---|
| `{{SLI_1}}` (e.g., availability) | `{{SLO_1}}`% | `{{WINDOW_1}}` | `{{CURRENT_STATUS_1}}` |
| `{{SLI_2}}` (e.g., latency P99 ≤ `{{LATENCY_TARGET}}` ms) | `{{SLO_2}}`% of requests | `{{WINDOW_2}}` | `{{CURRENT_STATUS_2}}` |

Error budget remaining: `{{ERROR_BUDGET_REMAINING}}`%

Error budget dashboard: `{{ERROR_BUDGET_DASHBOARD_LINK}}`

## Architecture

**Technology stack**: `{{TECH_STACK}}`

**Architecture diagram**: `{{ARCHITECTURE_DIAGRAM_LINK}}`

**Key components**:
- `{{COMPONENT_1}}`: `{{COMPONENT_1_DESCRIPTION}}`
- `{{COMPONENT_2}}`: `{{COMPONENT_2_DESCRIPTION}}`

## Dependencies

| Dependency | Type | Criticality | Contact | Fallback |
|---|---|---|---|---|
| `{{DEPENDENCY_1}}` | `{{DEP_1_TYPE}}` (upstream / downstream / external) | `{{DEP_1_CRITICALITY}}` | `{{DEP_1_CONTACT}}` | `{{DEP_1_FALLBACK}}` |
| `{{DEPENDENCY_2}}` | `{{DEP_2_TYPE}}` | `{{DEP_2_CRITICALITY}}` | `{{DEP_2_CONTACT}}` | `{{DEP_2_FALLBACK}}` |

**Consumers of this service** (downstream): `{{CONSUMERS_LIST}}`

## Operational Resources

| Resource | Link |
|---|---|
| Monitoring dashboard | `{{MONITORING_DASHBOARD_LINK}}` |
| Alerting configuration | `{{ALERTING_CONFIG_LINK}}` |
| Runbook index | `{{RUNBOOK_INDEX_LINK}}` |
| Incident playbook | `{{INCIDENT_PLAYBOOK_LINK}}` |
| Deployment pipeline | `{{DEPLOYMENT_PIPELINE_LINK}}` |
| Postmortem history | `{{POSTMORTEM_HISTORY_LINK}}` |
| Known errors (KEDB) | `{{KEDB_LINK}}` |

## Common Failure Modes

| Failure Mode | Symptoms | Diagnosis | Runbook |
|---|---|---|---|
| `{{FAILURE_MODE_1}}` | `{{SYMPTOMS_1}}` | `{{DIAGNOSIS_1}}` | `{{RUNBOOK_1_LINK}}` |
| `{{FAILURE_MODE_2}}` | `{{SYMPTOMS_2}}` | `{{DIAGNOSIS_2}}` | `{{RUNBOOK_2_LINK}}` |

## Key Operational Thresholds

| Metric | Normal Range | Warning | Critical | Alert Rule |
|---|---|---|---|---|
| CPU usage | `{{CPU_NORMAL}}` | > `{{CPU_WARNING}}`% | > `{{CPU_CRITICAL}}`% | `{{CPU_ALERT_LINK}}` |
| Memory usage | `{{MEM_NORMAL}}` | > `{{MEM_WARNING}}`% | > `{{MEM_CRITICAL}}`% | `{{MEM_ALERT_LINK}}` |
| Request latency (P99) | ≤ `{{LATENCY_NORMAL}}` ms | > `{{LATENCY_WARNING}}` ms | > `{{LATENCY_CRITICAL}}` ms | `{{LATENCY_ALERT_LINK}}` |
| Error rate | ≤ `{{ERROR_NORMAL}}`% | > `{{ERROR_WARNING}}`% | > `{{ERROR_CRITICAL}}`% | `{{ERROR_ALERT_LINK}}` |

## Source Attribution

- Source manifests: operations__google_sre.md, platform__aws_well_architected.md
- Primary source basis: Google SRE service documentation guidance and AWS operating model guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27

