# Evidence audit protocol

## Contents

1. Scope and evidence levels
2. Claim tracing
3. Numbers and statistics
4. Tables and figures
5. Citations
6. LLM and Agent attribution
7. Findings and closure

## 1. Scope and evidence levels

Record the manuscript revision and the requested audit scope.
For a local contradiction, inspect the affected claim and its dependencies.
For pre-submission review, inspect the claims used in the abstract, results,
conclusion, contribution statements, and supporting tables or figures.

Inventory available sources before drawing conclusions:

| Material actually read | What it can establish |
| --- | --- |
| Manuscript and its tables | Internal agreement or contradiction |
| Raw outputs with traceable configuration | What the recorded run produced |
| Analysis code plus inputs, actually recomputed | Whether the reported calculation follows |
| Cited original paper, with relevant passages | Whether that source supports the attributed claim |
| Abstract, search snippet, or second-hand summary | A lead requiring further reading |

Treat repeated summaries of one run as one evidence source.
State the inspected files and any inaccessible inputs.
Do not describe an unexecuted calculation as reproduced.

## 2. Claim tracing

For each material claim, record:

- Exact location and current wording.
- Population or task; proposed change; comparator.
- Conditions: data split, budget, tools, access, and evaluation setup.
- Evidence identifier, source path or URL, and precise source location.
- Evidence status: distinguish a proposal, plan, implementation, measurement,
  derivation, and a completed check with an explicitly stated scope.
- What the evidence supports and what remains unresolved.

Keep three different status fields separate:

| Record | Field and permitted meaning |
| --- | --- |
| Extracted candidate TSV | `status` stays `unverified`; extraction is only an index. |
| Audit findings report | Use `supported`, `internal_consistency_only`, `contradicted`, `missing_source`, or `needs_interpretation`, as defined in section 7. |
| Project `research/claims.tsv` | Use the project's `evidence_status` schema: `proposed`, `planned`, `implemented`, `measured`, `derived`, or `verified`. |

For this starter, use the definitions in `RESEARCH_HARNESS.md` when writing the
project ledger. A simulated run is a setting, not an additional evidence-status
value: a recorded simulated result can be `measured`, with simulation and run
count stated in `boundary`. A causal hypothesis not tested by the supplied
measurements remains a separate `proposed` claim. Do not automatically label
it `derived` merely because an author calls it an inference. Use `derived` for
a stated derivation from identified inputs; use `verified` only with the actual
check and its scope. An audit finding of `supported` does not automatically
promote every associated claim to `verified`.

Trace a quantitative claim to the run, then to the calculation, then to the
table or figure, then to the sentence. Stop at the first missing link and
report that link; do not silently fill it with a plausible assumption.

## 3. Numbers and statistics

Check sign, decimal point, scientific exponent, unit, denominator, and rounding.
Distinguish percentages, percentage points, ratios, counts, and normalized scores.
For rates, identify both the numerator and eligible denominator.
Check whether the same tasks failed, were retried, or were excluded across methods.
Distinguish task-level, run-level, and sample-level averages.
Keep micro, macro, weighted, and per-category averages separate.

Constructed arithmetic example, not a result for this project:

    Baseline success: 60 / 100 = 60%.
    Proposed success: 75 / 100 = 75%.
    Absolute change: 75% - 60% = 15 percentage points.
    Relative change: (75 - 60) / 60 = 25%.

With different denominators, recompute each rate before comparing rates.
With a zero baseline, report the absolute difference; relative change is undefined.
Check whether lower or higher is better for the named metric.
Do not interchange milliseconds and seconds, tokens and calls, or cost and latency.
Read confidence levels, interval endpoints, error-bar definitions, and aggregation.
Distinguish standard deviation, standard error, and confidence intervals.
Check paired versus unpaired comparisons and independent versus repeated samples.
Do not infer a statistical test from the presence of a p-value.
Keep exploratory and confirmatory analyses identifiable when that affects a claim.
Preserve unfavorable results that bear on the principal conclusion.

The extractor does not perform these checks. In particular, it does not parse
arbitrary LaTeX expressions, reconstruct CSV cell semantics, or validate JSON.
Review candidates against the original file and source records.

## 4. Tables and figures

Match every discussed table row or figure panel to its source data.
Check titles, row and column headings, units, legends, split names, and captions.
Check axis limits, logarithmic scales, omitted categories, and error-bar labels.
Recompute displayed aggregates when the underlying records and script are available.
Check that a figure and table do not present different filters as the same cohort.
Verify statement direction: an arrow, ranking, or highlighted best value must
agree with the metric definition and the underlying entries.
Record figure regions inspected; text extraction alone cannot verify the plot.

## 5. Citations

Resolve a citation key to its bibliography record and then to the actual source.
Verify authors, title, year, version, venue, DOI or stable URL where available.
Read the passage, theorem, method, or result being attributed.
Check whether the reference supports the exact scope of the sentence.
Separate a source's proposal, empirical finding, opinion, and survey summary.
Use the relevant version; note material differences between versions.
An existing citation key, valid URL, or matching title establishes identification,
not evidential support. Mark unavailable full text rather than inventing support.
Do not replace a relevant source merely to make a reference list look newer.

## 6. LLM and Agent attribution

Record the model and version, prompts, decoding settings, and available context.
For retrieval, record the corpus snapshot, index, retrieval depth, and reranking.
For tools, record schemas, access, failures, retries, and recovery policy.
For agents, record orchestration, number of agents, stopping rules, and budgets.
For evaluation, record tasks, splits, seeds, repetitions, metrics, and judge setup.
Include tool calls, retries, or judge calls in cost if the metric claims total cost.
Check comparators received equivalent information and stated resource constraints.
Attribute results to the evaluated system configuration, not automatically to
its LLM, ontology, planner, retriever, or number of agents in isolation.
Describe a component-level explanation as a hypothesis unless evidence isolates it.
Keep simulated API failures distinct from observations of live service outages.
Keep successful recovery examples distinct from measured recovery rates.
Check whether evaluation data or answers entered prompts, retrieval, or tuning.

## 7. Findings and closure

Use one finding per concrete problem with source locations and an actionable remedy.

| Status | Meaning |
| --- | --- |
| supported | The stated claim was checked against the specified evidence |
| internal_consistency_only | Supplied representations agree; original records were not checked |
| contradicted | Identified evidence conflicts with the claim |
| missing_source | The necessary source could not be inspected |
| needs_interpretation | Evidence is available, but the inferential step needs resolution |

Do not use supported for scientific correctness beyond the inspection performed.
Keep extraction status unverified; put audit decisions in a separate findings report.
For a requested edit, correct a demonstrable arithmetic or transcription error
only after resolving the source of truth. Retain the evidence record unchanged.
For unavailable evidence, finish the other checks and name the smallest missing input.
Use unresolved issues to guide the next action; do not insert generic caution
paragraphs into the manuscript. Record known limitations where readers need them.
End when the requested scope is checked and remaining gaps are explicit.
