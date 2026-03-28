---
title: Pre-mortem / Failure Scenario Review Template
artifact_type: template
status: draft
visibility: public
classification: public
owner: governance@org
review_cadence: quarterly
applies_to: discovery and risk anticipation
source_basis: Gary Klein prospective hindsight pre-mortem method (Klein 2007)
source_manifests:
  - operations__google_sre.md
  - platform__microsoft_learn.md
alignment_mode: guided-synthesis
updated: 2026-03-27
---

## Pre-mortem — `{{PROJECT_NAME}}`

A pre-mortem applies Gary Klein's prospective hindsight technique: the team imagines the project has already failed and then works backward to identify causes. This mental time-travel overcomes optimism bias that suppresses risk identification in forward-looking planning. Unlike a risk register, a pre-mortem produces causes through narrative imagination, not abstract scoring.

> **How to run:** Before the session, all participants are told: "Imagine it is six months from now. The project has failed completely. Your task is to write down every reason you can think of for why it failed."

---

### Setup

| Field | Value |
|---|---|
| Project / initiative | `{{PROJECT_NAME}}` |
| Pre-mortem date | `{{DATE}}` |
| Facilitator | `{{FACILITATOR}}` |
| Participants | `{{PARTICIPANTS}}` |

---

### Imagined Failure Scenario

> Assume this project / release has completely failed. Describe the failure state as if you are writing a post-incident review six months from now.

`{{FAILURE_STATE}}`

Make the failure vivid and specific. Vague failure scenarios produce vague causes. Include: what did not get delivered, what broke, who was affected, and what the business/user impact was.

---

### Causes Brainstorm

Each participant writes their causes independently before group discussion. Collect all causes without judgment — evaluation comes later. Use the table to attribute causes to participants.

| Participant | Cause |
|---|---|
| `{{PARTICIPANT_1}}` | `{{CAUSE_1}}` |
| `{{PARTICIPANT_2}}` | `{{CAUSE_2}}` |
| `{{PARTICIPANT_3}}` | `{{CAUSE_3}}` |
| `{{PARTICIPANT_4}}` | `{{CAUSE_4}}` |

No cause is too obvious or too speculative at this stage. Silence optimism bias — every plausible cause is worth recording.

---

### Cause Clustering and Prioritisation

Group causes into thematic clusters, then assess each cluster's likelihood and impact.

| Cluster | Causes included | Likelihood (H/M/L) | Impact (H/M/L) |
|---|---|---|---|
| `{{CLUSTER_1}}` | `{{CLUSTER_1_CAUSES}}` | `{{LIKELIHOOD_1}}` | `{{IMPACT_1}}` |
| `{{CLUSTER_2}}` | `{{CLUSTER_2_CAUSES}}` | `{{LIKELIHOOD_2}}` | `{{IMPACT_2}}` |

High-likelihood + high-impact clusters require immediate prevention actions. Address these before the project proceeds past the current gate.

---

### Prevention Actions

For each prioritised cause cluster, define a concrete action that reduces either the likelihood or the impact of that failure.

| Cause cluster | Prevention action | Owner | Trigger |
|---|---|---|---|
| `{{CLUSTER_REF_1}}` | `{{PREVENTION_ACTION_1}}` | `{{OWNER_1}}` | `{{TRIGGER_1}}` |
| `{{CLUSTER_REF_2}}` | `{{PREVENTION_ACTION_2}}` | `{{OWNER_2}}` | `{{TRIGGER_2}}` |

**Trigger** defines the condition or event that activates the action (e.g., "if velocity drops below 60% of plan by Sprint 3").

---

### Early Warning Signals

Define observable signals that would indicate a failure cluster is becoming real. These are leading indicators, not lag indicators.

| Signal | Monitoring method | Threshold |
|---|---|---|
| `{{SIGNAL_1}}` | `{{MONITORING_METHOD_1}}` | `{{THRESHOLD_1}}` |
| `{{SIGNAL_2}}` | `{{MONITORING_METHOD_2}}` | `{{THRESHOLD_2}}` |

---

### Commitment to Actions

`{{COMMITMENT_SUMMARY}}`

The team commits to the prevention actions listed above. This summary is shared with stakeholders and referenced in the next project retrospective. Actions without owners and triggers do not constitute commitments.

## Source Attribution

- Source manifests: `operations__google_sre.md`, `platform__microsoft_learn.md`
- Primary source basis: Gary Klein, "Performing a Project Pre-mortem" (*Harvard Business Review*, 2007); prospective hindsight research (Klein et al., 1989)
- Alignment mode: guided-synthesis
- Reviewed on: 2026-03-27
