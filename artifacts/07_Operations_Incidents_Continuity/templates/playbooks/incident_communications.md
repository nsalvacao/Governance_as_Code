---
title: Incident Communications Playbook
artifact_type: template
status: public-draft
visibility: public
classification: public
owner: "{{OWNER_NAME}}"
review_cadence: quarterly
applies_to: communications playbook
source_basis: Google SRE Incident Management Guide and PagerDuty Incident Response communications practices
source_manifests:
  - operations__google_sre.md
  - operations__nist_cisa.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Purpose

Define how and when to communicate during an incident — internally to the team and externally to customers and stakeholders. Activate this playbook at SEV `{{MIN_SEVERITY}}` or whenever customer impact is confirmed.

---

## Trigger

Activate this playbook when:
- Incident severity is SEV ≤ `{{MIN_SEVERITY}}`
- Customer-impacting behaviour is confirmed
- An executive or external stakeholder requests a status update

Communications must begin before the root cause is known. Silence is worse than uncertainty — stakeholders need to know the team is aware and working on the problem.

---

## Stakeholder Activation List

| Stakeholder | Notify at severity | Channel |
|------------|-------------------|---------|
| `{{STAKEHOLDER_1}}` | SEV `{{NOTIFY_THRESHOLD_1}}` | `{{CHANNEL_1}}` |
| `{{STAKEHOLDER_2}}` | SEV `{{NOTIFY_THRESHOLD_2}}` | `{{CHANNEL_2}}` |
| `{{STAKEHOLDER_3}}` | SEV `{{NOTIFY_THRESHOLD_3}}` | `{{CHANNEL_3}}` |
| `{{STAKEHOLDER_N}}` | SEV `{{NOTIFY_THRESHOLD_N}}` | `{{CHANNEL_N}}` |

Notify stakeholders as soon as the severity threshold is confirmed. Do not wait for a resolution path to be identified before notifying — late notifications damage trust more than uncertain early notifications.

---

## Internal Communications Cadence

Update internal stakeholders every `{{UPDATE_INTERVAL}}` via `{{INTERNAL_CHANNEL}}`.

**Internal update format:**
```
{{INTERNAL_MSG_TEMPLATE}}
```

Assign the communications track owner to maintain this cadence. The IC should not be writing updates — they should be coordinating the response.

---

## External Communications Decision

Publish a public status page update if: `{{PUBLIC_CRITERIA}}`

**Decision checklist before publishing externally:**
- [ ] Impact to customers is confirmed
- [ ] Content approved by `{{APPROVAL_AUTHORITY}}`
- [ ] Legal or compliance review completed if required

**Public update format:**
```
{{PUBLIC_MSG_TEMPLATE}}
```

Do not publish external updates without approval from `{{APPROVAL_AUTHORITY}}`. A premature or inaccurate public update is harder to retract than a delayed one.

---

## Message Templates

### Internal Update

```
{{INTERNAL_MSG_TEMPLATE}}
```

### Public Status Page Update

```
{{PUBLIC_MSG_TEMPLATE}}
```

### Resolution Announcement

```
{{RESOLUTION_MSG_TEMPLATE}}
```

Store approved templates in `{{TEMPLATE_LOCATION}}` and reference them by name during incidents. Pre-approved templates reduce approval delays under pressure.

---

## Approval Process

All external messages must be approved by `{{APPROVAL_AUTHORITY}}` before publishing.

**Approval workflow:**
1. Communications lead drafts message using approved template
2. Submit to `{{APPROVAL_AUTHORITY}}` via `{{APPROVAL_CHANNEL}}`
3. Target approval time: `{{APPROVAL_SLA}}`
4. If approval is not received within `{{APPROVAL_ESCALATION_TIME}}`, escalate to `{{APPROVAL_ESCALATION_CONTACT}}`

---

## Communications Log

Maintain a log of all communications at `{{LOG_LOCATION}}`.

| Time | Audience | Channel | Message summary | Approved by |
|------|---------|---------|----------------|------------|
| `{{LOG_TIME_1}}` | `{{LOG_AUDIENCE_1}}` | `{{LOG_CHANNEL_1}}` | `{{LOG_SUMMARY_1}}` | `{{LOG_APPROVER_1}}` |

The communications log is required input for the post-incident review and any customer-facing postmortem.

---

## Source Attribution

- Source manifests: `operations__google_sre.md`, `operations__nist_cisa.md`
- Primary source basis: Google SRE Incident Management Guide and PagerDuty Incident Response communications practices
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
