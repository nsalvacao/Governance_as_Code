[![Status](https://img.shields.io/badge/status-discovery-2563eb)](./decision_log.md)
[![Wave](https://img.shields.io/badge/wave-first--wave-0f766e)](./decision_log.md)
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

The repository has moved out of pure discovery and into its first implementation wave. The current focus is to make the operating model explicit, reusable, and machine-consumable before expanding the catalog of templates and schemas.

## Repository model

| Layer | Purpose | Location |
|---|---|---|
| Repository instance | Documents and GitHub-native files that describe and operate **this** repository | repository root and `/.github/` |
| Artifact library | Reusable standards, templates, schemas, scripts, partials, and workflow definitions for downstream repositories | [`artifacts/`](./artifacts/README.md) |
| Private working material | Drafts, source extraction, internal rationale, and implementation notes not intended for publication | `/.private/` |

## Current first-wave coverage

| Dimension | Current status | Canonical location |
|---|---|---|
| Cross-cutting conventions | Implemented | [`artifacts/conventions/`](./artifacts/conventions) |
| Governance and decision architecture | Implemented | [`artifacts/governance/`](./artifacts/governance) |
| Reliability | Implemented | [`artifacts/reliability/`](./artifacts/reliability) |
| Operations and incidents | Implemented | [`artifacts/operations/`](./artifacts/operations) |
| Continuity | Implemented | [`artifacts/continuity/`](./artifacts/continuity) |
| Later dimensions from the public map | Planned | [`Public Document Map`](#public-document-map) |

## How to navigate

- Start with the [`Public Document Map`](#public-document-map) section below to understand the target corpus.
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

| Document | Nature | Public role | Primary source basis |
|---|---|---|---|
| README / Repository Overview | Normative | Presents the repository purpose, scope, structure, and navigation | GitHub Docs |
| GOVERNANCE.md / Governance Overview | Normative | Explains how the system is governed, who decides, and how it evolves | GitHub Docs |
| Engineering Handbook | Normative | Anchor document for the operating model, roles, lifecycle, and required artifacts | Scrum Guide, GitHub Docs |
| Workflow Definition | Normative | Defines the workflow used for development, review, and delivery | GitHub Docs, Scrum Guide |
| Contribution Guidelines | Normative | Explains how to contribute, propose changes, and submit artifacts | GitHub Docs, Open Source Guides |
| Code of Conduct | Normative | Defines behavioral standards and moderation mechanisms | GitHub Docs, Open Source Guides |
| Coding Standards | Normative | Defines technical quality and consistency standards | GitHub Docs, Microsoft Learn |
| Definition of Done / Quality Gates | Normative | States the minimum completion and validation criteria | Scrum Guide |
| Documentation Policy | Normative | Defines what to document, when, and at what level of rigor | GitHub Docs, Diataxis |
| ADR Policy | Normative | Defines when a decision requires a formal record | GitHub Docs, Microsoft Learn |
| Incident Management Policy | Normative | Defines incident principles, severity, roles, and governance | NIST, Google SRE |
| Release & Versioning Policy | Normative | Defines release rules, versioning, and change communication | GitHub Docs, Google SRE |
| Knowledge Lifecycle Policy | Normative | Defines creation, review, update, archive, and retirement of knowledge | Diataxis, GitHub Docs |

## 2. Discovery, Planning & Early Learning

| Document | Nature | Public role | Primary source basis |
|---|---|---|---|
| Discovery Brief / Problem Framing | Instantiable | Frames the problem, goal, constraints, and decision context | Scrum Guide |
| Product Goal / Outcome Statement | Instantiable | States the product or initiative goal to pursue | Scrum Guide |
| Product Backlog | Instantiable | Maintains the prioritized inventory of future work | Scrum Guide |
| Planning Record | Instantiable | Records cycle goal, scope, and planning decisions | Scrum Guide |
| Research / Experiment Log | Instantiable | Records hypotheses, tests, results, and observations | Scrum Guide, Google SRE |
| Assumptions Register | Instantiable | Makes fragile or unvalidated assumptions explicit | Microsoft Learn |
| Technical Retrospective | Instantiable | Reviews an iteration, cycle, or phase of work | Scrum Guide |
| Pre-mortem / Failure Scenario Review | Instantiable | Anticipates failure modes, impact, and required preparation | Google SRE, Microsoft Learn |
| FMEA / Failure Mode Analysis | Instantiable | Preemptively analyzes failure modes and mitigation | NIST, Microsoft Learn |

## 3. Architecture, Security & Decision

| Document | Nature | Public role | Primary source basis |
|---|---|---|---|
| Architecture Decision Record (ADR) | Instantiable | Records hard-to-reverse decisions and their context | GitHub Docs, AWS Docs |
| Design Rationale | Evidence | Preserves the detailed reasoning behind a complex decision | Microsoft Learn |
| Trade-off Analysis | Instantiable | Compares viable options with costs, risk, and benefits | AWS Docs, Microsoft Learn |
| Architecture Review Record | Evidence | Records the formal architecture review and its outcome | Microsoft Learn, AWS Docs |
| Threat Model | Instantiable | Models threats, attack surfaces, and defensive priorities | Microsoft Learn |
| Security Requirements Record | Instantiable | Links security requirements to decisions and mitigations | Microsoft Learn |

## 4. Quality, Review & Control

| Document | Nature | Public role | Primary source basis |
|---|---|---|---|
| Review Ruleset / Merge Policy | Normative | Formalizes checks, minimum reviews, rulesets, and exceptions | GitHub Docs |
| CODEOWNERS / Ownership Map | Normative | Defines ownership of code and documentation surfaces | GitHub Docs |
| Issue Forms / Issue Templates | Operational | Standardizes the intake of bugs, requests, incidents, and investigations | GitHub Docs |
| Pull Request Template | Operational | Standardizes context, impact, validation, and cross-links in PRs | GitHub Docs |
| Security Policy | Normative | Defines how to report vulnerabilities and supported versions | GitHub Docs |
| Test Strategy / Verification Policy | Normative | Explains validation types, criteria, and responsibilities | Microsoft Learn, Google SRE |
| Operational / Production Readiness Review | Instantiable | Verifies whether the team can operate the change or service safely | Google SRE, AWS Docs |
| Support Guidelines | Normative | Explains where to ask for help and how to distinguish support from contribution | GitHub Docs |

## 5. Delivery, Change & Readiness

| Document | Nature | Public role | Primary source basis |
|---|---|---|---|
| Release Plan / Rollout Plan | Instantiable | Defines order, windows, dependencies, and rollout criteria | Google SRE, AWS Docs |
| Release Checklist | Operational | Lists mandatory checks before publishing | GitHub Docs, Google SRE |
| Rollback / Backout Plan | Operational | Defines how to safely revert a change | Google SRE, Microsoft Learn |
| Change Record | Instantiable | Records the approved change, its context, and expected impact | NIST, AWS Docs |
| Change Log / Release Notes | Evidence | Communicates what changed in a traceable way | GitHub Docs |
| Change Communication | Instantiable | Defines the message, audience, and channels for change communication | Google SRE |
| Post-Implementation Review (PIR) | Evidence | Evaluates real outcomes after enough operating time has passed | NIST, GOV.UK |

## 6. Platform Delivery, Automation & AI Operations

| Document | Nature | Public role | Primary source basis |
|---|---|---|---|
| CI/CD Policy | Normative | Defines how build, test, release, and deployment automation should behave across environments | GitHub Docs |
| CI Workflow / Build Pipeline Record | Operational or instantiable | Defines or records automated build, test, and validation flows | GitHub Docs |
| CD / Deployment Pipeline Record | Operational or instantiable | Defines or records automated deployment and promotion flows | GitHub Docs, Microsoft Learn |
| Environment Promotion Policy | Normative | Defines promotion rules across dev, test, staging, and production environments | GitHub Docs, Microsoft Learn |
| Environment / Deployment Configuration Record | Instantiable | Captures deployable environment definitions, variables, and controlled configuration | GitHub Docs, OpenGitOps |
| Infrastructure as Code / Platform Baseline Record | Instantiable | Records declarative infrastructure, platform defaults, and reusable baseline patterns | OpenGitOps, AWS Docs, Microsoft Learn |
| Artifact / Build Provenance Record | Evidence | Preserves traceability between source, pipeline run, artifact, and deployment outcome | GitHub Docs |
| GitOps Policy | Normative | Defines declarative delivery, reconciliation, and Git-as-source-of-truth rules | OpenGitOps |
| GitOps Application / Environment Definition | Instantiable | Defines the desired state for workloads or environments under GitOps control | OpenGitOps, Flux, Argo CD |
| MLOps / GenAIOps Policy | Normative | Defines the operating model for model lifecycle, automation, evaluation, and governance | Microsoft Learn, Google Cloud |
| Model Registry Record | Evidence or instantiable | Tracks model versions, ownership, lineage, approval, and deployment state | Microsoft Learn, Google Cloud |
| Dataset / Training Data Record | Evidence or instantiable | Tracks training data sources, versions, suitability, and lineage | Microsoft Learn, Google Cloud |
| Evaluation Suite / Benchmark Record | Instantiable | Defines repeatable evaluation sets, metrics, thresholds, and comparison logic | OpenAI Docs, Microsoft Learn |
| Prompt / System Instruction Registry | Instantiable | Tracks versioned prompts or system instructions used in production AI systems | OpenAI Docs, Microsoft Learn |
| Model Release / Serving Record | Instantiable | Records model deployment, serving configuration, rollout, and rollback context | Microsoft Learn, Google Cloud |
| Model Monitoring / Drift Report | Evidence | Records quality, drift, regressions, and operational signals after deployment | Microsoft Learn, Google Cloud |
| AI Safety / Guardrail Policy | Normative | Defines safety checks, usage constraints, and operational guardrails for AI systems | OpenAI Docs, Microsoft Learn |

## 7. Operations, Incidents & Continuity

| Document | Nature | Public role | Primary source basis |
|---|---|---|---|
| Service Overview / Service Fact Sheet | Instantiable | Summarizes purpose, dependencies, owners, SLOs, and operational context of the service | Google SRE, AWS Docs |
| Incident Response Plan | Normative or operational | Defines process, roles, escalation, and coordination during incidents | NIST, Google SRE |
| Incident Report | Evidence | Records the incident facts, impact, and base chronology | NIST |
| Incident Timeline | Evidence | Preserves the temporal sequence of events during the incident | Google SRE |
| Playbook | Operational | Guides investigation, triage, and decision-making in specific scenarios | AWS Docs, NIST |
| Runbook | Operational | Guides mitigation, recovery, or repeatable step-by-step operation | AWS Docs, Google SRE |
| SOP (Standard Operating Procedure) | Operational | Standardizes stable operational processes | NIST |
| Incident Communications Plan | Operational | Defines how to communicate during an incident to teams, stakeholders, and users | Google SRE, NIST |
| On-call & Escalation Guide | Operational | Explains escalation path, handoffs, and response expectations | Google SRE |
| Service Continuity Plan / ISCP / DR Plan | Operational | Defines continuity, recovery, and service reconstitution | NIST |
| Exercise / Drill Record | Evidence | Records drills, response tests, and lessons extracted | NIST, Google SRE |

## 8. Knowledge, Documentation & Continuous Improvement

| Document | Nature | Public role | Primary source basis |
|---|---|---|---|
| Postmortem | Evidence | Blamelessly analyzes the incident, impact, and improvements | Google SRE |
| Root Cause Analysis (RCA) | Evidence | Identifies causes and contributing factors explicitly | NIST |
| Lessons Learned | Evidence | Consolidates reusable lessons | NIST, Google SRE |
| Corrective Action Register | Evidence | Tracks corrective action, owner, due date, and status | Google SRE, NIST |
| Knowledge Base Article | Instantiable | Turns stabilized knowledge into a reusable reference | GitHub Docs, Google SRE |
| Service Review / Reliability Review | Instantiable | Reviews service health, operational trends, and improvement decisions | Google SRE |
| SLO / Error Budget Policy | Normative or instantiable | Formalizes service objectives and decision rules when the budget is consumed | Google SRE |
| Documentation Architecture / Information Model | Normative | Organizes the document corpus by types, relationships, and navigation | Diataxis |
| Documentation Style Guide | Normative | Standardizes voice, structure, naming, and editorial conventions | GitHub Docs, Microsoft Learn, Diataxis |
| Documentation Review & Ownership Matrix | Normative | Assigns ownership and review cadence to the document corpus | GitHub Docs |
| Deprecation & Archival Policy | Normative | Regulates sunset, obsolescence, and document retention | GitHub Docs, Diataxis |
| Decision Log | Evidence | Records official decisions in a traceable and cumulative way | GitHub Docs |

## 9. Project, Portfolio & Service Governance

| Document | Nature | Public role | Primary source basis |
|---|---|---|---|
| Business Case / Value Case | Instantiable | Justifies the initiative in terms of value, cost, risk, and expected outcomes | PMI, PRINCE2 |
| Project Charter / Project Brief | Instantiable | Formally frames the initiative, authority, scope, and initial direction | PMI, PRINCE2 |
| Project Initiation / Management Plan | Instantiable | Consolidates the baseline approach for planning, governance, controls, and delivery | PMI, PRINCE2 |
| Stakeholder Register | Instantiable | Records key stakeholders, their roles, interest, and influence | PMI |
| Communications Management Plan | Instantiable | Defines communication objectives, audiences, cadence, and channels | PMI |
| Issue Log / Issue Register | Evidence | Tracks issues requiring action, escalation, or resolution | PMI, PRINCE2 |
| Status / Highlight Report | Evidence | Provides periodic visibility into progress, health, and material deviations | PRINCE2 |
| Exception / Escalation Report | Evidence | Records deviations beyond agreed tolerances and the need for decision or intervention | PRINCE2 |
| Benefits Review / Benefits Realization Record | Evidence | Reviews whether intended benefits were achieved and how they were sustained | PMI, PRINCE2 |
| Service Catalog / Service Portfolio Record | Instantiable | Defines the set of services offered, their scope, and ownership | ITIL |
| Service Level Policy / SLA Record | Normative or instantiable | Defines service targets, commitments, and review expectations | ITIL |
| Service Request Model / Request Catalog | Operational | Standardizes repeatable request types and fulfillment paths | ITIL |
| Problem Record / Problem Management Policy | Evidence or normative | Formalizes recurring-problem analysis and the practice for reducing incident recurrence | ITIL |
| Known Error Record | Evidence | Preserves diagnosed but unresolved errors and known workarounds | ITIL |
| Service Configuration / Asset Record | Evidence | Maintains traceable service components, dependencies, and managed assets | ITIL |

## 10. Risk, Exceptions & Traceability

| Document | Nature | Public role | Primary source basis |
|---|---|---|---|
| Risk Register | Evidence | Tracks relevant risks, impact, probability, owner, and mitigation | NIST, Microsoft Learn |
| Exception / Deviation Record | Evidence | Records deliberate deviations from policies, standards, or controls | NIST, Microsoft Learn |
| Security Advisory / Vulnerability Record | Evidence | Records public advisories and the remediation history | GitHub Docs |
| Audit Trail Policy | Normative | Defines minimum traceability for decisions, changes, and evidence | NIST |
| Metrics & Review Cadence | Normative | Establishes review moments for the governance system itself | Google SRE, Scrum Guide |

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
