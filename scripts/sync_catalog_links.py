#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path


README_PATH = Path("README.md")


CATALOG_LINKS = {
    "README / Repository Overview": "artifacts/governance/templates/repository_overview.md",
    "GOVERNANCE.md / Governance Overview": "artifacts/governance/templates/governance_overview.md",
    "Engineering Handbook": "artifacts/governance/templates/engineering_handbook.md",
    "Workflow Definition": "artifacts/governance/standards/workflow_definition.md",
    "Contribution Guidelines": "artifacts/governance/templates/contribution_guidelines.md",
    "Code of Conduct": "artifacts/governance/policies/code_of_conduct_policy.md",
    "Coding Standards": "artifacts/conventions/standards/coding_standards.md",
    "Definition of Done / Quality Gates": "artifacts/conventions/standards/definition_of_done_quality_gates.md",
    "Documentation Policy": "artifacts/conventions/standards/documentation_policy.md",
    "ADR Policy": "artifacts/conventions/policies/adr_policy.md",
    "Incident Management Policy": "artifacts/operations/policies/incident_management_policy.md",
    "Release & Versioning Policy": "artifacts/conventions/policies/release_versioning_policy.md",
    "Knowledge Lifecycle Policy": "artifacts/conventions/policies/knowledge_lifecycle_policy.md",
    "Discovery Brief / Problem Framing": "artifacts/discovery/templates/discovery_brief.md",
    "Product Goal / Outcome Statement": "artifacts/discovery/templates/product_goal_outcome_statement.md",
    "Product Backlog": "artifacts/discovery/templates/product_backlog.md",
    "Planning Record": "artifacts/discovery/templates/planning_record.md",
    "Research / Experiment Log": "artifacts/discovery/templates/research_experiment_log.md",
    "Assumptions Register": "artifacts/discovery/templates/assumptions_register.md",
    "Technical Retrospective": "artifacts/discovery/templates/technical_retrospective.md",
    "Pre-mortem / Failure Scenario Review": "artifacts/discovery/templates/pre_mortem_failure_scenario_review.md",
    "FMEA / Failure Mode Analysis": "artifacts/discovery/templates/fmea_failure_mode_analysis.md",
    "Architecture Decision Record (ADR)": "artifacts/architecture/standards/architecture_decision_record_standard.md",
    "Design Rationale": "artifacts/architecture/templates/design_rationale.md",
    "Trade-off Analysis": "artifacts/architecture/templates/trade_off_analysis.md",
    "Architecture Review Record": "artifacts/architecture/templates/architecture_review_record.md",
    "Threat Model": "artifacts/architecture/templates/threat_model.md",
    "Security Requirements Record": "artifacts/architecture/templates/security_requirements_record.md",
    "Review Ruleset / Merge Policy": "artifacts/quality/standards/review_ruleset_and_merge_policy.md",
    "CODEOWNERS / Ownership Map": "artifacts/quality/standards/codeowners_ownership_map.md",
    "Issue Forms / Issue Templates": "artifacts/quality/templates/issue_forms_and_templates.md",
    "Pull Request Template": "artifacts/quality/templates/pull_request_template.md",
    "Security Policy": "artifacts/quality/policies/security_policy.md",
    "Test Strategy / Verification Policy": "artifacts/quality/standards/test_strategy_and_verification_policy.md",
    "Operational / Production Readiness Review": "artifacts/quality/templates/production_readiness_review.md",
    "Support Guidelines": "artifacts/quality/standards/support_guidelines.md",
    "Release Plan / Rollout Plan": "artifacts/delivery/templates/release_plan_rollout_plan.md",
    "Release Checklist": "artifacts/delivery/templates/release_checklist.md",
    "Rollback / Backout Plan": "artifacts/delivery/templates/rollback_backout_plan.md",
    "Change Record": "artifacts/delivery/templates/change_record.md",
    "Change Log / Release Notes": "artifacts/delivery/templates/change_log_release_notes.md",
    "Change Communication": "artifacts/delivery/templates/change_communication.md",
    "Post-Implementation Review (PIR)": "artifacts/delivery/templates/post_implementation_review.md",
    "CI/CD Policy": "artifacts/platform/policies/ci_cd_policy.md",
    "CI Workflow / Build Pipeline Record": "artifacts/platform/templates/ci_workflow_build_pipeline_record.md",
    "CD / Deployment Pipeline Record": "artifacts/platform/templates/cd_deployment_pipeline_record.md",
    "Environment Promotion Policy": "artifacts/platform/policies/environment_promotion_policy.md",
    "Environment / Deployment Configuration Record": "artifacts/platform/templates/environment_deployment_configuration_record.md",
    "Infrastructure as Code / Platform Baseline Record": "artifacts/platform/templates/infrastructure_as_code_platform_baseline_record.md",
    "Artifact / Build Provenance Record": "artifacts/platform/templates/artifact_build_provenance_record.md",
    "GitOps Policy": "artifacts/platform/policies/gitops_policy.md",
    "GitOps Application / Environment Definition": "artifacts/platform/templates/gitops_application_environment_definition.md",
    "MLOps / GenAIOps Policy": "artifacts/platform/policies/mlops_genaiops_policy.md",
    "Model Registry Record": "artifacts/platform/templates/model_registry_record.md",
    "Dataset / Training Data Record": "artifacts/platform/templates/dataset_training_data_record.md",
    "Evaluation Suite / Benchmark Record": "artifacts/platform/templates/evaluation_suite_benchmark_record.md",
    "Prompt / System Instruction Registry": "artifacts/platform/templates/prompt_system_instruction_registry.md",
    "Model Release / Serving Record": "artifacts/platform/templates/model_release_serving_record.md",
    "Model Monitoring / Drift Report": "artifacts/platform/templates/model_monitoring_drift_report.md",
    "AI Safety / Guardrail Policy": "artifacts/platform/policies/ai_safety_guardrail_policy.md",
    "Service Overview / Service Fact Sheet": "artifacts/operations/templates/service_fact_sheet.md",
    "Incident Response Plan": "artifacts/operations/templates/incident_response_plan.md",
    "Incident Report": "artifacts/operations/templates/incident_report.md",
    "Incident Timeline": "artifacts/operations/templates/incident_timeline.md",
    "Playbook": "artifacts/operations/templates/playbook.md",
    "Runbook": "artifacts/operations/templates/runbook.md",
    "SOP (Standard Operating Procedure)": "artifacts/operations/templates/standard_operating_procedure.md",
    "Incident Communications Plan": "artifacts/operations/templates/incident_communications_plan.md",
    "On-call & Escalation Guide": "artifacts/operations/templates/on_call_escalation_guide.md",
    "Service Continuity Plan / ISCP / DR Plan": "artifacts/continuity/templates/service_continuity_plan.md",
    "Exercise / Drill Record": "artifacts/continuity/templates/exercise_drill_record.md",
    "Postmortem": "artifacts/knowledge/templates/postmortem.md",
    "Root Cause Analysis (RCA)": "artifacts/knowledge/templates/root_cause_analysis.md",
    "Lessons Learned": "artifacts/knowledge/templates/lessons_learned.md",
    "Corrective Action Register": "artifacts/knowledge/templates/corrective_action_register.md",
    "Knowledge Base Article": "artifacts/knowledge/templates/knowledge_base_article.md",
    "Service Review / Reliability Review": "artifacts/knowledge/templates/service_review.md",
    "SLO / Error Budget Policy": "artifacts/knowledge/policies/slo_error_budget_policy.md",
    "Documentation Architecture / Information Model": "artifacts/knowledge/standards/documentation_architecture_information_model.md",
    "Documentation Style Guide": "artifacts/knowledge/standards/documentation_style_guide.md",
    "Documentation Review & Ownership Matrix": "artifacts/knowledge/standards/documentation_review_ownership_matrix.md",
    "Deprecation & Archival Policy": "artifacts/knowledge/policies/deprecation_archival_policy.md",
    "Decision Log": "artifacts/knowledge/standards/decision_log_standard.md",
    "Business Case / Value Case": "artifacts/project-governance/templates/business_case.md",
    "Project Charter / Project Brief": "artifacts/project-governance/templates/project_charter.md",
    "Project Initiation / Management Plan": "artifacts/project-governance/templates/project_initiation_management_plan.md",
    "Stakeholder Register": "artifacts/project-governance/templates/stakeholder_register.md",
    "Communications Management Plan": "artifacts/project-governance/templates/communications_management_plan.md",
    "Issue Log / Issue Register": "artifacts/project-governance/templates/issue_log_register.md",
    "Status / Highlight Report": "artifacts/project-governance/templates/status_highlight_report.md",
    "Exception / Escalation Report": "artifacts/project-governance/templates/exception_escalation_report.md",
    "Benefits Review / Benefits Realization Record": "artifacts/project-governance/templates/benefits_realization_record.md",
    "Service Catalog / Service Portfolio Record": "artifacts/project-governance/templates/service_catalog.md",
    "Service Level Policy / SLA Record": "artifacts/project-governance/policies/service_level_policy.md",
    "Service Request Model / Request Catalog": "artifacts/project-governance/templates/service_request_model.md",
    "Problem Record / Problem Management Policy": "artifacts/project-governance/policies/problem_management_policy.md",
    "Known Error Record": "artifacts/project-governance/templates/known_error_record.md",
    "Service Configuration / Asset Record": "artifacts/project-governance/templates/service_configuration_asset_record.md",
    "Risk Register": "artifacts/risk/templates/risk_register.md",
    "Exception / Deviation Record": "artifacts/risk/templates/exception_deviation_record.md",
    "Security Advisory / Vulnerability Record": "artifacts/risk/templates/security_advisory_vulnerability_record.md",
    "Audit Trail Policy": "artifacts/risk/policies/audit_trail_policy.md",
    "Metrics & Review Cadence": "artifacts/risk/standards/metrics_review_cadence.md",
}


