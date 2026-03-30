---
title: Incident Playbook Standard
artifact_type: standard
status: public
visibility: public
classification: public
owner: "{{OWNER_NAME}}"
review_cadence: quarterly
applies_to: incident responders
source_basis: Google SRE Incident Management Guide, NIST SP 800-61r3
source_manifests: operations__google_sre.md, operations__nist_cisa.md
alignment_mode: hybrid-synthesis
updated: 2026-03-30
---

## Standard Overview

Playbooks must be modular, short-lived, and automatable. Each playbook adheres to the `{{IMPACT_CLASS}}` taxonomy and references the relevant incident report, timeline, escalation, and service recovery templates. A playbook that cannot be executed by an unfamiliar on-call engineer is not a compliant playbook.

## When a Playbook Is Required

A playbook is required in the following situations. The responsible team must create and review it before the trigger event occurs, not during the incident.

- **New service onboarding:** every service reaching production must have at least one playbook covering its most likely failure mode before go-live.
- **After a SEV1 incident (`{{PLAYBOOK_TRIGGER}}`):** a new or updated playbook capturing the response steps is required as part of the postmortem action items.
- **After a novel SEV2 incident:** if the incident revealed a gap in existing playbooks.
- **Scheduled review trigger:** any playbook not executed or reviewed in the past `{{PLAYBOOK_MAX_AGE}}` is flagged for revalidation.

## Required Playbook Sections

Every compliant playbook must contain all sections listed below. Omitting a section is a compliance failure and the playbook must not be used until corrected.

### 1. Trigger Condition

Describe the specific observable condition that activates this playbook. Be precise enough that an automated alert can link to this playbook. Example: "`{{TRIGGER_CONDITION}}` — alert `{{ALERT_NAME}}` fires with threshold `{{ALERT_THRESHOLD}}`."

### 2. Severity Assessment

Provide a decision guide to help the first responder assign the correct severity (SEV1–SEV4) using the criteria in the incident management policy. Include blast-radius indicators specific to this service: `{{SEVERITY_ASSESSMENT_GUIDE}}`.

### 3. Incident Commander Assignment

Name the primary IC assignment path and backup: IC first call to `{{IC_PRIMARY_CONTACT}}`, fallback to `{{IC_SECONDARY_CONTACT}}`. Reference the on-call schedule at `{{ONCALL_SCHEDULE_LOCATION}}`.

### 4. Initial Response Steps

Numbered steps that can be executed sequentially without prior context. Each step must include a verification check so the responder confirms the step had the expected effect.

Steps must total fewer than `{{MAX_STEPS}}`. If more steps are needed, split into sub-playbooks linked from this one.

```
Step 1: {{STEP_1_ACTION}}
  Verify: {{STEP_1_VERIFY}}
Step 2: {{STEP_2_ACTION}}
  Verify: {{STEP_2_VERIFY}}
...
```

### 5. Escalation Path

Define when and to whom to escalate. Do not require judgment calls without explicit thresholds.

| Condition | Escalate to | Method |
|-----------|------------|--------|
| `{{ESCALATION_CONDITION_1}}` | `{{ESCALATION_TARGET_1}}` | `{{ESCALATION_METHOD_1}}` |
| `{{ESCALATION_CONDITION_2}}` | `{{ESCALATION_TARGET_2}}` | `{{ESCALATION_METHOD_2}}` |

### 6. Communications Template

Provide the initial status message pre-filled for this service and scenario. Link to the full incident communications plan for update cadence and stakeholder matrix. Example initial message: `{{COMMS_TEMPLATE}}`.

### 7. Resolution Criteria

Define the exact observable state that constitutes resolution. The IC must confirm all criteria are met before closing the incident.

- `{{RESOLUTION_CRITERION_1}}`
- `{{RESOLUTION_CRITERION_2}}`
- `{{RESOLUTION_CRITERION_N}}`

### 8. Rollback Option

If a rollback path exists, describe it here. Include the command or procedure (`{{ROLLBACK_PROCEDURE}}`), who must authorize it (`{{ROLLBACK_APPROVER}}`), and expected recovery time (`{{ROLLBACK_ETA}}`). If no rollback is available, state this explicitly.

## Playbook Quality Criteria

A playbook passes quality review when all of the following are true:

- An on-call engineer unfamiliar with this service can execute it without asking for context.
- Total step count is fewer than `{{MAX_STEPS}}`.
- Every step includes a verification check.
- All external references (runbooks, dashboards, escalation contacts) are working links.
- Playbook was reviewed or executed within `{{PLAYBOOK_MAX_AGE}}`.

## Playbook Testing Requirements

Untested playbooks degrade under pressure. Testing requirements exist to prevent silent rot.

- **Tabletop review annually (`{{ANNUAL_REVIEW}}`):** walk through the playbook scenario with the on-call team; identify gaps without running production commands.
- **Post-execution review:** every time a playbook is used in a real incident, the IC records what worked, what was skipped, and what was unclear. Updates are required within `{{POST_EXECUTION_UPDATE_SLA}}` of incident closure.
- **Automated lint check:** the playbook file must pass the governance validator (frontmatter, source attribution).

## Playbook Directory Structure

All playbooks are stored under `{{PLAYBOOK_DIRECTORY}}`. The directory structure is:

```
{{PLAYBOOK_DIRECTORY}}/
  <service>/
    playbook-<service>-<scenario>.md
```

Sub-directories are named after the service identifier used in the service fact sheet (`{{SERVICE_NAME}}`).

## Naming Convention

Files must follow the pattern: `playbook-{{SERVICE}}-{{SCENARIO}}.md`

Examples:
- `playbook-{{SERVICE}}-high-error-rate.md`
- `playbook-{{SERVICE}}-database-failover.md`
- `playbook-{{SERVICE}}-dependency-timeout.md`

Non-conforming filenames must be renamed before the next quarterly review.

## Review and Update Triggers

A playbook must be reviewed and updated when any of the following occur:

- A SEV1 or SEV2 incident uses or should have used this playbook.
- The service architecture, dependencies, or escalation contacts change.
- The annual tabletop review identifies gaps.
- The playbook has not been reviewed in more than `{{PLAYBOOK_MAX_AGE}}`.
- A new monitoring alert is added that maps to this scenario.

## Automation Guidance

- Each playbook must expose inputs compatible with GitHub Actions or AI assistants (e.g., `{{INCIDENT_ID}}`, `{{COMM_CHANNEL}}`, `{{ESCALATION_THRESHOLD}}`).
- Use the automation validator to ensure the playbook file includes frontmatter metadata and source attribution.

## Source Attribution

- Source manifests: `operations__google_sre.md`, `operations__nist_cisa.md`
- Primary source basis: Google SRE Incident Management Guide, NIST SP 800-61r3
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-30
