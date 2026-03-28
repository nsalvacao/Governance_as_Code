---
title: Postmortem Standard
artifact_type: policy
status: public-draft
visibility: public
classification: public
owner: reliability-platform
review_cadence: quarterly
applies_to: all critical services
source_basis: Google SRE Incident Management Guide & Postmortem Culture
source_manifests: operations__google_sre.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Purpose

Define triggering criteria, required sections, review process, and blameless culture guidance for postmortems (Google SRE Book Ch.15 + SRE Workbook).

## Triggering Criteria

A postmortem MUST be initiated for any of the following:

| Trigger | Mandatory? | Notes |
|---|---|---|
| SEV1 incident (complete service unavailability) | Yes | Always, no exceptions |
| SEV2 incident (major degradation) | Yes | Always |
| SEV2 incident (minor / novel failure mode) | Yes | Required if failure mode is new or unexpected |
| Error budget consumed > `{{POSTMORTEM_BUDGET_TRIGGER}}`% in a single incident | Yes | |
| Customer-visible data loss or corruption | Yes | Regardless of severity classification |
| On-call engineer discretion | Optional | For learning opportunity or near-miss |
| User-reported issue with no internal detection | Yes — retrospective | Signals monitoring gap |

## Required Sections

Every postmortem MUST contain all of the following sections in this order:

1. **Incident Metadata** — date, duration, services, severity, incident commander
2. **Executive Summary** — ≤ 5 sentences: what happened, customer impact, current status
3. **Impact** — quantitative: users affected `{{USERS_AFFECTED}}`, error budget consumed `{{BUDGET_CONSUMED}}`%, revenue impact if known
4. **Timeline** — UTC-stamped chronological log from first signal to resolution (minimum 5-minute granularity during active response)
5. **Root Cause Analysis** — minimal causal chain; distinguish immediate cause from systemic contributing factors
6. **Contributing Factors** — technical, process, tooling, and human factors that enabled or amplified the incident
7. **What Went Well** — actions that limited the blast radius or accelerated recovery
8. **Action Items** — each item must have owner `{{ACTION_OWNER}}`, due date `{{ACTION_DUE_DATE}}`, and tracking link `{{ACTION_TRACKER_LINK}}`
9. **Lessons Learned** — non-obvious insights not captured in action items

## Timeline Requirements

- All times in UTC
- Minimum events to include: first signal, first notification, IC declared, impact scope established, mitigation applied, service restored, postmortem opened
- Reference log queries, alert links, or graph snapshots for each entry
- Format: `HH:MM UTC — {{EVENT_DESCRIPTION}}` (`{{EVIDENCE_LINK}}`)

## Blameless Culture Language

Avoid in postmortems:

| ❌ Avoid | ✅ Use Instead |
|---|---|
| "{{PERSON}} made a mistake" | "The process did not prevent `{{ERROR_CONDITION}}`" |
| "Human error" as root cause | Describe the system condition that made the error likely |
| "Should have known" | "Monitoring did not alert on `{{SIGNAL}}`" |
| Passive voice to obscure actions | Active voice attributing actions to roles, not persons |

Postmortems are not disciplinary documents. Their purpose is systemic learning.

## Review Process

| Stage | Owner | Deadline | Criteria |
|---|---|---|---|
| Draft | Incident Commander `{{IC_CONTACT}}` | `{{DRAFT_DEADLINE}}` business days | All required sections present, timeline complete |
| Technical review | `{{TECH_REVIEW_TEAM}}` | `{{TECH_REVIEW_DEADLINE}}` business days | Root cause validated, action items actionable |
| Management review | `{{MGMT_REVIEWER}}` | `{{MGMT_REVIEW_DEADLINE}}` business days | Customer comms alignment, escalation decisions |
| Published | `{{POSTMORTEM_CURATOR}}` | `{{PUBLISH_DEADLINE}}` business days | Stored in `{{POSTMORTEM_REPOSITORY}}`, linked from incident record |

Total deadline from incident resolution to published postmortem: `{{TOTAL_POSTMORTEM_DEADLINE}}` business days.

## Writing Guidance

- Write in plain English; reference logs/graphs/dashboards — do not paraphrase telemetry.
- Quote SLO dashboard readings when stating impact.
- Redact PII, customer identifiers, and credentials before sharing; coordinate with `{{PRIVACY_REVIEWER}}`.

## Source Attribution

- Source manifests: `operations__google_sre.md`
- Primary source basis: Google SRE Incident Management Guide & Postmortem Culture
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