def relative_link(path: str) -> str:
    return f"[`{path}`](./{path})"


def main() -> int:
    lines = README_PATH.read_text(encoding="utf-8").splitlines()
    new_lines: list[str] = []
    current_section = ""
    in_catalog_table = False
    seen_rows: set[str] = set()

    for line in lines:
        if re.match(r"^## \d+\.", line):
            current_section = line[3:].strip()
            in_catalog_table = False
            new_lines.append(line)
            continue

        if current_section and line.startswith("| Document | Nature | Public role | Primary source basis"):
            in_catalog_table = True
            new_lines.append("| Document | Nature | Public role | Primary source basis | Canonical primary artifact |")
            continue

        if in_catalog_table and line.startswith("|---"):
            new_lines.append("|---|---|---|---|---|")
            continue

        if in_catalog_table and line.startswith("|"):
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if len(cells) < 4:
                new_lines.append(line)
                continue
            document = cells[0]
            if document == "Document":
                new_lines.append(line)
                continue
            try:
                path = CATALOG_LINKS[document]
            except KeyError as exc:
                raise SystemExit(f"Missing catalog link mapping for row: {document}") from exc
            seen_rows.add(document)
            new_lines.append(
                f"| {cells[0]} | {cells[1]} | {cells[2]} | {cells[3]} | {relative_link(path)} |"
            )
            continue

        if in_catalog_table and not line.startswith("|"):
            in_catalog_table = False

        new_lines.append(line)

    missing = sorted(set(CATALOG_LINKS) - seen_rows)
    if missing:
        raise SystemExit(f"Unused catalog link mappings: {', '.join(missing)}")

    README_PATH.write_text("\n".join(new_lines) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
