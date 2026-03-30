---
title: Source attribution partial
artifact_type: template-partial
status: public
visibility: public
classification: public
owner: governance-team
review_cadence: quarterly
applies_to: governance artifacts
source_basis: governance__github_docs
source_manifests: governance__github_docs.md
alignment_mode: direct-adaptation
updated: 2026-03-30
---

<!-- HOW TO USE THIS PARTIAL
Copy the ## Source Attribution block below and append it as the final section of your artifact.
Replace each {{PLACEHOLDER}} with the correct value before committing.

Field guidance:
- {{SOURCE_MANIFEST_1}}, {{SOURCE_MANIFEST_2}}: Filenames of the source manifests that informed this artifact
  (e.g., `documentation__diataxis.md`). List all relevant manifests, comma-separated. At least one is required.
  Follow the naming convention: {{DOMAIN}}__{{SOURCE_NAME}}.md
- {{PRIMARY_SOURCE_BASIS}}: A short, human-readable description of the dominant source family
  (e.g., "Diataxis framework (Daniele Procida)" or "Scrum Guide 2020").
- {{ALIGNMENT_MODE}}: One of four values that describes how closely the artifact follows its source:
    direct-adaptation   — minimal deviation; structure and terminology closely follow the source.
    guided-synthesis    — synthesized from one primary source with meaningful additions or reorganization.
    hybrid-synthesis    — actively reconciled from two or more sources; no single source is dominant.
    native-platform-binding — follows the platform-native spec exactly (e.g., GitHub Actions, JSON Schema).
- {{REVIEWED_ON_DATE}}: ISO date of the most recent review (YYYY-MM-DD).
  Update this field each time the artifact is reviewed, even if no content changes.

Do not omit or rename the ## Source Attribution heading. The validator requires its exact presence.
-->

## Source Attribution

- Source manifests: `{{SOURCE_MANIFEST_1}}`, `{{SOURCE_MANIFEST_2}}`
- Primary source basis: {{PRIMARY_SOURCE_BASIS}}
- Alignment mode: {{ALIGNMENT_MODE}}
- Reviewed on: {{REVIEWED_ON_DATE}}
