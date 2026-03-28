---
title: Operational Playbook
artifact_type: template
status: public-draft
visibility: public
classification: public
owner: "{{OWNER_NAME}}"
review_cadence: quarterly
applies_to: repeatable operational scenarios
source_basis: PagerDuty Incident Response Guide and Google SRE incident management practices
source_manifests:
  - operations__nist_cisa.md
  - operations__google_sre.md
  - platform__aws_well_architected.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Purpose

Provide the generic structure for scenario-specific playbooks used in incident handling, triage, or recovery. Each playbook covers exactly one trigger scenario. Fill every `{{PLACEHOLDER}}` before activating.

---

## Playbook Metadata

| Field | Value |
|---|---|
| Playbook name | `{{PLAYBOOK_NAME}}` |
| Trigger condition | `{{TRIGGER_CONDITION}}` |
| Severity | `{{SEVERITY}}` |
| Last reviewed | `{{LAST_REVIEWED}}` |

Name the playbook after the scenario, not the symptom, so it remains reusable across alert variants. Record the last-reviewed date to ensure playbooks are exercised at least once per quarter.

---

## Trigger Condition

**Specific alert or event that activates this playbook:**
`{{TRIGGER_DETAIL}}`

Define the trigger precisely — alert name, threshold crossed, or event type. A playbook with a vague trigger will be activated inconsistently and may be skipped when most needed.

---

## Initial Assessment

Determine whether this is a `{{INCIDENT_TYPE}}` incident.

**Severity assessment criteria:**

| Criterion | Observed value | SEV level |
|-----------|---------------|-----------|
| Customer impact | `{{CUSTOMER_IMPACT_CRITERION}}` | `{{SEV_CUSTOMER}}` |
| Data loss risk | `{{DATA_LOSS_CRITERION}}` | `{{SEV_DATA}}` |
| Blast radius | `{{BLAST_RADIUS_CRITERION}}` | `{{SEV_BLAST}}` |

Use this table to confirm or upgrade the initial severity before taking action. Do not skip the assessment step even under time pressure — a wrong severity rating delays the right people joining the response.

---

## Incident Commander Designation

IC assignment rule: `{{IC_ASSIGNMENT_RULE}}`

The Incident Commander is the single decision-maker for the duration of this incident. Establish IC clearly within the first two minutes of activation — ambiguity on IC causes coordination failures.

---

## Immediate Actions

Time-sensitive steps to be completed within the first `{{INITIAL_RESPONSE_WINDOW}}` minutes.

| Step | Action | Verify |
|------|--------|--------|
| 1 | `{{ACTION_1}}` | `{{VERIFY_1}}` |
| 2 | `{{ACTION_2}}` | `{{VERIFY_2}}` |
| 3 | `{{ACTION_3}}` | `{{VERIFY_3}}` |
| N | `{{ACTION_N}}` | `{{VERIFY_N}}` |

Complete these steps before branching into parallel tracks. Confirm each action is done before moving to the next — partial execution is worse than no execution for containment steps.

---

## Parallel Tracks

After immediate actions, split work across two tracks. The IC owns coordination, not execution.

**Track A — Technical:**
`{{TECH_ACTIONS}}`

**Track B — Communications:**
`{{COMMS_ACTIONS}}`

Assign a named owner to each track at activation. Track owners report status to IC every `{{STATUS_CADENCE}}` minutes until the incident is resolved.

---

## Decision Points

| Condition | If yes | If no |
|-----------|--------|-------|
| `{{CONDITION_1}}` | `{{YES_PATH_1}}` | `{{NO_PATH_1}}` |
| `{{CONDITION_2}}` | `{{YES_PATH_2}}` | `{{NO_PATH_2}}` |
| `{{CONDITION_N}}` | `{{YES_PATH_N}}` | `{{NO_PATH_N}}` |

Document every branching decision explicitly. Engineers should not need to infer which path to follow — if a condition requires judgment, add the criteria needed to make that judgment here.

---

## Resolution Criteria

`{{RESOLUTION_CRITERIA}}`

Resolution criteria must be objective and verifiable. Avoid subjective criteria like "service feels stable" — instead define specific metrics, health checks, or confirmation steps that must all pass.

---

## Post-Incident Actions

- **Postmortem trigger:** open postmortem document if SEV ≤ `{{POSTMORTEM_THRESHOLD}}`
- **Retrospective note:** `{{RETROSPECTIVE_NOTE}}`
- **Playbook review:** update this playbook within `{{PLAYBOOK_REVIEW_WINDOW}}` days of the incident

Schedule the postmortem within 48 hours while memory is fresh. Use the retrospective note to capture immediate learnings even before the full postmortem is complete.

---

## Source Attribution

- Source manifests: operations__nist_cisa.md, operations__google_sre.md, platform__aws_well_architected.md
- Primary source basis: PagerDuty Incident Response Guide and Google SRE incident management practices
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
