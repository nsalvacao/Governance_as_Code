---
title: Corrective Action Register Template
artifact_type: template
status: public-draft
visibility: public
classification: public
owner: knowledge-platform
review_cadence: monthly
applies_to: postmortems, RCAs, reviews, and continuous improvement work
source_basis: PDCA (Plan-Do-Check-Act) cycle for continuous operational improvement
source_manifests:
  - operations__google_sre.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Purpose

Track action items that arise from incidents, reviews, and analysis so that improvement work stays visible, owned, and verifiable. A corrective action register is only effective if it is reviewed regularly and statuses are kept current.

---

## Register Context

**System or service:** {{SYSTEM_OR_SERVICE}}
**Register owner:** {{REGISTER_OWNER}}

The register owner is accountable for the review cadence and for escalating blocked or overdue actions. One register per service or bounded context is recommended to keep reviews focused.

---

## Corrective Actions

| CA ID | Source | Description | Root cause ref | Priority | Owner | Target date | PDCA phase | Evidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| CA-001 | {{SOURCE}} | {{CA_DESCRIPTION}} | {{ROOT_CAUSE_REF}} | P1/P2/P3 | {{OWNER}} | {{TARGET_DATE}} | Plan/Do/Check/Act | {{EVIDENCE}} | open / in-progress / closed / deferred |
| CA-002 | {{SOURCE}} | {{CA_DESCRIPTION}} | {{ROOT_CAUSE_REF}} | P1/P2/P3 | {{OWNER}} | {{TARGET_DATE}} | Plan/Do/Check/Act | {{EVIDENCE}} | open / in-progress / closed / deferred |
| CA-N | {{SOURCE}} | {{CA_DESCRIPTION}} | {{ROOT_CAUSE_REF}} | P1/P2/P3 | {{OWNER}} | {{TARGET_DATE}} | Plan/Do/Check/Act | {{EVIDENCE}} | open / in-progress / closed / deferred |

Source values: incident / audit / review / experiment. Priority: P1 = critical (complete within 7 days); P2 = high (complete within 30 days); P3 = standard (complete within 90 days). Deferred actions must include a deferral reason and new target date.

---

## PDCA Phase Requirements

### Plan

Before moving a CA to the Do phase, confirm:

- Problem is defined and the root cause is confirmed (link to RCA or postmortem).
- Solution is designed and reviewed by at least one peer.
- Success criteria and rollback plan are documented.

### Do

Before moving a CA to the Check phase, confirm:

- Solution has been implemented in the target environment.
- Evidence of implementation is captured (deploy record, PR link, config diff, or equivalent).
- No unintended side effects observed during rollout.

### Check

Before moving a CA to the Act phase, confirm:

- Effectiveness has been verified using the defined method: **{{VERIFICATION_METHOD}}**
- Metrics or observable signals confirm the root cause condition no longer exists.
- Verification was performed by someone other than the implementer, where feasible.

### Act

Before closing a CA as done, confirm:

- If effective: the fix has been standardized (runbook updated, automation added, policy revised).
- Lessons from this corrective action have been shared with relevant teams.
- If ineffective: a new CA has been opened with a revised approach and this CA is closed as superseded.

---

## Open Actions Review Cadence

**Review cadence:** {{REVIEW_CADENCE}}

At each review: confirm statuses are accurate, escalate overdue P1 and P2 actions, triage new actions from recent incidents, and archive closed actions older than one reset period. The register owner is responsible for driving this meeting.

---

## Source Attribution

- Source manifests: operations__google_sre.md
- Primary source basis: PDCA (Plan-Do-Check-Act) cycle for continuous operational improvement
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
