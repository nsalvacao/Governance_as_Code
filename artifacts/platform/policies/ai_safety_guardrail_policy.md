---
title: AI Safety / Guardrail Policy
artifact_type: policy
status: draft
visibility: public
classification: public
owner: platform-governance
review_cadence: quarterly
applies_to: AI systems, prompts, evaluations, and model-serving workflows
source_basis: NIST AI Risk Management Framework 1.0 + EU AI Act Article 13
source_manifests:
  - ai_ops__openai_docs.md
  - platform__microsoft_learn.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

# AI Safety / Guardrail Policy

## Policy Scope

This policy applies to all AI systems covered by `{{AI_SYSTEM_SCOPE}}` (e.g., production LLM APIs, fine-tuned classifiers, decision-support tools). Any system that generates, classifies, or ranks content on behalf of users must comply. Declare the full inventory of in-scope systems when instantiating this template.

## GOVERN — Governance Structure

NIST AI RMF GOVERN function requires accountability and policies to be established before an AI system is deployed.

- AI governance body: `{{AI_GOVERNANCE_BODY}}` (e.g., AI Review Board, ML Platform Team) — responsible for policy approval, exception handling, and risk acceptance.
- Accountable role: `{{ACCOUNTABLE_ROLE}}` (e.g., Chief AI Officer, VP Engineering) — individual who accepts organisational accountability for AI risk.
- Policy review cadence: quarterly or after any significant model change, whichever comes first.
- Risk tolerance statement: document the acceptable risk posture for `{{AI_SYSTEM_SCOPE}}` as part of the governance charter.

## MAP — Risk Identification

NIST AI RMF MAP function requires systematic identification of risks before and during system operation.

- Risk identification method: `{{RISK_ID_METHOD}}` (e.g., structured red-team exercise, STRIDE-AI threat model, FMEA).
- Use case categories in scope:
  - Category 1: `{{USE_CASE_CATEGORY_1}}`
  - Category 2: `{{USE_CASE_CATEGORY_2}}`
  - Category N: `{{USE_CASE_CATEGORY_N}}`
- Map each use case to its risk profile, data sensitivity tier, and applicable regulatory context before deployment.

## MEASURE — Risk Metrics and Evaluation

NIST AI RMF MEASURE function requires quantitative and qualitative metrics to track risk over time.

| Risk Metric | Placeholder | Evaluation Frequency |
|---|---|---|
| `{{RISK_METRIC_1}}` (e.g., harmful output rate) | value at last eval | `{{EVAL_FREQUENCY}}` |
| `{{RISK_METRIC_2}}` (e.g., fairness disparity index) | value at last eval | `{{EVAL_FREQUENCY}}` |
| `{{RISK_METRIC_N}}` | value at last eval | `{{EVAL_FREQUENCY}}` |

Evaluation frequency `{{EVAL_FREQUENCY}}` must be specified (e.g., weekly automated, monthly manual red-team). Results must be stored in the evaluation suite benchmark record.

## MANAGE — Risk Treatment and Acceptance

NIST AI RMF MANAGE function requires active treatment of identified risks and explicit acceptance of residual risks.

- Risk treatment approach: `{{RISK_TREATMENT}}` (e.g., retrain on safety-augmented data, add output classifier, restrict use case scope).
- Residual risk acceptance authority: `{{RISK_ACCEPTANCE_AUTHORITY}}` — the individual or body that signs off on risks that cannot be fully mitigated.
- Risk treatment decisions must be logged with rationale and reviewed at the next governance cycle.

## EU AI Act Article 13 — Transparency Requirements

EU AI Act Article 13 mandates that high-risk AI systems provide sufficient transparency to enable informed human oversight.

- Capability disclosure: `{{CAPABILITY_DISCLOSURE}}` — describe what the system can and cannot do, in language accessible to the intended user population.
- Limitations disclosure: `{{LIMITATIONS}}` — enumerate known failure modes, data conditions under which performance degrades, and out-of-scope uses.
- Human oversight mechanisms: `{{OVERSIGHT_MECHANISM}}` (e.g., mandatory human review before acting on high-stakes outputs, audit log accessible to regulators, ability to disable automated decision-making on request).

## Safety Guardrails

Guardrails must be applied at input and output layers for all in-scope systems.

- Input filtering rules:
  - Rule 1: `{{INPUT_FILTER_RULE_1}}` (e.g., block PII patterns before sending to model)
  - Rule 2: `{{INPUT_FILTER_RULE_2}}` (e.g., reject inputs matching known jailbreak signatures)
  - Rule N: `{{INPUT_FILTER_RULE_N}}`
- Output filtering rules:
  - Rule 1: `{{OUTPUT_FILTER_RULE_1}}` (e.g., run safety classifier on all generated text; block if score > threshold)
  - Rule 2: `{{OUTPUT_FILTER_RULE_2}}` (e.g., redact detected PII in model outputs before returning to caller)
  - Rule N: `{{OUTPUT_FILTER_RULE_N}}`
- Rate limiting: `{{RATE_LIMIT}}` — specify request-per-minute and token-per-day limits per user/service identity to prevent abuse and runaway costs.

## Prohibited Use Cases

The following use cases are explicitly prohibited for systems in scope of this policy. Attempting to use an in-scope system for these purposes must be blocked at the application layer.

- `{{PROHIBITED_USE_1}}` (e.g., automated generation of disinformation)
- `{{PROHIBITED_USE_2}}` (e.g., real-time facial recognition of individuals without consent)
- `{{PROHIBITED_USE_N}}`

## AI Incident Reporting

AI-specific incidents (e.g., harmful output, unexpected bias, safety guardrail bypass) require a dedicated reporting path.

- AI incident process: `{{AI_INCIDENT_PROCESS}}` — describe how incidents are reported, triaged, escalated, and resolved. Reference the incident management runbook or ticketing workflow.
- Incidents must be reviewed by `{{AI_GOVERNANCE_BODY}}` within the SLA defined for the risk severity tier.
- Post-incident reviews must produce a root cause and a guardrail improvement action item.

## Source Attribution

- Source manifests: `ai_ops__openai_docs.md`, `platform__microsoft_learn.md`
- Primary source basis: NIST AI Risk Management Framework 1.0 + EU AI Act Article 13
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
