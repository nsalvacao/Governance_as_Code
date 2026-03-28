---
title: Service Continuity Plan
artifact_type: template
status: public-draft
visibility: public
classification: public
owner: "{{OWNER_NAME}}"
review_cadence: annual
applies_to: service continuity and disaster recovery planning
source_basis: ISO 22301:2019
source_manifests:
  - operations__nist_cisa.md
  - operations__google_sre.md
  - platform__aws_well_architected.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Service Context

Identify the service covered by this plan and define its continuity requirements. Per ISO 22301:2019 clause 8.4, the plan must be scoped to a specific service with documented continuity objectives.

- **Service name:** `{{SERVICE_NAME}}`
- **Service owner:** `{{SERVICE_OWNER}}`
- **Service description:** `{{SERVICE_DESCRIPTION}}`
- **Continuity objectives:** `{{CONTINUITY_OBJECTIVE}}`
- **Service tier:** `{{SERVICE_TIER}}`
- **Applicable regulations:** `{{APPLICABLE_REGULATIONS}}`
- **Plan version:** `{{PLAN_VERSION}}`
- **Plan date:** `{{PLAN_DATE}}`
- **Activation authority:** `{{ACTIVATION_AUTHORITY}}`

## Recovery Objectives

State the recovery targets for this service. These values must be derived from the BIA and approved by the service owner. All response procedures in this plan must be designed to meet or exceed these targets.

- **Recovery Time Objective (RTO):** `{{RTO}}`
- **Recovery Point Objective (RPO):** `{{RPO}}`
- **Maximum Tolerable Period of Disruption (MTPD):** `{{MTPD}}`
- **Minimum Business Continuity Objective (MBCO):** `{{MBCO}}`

The MBCO defines the minimum level of service that must be delivered during a disruption before full recovery is achieved. If the MBCO cannot be met within the RTO, escalate to `{{ESCALATION_CONTACT}}` immediately.

## Continuity Strategies

Define the primary and alternate strategies for maintaining service continuity. Each strategy must be viable within the RTO and must have been validated through testing.

- **Primary strategy:** `{{PRIMARY_STRATEGY}}` — describe how normal service will be maintained or restored as the first-choice approach.
- **Alternate strategy:** `{{ALTERNATE_STRATEGY}}` — describe the fallback approach if the primary strategy is unavailable or insufficient.
- **Manual workaround:** `{{MANUAL_WORKAROUND}}` — describe any non-automated procedure that can sustain minimum acceptable service levels during recovery.
- **Strategy selection criteria:** `{{STRATEGY_SELECTION_CRITERIA}}` — conditions under which the activation authority switches from primary to alternate strategy.

## Response Procedures by Disruption Type

For each plausible disruption type, define the trigger condition, response steps, and escalation path. Steps must be specific enough to be executable by a trained team member without additional context.

| Disruption Type | Trigger | Initial Response Steps | Escalation Contacts | Expected RTO |
|---|---|---|---|---|
| `{{DISRUPTION_TYPE}}` | `{{TRIGGER}}` | `{{RESPONSE_STEPS}}` | `{{ESCALATION_CONTACTS}}` | `{{EXPECTED_RTO}}` |

Add one row per disruption type. Common disruption types include: infrastructure failure, data loss, cybersecurity incident, facility loss, key personnel unavailability, and third-party service failure. Each trigger must be unambiguous and objectively observable.

## Team Structure

Define all roles involved in service continuity execution. Every named role must have a documented backup to avoid single points of failure in the response team.

| Role Name | Responsibilities | Primary Contact | Backup Contact |
|---|---|---|---|
| `{{ROLE_NAME}}` | `{{RESPONSIBILITIES}}` | `{{CONTACT_DETAILS}}` | `{{BACKUP_CONTACT}}` |

Roles must cover at minimum: plan activation authority, technical recovery lead, communications lead, and business liaison. Assign named individuals or position titles using `{{CONTACT_DETAILS}}`.

## Communication Plan During Disruption

Define communication protocols for internal and external stakeholders during a disruption. Communication failures are a common cause of prolonged outages; this section must be executable without access to the primary production environment.

### Internal Communication

- **Primary internal channel:** `{{INTERNAL_CHANNEL}}`
- **Backup internal channel:** `{{BACKUP_INTERNAL_CHANNEL}}`
- **Internal notification list:** `{{INTERNAL_NOTIFICATION_LIST}}`
- **Update frequency during disruption:** `{{INTERNAL_UPDATE_FREQUENCY}}`
- **Status page or dashboard:** `{{STATUS_PAGE}}`

### External Communication

- **Primary external channel:** `{{EXTERNAL_CHANNEL}}`
- **Customer notification template:** `{{CUSTOMER_NOTIFICATION_TEMPLATE}}`
- **Regulatory notification requirements:** `{{REGULATORY_NOTIFICATION}}`
- **External communication authority:** `{{EXTERNAL_COMMUNICATION_AUTHORITY}}`
- **Media / PR escalation:** `{{MEDIA_ESCALATION}}`

All external communications must be approved by `{{EXTERNAL_COMMUNICATION_AUTHORITY}}` before release. Do not disclose technical root cause externally until authorized.

## Resource Requirements

List all resources required to execute this plan. Resources must be pre-positioned or have documented procurement procedures with confirmed lead times that fit within the RTO.

- **Resource requirements:** `{{RESOURCE_REQUIREMENTS}}`
- **Alternate processing site:** `{{ALT_SITE}}`
- **Minimum staffing level:** `{{MINIMUM_STAFFING}}`
- **Critical tooling and access:** `{{CRITICAL_TOOLING}}`
- **Data backup location:** `{{BACKUP_LOCATION}}`
- **Third-party dependencies:** `{{THIRD_PARTY_DEPENDENCIES}}`

For each third-party dependency, confirm that the vendor's RTO is compatible with this plan's RTO. Incompatible vendor RTOs must be escalated to `{{OWNER_NAME}}` and documented as a risk.

## Plan Maintenance and Testing Schedule

Define when this plan will be tested and reviewed. Per ISO 22301:2019 clause 8.5, continuity plans must be tested at a frequency that maintains confidence in their executability.

| Activity | Type | Cadence | Responsible | Next Scheduled |
|---|---|---|---|---|
| Tabletop exercise | Test | `{{TABLETOP_CADENCE}}` | `{{TABLETOP_OWNER}}` | `{{NEXT_TABLETOP}}` |
| Functional exercise | Test | `{{FUNCTIONAL_CADENCE}}` | `{{FUNCTIONAL_OWNER}}` | `{{NEXT_FUNCTIONAL}}` |
| Full-scale exercise | Test | `{{FULL_SCALE_CADENCE}}` | `{{FULL_SCALE_OWNER}}` | `{{NEXT_FULL_SCALE}}` |
| Annual plan review | Maintenance | `{{ANNUAL_REVIEW_CADENCE}}` | `{{OWNER_NAME}}` | `{{NEXT_ANNUAL_REVIEW}}` |
| Post-incident review | Maintenance | After each activation | `{{OWNER_NAME}}` | N/A |

Test results must be recorded using the exercise drill record template. Material gaps found during testing must generate corrective actions and may trigger an unscheduled plan review.

## Source Attribution

- Source manifests: `operations__nist_cisa.md`, `operations__google_sre.md`, `platform__aws_well_architected.md`
- Primary source basis: ISO 22301:2019 clause 8.4
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
