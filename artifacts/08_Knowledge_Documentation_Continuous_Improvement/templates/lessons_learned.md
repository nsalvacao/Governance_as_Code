---
title: Lessons Learned Template
artifact_type: template
status: public
visibility: public
classification: public
owner: knowledge-platform
review_cadence: quarterly
applies_to: stabilized incidents, experiments, and delivery retrospectives
source_basis: Google SRE and NIST learning-from-events practices
source_manifests:
  - operations__google_sre.md
  - operations__nist_cisa.md
alignment_mode: hybrid-synthesis
updated: 2026-03-30
---

## Purpose

Record reusable lessons that should change future behavior, not just summarize a past event. A lesson learned is only complete when it identifies who should act on it, how that change will be verified, and where this document is archived for future reference.

---

## Event Context

**Event type:** {{EVENT_TYPE}} _(incident / project / experiment — select one)_
**Date:** {{DATE}}
**Participants:**
- {{PARTICIPANT_1}}
- {{PARTICIPANT_2}}
- {{PARTICIPANT_N}}

The event type determines the appropriate framing. Incident lessons focus on detection, response, and systemic gaps. Project lessons focus on delivery process and decision quality. Experiment lessons focus on hypothesis validity and methodology.

---

## What Happened

{{SUMMARY}}

Provide a concise, factual summary of the event. This is context for readers who were not involved. Keep it to 3–5 sentences and link to the source document (postmortem, RCA, or project record) for full detail.

---

## Lessons

Each lesson must be specific enough to act on and general enough to apply beyond this single event.

| Lesson | Category | Impact | Applicable to |
|---|---|---|---|
| {{LESSON_1}} | technical / process / people / communication | high / medium / low | {{APPLICABILITY}} |
| {{LESSON_2}} | technical / process / people / communication | high / medium / low | {{APPLICABILITY}} |
| {{LESSON_N}} | technical / process / people / communication | high / medium / low | {{APPLICABILITY}} |

Applicability describes the scope of teams, services, or contexts where this lesson applies. A lesson with narrow applicability may still be high-impact if the context is critical.

---

## What Worked Well

Explicitly capturing strengths prevents them from being accidentally eliminated in future process changes.

- {{STRENGTH_1}}
- {{STRENGTH_2}}
- {{STRENGTH_N}}

---

## What to Improve

Improvement areas should map directly to lessons. Avoid vague statements like "improve communication" — name the specific gap and the mechanism for addressing it.

- {{IMPROVE_1}}
- {{IMPROVE_2}}
- {{IMPROVE_N}}

---

## Action Items

| Action | Owner | Due | Done |
|---|---|---|---|
| {{ACTION_1}} | {{OWNER}} | {{DUE}} | yes / no |
| {{ACTION_2}} | {{OWNER}} | {{DUE}} | yes / no |
| {{ACTION_N}} | {{OWNER}} | {{DUE}} | yes / no |

Action items here are the direct follow-through on lessons. Each action must trace to at least one lesson. Actions without owners will not be completed.

---

## Knowledge Artifacts Created

Documents produced as a direct result of this lessons-learned exercise.

| Link | Type |
|---|---|
| {{ARTIFACT_LINK}} | runbook / ADR / postmortem / policy |
| {{ARTIFACT_LINK}} | runbook / ADR / postmortem / policy |

If no artifacts were created, explain why — either the learning was already captured elsewhere, or it is a gap to address.

---

## Distribution List

**Who should read this:** {{DISTRIBUTION}}

Name the teams, roles, or individuals who should be notified of these lessons. Lessons that are not distributed do not change behavior beyond the immediate participants.

---

## Archived at

{{ARCHIVE_LOCATION}}

Record the canonical location where this document is stored long-term. The archive location enables future teams to search for prior learning when facing similar situations.

---

## Source Attribution

- Source manifests: operations__google_sre.md, operations__nist_cisa.md
- Primary source basis: Google SRE and NIST learning-from-events practices
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-30
