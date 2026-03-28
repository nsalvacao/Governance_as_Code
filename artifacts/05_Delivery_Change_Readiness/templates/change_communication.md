---
title: Change Communication Template
artifact_type: template
status: public-draft
visibility: public
classification: public
owner: "{{DELIVERY_OWNER}}"
review_cadence: quarterly
applies_to: release and change communication
source_basis: Stakeholder communication best practices aligned with ITIL 4 and SRE change communication guidance
source_manifests:
  - operations__google_sre.md
  - governance__github_docs.md
alignment_mode: guided-synthesis
updated: 2026-03-27
---

## Change Communication - `{{CHANGE_ID}}`

This template provides four sub-templates covering the full lifecycle of change communication: pre-change announcement, during-change status update, post-change confirmation, and rollback/incident notification. Select and populate the sub-template(s) appropriate to the communication event. Send each communication to the audiences and via the channels defined in the release plan.

---

### 1. Communication Metadata

| Field | Value |
|---|---|
| Change ID | `{{CHANGE_ID}}` |
| Change title | `{{CHANGE_TITLE}}` |
| Communication owner | `{{COMMUNICATION_OWNER}}` |
| Audience | `{{AUDIENCE}}` |
| Channel(s) | `{{CHANNEL}}` |
| Timing | `{{TIMING}}` |

The communication owner is accountable for sending all messages for this change on time. Audience and channel entries must match the communication plan in the release plan document.

---

### 2. Pre-Change Announcement

Send this message before the change implementation window opens. Timing is defined in the communication plan; typical lead time is 24–48 hours for significant changes affecting users.

**Subject / title:** `{{PRE_CHANGE_SUBJECT}}`

**Body:**

> **Upcoming change: `{{CHANGE_SUMMARY}}`**
>
> **Who is affected:** `{{AUDIENCE}}`
>
> **What is changing:** `{{CHANGE_DESCRIPTION}}`
>
> **Expected impact on users:** `{{USER_IMPACT}}`
>
> **When:** `{{IMPLEMENTATION_WINDOW_START}}` to `{{IMPLEMENTATION_WINDOW_END}}`
>
> **Expected duration:** `{{DURATION}}`
>
> **Action required (if any):** `{{USER_ACTION_REQUIRED}}`
>
> **Contact / support:** `{{CONTACT_POINT}}`

State the user impact clearly and honestly. If there is no user-facing impact, say so explicitly. Include a contact point for questions before the change window opens.

---

### 3. During-Change Status Update

Send this message at the start of the implementation window and at any significant milestone (phase gate reached, unexpected delay, issue encountered). Repeat as needed throughout the window.

**Subject / title:** `{{STATUS_UPDATE_SUBJECT}}`

**Body:**

> **Change status update: `{{CHANGE_TITLE}}`**
>
> **Status:** [in progress / phase N of N complete / delayed / issue encountered]
>
> **Current state:** `{{CURRENT_STATE}}`
>
> **Estimated completion:** `{{ESTIMATED_COMPLETION}}`
>
> **Any user impact right now:** `{{CURRENT_USER_IMPACT}}`
>
> **Next update expected at:** `{{NEXT_UPDATE_TIME}}`
>
> **Contact:** `{{CONTACT_POINT}}`

Send a status update at least every `{{STATUS_UPDATE_FREQUENCY}}` during the implementation window. If the estimated completion changes by more than 30 minutes, send an immediate update.

---

### 4. Post-Change Confirmation

Send this message as soon as post-deployment verification is complete and the change record is ready to close. Do not send until smoke tests and monitoring checks confirm success.

**Subject / title:** `{{POST_CHANGE_SUBJECT}}`

**Body:**

> **Change complete: `{{CHANGE_TITLE}}`**
>
> **Outcome:** [success / partial success — see notes / rolled back — see rollback notification]
>
> **Completed at:** `{{COMPLETION_TIME}}`
>
> **Verified by:** `{{VERIFIER}}`
>
> **Summary of what changed:** `{{CHANGE_SUMMARY}}`
>
> **User-facing result:** `{{USER_FACING_RESULT}}`
>
> **Next steps (if any):** `{{NEXT_STEPS}}`
>
> **Contact for issues:** `{{CONTACT_POINT}}`

If the outcome is "partial success", describe what was and was not completed and provide a timeline for the remaining work.

---

### 5. Rollback / Incident Notification

Send this message immediately when a rollback is initiated. Speed and clarity are more important than polish — send a brief initial message within 5 minutes of the rollback decision, then follow up with details.

**Subject / title:** `{{ROLLBACK_NOTIFICATION_SUBJECT}}`

**Body — initial (send within 5 minutes):**

> **ALERT: Rollback initiated for `{{CHANGE_TITLE}}`**
>
> **Time:** `{{ROLLBACK_INITIATED_AT}}`
>
> **Current state:** `{{ROLLBACK_CURRENT_STATE}}`
>
> **Impact:** `{{ROLLBACK_USER_IMPACT}}`
>
> **Next update:** `{{ROLLBACK_NEXT_UPDATE}}`
>
> **Contact:** `{{CONTACT_POINT}}`

**Body — follow-up (send when rollback complete):**

> **Rollback complete for `{{CHANGE_TITLE}}`**
>
> **Rollback completed at:** `{{ROLLBACK_COMPLETED_AT}}`
>
> **System state:** [restored to previous version / partial restoration — see notes]
>
> **Cause summary:** `{{ROLLBACK_CAUSE}}`
>
> **User impact duration:** `{{IMPACT_DURATION}}`
>
> **Next steps:** `{{ROLLBACK_NEXT_STEPS}}`
>
> **Post-incident review scheduled:** `{{PIR_DATE}}`

Do not speculate on root cause in the initial notification. Provide a factual summary in the follow-up only after the rollback is confirmed complete.

---

### 6. Follow-Up Routing

| Query type | Route to | Channel |
|---|---|---|
| User questions about the change | `{{QUESTIONS_ROUTE}}` | `{{QUESTIONS_CHANNEL}}` |
| Escalations / incidents post-release | `{{ESCALATION_ROUTE}}` | `{{ESCALATION_CHANNEL}}` |
| PIR participation requests | `{{PIR_ROUTE}}` | `{{PIR_CHANNEL}}` |

---

## Source Attribution

- Source manifests: `operations__google_sre.md`, `governance__github_docs.md`
- Primary source basis: Stakeholder communication best practices aligned with ITIL 4 and SRE change communication guidance
- Alignment mode: guided-synthesis
- Reviewed on: 2026-03-27
