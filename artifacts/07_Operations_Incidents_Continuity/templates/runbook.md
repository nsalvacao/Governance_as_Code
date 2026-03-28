---
title: Runbook
artifact_type: template
status: public-draft
visibility: public
classification: public
owner: "{{OWNER_NAME}}"
review_cadence: quarterly
applies_to: repeatable operational procedures
source_basis: Google SRE Workbook runbook practices and AWS Operational Runbooks
source_manifests:
  - operations__google_sre.md
  - platform__aws_well_architected.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Purpose

Provide the reusable structure for step-by-step operational execution that can be followed by humans and automation. Fill every `{{PLACEHOLDER}}` before activating. Keep each runbook scoped to a single symptom or alert.

---

## Runbook Header

| Field | Value |
|---|---|
| Service | `{{SERVICE_NAME}}` |
| Symptom | `{{SYMPTOM}}` |
| Typical severity | `{{TYPICAL_SEVERITY}}` |
| Last tested | `{{LAST_TESTED_DATE}}` |

Identify the service and the observable symptom this runbook addresses. The severity field guides initial triage priority — use SEV-1/SEV-2/SEV-3 or your team's defined scale.

---

## Symptom Description

**What the alert/symptom looks like:**
`{{SYMPTOM_DETAIL}}`

**Sample alert body:**
```
{{ALERT_EXAMPLE}}
```

Describe the alert or signal precisely so the on-call engineer can confirm they are looking at the right problem. Include dashboard links or log query references where applicable.

---

## Prerequisites

**Access required:**
`{{ACCESS_REQUIREMENT}}`

**Tools needed:**

| # | Tool |
|---|------|
| 1 | `{{TOOL_1}}` |
| 2 | `{{TOOL_2}}` |
| N | `{{TOOL_N}}` |

List all access permissions and CLI tools that must be available before the engineer begins. Validate these prerequisites during runbook test exercises.

---

## Diagnosis Steps

Work through the numbered steps in sequence. Branch only when the expected output does not match.

| Step | Command / Action | Expected output | If unexpected |
|------|-----------------|-----------------|---------------|
| 1 | `{{COMMAND_1}}` | `{{EXPECTED_1}}` | `{{DIAGNOSIS_BRANCH_1}}` |
| 2 | `{{COMMAND_2}}` | `{{EXPECTED_2}}` | `{{DIAGNOSIS_BRANCH_2}}` |
| N | `{{COMMAND_N}}` | `{{EXPECTED_N}}` | `{{DIAGNOSIS_BRANCH_N}}` |

Each diagnosis branch should either point to a more specific runbook or list the next investigation action. Avoid open-ended "investigate further" instructions.

---

## Remediation Steps

Apply remediations in order. Verify after each step before proceeding.

| Step | Action | Verification | Rollback if needed |
|------|--------|--------------|-------------------|
| 1 | `{{ACTION_1}}` | `{{VERIFICATION_1}}` | `{{ROLLBACK_STEP_1}}` |
| 2 | `{{ACTION_2}}` | `{{VERIFICATION_2}}` | `{{ROLLBACK_STEP_2}}` |
| N | `{{ACTION_N}}` | `{{VERIFICATION_N}}` | `{{ROLLBACK_STEP_N}}` |

Each remediation step must include a verification test so the engineer knows whether the action succeeded. Define the rollback path before executing any step that is not trivially reversible.

---

## Escalation Threshold

If not resolved after `{{ESCALATION_TIME}}`, escalate to `{{ESCALATION_CONTACT}}`.

Specify the concrete time limit and escalation target so engineers do not spend indefinite time on a runbook that is not converging. Include the communication channel (e.g., Slack, PagerDuty, phone) for reaching the escalation contact.

---

## Post-Resolution Verification

Confirm the service has returned to a healthy state before closing the incident.

| # | Verification check |
|---|-------------------|
| 1 | `{{VERIFY_1}}` |
| 2 | `{{VERIFY_2}}` |
| N | `{{VERIFY_N}}` |

All checks must pass before the incident is declared resolved. Capture evidence (screenshot, log excerpt) in the incident report.

---

## Related Runbooks

| # | Runbook |
|---|---------|
| 1 | `{{RELATED_RUNBOOK_1}}` |
| 2 | `{{RELATED_RUNBOOK_2}}` |
| N | `{{RELATED_RUNBOOK_N}}` |

Link to runbooks covering adjacent symptoms or dependencies so the on-call engineer can navigate quickly if this runbook's scope is not the root cause.

---

## Notes and Gotchas

| # | Note |
|---|------|
| 1 | `{{GOTCHA_1}}` |
| 2 | `{{GOTCHA_2}}` |
| N | `{{GOTCHA_N}}` |

Document known edge cases, environment-specific quirks, or common mistakes that have caused problems during previous incidents. Update this section after every post-mortem that involves this runbook.

---

## Source Attribution

- Source manifests: operations__google_sre.md, platform__aws_well_architected.md
- Primary source basis: Google SRE Workbook runbook practices and AWS Operational Runbooks
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
