---
title: Engineering Handbook
artifact_type: template
status: public-draft
visibility: public
classification: public
owner: "{{OWNER_NAME}}"
review_cadence: semiannual
applies_to: engineering operating model
source_basis: Scrum Guide and GitHub Docs guidance for repository operations
source_manifests:
  - governance__github_docs.md
  - method__scrum_guide.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Purpose

Capture the operating model for an engineering team: principles, roles, delivery lifecycle, on-call expectations, deployment standards, incident ownership, and learning culture. Replace all `{{PLACEHOLDER}}` values before publishing.

---

## Mission and Scope

**Team mission**: `{{TEAM_MISSION}}`

**Scope**: `{{TEAM_SCOPE}}` — services owned: `{{SERVICES_OWNED}}`

**Out of scope**: `{{OUT_OF_SCOPE}}`

**Reporting to**: `{{ENGINEERING_LEAD}}`

---

## Engineering Principles

Following Spotify/GitHub engineering culture norms:

| Principle | Description |
|---|---|
| Autonomy within alignment | Teams own their delivery end-to-end within shared conventions |
| Small and frequent changes | Prefer small PRs with CI gating over large batches |
| Fail safe, learn fast | Blameless postmortems; treat failures as learning events |
| Automation first | Manual processes must have a documented path to automation |
| Observable by default | Every service ships with SLOs, alerts, runbooks, and dashboards |
| Documentation as code | Governance artifacts version-controlled alongside implementation |

---

## Team Roles and Responsibilities

| Role | Responsibility | Current Holder | Backup |
|---|---|---|---|
| Engineering Lead | Technical strategy, delivery accountability, escalation | `{{ENGINEERING_LEAD}}` | `{{ENGINEERING_LEAD_BACKUP}}` |
| Tech Lead | Architecture decisions, ADR ownership, design review | `{{TECH_LEAD}}` | `{{TECH_LEAD_BACKUP}}` |
| Engineer | Feature development, testing, documentation, on-call | `{{ENGINEER_NAMES}}` | — |
| On-Call Primary | First-responder for SEV1/SEV2 per on-call schedule | Rotates — see `{{ONCALL_SCHEDULE_LINK}}` | `{{SECONDARY_ONCALL}}` |
| Release Manager | Release coordination, rollback authority | Rotates — `{{RELEASE_MANAGER_ROTATION}}` | `{{RM_BACKUP}}` |

---

## Delivery Lifecycle

| Phase | Activities | Required Artifacts | Gate |
|---|---|---|---|
| Discovery | Problem framing, research, spike | Discovery brief, assumptions register | Go/no-go review |
| Planning | Sprint planning, backlog refinement | Product backlog, planning record | Sprint kickoff |
| Development | Implementation, unit tests, peer review | PR, test results | CI pass + `{{MIN_REVIEWERS}}` approvals |
| Validation | Integration tests, staging deploy, smoke test | Release checklist | Staging sign-off |
| Release | Production deploy, traffic ramp, monitor | Deployment record, change record | SLO healthy for `{{STABILIZATION_PERIOD}}` |
| Post-release | Metrics review, postmortem (if incident) | Service review, postmortem (SEV1/SEV2) | Action items assigned |

---

## On-Call Expectations

| Expectation | Detail |
|---|---|
| Rotation length | `{{ONCALL_ROTATION_LENGTH}}` (e.g., 1 week) |
| Pager coverage | `{{ONCALL_COVERAGE_HOURS}}` |
| Response SLA (SEV1) | Acknowledge within `{{SEV1_ACK_SLA}}` |
| Response SLA (SEV2) | Acknowledge within `{{SEV2_ACK_SLA}}` |
| Handoff | Written handoff required: open incidents, toil items, watch-outs |
| Sleep protection | Off-call hours `{{SLEEP_PROTECTION_HOURS}}` — escalate to secondary if paged |
| Toil tracking | Log toil >30 min in `{{TOIL_TRACKER_LINK}}` for elimination planning |

On-call runbooks: `{{RUNBOOK_INDEX_LINK}}`
Escalation guide: `artifacts/07_Operations_Incidents_Continuity/operations/templates/on_call_escalation_guide.md`

---

## Deployment Standards

