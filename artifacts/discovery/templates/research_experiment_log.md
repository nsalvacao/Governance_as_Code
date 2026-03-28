---
title: Research / Experiment Log Template
artifact_type: template
status: draft
visibility: public
classification: public
owner: governance@org
review_cadence: quarterly
applies_to: research, experimentation, and learning loops
source_basis: Lean Startup Build-Measure-Learn + Google SRE experimentation practices
source_manifests:
  - method__scrum_guide.md
  - operations__google_sre.md
alignment_mode: guided-synthesis
updated: 2026-03-27
---

## Research / Experiment Log — `{{EXPERIMENT_NAME}}`

Each experiment follows the Build-Measure-Learn loop from Lean Startup methodology, combined with Google SRE rigour around measurement conditions, sample integrity, and decision traceability. Log one experiment per entry. Do not aggregate multiple experiments into a single record — each hypothesis deserves its own cycle.

---

### Experiment Identification

| Field | Value |
|---|---|
| Experiment ID | `{{EXPERIMENT_ID}}` |
| Date | `{{DATE}}` |
| Owner | `{{EXPERIMENT_OWNER}}` |

**Hypothesis:**

> `{{HYPOTHESIS}}`

State the hypothesis in falsifiable form: "We believe that [doing X] for [user segment] will result in [measurable outcome], because [rationale]." A hypothesis that cannot be falsified is an assumption — move it to the Assumptions Register instead.

---

### Build

**What was built / tested:**

`{{ARTIFACT_BUILT}}`

Describe the prototype, mock, test, script, or feature slice used to run the experiment. Include what was deliberately simplified or excluded.

**Test conditions:**

`{{TEST_CONDITIONS}}`

Describe the environment, population, time window, and any controls applied. Note anything that could introduce bias or confound the results.

---

### Measure

| Metric | Method | Sample size |
|---|---|---|
| `{{METRIC_1}}` | `{{METHOD_1}}` | `{{SAMPLE_SIZE_1}}` |
| `{{METRIC_2}}` | `{{METHOD_2}}` | `{{SAMPLE_SIZE_2}}` |

Metrics must be defined before the experiment runs, not after. Post-hoc metric selection invalidates the experiment.

---

### Learn

**Results summary:**

`{{RESULTS_SUMMARY}}`

State what was observed, factually. Separate observation from interpretation.

| Field | Value |
|---|---|
| Hypothesis supported | `{{HYPOTHESIS_SUPPORTED}}` (yes / no / partial) |
| Confidence level | `{{CONFIDENCE}}` (High / Medium / Low) |

---

### Decide

**Decision:**

`{{DECISION}}` — persevere / pivot / stop

**Rationale:**

`{{RATIONALE}}`

Every experiment must end in a decision. "We need more data" is not a decision — it is a new hypothesis that requires a new experiment entry. Decisions that do not change the backlog are wasted learning.

---

### Links

| Field | Value |
|---|---|
| Backlog items affected | `{{BACKLOG_ITEM}}` |
| Related experiments | `{{RELATED_EXPERIMENT}}` |
| Assumptions invalidated | `{{ASSUMPTION_REF}}` |

## Source Attribution

- Source manifests: `method__scrum_guide.md`, `operations__google_sre.md`
- Primary source basis: Lean Startup Build-Measure-Learn (Ries, 2011) + Google SRE operational experimentation practices
- Alignment mode: guided-synthesis
- Reviewed on: 2026-03-27
