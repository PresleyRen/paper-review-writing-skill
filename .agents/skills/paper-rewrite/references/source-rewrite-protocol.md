# Source-based rewriting protocol

## Diagnose an overlap before editing

| Match type | Suitable response |
| --- | --- |
| Bibliography or correctly marked quotation | Check reporting settings and attribution; retain necessary quoted wording. |
| Conventional technical expression | Keep accurate terminology; do not distort it for novelty. |
| Distinctive unquoted source wording | Quote and cite when exact wording matters, otherwise rewrite from the proposition and retain attribution. |
| A paragraph following a source sentence by sentence | Reorganize around the current paper's question and synthesize only supported relationships. |
| A match against the author's previous publication | Check the destination's reuse and disclosure requirements; citation may still be needed. |
| No source text or report available | Revise meaning and structure only; mark source comparison as unperformed when reporting checks. |

## A compact source record

Source and location:
Actual finding:
Setting and comparator:
Uncertainty or boundary:
What this manuscript needs from it:
Citation to retain:

Do not fill missing source details by inference from a title.

## Alternatives using fictional supplied facts

Supplied facts: 100 simulated refund tasks, one run, baseline 62 completions, state-checking agent 74 completions, the same six-tool-call budget including checks.

Result first:

> The state-checking agent completed 74 of 100 simulated refund tasks, compared with 62 for the baseline in a single run. Both used a six-call tool budget that included checking.

Method first:

> We evaluated both agents on 100 simulated refund tasks with a six-call tool budget, including checking. In this single run, the baseline completed 62 tasks and the state-checking agent completed 74.

Evaluation object first:

> The 100 simulated refund tasks were evaluated in a single run under the same six-call tool budget, with checking included. The baseline completed 62 tasks; the state-checking agent completed 74.

These versions change information order while preserving evidence. None establishes significance, stability or a causal mechanism. Use whichever fits the surrounding paragraph.

## Detection claims: consult current primary documentation

- Turnitin AI report: https://guides.turnitin.com/hc/en-us/articles/22774058814093-Using-the-AI-Writing-Report
- Turnitin similarity score: https://guides.turnitin.com/hc/en-us/articles/23435833938701-Understanding-the-similarity-score
- Liang et al. (2023), limited historical detector study: https://arxiv.org/abs/2304.02819
- Kirchenbauer et al. (ICML 2023), a statistical watermark design: https://proceedings.mlr.press/v202/kirchenbauer23a.html
- OpenAI provenance announcement, 2026-10-05: https://openai.com/index/eu-text-provenance/

Product support and provenance rollouts can change. Check the current product and settings when answering a provenance question. These references do not justify promising any detection outcome.

## Work from an actual report

If the task supplies a similarity or AI-writing report, identify its product, date, analyzed text, language, relevant settings and flagged locations before editing.

For each flagged passage, identify a writing issue that can actually be assessed: source-dependent phrasing, repetitive paragraph structure, empty claims, inconsistent author voice, unnecessary restatement or an unsupported generalization. A flag alone does not establish that one of these defects exists.

Revise the passage for that stated purpose and compare its meaning and attribution with the input. Preserve a good passage when no useful change is warranted.

If the task includes authorized access to the same reporting tool, compare the original and revised text under the same known settings and record the actual reported result. Otherwise record the follow-up measurement as not performed.

For an ongoing report-based task, a compact record may contain:

    report_type | tool/version/date | text_hash | language/settings | reported_value | changed_passages | meaning_check | follow_up_result

Keep raw indicator values distinct from authorship judgments. Do not label an unmeasured result as zero, infer a passing score from smoother prose, or change a research fact to improve an indicator. Stop once the requested faithful revision is complete; do not run an unlimited rewrite loop chasing a score.
