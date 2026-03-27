[![Status](https://img.shields.io/badge/status-discovery-2563eb)](./decision_log.md)
[![Wave](https://img.shields.io/badge/wave-catalog--coverage-0f766e)](./decision_log.md)
[![Validation](https://img.shields.io/badge/validation-deterministic-15803d)](./.github/workflows/validate-governance-artifacts.yml)
[![Visibility](https://img.shields.io/badge/visibility-public-475569)](#public-document-map)

# Central Governance Repository

This repository is the concrete public instance of the organisation's central governance system. It serves two roles at the same time:

1. it is the live repository where this governance corpus is maintained;
2. it is the source library for reusable templates, schemas, scripts, workflows, and standards that downstream repositories may selectively instantiate.

## What this repository is

- A single source of truth for governance method, document rules, reusable artifacts, and deterministic validation.
- A public anchor for discovery decisions, curation rules, and the evolving document map.
- A reusable library whose assets are organised by governance dimension, not by file type alone.

## Why now

The repository has moved out of pure discovery and into catalog coverage. The current focus is to make the operating model explicit, reusable, machine-consumable, and fully indexable from the public README before deeper schema and automation waves.

## Repository model

| Layer | Purpose | Location |
|---|---|---|
| Repository instance | Documents and GitHub-native files that describe and operate **this** repository | repository root and `/.github/` |
| Artifact library | Reusable standards, templates, schemas, scripts, partials, and workflow definitions for downstream repositories | [`artifacts/`](./artifacts/README.md) |
| Private working material | Drafts, source extraction, internal rationale, and implementation notes not intended for publication | `/.private/` |

## Current catalog coverage

| Dimension | Current status | Canonical location |
|---|---|---|
| Cross-cutting conventions | Canonical coverage in place | [`artifacts/conventions/`](./artifacts/conventions) |
| Governance and method | Canonical coverage in place | [`artifacts/governance/`](./artifacts/governance) |
| Discovery, planning, and early learning | Canonical coverage in place | [`artifacts/discovery/`](./artifacts/discovery) |
| Architecture, security, and decision | Canonical coverage in place | [`artifacts/architecture/`](./artifacts/architecture) |
| Quality, review, and control | Canonical coverage in place | [`artifacts/quality/`](./artifacts/quality) |
| Delivery, change, and readiness | Canonical coverage in place | [`artifacts/delivery/`](./artifacts/delivery) |
| Platform delivery, automation, and AI operations | Canonical coverage in place | [`artifacts/platform/`](./artifacts/platform) |
| Operations and incidents | Canonical coverage in place | [`artifacts/operations/`](./artifacts/operations) |
| Continuity | Canonical coverage in place | [`artifacts/continuity/`](./artifacts/continuity) |
| Knowledge, documentation, and continuous improvement | Canonical coverage in place | [`artifacts/knowledge/`](./artifacts/knowledge) |
| Project, portfolio, and service governance | Canonical coverage in place | [`artifacts/project-governance/`](./artifacts/project-governance) |
| Risk, exceptions, and traceability | Canonical coverage in place | [`artifacts/risk/`](./artifacts/risk) |

## How to navigate

- Start with the [`Public Document Map`](#public-document-map) section below to understand the target corpus and its canonical artifact links.
- Read [`decision_log.md`](./decision_log.md) for accepted principles and structural decisions.
- Use [`artifacts/README.md`](./artifacts/README.md) to find reusable assets by category.
- Use [`GOVERNANCE.md`](./GOVERNANCE.md) and [`CONTRIBUTING.md`](./CONTRIBUTING.md) to understand how this repository itself is maintained.

## How reuse works

- Root files are **not** templates. They are the concrete instance for this repository.
- Reusable assets live under `artifacts/<dimension>/<artifact-type>/`.
- Downstream repositories should instantiate only the subset they need, using the templates and schemas in the artifact library rather than copying the root instance files.

## Validation and contribution

- The deterministic validator is executed with `python scripts/validate_governance_artifacts.py`.
- The CI wrapper lives at [/.github/workflows/validate-governance-artifacts.yml](/mnt/d/GitHub/.github/.github/workflows/validate-governance-artifacts.yml).
- Changes to reusable assets should normally happen in `artifacts/`; changes to root and `/.github/` should only happen when this repository's own instance behavior changes.

# Public Document Map

This section defines the public document corpus for a central technical governance repository.

Objectives of this version:
- make explicit the set of documents that supports method, decision, delivery, operations, continuity, and learning;
- separate normative documents from instantiable documents and evidence records;
- fix a canonical map before the phase of templates, schemas, and frontmatter.

## Legend

| Nature | Meaning |
|---|---|
| Normative | Defines policies, rules, standards, and operational contracts |
| Operational | Guides recurring execution, coordination, or response |
| Instantiable | Is created by a project, release, incident, decision, or initiative |
| Evidence | Records facts, decisions, results, and learning |

## Publication Conventions

This corpus follows a few public-facing conventions:

- use short, stable, and recognizable names; prefer common public terms over internal jargon;
- include concise YAML frontmatter for publication metadata, ownership, review cadence, visibility, and classification;
- use classification labels consistently, at minimum across `public`, `public-redacted`, and `private` where applicable;
- record ownership and review metadata where a document needs a clear maintainer or review cadence;
- preserve provenance and cross-links so each document points to its source, parent, or related records;
- keep archival and deprecation rules explicit so obsolete material can be retired without ambiguity;
- keep the public corpus free of internal rationale that does not help readers understand the system.

## Repository Implementation Note

The current repository implementation distinguishes between:

- repository-instance files at the root and under `/.github/`, which describe and operate this repository itself;
- reusable assets under `artifacts/<dimension>/<artifact-type>/`, which are the canonical templates, schemas, scripts, workflows, policies, and standards for downstream repositories.

This layout is intended to mirror the dimensional structure of this map while keeping a clear boundary between instance documents and reusable sources.

## 1. Governance & Method

| Document | Nature | Public role | Primary source basis | Canonical primary artifact |
|---|---|---|---|---|
| README / Repository Overview | Normative | Presents the repository purpose, scope, structure, and navigation | GitHub Docs | [`artifacts/governance/templates/repository_overview.md`](./artifacts/governance/templates/repository_overview.md) |
| GOVERNANCE.md / Governance Overview | Normative | Explains how the system is governed, who decides, and how it evolves | GitHub Docs | [`artifacts/governance/templates/governance_overview.md`](./artifacts/governance/templates/governance_overview.md) |
| Engineering Handbook | Normative | Anchor document for the operating model, roles, lifecycle, and required artifacts | Scrum Guide, GitHub Docs | [`artifacts/governance/templates/engineering_handbook.md`](./artifacts/governance/templates/engineering_handbook.md) |
| Workflow Definition | Normative | Defines the workflow used for development, review, and delivery | GitHub Docs, Scrum Guide | [`artifacts/governance/standards/workflow_definition.md`](./artifacts/governance/standards/workflow_definition.md) |
| Contribution Guidelines | Normative | Explains how to contribute, propose changes, and submit artifacts | GitHub Docs, Open Source Guides | [`artifacts/governance/templates/contribution_guidelines.md`](./artifacts/governance/templates/contribution_guidelines.md) |
| Code of Conduct | Normative | Defines behavioral standards and moderation mechanisms | GitHub Docs, Open Source Guides | [`artifacts/governance/policies/code_of_conduct_policy.md`](./artifacts/governance/policies/code_of_conduct_policy.md) |
| Coding Standards | Normative | Defines technical quality and consistency standards | GitHub Docs, Microsoft Learn | [`artifacts/conventions/standards/coding_standards.md`](./artifacts/conventions/standards/coding_standards.md) |
| Definition of Done / Quality Gates | Normative | States the minimum completion and validation criteria | Scrum Guide | [`artifacts/conventions/standards/definition_of_done_quality_gates.md`](./artifacts/conventions/standards/definition_of_done_quality_gates.md) |
| Documentation Policy | Normative | Defines what to document, when, and at what level of rigor | GitHub Docs, Diataxis | [`artifacts/conventions/standards/documentation_policy.md`](./artifacts/conventions/standards/documentation_policy.md) |
| ADR Policy | Normative | Defines when a decision requires a formal record | GitHub Docs, Microsoft Learn | [`artifacts/conventions/policies/adr_policy.md`](./artifacts/conventions/policies/adr_policy.md) |
| Incident Management Policy | Normative | Defines incident principles, severity, roles, and governance | NIST, Google SRE | [`artifacts/operations/policies/incident_management_policy.md`](./artifacts/operations/policies/incident_management_policy.md) |
| Release & Versioning Policy | Normative | Defines release rules, versioning, and change communication | GitHub Docs, Google SRE | [`artifacts/conventions/policies/release_versioning_policy.md`](./artifacts/conventions/policies/release_versioning_policy.md) |
| Knowledge Lifecycle Policy | Normative | Defines creation, review, update, archive, and retirement of knowledge | Diataxis, GitHub Docs | [`artifacts/conventions/policies/knowledge_lifecycle_policy.md`](./artifacts/conventions/policies/knowledge_lifecycle_policy.md) |

## 2. Discovery, Planning & Early Learning

| Document | Nature | Public role | Primary source basis | Canonical primary artifact |
|---|---|---|---|---|
| Discovery Brief / Problem Framing | Instantiable | Frames the problem, goal, constraints, and decision context | Scrum Guide | [`artifacts/discovery/templates/discovery_brief.md`](./artifacts/discovery/templates/discovery_brief.md) |
| Product Goal / Outcome Statement | Instantiable | States the product or initiative goal to pursue | Scrum Guide | [`artifacts/discovery/templates/product_goal_outcome_statement.md`](./artifacts/discovery/templates/product_goal_outcome_statement.md) |
| Product Backlog | Instantiable | Maintains the prioritized inventory of future work | Scrum Guide | [`artifacts/discovery/templates/product_backlog.md`](./artifacts/discovery/templates/product_backlog.md) |
| Planning Record | Instantiable | Records cycle goal, scope, and planning decisions | Scrum Guide | [`artifacts/discovery/templates/planning_record.md`](./artifacts/discovery/templates/planning_record.md) |
| Research / Experiment Log | Instantiable | Records hypotheses, tests, results, and observations | Scrum Guide, Google SRE | [`artifacts/discovery/templates/research_experiment_log.md`](./artifacts/discovery/templates/research_experiment_log.md) |
| Assumptions Register | Instantiable | Makes fragile or unvalidated assumptions explicit | Microsoft Learn | [`artifacts/discovery/templates/assumptions_register.md`](./artifacts/discovery/templates/assumptions_register.md) |
| Technical Retrospective | Instantiable | Reviews an iteration, cycle, or phase of work | Scrum Guide | [`artifacts/discovery/templates/technical_retrospective.md`](./artifacts/discovery/templates/technical_retrospective.md) |
| Pre-mortem / Failure Scenario Review | Instantiable | Anticipates failure modes, impact, and required preparation | Google SRE, Microsoft Learn | [`artifacts/discovery/templates/pre_mortem_failure_scenario_review.md`](./artifacts/discovery/templates/pre_mortem_failure_scenario_review.md) |
| FMEA / Failure Mode Analysis | Instantiable | Preemptively analyzes failure modes and mitigation | NIST, Microsoft Learn | [`artifacts/discovery/templates/fmea_failure_mode_analysis.md`](./artifacts/discovery/templates/fmea_failure_mode_analysis.md) |

## 3. Architecture, Security & Decision

| Document | Nature | Public role | Primary source basis | Canonical primary artifact |
|---|---|---|---|---|
| Architecture Decision Record (ADR) | Instantiable | Records hard-to-reverse decisions and their context | GitHub Docs, AWS Docs | [`artifacts/architecture/standards/architecture_decision_record_standard.md`](./artifacts/architecture/standards/architecture_decision_record_standard.md) |
| Design Rationale | Evidence | Preserves the detailed reasoning behind a complex decision | Microsoft Learn | [`artifacts/architecture/templates/design_rationale.md`](./artifacts/architecture/templates/design_rationale.md) |
| Trade-off Analysis | Instantiable | Compares viable options with costs, risk, and benefits | AWS Docs, Microsoft Learn | [`artifacts/architecture/templates/trade_off_analysis.md`](./artifacts/architecture/templates/trade_off_analysis.md) |
| Architecture Review Record | Evidence | Records the formal architecture review and its outcome | Microsoft Learn, AWS Docs | [`artifacts/architecture/templates/architecture_review_record.md`](./artifacts/architecture/templates/architecture_review_record.md) |
| Threat Model | Instantiable | Models threats, attack surfaces, and defensive priorities | Microsoft Learn | [`artifacts/architecture/templates/threat_model.md`](./artifacts/architecture/templates/threat_model.md) |
| Security Requirements Record | Instantiable | Links security requirements to decisions and mitigations | Microsoft Learn | [`artifacts/architecture/templates/security_requirements_record.md`](./artifacts/architecture/templates/security_requirements_record.md) |

## 4. Quality, Review & Control

| Document | Nature | Public role | Primary source basis | Canonical primary artifact |
|---|---|---|---|---|
| Review Ruleset / Merge Policy | Normative | Formalizes checks, minimum reviews, rulesets, and exceptions | GitHub Docs | [`artifacts/quality/standards/review_ruleset_and_merge_policy.md`](./artifacts/quality/standards/review_ruleset_and_merge_policy.md) |
| CODEOWNERS / Ownership Map | Normative | Defines ownership of code and documentation surfaces | GitHub Docs | [`artifacts/quality/standards/codeowners_ownership_map.md`](./artifacts/quality/standards/codeowners_ownership_map.md) |
| Issue Forms / Issue Templates | Operational | Standardizes the intake of bugs, requests, incidents, and investigations | GitHub Docs | [`artifacts/quality/templates/issue_forms_and_templates.md`](./artifacts/quality/templates/issue_forms_and_templates.md) |
| Pull Request Template | Operational | Standardizes context, impact, validation, and cross-links in PRs | GitHub Docs | [`artifacts/quality/templates/pull_request_template.md`](./artifacts/quality/templates/pull_request_template.md) |
| Security Policy | Normative | Defines how to report vulnerabilities and supported versions | GitHub Docs | [`artifacts/quality/policies/security_policy.md`](./artifacts/quality/policies/security_policy.md) |
| Test Strategy / Verification Policy | Normative | Explains validation types, criteria, and responsibilities | Microsoft Learn, Google SRE | [`artifacts/quality/standards/test_strategy_and_verification_policy.md`](./artifacts/quality/standards/test_strategy_and_verification_policy.md) |
| Operational / Production Readiness Review | Instantiable | Verifies whether the team can operate the change or service safely | Google SRE, AWS Docs | [`artifacts/quality/templates/production_readiness_review.md`](./artifacts/quality/templates/production_readiness_review.md) |
| Support Guidelines | Normative | Explains where to ask for help and how to distinguish support from contribution | GitHub Docs | [`artifacts/quality/standards/support_guidelines.md`](./artifacts/quality/standards/support_guidelines.md) |

## 5. Delivery, Change & Readiness

| Document | Nature | Public role | Primary source basis | Canonical primary artifact |
|---|---|---|---|---|
| Release Plan / Rollout Plan | Instantiable | Defines order, windows, dependencies, and rollout criteria | Google SRE, AWS Docs | [`artifacts/delivery/templates/release_plan_rollout_plan.md`](./artifacts/delivery/templates/release_plan_rollout_plan.md) |
| Release Checklist | Operational | Lists mandatory checks before publishing | GitHub Docs, Google SRE | [`artifacts/delivery/templates/release_checklist.md`](./artifacts/delivery/templates/release_checklist.md) |
| Rollback / Backout Plan | Operational | Defines how to safely revert a change | Google SRE, Microsoft Learn | [`artifacts/delivery/templates/rollback_backout_plan.md`](./artifacts/delivery/templates/rollback_backout_plan.md) |
| Change Record | Instantiable | Records the approved change, its context, and expected impact | NIST, AWS Docs | [`artifacts/delivery/templates/change_record.md`](./artifacts/delivery/templates/change_record.md) |
| Change Log / Release Notes | Evidence | Communicates what changed in a traceable way | GitHub Docs | [`artifacts/delivery/templates/change_log_release_notes.md`](./artifacts/delivery/templates/change_log_release_notes.md) |
| Change Communication | Instantiable | Defines the message, audience, and channels for change communication | Google SRE | [`artifacts/delivery/templates/change_communication.md`](./artifacts/delivery/templates/change_communication.md) |
| Post-Implementation Review (PIR) | Evidence | Evaluates real outcomes after enough operating time has passed | NIST, GOV.UK | [`artifacts/delivery/templates/post_implementation_review.md`](./artifacts/delivery/templates/post_implementation_review.md) |

## 6. Platform Delivery, Automation & AI Operations

| Document | Nature | Public role | Primary source basis | Canonical primary artifact |
|---|---|---|---|---|
| CI/CD Policy | Normative | Defines how build, test, release, and deployment automation should behave across environments | GitHub Docs | [`artifacts/platform/policies/ci_cd_policy.md`](./artifacts/platform/policies/ci_cd_policy.md) |
| CI Workflow / Build Pipeline Record | Operational or instantiable | Defines or records automated build, test, and validation flows | GitHub Docs | [`artifacts/platform/templates/ci_workflow_build_pipeline_record.md`](./artifacts/platform/templates/ci_workflow_build_pipeline_record.md) |
| CD / Deployment Pipeline Record | Operational or instantiable | Defines or records automated deployment and promotion flows | GitHub Docs, Microsoft Learn | [`artifacts/platform/templates/cd_deployment_pipeline_record.md`](./artifacts/platform/templates/cd_deployment_pipeline_record.md) |
| Environment Promotion Policy | Normative | Defines promotion rules across dev, test, staging, and production environments | GitHub Docs, Microsoft Learn | [`artifacts/platform/policies/environment_promotion_policy.md`](./artifacts/platform/policies/environment_promotion_policy.md) |
| Environment / Deployment Configuration Record | Instantiable | Captures deployable environment definitions, variables, and controlled configuration | GitHub Docs, OpenGitOps | [`artifacts/platform/templates/environment_deployment_configuration_record.md`](./artifacts/platform/templates/environment_deployment_configuration_record.md) |
| Infrastructure as Code / Platform Baseline Record | Instantiable | Records declarative infrastructure, platform defaults, and reusable baseline patterns | OpenGitOps, AWS Docs, Microsoft Learn | [`artifacts/platform/templates/infrastructure_as_code_platform_baseline_record.md`](./artifacts/platform/templates/infrastructure_as_code_platform_baseline_record.md) |
| Artifact / Build Provenance Record | Evidence | Preserves traceability between source, pipeline run, artifact, and deployment outcome | GitHub Docs | [`artifacts/platform/templates/artifact_build_provenance_record.md`](./artifacts/platform/templates/artifact_build_provenance_record.md) |
| GitOps Policy | Normative | Defines declarative delivery, reconciliation, and Git-as-source-of-truth rules | OpenGitOps | [`artifacts/platform/policies/gitops_policy.md`](./artifacts/platform/policies/gitops_policy.md) |
| GitOps Application / Environment Definition | Instantiable | Defines the desired state for workloads or environments under GitOps control | OpenGitOps, Flux, Argo CD | [`artifacts/platform/templates/gitops_application_environment_definition.md`](./artifacts/platform/templates/gitops_application_environment_definition.md) |
| MLOps / GenAIOps Policy | Normative | Defines the operating model for model lifecycle, automation, evaluation, and governance | Microsoft Learn, Google Cloud | [`artifacts/platform/policies/mlops_genaiops_policy.md`](./artifacts/platform/policies/mlops_genaiops_policy.md) |
| Model Registry Record | Evidence or instantiable | Tracks model versions, ownership, lineage, approval, and deployment state | Microsoft Learn, Google Cloud | [`artifacts/platform/templates/model_registry_record.md`](./artifacts/platform/templates/model_registry_record.md) |
| Dataset / Training Data Record | Evidence or instantiable | Tracks training data sources, versions, suitability, and lineage | Microsoft Learn, Google Cloud | [`artifacts/platform/templates/dataset_training_data_record.md`](./artifacts/platform/templates/dataset_training_data_record.md) |
| Evaluation Suite / Benchmark Record | Instantiable | Defines repeatable evaluation sets, metrics, thresholds, and comparison logic | OpenAI Docs, Microsoft Learn | [`artifacts/platform/templates/evaluation_suite_benchmark_record.md`](./artifacts/platform/templates/evaluation_suite_benchmark_record.md) |
| Prompt / System Instruction Registry | Instantiable | Tracks versioned prompts or system instructions used in production AI systems | OpenAI Docs, Microsoft Learn | [`artifacts/platform/templates/prompt_system_instruction_registry.md`](./artifacts/platform/templates/prompt_system_instruction_registry.md) |
| Model Release / Serving Record | Instantiable | Records model deployment, serving configuration, rollout, and rollback context | Microsoft Learn, Google Cloud | [`artifacts/platform/templates/model_release_serving_record.md`](./artifacts/platform/templates/model_release_serving_record.md) |
| Model Monitoring / Drift Report | Evidence | Records quality, drift, regressions, and operational signals after deployment | Microsoft Learn, Google Cloud | [`artifacts/platform/templates/model_monitoring_drift_report.md`](./artifacts/platform/templates/model_monitoring_drift_report.md) |
| AI Safety / Guardrail Policy | Normative | Defines safety checks, usage constraints, and operational guardrails for AI systems | OpenAI Docs, Microsoft Learn | [`artifacts/platform/policies/ai_safety_guardrail_policy.md`](./artifacts/platform/policies/ai_safety_guardrail_policy.md) |

## 7. Operations, Incidents & Continuity

| Document | Nature | Public role | Primary source basis | Canonical primary artifact |
|---|---|---|---|---|
| Service Overview / Service Fact Sheet | Instantiable | Summarizes purpose, dependencies, owners, SLOs, and operational context of the service | Google SRE, AWS Docs | [`artifacts/operations/templates/service_fact_sheet.md`](./artifacts/operations/templates/service_fact_sheet.md) |
| Incident Response Plan | Normative or operational | Defines process, roles, escalation, and coordination during incidents | NIST, Google SRE | [`artifacts/operations/templates/incident_response_plan.md`](./artifacts/operations/templates/incident_response_plan.md) |
| Incident Report | Evidence | Records the incident facts, impact, and base chronology | NIST | [`artifacts/operations/templates/incident_report.md`](./artifacts/operations/templates/incident_report.md) |
| Incident Timeline | Evidence | Preserves the temporal sequence of events during the incident | Google SRE | [`artifacts/operations/templates/incident_timeline.md`](./artifacts/operations/templates/incident_timeline.md) |
| Playbook | Operational | Guides investigation, triage, and decision-making in specific scenarios | AWS Docs, NIST | [`artifacts/operations/templates/playbook.md`](./artifacts/operations/templates/playbook.md) |
| Runbook | Operational | Guides mitigation, recovery, or repeatable step-by-step operation | AWS Docs, Google SRE | [`artifacts/operations/templates/runbook.md`](./artifacts/operations/templates/runbook.md) |
| SOP (Standard Operating Procedure) | Operational | Standardizes stable operational processes | NIST | [`artifacts/operations/templates/standard_operating_procedure.md`](./artifacts/operations/templates/standard_operating_procedure.md) |
| Incident Communications Plan | Operational | Defines how to communicate during an incident to teams, stakeholders, and users | Google SRE, NIST | [`artifacts/operations/templates/incident_communications_plan.md`](./artifacts/operations/templates/incident_communications_plan.md) |
| On-call & Escalation Guide | Operational | Explains escalation path, handoffs, and response expectations | Google SRE | [`artifacts/operations/templates/on_call_escalation_guide.md`](./artifacts/operations/templates/on_call_escalation_guide.md) |
| Service Continuity Plan / ISCP / DR Plan | Operational | Defines continuity, recovery, and service reconstitution | NIST | [`artifacts/continuity/templates/service_continuity_plan.md`](./artifacts/continuity/templates/service_continuity_plan.md) |
| Exercise / Drill Record | Evidence | Records drills, response tests, and lessons extracted | NIST, Google SRE | [`artifacts/continuity/templates/exercise_drill_record.md`](./artifacts/continuity/templates/exercise_drill_record.md) |

## 8. Knowledge, Documentation & Continuous Improvement

| Document | Nature | Public role | Primary source basis | Canonical primary artifact |
|---|---|---|---|---|
| Postmortem | Evidence | Blamelessly analyzes the incident, impact, and improvements | Google SRE | [`artifacts/knowledge/templates/postmortem.md`](./artifacts/knowledge/templates/postmortem.md) |
| Root Cause Analysis (RCA) | Evidence | Identifies causes and contributing factors explicitly | NIST | [`artifacts/knowledge/templates/root_cause_analysis.md`](./artifacts/knowledge/templates/root_cause_analysis.md) |
| Lessons Learned | Evidence | Consolidates reusable lessons | NIST, Google SRE | [`artifacts/knowledge/templates/lessons_learned.md`](./artifacts/knowledge/templates/lessons_learned.md) |
| Corrective Action Register | Evidence | Tracks corrective action, owner, due date, and status | Google SRE, NIST | [`artifacts/knowledge/templates/corrective_action_register.md`](./artifacts/knowledge/templates/corrective_action_register.md) |
| Knowledge Base Article | Instantiable | Turns stabilized knowledge into a reusable reference | GitHub Docs, Google SRE | [`artifacts/knowledge/templates/knowledge_base_article.md`](./artifacts/knowledge/templates/knowledge_base_article.md) |
| Service Review / Reliability Review | Instantiable | Reviews service health, operational trends, and improvement decisions | Google SRE | [`artifacts/knowledge/templates/service_review.md`](./artifacts/knowledge/templates/service_review.md) |
| SLO / Error Budget Policy | Normative or instantiable | Formalizes service objectives and decision rules when the budget is consumed | Google SRE | [`artifacts/knowledge/policies/slo_error_budget_policy.md`](./artifacts/knowledge/policies/slo_error_budget_policy.md) |
| Documentation Architecture / Information Model | Normative | Organizes the document corpus by types, relationships, and navigation | Diataxis | [`artifacts/knowledge/standards/documentation_architecture_information_model.md`](./artifacts/knowledge/standards/documentation_architecture_information_model.md) |
| Documentation Style Guide | Normative | Standardizes voice, structure, naming, and editorial conventions | GitHub Docs, Microsoft Learn, Diataxis | [`artifacts/knowledge/standards/documentation_style_guide.md`](./artifacts/knowledge/standards/documentation_style_guide.md) |
| Documentation Review & Ownership Matrix | Normative | Assigns ownership and review cadence to the document corpus | GitHub Docs | [`artifacts/knowledge/standards/documentation_review_ownership_matrix.md`](./artifacts/knowledge/standards/documentation_review_ownership_matrix.md) |
| Deprecation & Archival Policy | Normative | Regulates sunset, obsolescence, and document retention | GitHub Docs, Diataxis | [`artifacts/knowledge/policies/deprecation_archival_policy.md`](./artifacts/knowledge/policies/deprecation_archival_policy.md) |
| Decision Log | Evidence | Records official decisions in a traceable and cumulative way | GitHub Docs | [`artifacts/knowledge/standards/decision_log_standard.md`](./artifacts/knowledge/standards/decision_log_standard.md) |

## 9. Project, Portfolio & Service Governance

| Document | Nature | Public role | Primary source basis | Canonical primary artifact |
|---|---|---|---|---|
| Business Case / Value Case | Instantiable | Justifies the initiative in terms of value, cost, risk, and expected outcomes | PMI, PRINCE2 | [`artifacts/project-governance/templates/business_case.md`](./artifacts/project-governance/templates/business_case.md) |
| Project Charter / Project Brief | Instantiable | Formally frames the initiative, authority, scope, and initial direction | PMI, PRINCE2 | [`artifacts/project-governance/templates/project_charter.md`](./artifacts/project-governance/templates/project_charter.md) |
| Project Initiation / Management Plan | Instantiable | Consolidates the baseline approach for planning, governance, controls, and delivery | PMI, PRINCE2 | [`artifacts/project-governance/templates/project_initiation_management_plan.md`](./artifacts/project-governance/templates/project_initiation_management_plan.md) |
| Stakeholder Register | Instantiable | Records key stakeholders, their roles, interest, and influence | PMI | [`artifacts/project-governance/templates/stakeholder_register.md`](./artifacts/project-governance/templates/stakeholder_register.md) |
| Communications Management Plan | Instantiable | Defines communication objectives, audiences, cadence, and channels | PMI | [`artifacts/project-governance/templates/communications_management_plan.md`](./artifacts/project-governance/templates/communications_management_plan.md) |
| Issue Log / Issue Register | Evidence | Tracks issues requiring action, escalation, or resolution | PMI, PRINCE2 | [`artifacts/project-governance/templates/issue_log_register.md`](./artifacts/project-governance/templates/issue_log_register.md) |
| Status / Highlight Report | Evidence | Provides periodic visibility into progress, health, and material deviations | PRINCE2 | [`artifacts/project-governance/templates/status_highlight_report.md`](./artifacts/project-governance/templates/status_highlight_report.md) |
| Exception / Escalation Report | Evidence | Records deviations beyond agreed tolerances and the need for decision or intervention | PRINCE2 | [`artifacts/project-governance/templates/exception_escalation_report.md`](./artifacts/project-governance/templates/exception_escalation_report.md) |
| Benefits Review / Benefits Realization Record | Evidence | Reviews whether intended benefits were achieved and how they were sustained | PMI, PRINCE2 | [`artifacts/project-governance/templates/benefits_realization_record.md`](./artifacts/project-governance/templates/benefits_realization_record.md) |
| Service Catalog / Service Portfolio Record | Instantiable | Defines the set of services offered, their scope, and ownership | ITIL | [`artifacts/project-governance/templates/service_catalog.md`](./artifacts/project-governance/templates/service_catalog.md) |
| Service Level Policy / SLA Record | Normative or instantiable | Defines service targets, commitments, and review expectations | ITIL | [`artifacts/project-governance/policies/service_level_policy.md`](./artifacts/project-governance/policies/service_level_policy.md) |
| Service Request Model / Request Catalog | Operational | Standardizes repeatable request types and fulfillment paths | ITIL | [`artifacts/project-governance/templates/service_request_model.md`](./artifacts/project-governance/templates/service_request_model.md) |
| Problem Record / Problem Management Policy | Evidence or normative | Formalizes recurring-problem analysis and the practice for reducing incident recurrence | ITIL | [`artifacts/project-governance/policies/problem_management_policy.md`](./artifacts/project-governance/policies/problem_management_policy.md) |
| Known Error Record | Evidence | Preserves diagnosed but unresolved errors and known workarounds | ITIL | [`artifacts/project-governance/templates/known_error_record.md`](./artifacts/project-governance/templates/known_error_record.md) |
| Service Configuration / Asset Record | Evidence | Maintains traceable service components, dependencies, and managed assets | ITIL | [`artifacts/project-governance/templates/service_configuration_asset_record.md`](./artifacts/project-governance/templates/service_configuration_asset_record.md) |

## 10. Risk, Exceptions & Traceability

| Document | Nature | Public role | Primary source basis | Canonical primary artifact |
|---|---|---|---|---|
| Risk Register | Evidence | Tracks relevant risks, impact, probability, owner, and mitigation | NIST, Microsoft Learn | [`artifacts/risk/templates/risk_register.md`](./artifacts/risk/templates/risk_register.md) |
| Exception / Deviation Record | Evidence | Records deliberate deviations from policies, standards, or controls | NIST, Microsoft Learn | [`artifacts/risk/templates/exception_deviation_record.md`](./artifacts/risk/templates/exception_deviation_record.md) |
| Security Advisory / Vulnerability Record | Evidence | Records public advisories and the remediation history | GitHub Docs | [`artifacts/risk/templates/security_advisory_vulnerability_record.md`](./artifacts/risk/templates/security_advisory_vulnerability_record.md) |
| Audit Trail Policy | Normative | Defines minimum traceability for decisions, changes, and evidence | NIST | [`artifacts/risk/policies/audit_trail_policy.md`](./artifacts/risk/policies/audit_trail_policy.md) |
| Metrics & Review Cadence | Normative | Establishes review moments for the governance system itself | Google SRE, Scrum Guide | [`artifacts/risk/standards/metrics_review_cadence.md`](./artifacts/risk/standards/metrics_review_cadence.md) |

## Primary Source Frameworks

Sources used to consolidate this map:

- [Scrum Guide](https://scrumguides.org/)
- [GitHub Docs](https://docs.github.com/)
- [Open Source Guides](https://opensource.guide/)
- [Diataxis](https://diataxis.fr/)
- [NIST SP 800-61r3 - Incident Response Recommendations and Considerations for Cybersecurity Risk Management](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r3.pdf)
- [NIST SP 800-34 Rev. 1 - Contingency Planning Guide for Federal Information Systems](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-34r1.pdf)
- [Google SRE - Incident Management Guide](https://sre.google/resources/practices-and-processes/incident-management-guide/)
- [Google SRE - Postmortem Culture: Learning from Failure](https://sre.google/workbook/postmortem-culture/)
- [Google SRE - Example Error Budget Policy](https://sre.google/workbook/error-budget-policy/)
- [Google SRE - Production Readiness Review](https://sre.google/sre-book/evolving-sre-engagement-model/)
- [AWS Well-Architected - Operational Readiness Reviews (ORR)](https://docs.aws.amazon.com/wellarchitected/latest/operational-readiness-reviews/wa-operational-readiness-reviews.html)
- [AWS Well-Architected - Use playbooks to investigate issues](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_ready_to_support_use_playbooks.html)
- [AWS Well-Architected - Perform post-incident analysis](https://docs.aws.amazon.com/wellarchitected/latest/framework/ops_evolve_ops_perform_rca_process.html)
- [Microsoft Azure Well-Architected - Develop an Incident Management Practice](https://learn.microsoft.com/en-us/azure/well-architected/design-guides/incident-management)
- [Microsoft Azure Well-Architected - Safe deployment and rollback guidance](https://learn.microsoft.com/en-us/azure/architecture/framework/devops/release-engineering-rollback)
- [GitHub Actions documentation](https://docs.github.com/en/actions)
- [GitHub Docs - Continuous integration](https://docs.github.com/actions/automating-builds-and-tests/about-continuous-integration)
- [OpenGitOps](https://opengitops.dev/about)
- [Flux documentation](https://fluxcd.io/flux/components/)
- [Argo CD documentation](https://argo-cd.readthedocs.io/)
- [Azure Well-Architected - MLOps and GenAIOps for AI workloads](https://learn.microsoft.com/en-us/azure/well-architected/ai/mlops-genaiops)
- [Azure Architecture Center - Machine learning operations](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/machine-learning-operations-v2)
- [Google Cloud - MLOps: Continuous delivery and automation pipelines in machine learning](https://cloud.google.com/solutions/machine-learning/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning)
- [OpenAI Docs - Evaluation best practices](https://platform.openai.com/docs/guides/evaluation-best-practices)
- [OpenAI Docs - Safety checks](https://platform.openai.com/docs/guides/safety-checks)
- [GOV.UK - Post-Implementation Review](https://www.gov.uk/government/publications/post-implementation-review)
- [PMI Lexicon of Project Management Terms](https://www.pmi.org/-/media/pmi/documents/registered/pdf/pmbok-standards/pmi-lexicon-pm-terms.pdf)
- [PMI - PMBOK references surfaced through official PMI materials](https://www.pmi.org/-/media/pmi/documents/public/pdf/pmbok-standards/pmbok-guide-6th-edition-errata-4th-printing.pdf)
- [Axelos PRINCE2 templates and resource hub](https://www.axelos.com/resource-hub/template/prince2-7-a1-business-case-template)
- [PeopleCert / Axelos ITIL practice references](https://atv.peoplecert.org/accreditation/accreditation-model/)

## How to Read This Map

Reading rules:
- normative documents define the system;
- operational documents guide execution, coordination, or response;
- instantiable and evidence documents record facts, decisions, events, analysis, and concrete operations;
- the value of the system lies in the links between discovery, decision, delivery, operations, and learning.

## Source Attribution

- Source manifests: `governance__github_docs.md`
- Primary source basis: GitHub Docs, Open Source Guides, and the repository's accepted governance decisions
- Alignment mode: `hybrid-synthesis`
- Reviewed on: 2026-03-27
