[![Status](https://img.shields.io/badge/status-public--hardening-2563eb)](./decision_log.md)
[![Wave](https://img.shields.io/badge/wave-public--readiness-0f766e)](./decision_log.md)
[![Validation](https://img.shields.io/badge/validation-deterministic-15803d)](./.github/workflows/validate-governance-artifacts.yml)
[![Catalog](https://img.shields.io/badge/catalog-canonical-blue)](./artifacts/README.md)
[![Standards](https://img.shields.io/badge/standards-NIST%20%7C%20ITIL%20%7C%20SRE-blueviolet)](#primary-source-frameworks)
[![Architecture](https://img.shields.io/badge/architecture-dual--layer-informational)](./decision_log.md)
[![License](https://img.shields.io/badge/license-MIT-lightgrey)](#license-usage)
[![Visibility](https://img.shields.io/badge/visibility-public-475569)](#public-document-map)
[![Language](https://img.shields.io/badge/language-english-lightgrey)](#publication-conventions)

# Central Governance Repository

This repository is the concrete public instance of the organization's central governance system. It functions as a **Governance-as-Code** infrastructure, providing both the live operating model and a reusable library of technical standards.

## Table of Contents
- [Central Governance Repository](#central-governance-repository)
  - [Table of Contents](#table-of-contents)
  - [Governance Compass (Executive Index)](#governance-compass-executive-index)
  - [Governance Operating Model](#governance-operating-model)
    - [Repository Architecture](#repository-architecture)
    - [How to navigate](#how-to-navigate)
  - [Quick Start: Project Onboarding](#quick-start-project-onboarding)
- [Public Document Map (The Corpus)](#public-document-map-the-corpus)
  - [Primary Source Frameworks](#primary-source-frameworks)
  - [Governance Stewards \& Support](#governance-stewards--support)
  - [License \& Usage](#license--usage)
  - [Source Attribution](#source-attribution)

---

## Governance Compass (Executive Index)

The governance corpus is organized into 10 logical dimensions that follow the industrial technical lifecycle.

| Section | Governance Dimension | Focus Area | Status | Reusable Library |
| :--- | :--- | :--- | :--- | :--- |
| **01** | **Governance & Method** | Foundation & Norms | ✅ Ready | [`artifacts/01_Governance_Method/`](./artifacts/01_Governance_Method/) |
| **02** | **Discovery & Planning** | Ideation & Framing | ✅ Ready | [`artifacts/02_Discovery_Planning_Early_Learning/`](./artifacts/02_Discovery_Planning_Early_Learning/) |
| **03** | **Architecture & Security** | Design & Decision | ✅ Ready | [`artifacts/03_Architecture_Security_Decision/`](./artifacts/03_Architecture_Security_Decision/) |
| **04** | **Quality & Review** | Assurance & Ownership | ✅ Ready | [`artifacts/04_Quality_Review_Control/`](./artifacts/04_Quality_Review_Control/) |
| **05** | **Delivery & Readiness** | Change & Release | ✅ Ready | [`artifacts/05_Delivery_Change_Readiness/`](./artifacts/05_Delivery_Change_Readiness/) |
| **06** | **Platform & AI Ops** | Automation & AI Execution | ✅ Ready | [`artifacts/06_Platform_Delivery_Automation_AI_Operations/`](./artifacts/06_Platform_Delivery_Automation_AI_Operations/) |
| **07** | **Operations & Incidents** | Execution & Continuity | ✅ Ready | [`artifacts/07_Operations_Incidents_Continuity/`](./artifacts/07_Operations_Incidents_Continuity/) |
| **08** | **Knowledge & Learning** | Evolution & SRE | ✅ Ready | [`artifacts/08_Knowledge_Documentation_Continuous_Improvement/`](./artifacts/08_Knowledge_Documentation_Continuous_Improvement/) |
| **09** | **Project & Portfolio** | Strategy & Value | ✅ Ready | [`artifacts/09_Project_Portfolio_Service_Governance/`](./artifacts/09_Project_Portfolio_Service_Governance/) |
| **10** | **Risk & Traceability** | Control & Exceptions | ✅ Ready | [`artifacts/10_Risk_Exceptions_Traceability/`](./artifacts/10_Risk_Exceptions_Traceability/) |

---

## Governance Operating Model

The organization follows a **lifecycle-oriented governance flow**, where every project or service evolves through these standard gates.

```mermaid
graph LR
    A[01. Governance] --> B[02. Discovery]
    B --> C[03. Architecture]
    C --> D[04. Quality]
    D --> E[05. Delivery]
    E --> F[06. Platform]
    F --> G[07. Operations]
    G --> H[08. Knowledge]
    H --> I[09. Portfolio]
    I --> J[10. Risk]
    J --> A
    
    subgraph "The Feedback Loop"
    G -.-> B
    H -.-> C
    end
```

### Repository Architecture
| Layer | Purpose | Location |
|---|---|---|
| **Repository Instance** | Concrete documents and GitHub-native files operating **this** repository | Root and `/.github/` |
| **Artifact Library** | Reusable standards, templates, schemas, and workflows for **downstream** projects | [`artifacts/`](./artifacts/README.md) |
| **Private Workspace** | Internal rationale and drafts not intended for publication | `/.private/` |

### How to navigate
- **Physical structure:** The [`artifacts/`](./artifacts/README.md) directory is organized into 10 numbered sections (01 to 10) matching this map.
- **Governance Enforcement:** Standards are enforced via deterministic validation. Refer to [`scripts/validate_governance_artifacts.py`](./scripts/validate_governance_artifacts.py).
- **Public provenance:** Source manifests live under [`sources/manifests/`](./sources/README.md) and are the public basis for traceable attribution.
- **Exceptions & Deviations:** Recorded via the [`Exception / Deviation Record`](./artifacts/10_Risk_Exceptions_Traceability/templates/exception_deviation_record.md).

---

## Quick Start: Project Onboarding

To adopt this governance framework in a new repository, follow these three steps:

1.  **Initialize Metadata:** Copy the [Pull Request Template](./artifacts/04_Quality_Review_Control/templates/pull_request_template.md) and [Issue Forms](./artifacts/04_Quality_Review_Control/templates/issue_forms_and_templates.md) to your `.github/` folder.
2.  **Dimension Selection:** Identify which Governance Dimensions (01-10) apply to your project. Instantiate the corresponding `Normative` policies.
3.  **Validate Compliance:** Run the [Deterministic Validator](./scripts/validate_governance_artifacts.py) locally or integrate it into your CI/CD pipeline.

---

# Public Document Map (The Corpus)

Click on a dimension to explore its associated policies, standards, and templates. Each section includes the canonical catalog and, where relevant, a supporting-artifact table so the public index covers both primary anchors and secondary reusable assets.

<details>
<summary><b>01. Governance & Method (Foundation & Norms)</b></summary>

| Document | Nature | Public role | Primary source basis | Canonical primary artifact |
|---|---|---|---|---|
| README / Repository Overview | Normative | Presents the purpose and navigation | GitHub Docs | [Artifact](./artifacts/01_Governance_Method/templates/repository_overview.md) |
| GOVERNANCE.md / Governance Overview | Normative | Explains how the system evolves | GitHub Docs | [Artifact](./artifacts/01_Governance_Method/templates/governance_overview.md) |
| Engineering Handbook | Normative | Anchor document for the operating model | Scrum Guide | [Artifact](./artifacts/01_Governance_Method/templates/engineering_handbook.md) |
| Workflow Definition | Normative | Defines dev, review, and delivery flows | GitHub Docs | [Artifact](./artifacts/01_Governance_Method/standards/workflow_definition.md) |
| Contribution Guidelines | Normative | Explains how to submit changes | GitHub Docs | [Artifact](./artifacts/01_Governance_Method/templates/contribution_guidelines.md) |
| Code of Conduct | Normative | Defines behavioral standards | GitHub Docs | [Artifact](./artifacts/01_Governance_Method/policies/code_of_conduct_policy.md) |
| Coding Standards | Normative | Defines technical consistency standards | Microsoft Learn | [Artifact](./artifacts/01_Governance_Method/standards/coding_standards.md) |
| Definition of Done / Quality Gates | Normative | States minimum completion criteria | Scrum Guide | [Artifact](./artifacts/01_Governance_Method/standards/definition_of_done_quality_gates.md) |
| Documentation Policy | Normative | Defines level of rigor for documentation | Diataxis | [Artifact](./artifacts/01_Governance_Method/standards/documentation_policy.md) |
| ADR Policy | Normative | Defines when a formal record is required | AWS Docs | [Artifact](./artifacts/01_Governance_Method/policies/adr_policy.md) |
| Incident Management Policy | Normative | Defines severity, roles, and governance | NIST | [Artifact](./artifacts/01_Governance_Method/policies/incident_management_policy.md) |
| Release & Versioning Policy | Normative | Defines release and versioning rules | Google SRE | [Artifact](./artifacts/01_Governance_Method/policies/release_versioning_policy.md) |
| Knowledge Lifecycle Policy | Normative | Defines creation and archival of knowledge | Diataxis | [Artifact](./artifacts/01_Governance_Method/policies/knowledge_lifecycle_policy.md) |

### Supporting Artifacts

| Artifact | Role | Maturity | Public status | Primary link |
|---|---|---|---|---|
| ADR Standard | Governs how ADR templates and accepted decisions interact | Public draft | Supporting standard | [Link](./artifacts/01_Governance_Method/standards/adr_standard.md) |
| Automation & AI Execution | Defines deterministic versus AI-assisted execution behavior | Public draft | Supporting standard | [Link](./artifacts/01_Governance_Method/standards/automation_and_ai_execution.md) |
| Document Conventions | Defines placeholders, frontmatter, and writing rules | Public draft | Supporting standard | [Link](./artifacts/01_Governance_Method/standards/document_conventions.md) |
| Source Attribution Standard | Governs traceable attribution blocks and alignment modes | Public draft | Supporting standard | [Link](./artifacts/01_Governance_Method/standards/source_attribution_standard.md) |
| Architecture Decision Record Template | Reusable ADR body template for downstream repositories | Public draft | Supporting template | [Link](./artifacts/01_Governance_Method/templates/architecture_decision_record.md) |
| Decision Log Entry Template | Reusable decision entry template aligned with the public decision log | Public draft | Supporting template | [Link](./artifacts/01_Governance_Method/templates/decision_log_entry.md) |
| GitHub-native Pull Request Template | Ready-to-copy PR template for downstream repositories | Public | Supporting GitHub-native template | [Link](./artifacts/01_Governance_Method/templates/github-native/PULL_REQUEST_TEMPLATE.md) |
| Source Attribution Partial | Reusable attribution footer partial for template composition | Public draft | Supporting partial | [Link](./artifacts/01_Governance_Method/templates/partials/source_attribution.md) |
| Repository-health README Template | Reusable instance README baseline for downstream repositories | Public | Supporting instance template | [Link](./artifacts/01_Governance_Method/templates/repository-health/README.md) |
| Repository-health GOVERNANCE Template | Reusable instance governance baseline for downstream repositories | Public | Supporting instance template | [Link](./artifacts/01_Governance_Method/templates/repository-health/GOVERNANCE.md) |
| Repository-health CONTRIBUTING Template | Reusable instance contribution baseline for downstream repositories | Public | Supporting instance template | [Link](./artifacts/01_Governance_Method/templates/repository-health/CONTRIBUTING.md) |
| Repository-health CODE_OF_CONDUCT Template | Reusable instance conduct baseline for downstream repositories | Public | Supporting instance template | [Link](./artifacts/01_Governance_Method/templates/repository-health/CODE_OF_CONDUCT.md) |
| Repository-health SECURITY Template | Reusable instance security baseline for downstream repositories | Public | Supporting instance template | [Link](./artifacts/01_Governance_Method/templates/repository-health/SECURITY.md) |
| Repository-health SUPPORT Template | Reusable instance support baseline for downstream repositories | Public | Supporting instance template | [Link](./artifacts/01_Governance_Method/templates/repository-health/SUPPORT.md) |

</details>

<details>
<summary><b>02. Discovery, Planning & Early Learning (Ideation & Framing)</b></summary>

| Document | Nature | Public role | Primary source basis | Canonical primary artifact |
|---|---|---|---|---|
| Discovery Brief / Problem Framing | Instantiable | Frames problem, goal, and constraints | Scrum Guide | [Artifact](./artifacts/02_Discovery_Planning_Early_Learning/templates/discovery_brief.md) |
| Product Goal / Outcome Statement | Instantiable | States the target product goal | Scrum Guide | [Artifact](./artifacts/02_Discovery_Planning_Early_Learning/templates/product_goal_outcome_statement.md) |
| Product Backlog | Instantiable | Inventory of prioritized future work | Scrum Guide | [Artifact](./artifacts/02_Discovery_Planning_Early_Learning/templates/product_backlog.md) |
| Planning Record | Instantiable | Records cycle goal and scope decisions | Scrum Guide | [Artifact](./artifacts/02_Discovery_Planning_Early_Learning/templates/planning_record.md) |
| Research / Experiment Log | Instantiable | Records hypotheses and observations | Google SRE | [Artifact](./artifacts/02_Discovery_Planning_Early_Learning/templates/research_experiment_log.md) |
| Assumptions Register | Instantiable | Makes unvalidated assumptions explicit | Microsoft Learn | [Artifact](./artifacts/02_Discovery_Planning_Early_Learning/templates/assumptions_register.md) |
| Technical Retrospective | Instantiable | Reviews an iteration or phase of work | Scrum Guide | [Artifact](./artifacts/02_Discovery_Planning_Early_Learning/templates/technical_retrospective.md) |
| Pre-mortem / Failure Scenario Review | Instantiable | Anticipates failure modes and impact | Google SRE | [Artifact](./artifacts/02_Discovery_Planning_Early_Learning/templates/pre_mortem_failure_scenario_review.md) |
| FMEA / Failure Mode Analysis | Instantiable | Preemptively analyzes mitigation | NIST | [Artifact](./artifacts/02_Discovery_Planning_Early_Learning/templates/fmea_failure_mode_analysis.md) |

</details>

<details>
<summary><b>03. Architecture, Security & Decision (Design & Decision)</b></summary>

| Document | Nature | Public role | Primary source basis | Canonical primary artifact |
|---|---|---|---|---|
| Architecture Decision Record (ADR) | Instantiable | Records hard-to-reverse decisions | AWS Docs | [Artifact](./artifacts/03_Architecture_Security_Decision/standards/architecture_decision_record_standard.md) |
| Design Rationale | Evidence | Preserves reasoning behind decisions | Microsoft Learn | [Artifact](./artifacts/03_Architecture_Security_Decision/templates/design_rationale.md) |
| Trade-off Analysis | Instantiable | Compares options with costs and risks | AWS Docs | [Artifact](./artifacts/03_Architecture_Security_Decision/templates/trade_off_analysis.md) |
| Architecture Review Record | Evidence | Records formal architecture review | Microsoft Learn | [Artifact](./artifacts/03_Architecture_Security_Decision/templates/architecture_review_record.md) |
| Threat Model | Instantiable | Models threats and defensive priorities | Microsoft Learn | [Artifact](./artifacts/03_Architecture_Security_Decision/templates/threat_model.md) |
| Security Requirements Record | Instantiable | Links requirements to mitigations | Microsoft Learn | [Artifact](./artifacts/03_Architecture_Security_Decision/templates/security_requirements_record.md) |

</details>

<details>
<summary><b>04. Quality, Review & Control (Assurance & Ownership)</b></summary>

| Document | Nature | Public role | Primary source basis | Canonical primary artifact |
|---|---|---|---|---|
| Review Ruleset / Merge Policy | Normative | Formalizes checks and merge policies | GitHub Docs | [Artifact](./artifacts/04_Quality_Review_Control/standards/review_ruleset_and_merge_policy.md) |
| CODEOWNERS / Ownership Map | Normative | Defines code and doc ownership | GitHub Docs | [Artifact](./artifacts/04_Quality_Review_Control/standards/codeowners_ownership_map.md) |
| Issue Forms / Issue Templates | Operational | Standardizes intake of requests | GitHub Docs | [Artifact](./artifacts/04_Quality_Review_Control/templates/issue_forms_and_templates.md) |
| Pull Request Template | Operational | Standardizes context and validation | GitHub Docs | [Artifact](./artifacts/04_Quality_Review_Control/templates/pull_request_template.md) |
| Security Policy | Normative | Defines vulnerability reporting | GitHub Docs | [Artifact](./artifacts/04_Quality_Review_Control/policies/security_policy.md) |
| Test Strategy / Verification Policy | Normative | Explains validation criteria | Google SRE | [Artifact](./artifacts/04_Quality_Review_Control/standards/test_strategy_and_verification_policy.md) |
| Operational / Production Readiness | Instantiable | Verifies change or service safety | Google SRE | [Artifact](./artifacts/04_Quality_Review_Control/templates/production_readiness_review.md) |
| Support Guidelines | Normative | Explains where to ask for help | GitHub Docs | [Artifact](./artifacts/04_Quality_Review_Control/standards/support_guidelines.md) |

</details>

<details>
<summary><b>05. Delivery, Change & Readiness (Change & Release)</b></summary>

| Document | Nature | Public role | Primary source basis | Canonical primary artifact |
|---|---|---|---|---|
| Release Plan / Rollout Plan | Instantiable | Defines order and rollout criteria | Google SRE | [Artifact](./artifacts/05_Delivery_Change_Readiness/templates/release_plan_rollout_plan.md) |
| Release Checklist | Operational | Mandatory checks before publishing | GitHub Docs | [Artifact](./artifacts/05_Delivery_Change_Readiness/templates/release_checklist.md) |
| Rollback / Backout Plan | Operational | Defines how to safely revert | Google SRE | [Artifact](./artifacts/05_Delivery_Change_Readiness/templates/rollback_backout_plan.md) |
| Change Record | Instantiable | Records approved change and impact | NIST | [Artifact](./artifacts/05_Delivery_Change_Readiness/templates/change_record.md) |
| Change Log / Release Notes | Evidence | Communicates what changed | GitHub Docs | [Artifact](./artifacts/05_Delivery_Change_Readiness/templates/change_log_release_notes.md) |
| Change Communication | Instantiable | Defines message and channels | Google SRE | [Artifact](./artifacts/05_Delivery_Change_Readiness/templates/change_communication.md) |
| Post-Implementation Review (PIR) | Evidence | Evaluates real outcomes | NIST | [Artifact](./artifacts/05_Delivery_Change_Readiness/templates/post_implementation_review.md) |

</details>

<details>
<summary><b>06. Platform Delivery, Automation & AI Operations (Automation & AI Execution)</b></summary>

| Document | Nature | Public role | Primary source basis | Canonical primary artifact |
|---|---|---|---|---|
| CI/CD Policy | Normative | Defines automation behavior | GitHub Docs | [Artifact](./artifacts/06_Platform_Delivery_Automation_AI_Operations/policies/ci_cd_policy.md) |
| CI Workflow Record | Operational | Records automated build flows | GitHub Docs | [Artifact](./artifacts/06_Platform_Delivery_Automation_AI_Operations/templates/ci_workflow_build_pipeline_record.md) |
| CD / Deployment Record | Operational | Records automated deployment flows | Microsoft Learn | [Artifact](./artifacts/06_Platform_Delivery_Automation_AI_Operations/templates/cd_deployment_pipeline_record.md) |
| Environment Promotion Policy | Normative | Defines promotion rules across envs | Microsoft Learn | [Artifact](./artifacts/06_Platform_Delivery_Automation_AI_Operations/policies/environment_promotion_policy.md) |
| Deployment Configuration Record | Instantiable | Captures environment variables | GitHub Docs | [Artifact](./artifacts/06_Platform_Delivery_Automation_AI_Operations/templates/environment_deployment_configuration_record.md) |
| Infrastructure as Code Baseline | Instantiable | Records platform baseline patterns | OpenGitOps | [Artifact](./artifacts/06_Platform_Delivery_Automation_AI_Operations/templates/infrastructure_as_code_platform_baseline_record.md) |
| Artifact / Build Provenance | Evidence | Preserves traceability of artifacts | GitHub Docs | [Artifact](./artifacts/06_Platform_Delivery_Automation_AI_Operations/templates/artifact_build_provenance_record.md) |
| GitOps Policy | Normative | Defines declarative delivery rules | OpenGitOps | [Artifact](./artifacts/06_Platform_Delivery_Automation_AI_Operations/policies/gitops_policy.md) |
| GitOps Environment Definition | Instantiable | Defines desired state for workloads | Flux / Argo CD | [Artifact](./artifacts/06_Platform_Delivery_Automation_AI_Operations/templates/gitops_application_environment_definition.md) |
| MLOps / GenAIOps Policy | Normative | Defines model lifecycle governance | Google Cloud | [Artifact](./artifacts/06_Platform_Delivery_Automation_AI_Operations/policies/mlops_genaiops_policy.md) |
| Model Registry Record | Evidence | Tracks model versions and lineage | Microsoft Learn | [Artifact](./artifacts/06_Platform_Delivery_Automation_AI_Operations/templates/model_registry_record.md) |
| Dataset / Training Data Record | Evidence | Tracks data lineage and suitability | Microsoft Learn | [Artifact](./artifacts/06_Platform_Delivery_Automation_AI_Operations/templates/dataset_training_data_record.md) |
| Evaluation Suite / Benchmark | Instantiable | Defines metrics and comparison logic | OpenAI Docs | [Artifact](./artifacts/06_Platform_Delivery_Automation_AI_Operations/templates/evaluation_suite_benchmark_record.md) |
| Prompt / Instruction Registry | Instantiable | Tracks production prompts | OpenAI Docs | [Artifact](./artifacts/06_Platform_Delivery_Automation_AI_Operations/templates/prompt_system_instruction_registry.md) |
| Model Release / Serving Record | Instantiable | Records rollout and rollback context | Google Cloud | [Artifact](./artifacts/06_Platform_Delivery_Automation_AI_Operations/templates/model_release_serving_record.md) |
| Model Monitoring / Drift Report | Evidence | Records operational signals after deploy | Microsoft Learn | [Artifact](./artifacts/06_Platform_Delivery_Automation_AI_Operations/templates/model_monitoring_drift_report.md) |
| AI Safety / Guardrail Policy | Normative | Defines operational guardrails | OpenAI Docs | [Artifact](./artifacts/06_Platform_Delivery_Automation_AI_Operations/policies/ai_safety_guardrail_policy.md) |

</details>

<details>
<summary><b>07. Operations, Incidents & Continuity (Execution & Continuity)</b></summary>

| Document | Nature | Public role | Primary source basis | Canonical primary artifact |
|---|---|---|---|---|
| Service Overview / Fact Sheet | Instantiable | Summarizes operational context | AWS Docs | [Artifact](./artifacts/07_Operations_Incidents_Continuity/templates/service_fact_sheet.md) |
| Incident Response Plan | Normative | Defines process, roles, and escalation | NIST | [Artifact](./artifacts/07_Operations_Incidents_Continuity/templates/incident_response_plan.md) |
| Incident Report | Evidence | Records facts and impact | NIST | [Artifact](./artifacts/07_Operations_Incidents_Continuity/templates/incident_report.md) |
| Incident Timeline | Evidence | Preserves the chronology of events | Google SRE | [Artifact](./artifacts/07_Operations_Incidents_Continuity/templates/incident_timeline.md) |
| Playbook | Operational | Guides triage and decision-making | AWS Docs | [Artifact](./artifacts/07_Operations_Incidents_Continuity/templates/playbook.md) |
| Runbook | Operational | Guides mitigation and recovery | Google SRE | [Artifact](./artifacts/07_Operations_Incidents_Continuity/templates/runbook.md) |
| SOP (Standard Op. Procedure) | Operational | Standardizes stable processes | NIST | [Artifact](./artifacts/07_Operations_Incidents_Continuity/templates/standard_operating_procedure.md) |
| Incident Communications Plan | Operational | Defines channels and stakeholders | Google SRE | [Artifact](./artifacts/07_Operations_Incidents_Continuity/templates/incident_communications_plan.md) |
| On-call & Escalation Guide | Operational | Explains handoffs and response | Google SRE | [Artifact](./artifacts/07_Operations_Incidents_Continuity/templates/on_call_escalation_guide.md) |
| Service Continuity Plan / DR | Operational | Defines recovery and ISCP | NIST | [Artifact](./artifacts/07_Operations_Incidents_Continuity/templates/service_continuity_plan.md) |
| Exercise / Drill Record | Evidence | Records drills and extracted lessons | NIST | [Artifact](./artifacts/07_Operations_Incidents_Continuity/templates/exercise_drill_record.md) |

### Supporting Artifacts

| Artifact | Role | Maturity | Public status | Primary link |
|---|---|---|---|---|
| Incident Response Policy | Governs incident process expectations behind the plan and report set | Public draft | Supporting policy | [Link](./artifacts/07_Operations_Incidents_Continuity/policies/incident_response_policy.md) |
| Incident Playbook Standard | Defines the common structure for specialized incident playbooks | Public draft | Supporting standard | [Link](./artifacts/07_Operations_Incidents_Continuity/standards/incident_playbook_standard.md) |
| Business Impact Analysis Standard | Governs how BIAs are authored and refreshed | Public draft | Supporting standard | [Link](./artifacts/07_Operations_Incidents_Continuity/standards/business_impact_analysis_standard.md) |
| Contingency Planning Standard | Governs contingency plan scope and review expectations | Public draft | Supporting standard | [Link](./artifacts/07_Operations_Incidents_Continuity/standards/contingency_planning_standard.md) |
| Business Impact Analysis Template | Reusable BIA template that feeds continuity planning | Public draft | Supporting template | [Link](./artifacts/07_Operations_Incidents_Continuity/templates/business_impact_analysis.md) |
| Contingency Plan Template | Reusable contingency planning template for downstream repositories | Public draft | Supporting template | [Link](./artifacts/07_Operations_Incidents_Continuity/templates/contingency_plan.md) |
| Escalation Playbook | Specialized playbook for escalation sequencing and ownership | Public draft | Supporting playbook | [Link](./artifacts/07_Operations_Incidents_Continuity/templates/playbooks/escalation.md) |
| Incident Communications Playbook | Specialized playbook for stakeholder messaging during incidents | Public draft | Supporting playbook | [Link](./artifacts/07_Operations_Incidents_Continuity/templates/playbooks/incident_communications.md) |
| Incident Coordination Playbook | Specialized playbook for coordination mechanics during active response | Public draft | Supporting playbook | [Link](./artifacts/07_Operations_Incidents_Continuity/templates/playbooks/incident_coordination.md) |
| Service Recovery Playbook | Specialized playbook for recovery sequencing and restoration control | Public draft | Supporting playbook | [Link](./artifacts/07_Operations_Incidents_Continuity/templates/playbooks/service_recovery.md) |

</details>

<details>
<summary><b>08. Knowledge, Documentation & Continuous Improvement (Evolution & SRE)</b></summary>

| Document | Nature | Public role | Primary source basis | Canonical primary artifact |
|---|---|---|---|---|
| Postmortem | Evidence | Blameless analysis of improvements | Google SRE | [Artifact](./artifacts/08_Knowledge_Documentation_Continuous_Improvement/templates/postmortem.md) |
| Root Cause Analysis (RCA) | Evidence | Identifies explicit causes | NIST | [Artifact](./artifacts/08_Knowledge_Documentation_Continuous_Improvement/templates/root_cause_analysis.md) |
| Lessons Learned | Evidence | Consolidates reusable lessons | Google SRE | [Artifact](./artifacts/08_Knowledge_Documentation_Continuous_Improvement/templates/lessons_learned.md) |
| Corrective Action Register | Evidence | Tracks owner and due date | NIST | [Artifact](./artifacts/08_Knowledge_Documentation_Continuous_Improvement/templates/corrective_action_register.md) |
| Knowledge Base Article | Instantiable | Reusable reference for knowledge | GitHub Docs | [Artifact](./artifacts/08_Knowledge_Documentation_Continuous_Improvement/templates/knowledge_base_article.md) |
| Service Review / Reliability | Instantiable | Reviews health and improvement | Google SRE | [Artifact](./artifacts/08_Knowledge_Documentation_Continuous_Improvement/templates/service_review.md) |
| SLO / Error Budget Policy | Normative | Formalizes service objectives | Google SRE | [Artifact](./artifacts/08_Knowledge_Documentation_Continuous_Improvement/policies/slo_error_budget_policy.md) |
| Documentation Architecture | Normative | Organizes information model | Diataxis | [Artifact](./artifacts/08_Knowledge_Documentation_Continuous_Improvement/standards/documentation_architecture_information_model.md) |
| Documentation Style Guide | Normative | Standardizes voice and structure | Microsoft Learn | [Artifact](./artifacts/08_Knowledge_Documentation_Continuous_Improvement/standards/documentation_style_guide.md) |
| Ownership Matrix | Normative | Assigns review cadence to corpus | GitHub Docs | [Artifact](./artifacts/08_Knowledge_Documentation_Continuous_Improvement/standards/documentation_review_ownership_matrix.md) |
| Deprecation & Archival Policy | Normative | Regulates document sunset | Diataxis | [Artifact](./artifacts/08_Knowledge_Documentation_Continuous_Improvement/policies/deprecation_archival_policy.md) |
| Decision Log | Evidence | Records official decisions | GitHub Docs | [Artifact](./artifacts/08_Knowledge_Documentation_Continuous_Improvement/standards/decision_log_standard.md) |

### Supporting Artifacts

| Artifact | Role | Maturity | Public status | Primary link |
|---|---|---|---|---|
| Error Budget Policy | Reliability companion policy used by service reviews and SLO governance | Public draft | Supporting policy | [Link](./artifacts/08_Knowledge_Documentation_Continuous_Improvement/policies/error_budget_policy.md) |
| Postmortem Standard | Defines how postmortems should be authored and evaluated | Public draft | Supporting standard | [Link](./artifacts/08_Knowledge_Documentation_Continuous_Improvement/standards/postmortem_standard.md) |
| Production Readiness Standard | Defines how readiness evidence should be interpreted across services | Public draft | Supporting standard | [Link](./artifacts/08_Knowledge_Documentation_Continuous_Improvement/standards/production_readiness_standard.md) |

</details>

<details>
<summary><b>09. Project, Portfolio & Service Governance (Strategy & Value)</b></summary>

| Document | Nature | Public role | Primary source basis | Canonical primary artifact |
|---|---|---|---|---|
| Business Case / Value Case | Instantiable | Justifies initiative value and risk | PRINCE2 | [Artifact](./artifacts/09_Project_Portfolio_Service_Governance/templates/business_case.md) |
| Project Charter / Brief | Instantiable | Frames authority and scope | PMI | [Artifact](./artifacts/09_Project_Portfolio_Service_Governance/templates/project_charter.md) |
| Project Management Plan | Instantiable | Consolidates baseline approach | PRINCE2 | [Artifact](./artifacts/09_Project_Portfolio_Service_Governance/templates/project_initiation_management_plan.md) |
| Stakeholder Register | Instantiable | Records key stakeholders and roles | PMI | [Artifact](./artifacts/09_Project_Portfolio_Service_Governance/templates/stakeholder_register.md) |
| Communications Plan | Instantiable | Defines objectives and channels | PMI | [Artifact](./artifacts/09_Project_Portfolio_Service_Governance/templates/communications_management_plan.md) |
| Issue Log / Register | Evidence | Tracks issues requiring action | PRINCE2 | [Artifact](./artifacts/09_Project_Portfolio_Service_Governance/templates/issue_log_register.md) |
| Status / Highlight Report | Evidence | Periodic visibility into health | PRINCE2 | [Artifact](./artifacts/09_Project_Portfolio_Service_Governance/templates/status_highlight_report.md) |
| Exception / Escalation Report | Evidence | Records deviations beyond tolerances | PRINCE2 | [Artifact](./artifacts/09_Project_Portfolio_Service_Governance/templates/exception_escalation_report.md) |
| Benefits Review Record | Evidence | Reviews if benefits were achieved | PMI | [Artifact](./artifacts/09_Project_Portfolio_Service_Governance/templates/benefits_realization_record.md) |
| Service Catalog | Instantiable | Defines the service value proposition | ITIL | [Artifact](./artifacts/09_Project_Portfolio_Service_Governance/templates/service_catalog.md) |
| Service Level Policy / SLA | Normative | Formalizes SLAs and commitments | ITIL | [Artifact](./artifacts/09_Project_Portfolio_Service_Governance/policies/service_level_policy.md) |
| Service Request Model | Operational | Optimizes delivery through request models | ITIL | [Artifact](./artifacts/09_Project_Portfolio_Service_Governance/templates/service_request_model.md) |
| Problem Management Policy | Normative | Practice for reducing incident recurrence | ITIL | [Artifact](./artifacts/09_Project_Portfolio_Service_Governance/policies/problem_management_policy.md) |
| Known Error Record | Evidence | Preserves diagnosed workarounds | ITIL | [Artifact](./artifacts/09_Project_Portfolio_Service_Governance/templates/known_error_record.md) |
| Service Configuration Asset | Evidence | Maintains traceable service components | ITIL | [Artifact](./artifacts/09_Project_Portfolio_Service_Governance/templates/service_configuration_asset_record.md) |

</details>

<details>
<summary><b>10. Risk, Exceptions & Traceability (Control & Exceptions)</b></summary>

| Document | Nature | Public role | Primary source basis | Canonical primary artifact |
|---|---|---|---|---|
| Risk Register | Evidence | Tracks risks, impact, and mitigation | NIST | [Artifact](./artifacts/10_Risk_Exceptions_Traceability/templates/risk_register.md) |
| Exception / Deviation Record | Evidence | Records deliberate policy deviations | Microsoft Learn | [Artifact](./artifacts/10_Risk_Exceptions_Traceability/templates/exception_deviation_record.md) |
| Security Advisory Record | Evidence | Records public advisories and remediation | GitHub Docs | [Artifact](./artifacts/10_Risk_Exceptions_Traceability/templates/security_advisory_vulnerability_record.md) |
| Audit Trail Policy | Normative | Defines minimum traceability rules | NIST | [Artifact](./artifacts/10_Risk_Exceptions_Traceability/policies/audit_trail_policy.md) |
| Metrics & Review Cadence | Normative | Establishes review moments for governance | Scrum Guide | [Artifact](./artifacts/10_Risk_Exceptions_Traceability/standards/metrics_review_cadence.md) |

</details>

---

## Primary Source Frameworks

This governance system is a hybrid synthesis of the following official source families:

- [**GitHub Docs**](https://docs.github.com/) - Community health files, repository governance, issue forms, pull request templates, workflows, and security reporting surfaces.
- [**Scrum Guide**](https://scrumguides.org/scrum-guide.html) - Planning, backlog management, iteration cadence, and retrospectives.
- [**Diataxis**](https://diataxis.fr/) - Documentation architecture and information design.
- [**NIST / CISA**](https://www.nist.gov/cyberframework) - Incident response, risk management, auditability, and continuity-aligned governance.
- [**Google SRE**](https://sre.google/workbook/) - Postmortems, error budgets, operational readiness, and reliability learning loops.
- [**AWS Well-Architected**](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) - Architecture trade-offs, reliability, and operational readiness.
- [**Microsoft Learn**](https://learn.microsoft.com/) - Platform delivery, security, architecture, and operational practice guidance.
- [**OpenAI Docs**](https://platform.openai.com/docs/overview) - AI operations, evaluation, prompt lifecycle, and safety guidance.
- [**PMI**](https://www.pmi.org/) - Project framing, stakeholder and communications governance.
- [**PRINCE2**](https://www.peoplecert.org/browse-certifications/project-programme-and-portfolio-management/PRINCE2-7) - Business case, project governance, and exception reporting.
- [**ITIL / PeopleCert**](https://www.peoplecert.org/browse-certifications/it-governance-and-service-management/ITIL-1) - Service catalog, service levels, requests, change enablement, and problem management.

Public source manifests for the currently adopted source families are published in [`sources/manifests/`](./sources/README.md).

## Governance Stewards & Support

This repository is maintained through pull requests, deterministic validation, and curator review by the repository maintainer.

- **Support:** Open an [Investigation Request](./.github/ISSUE_TEMPLATE/investigation_request.yml) for framework guidance.
- **Reporting:** Use [Incident Report](./.github/ISSUE_TEMPLATE/incident_report.yml) for governance breaches.

---

## License & Usage

This governance corpus is licensed under the [**MIT License**](./LICENSE). Reusable artifacts are provided as-is for organizational instantiation.

## Source Attribution

- **Source manifests:** [`governance__github_docs.md`](./sources/manifests/governance__github_docs.md), [`platform__aws_well_architected.md`](./sources/manifests/platform__aws_well_architected.md), [`platform__microsoft_learn.md`](./sources/manifests/platform__microsoft_learn.md)
- **Primary source basis:** GitHub Docs community governance guidance plus industrial technical frameworks.
- **Alignment mode:** `hybrid-synthesis`
- **Reviewed on:** 2026-03-28