| Standard | Policy |
|---|---|
| Deployment frequency target | `{{TARGET_DEPLOY_FREQ}}` (DORA metric baseline) |
| Lead time target | `{{TARGET_LEAD_TIME}}` |
| Change fail rate target | ≤ `{{TARGET_CFR}}`% |
| MTTR target | ≤ `{{TARGET_MTTR}}` |
| Feature flags | Required for changes affecting ≥ `{{FEATURE_FLAG_THRESHOLD}}`% of traffic |
| Canary threshold | `{{CANARY_TRAFFIC_PERCENT}}`% before full rollout |
| Rollback trigger | SLO error rate > `{{ROLLBACK_THRESHOLD}}`% or explicit IC decision |
| Post-deploy monitoring | Minimum `{{MONITORING_WINDOW}}` before declaring success |

---

## Required Artifacts by Phase

| Phase | Artifact | Owner | Link |
|---|---|---|---|
| Discovery | Discovery brief | Product / Tech Lead | `artifacts/02_Discovery_Planning_Early_Learning/discovery/templates/discovery_brief.md` |
| Planning | Product backlog, sprint planning record | Engineering Lead | `artifacts/02_Discovery_Planning_Early_Learning/discovery/templates/product_backlog.md` |
| Development | ADR (architectural decisions) | Tech Lead | `artifacts/01_Governance_Method/governance/templates/architecture_decision_record.md` |
| Release | Change record, release checklist | Release Manager | `artifacts/05_Delivery_Change_Readiness/delivery/templates/change_record.md`, `artifacts/05_Delivery_Change_Readiness/delivery/templates/release_checklist.md` |
| Incident | Incident report, postmortem | IC / On-Call Lead | `artifacts/07_Operations_Incidents_Continuity/operations/templates/incident_report.md`, `artifacts/08_Knowledge_Documentation_Continuous_Improvement/knowledge/templates/postmortem.md` |
| Review | Service review, lessons learned | Engineering Lead | `artifacts/08_Knowledge_Documentation_Continuous_Improvement/knowledge/templates/service_review.md` |

---

## Quality and Validation

| Check | Tool / Method | Frequency | Owner |
|---|---|---|---|
| Unit tests | `{{TEST_FRAMEWORK}}` | Every commit | Engineer |
| Integration tests | `{{INTEGRATION_TEST_TOOL}}` | Every PR | CI |
| Governance validation | `python3 scripts/validate_governance_artifacts.py` | Every PR (CI) | CI / Contributor |
| Code review | GitHub PR reviews | Every PR | `{{REVIEW_TEAM}}` |
| Security scan | `{{SECURITY_SCAN_TOOL}}` | Every PR (CI) | CI |
| SLO review | Error budget dashboard | Monthly | Engineering Lead |

Definition of Done: `artifacts/01_Governance_Method/conventions/standards/definition_of_done_quality_gates.md`

---

## Escalation and Decision Paths

| Situation | First Contact | Escalation Path |
|---|---|---|
| Technical blocker | Tech Lead | Engineering Lead → `{{MANAGER_CONTACT}}` |
| Production incident (SEV1) | On-Call Primary | IC → Engineering Lead → `{{EXECUTIVE_CONTACT}}` |
| Architecture dispute | Tech Lead | ADR proposal → team vote → Engineering Lead decision |
| Security vulnerability | `{{SECURITY_CONTACT}}` | Security team → Engineering Lead → `{{EXECUTIVE_CONTACT}}` |
| Team conflict | Engineering Lead | `{{HR_CONTACT}}` |

---

## Learning and Improvement Culture

- **Retrospectives**: held every `{{RETRO_CADENCE}}` — template: `artifacts/02_Discovery_Planning_Early_Learning/discovery/templates/technical_retrospective.md`
- **Postmortems**: blameless; required for all SEV1 and novel SEV2 — template: `artifacts/08_Knowledge_Documentation_Continuous_Improvement/knowledge/templates/postmortem.md`
- **Knowledge sharing**: `{{KNOWLEDGE_SHARING_FORUM}}` — frequency: `{{KS_FREQUENCY}}`
- **Learning budget**: `{{LEARNING_BUDGET_PER_PERSON}}` per engineer per year for conferences, courses, certifications
- **Incident reviews**: each incident action item reviewed at next sprint retrospective

## Source Attribution

- Source manifests: governance__github_docs.md, method__scrum_guide.md
- Primary source basis: GitHub Docs and Scrum Guide
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27

