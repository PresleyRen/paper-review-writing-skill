# Natural Academic Writing Rules for Codex

Version: 2026-10-19, revision 2
Scope: Rough research notes, spoken drafts, manuscripts, abstracts, introductions, methods, results, discussions, conclusions, and their revision.
Language: Discuss research and editorial decisions in Chinese. Write manuscript prose in English unless the user requests another language.

## 1. Purpose and activation

Make the paper readable and faithful to both the author's meaning and the evidence. Accept disordered notes, spoken-language transcripts, mixed-language fragments, and incomplete drafts. Preserve the author's observations, emphasis, useful qualifications, and natural phrasing. Organize them for the requested text and its readers. A research audit, experiment plan, reviewer response, notebook, and manuscript are different deliverables; infer the requested deliverable from the task.

Initial setup only: place this file beside the project-root AGENTS.md (create that AGENTS.md if needed) and add this instruction:

> For manuscript drafting or revision, read the ACADEMIC_WRITING.md located beside this AGENTS.md and apply its rules to manuscript content.

A standalone file named ACADEMIC_WRITING.md is not automatically an AGENTS.md instruction source. Reconcile overlapping writing rules during setup and preserve unrelated project instructions. Ordinary manuscript tasks do not call for configuration changes.

## 2. Protect the manuscript boundary

A manuscript sentence should contribute research content or necessary reader guidance: a problem, definition, method, rationale, comparison, observation, argument, evidence, interpretation, scope condition, or meaningful transition.

Keep these outside the manuscript:

- Instructions to the assistant, responses to the user, progress updates, and descriptions of this editing session.
- Self-evaluations such as "to avoid overclaiming," "to make our contribution sound stronger," or "we carefully word this claim."
- Hypothetical reviewer dialogue, compliance checklists, TODOs, unresolved citation markers, and edit explanations.

An explanation of an actual research decision belongs in the paper when it helps readers assess the method. For example, a rationale for matching a computational budget is research content. A rationale for making the manuscript sound persuasive is editorial content.

Follow the destination journal's applicable reporting and disclosure requirements in their required locations.

## 3. Preserve scientific meaning during editing

For every substantive claim, retain its subject, outcome, comparator, direction, magnitude, population, conditions, uncertainty, and evidence status when applicable. A style edit must not silently change any of these.

Do not add a dataset, experiment, mechanism, reference, result, deployment fact, or advantage that is absent from the supplied evidence. Illustrative examples and placeholders are not evidence.

Distinguish:

- What a method is designed to do.
- What an implementation actually does.
- What an experiment observed.
- A proposed explanation for that observation.
- A demonstrated causal mechanism or theoretical result.
- A prediction for a setting that has not been evaluated.

Use clear wording calibrated to the evidence and the author's intended emphasis. Do not intensify a claim merely to sound authoritative. Never promote a design intention into a measured improvement, an association into causation, or a limited evaluation into universal effectiveness.

## 4. Repair problems at the claim level

When a sentence feels difficult to defend, identify the actual issue and edit that issue.

| Issue | Required action |
| --- | --- |
| The claim exceeds the evaluated setting | Name the setting and narrow the claim. |
| A result is known, but its mechanism is untested | Report the result; identify the explanation as a hypothesis if it is useful. |
| A central claim lacks evidence | Remove or suspend the unsupported claim and record the concrete evidence gap outside the manuscript. |
| A comparison is vague | Identify the actual comparator, conditions, and metric from available evidence. |
| A limitation is repeated | Keep it where needed for interpretation and consolidate redundant discussion. |
| A concern is only speculative | Investigate it when material; do not convert it automatically into an established limitation. |

Do not repair an unsupported statement merely by adding "may," "potentially," "to some extent," or a generic disclaimer. When the task is hypothesis development, explicitly frame a hypothesis and its rationale without inventing a result.

## 5. Preserve author voice and natural information flow

Let a paragraph develop from the detail the author considers important: a concrete observation, an unexpected result, a question, a design choice, or an argument. Make the links intelligible. Do not impose a universal background–problem–method–result structure, a fixed number of background sentences, or a conclusion at every paragraph opening and ending. Follow a venue's required abstract format when applicable.

Use the author's supplied or explicitly approved writing as the main style reference. Match the genre and audience. From a suitable reference, learn useful choices in emphasis, first person, sentence rhythm, clause structure, and transitions. From separate style references, learn these patterns without importing their findings, experiences, citations, or source-specific phrasing. This does not prevent retaining useful wording from the author's current notes or draft. When no suitable English sample exists, follow the current preferences without claiming an exact match to the author's published voice.

Preserve readable idiosyncrasies and meaningful self-corrections. Rough notes can retain fragments and conversational pivots; manuscript prose needs clear reference and grammatical relationships. Keep a genuine discovery sequence when it explains the research decision. Do not invent an experience, surprise, failed attempt, or insight to create an impression of human authorship.

Use familiar, precise words. Concrete subjects, accurate verbs, and named conditions usually carry more information than ornamental academic vocabulary. Preserve technical terms consistently: state, memory, and context are not interchangeable; neither are accuracy, reliability, and robustness.

Allow long and short sentences, active and passive constructions, subordinate clauses, and first person when they serve meaning and fit the venue. Choose voice according to what the sentence is about. Do not require an artificial mixture, syntactic quotas, deliberately awkward inversions, grammar errors, or random reordering. Keep necessary links between conditions, reasons, and outcomes.

Remove repetitive apologies, unsupported promotional adjectives, and empty introductory phrases. Treat may, suggests, although, only, and not as review signals rather than banned tokens. Keep a contrast that clarifies a real distinction. Do not rewrite every clear, ordinary sentence merely because it is predictable.

If alternative versions would help, offer genuinely different emphases or information orders, explain the difference only when requested, and select for meaning and readability. Syntactic change does not remove attribution obligations. Assess a revision by fidelity, precision, and readability; do not promise a detector score or watermark outcome.

## 6. Place qualifications where they are needed

A qualification belongs next to a claim when removing it would change how a reader understands that claim. This includes claims in the abstract and conclusion.

Discuss broader limitations in Methods, Discussion, or Limitations as appropriate. Avoid repeating the same caveat within a passage, while retaining the scope needed when a section must stand on its own.

A negative statement can be necessary: "The experiment does not distinguish these explanations" carries information. "We must humbly acknowledge that our work is not perfect" usually does not.

Retain relevant unfavorable findings and trade-offs. Do not change a comparator, evaluation criterion, or reported result solely to make the prose sound successful. Report what changed, under which conditions, and what remains unknown.

## 7. Separate verification from prose revision

Use proportionate passes; a paragraph edit does not require a full-paper investigation.

For rough notes, distinguish observations, implemented actions, planned actions, interpretations, and unresolved questions before drafting. Keep this working classification outside the manuscript; show it only when requested or needed to resolve a material ambiguity. When turning a notes file into a manuscript, retain the original notes unless an in-place rewrite was requested. Do not demand a polished outline before helping.

For a language-only edit, preserve author-supplied facts as supplied claims without certifying them as independently verified. Check for contradictions and unsupported changes using available material. Do not expand a routine edit into a fresh evidentiary audit unless a concrete, material problem affects the requested revision.

1. Evidence pass: For a requested research audit, check material claims against their underlying evidence. For a language-only edit, check consistency and preservation of meaning. Distinguish supplied claims from independently verified findings.
2. Argument pass: Resolve the material issues and organize the content around the research question. Turn an accepted review finding into a concrete manuscript revision.
3. Language pass: Remove editorial contamination and unnecessary verbal padding while preserving the factual meaning established above.

A reviewer or checking agent should return a concise issue record: location, problem, significance, evidence status, and proposed action. Prioritize problems that affect interpretation or the main conclusion. Do not invent objections to meet a numerical quota, treat harshness as evidence, or report speculative concerns as demonstrated defects.

For a requested final factual audit, extract the numbers, units, denominators, signs, uncertainty intervals, statistical notation, result labels, and citations that need checking. Compare them with the supplied records and with all corresponding manuscript, table, figure, caption, and abstract occurrences. Preserve each result's model, dataset, baseline, evaluation condition, and aggregation method. Distinguish percentage-point changes from relative percentage changes. Check that a cited source supports the associated claim, not just that its number exists.

Keep the audit outside the manuscript, using a compact record such as: location | reported item and condition | source | match, mismatch, or unverifiable | action. Source verification requires the source. With no underlying record, report only the internal consistency actually checked. Resolve mismatches from evidence rather than guessing. Finding a preset number of errors is not an audit goal. After revising an affected sentence, recheck its material numbers and attribution; do not restart an unrelated full audit.

After a material issue is resolved, do not reintroduce it as a generic caveat. Reopen it only when new evidence or an unresolved inconsistency warrants doing so.

## 8. Delivery contract

When the requested passage can be completed faithfully and the user asks for manuscript text only, return it without an introduction, editing explanation, or concluding reminder. If a material evidence gap prevents completion, deliver the supported text and a clearly separate, minimal blocker note. Ordinary scientific uncertainty is not by itself a blocker.

When editing files, keep manuscript text in the manuscript file. Put material unresolved issues in an existing review-notes file or a clearly separate editorial report. Do not create a report for a routine edit with no material issues.

Complete all supported work. If missing evidence prevents a faithful completion of a requested claim, identify the specific blocker outside the manuscript instead of inventing evidence or calling the incomplete section final.

Preserve citations and technical notation. If a reference or claim cannot be checked, do not label it verified. Resolve citation and evidence placeholders before marking a manuscript ready for submission: supply the required support, or revise or remove the dependent claim. Deleting a marker alone does not resolve an evidence gap. A remaining material gap prevents a submission-ready status but does not block other supported edits.

## 9. Acceptance check

Before delivering, verify:

- The reader can identify the paragraph's purpose.
- The revision preserves the author's intended emphasis and useful phrasing without forcing a uniform rhythm or structure.
- Editing has preserved material numbers, comparators, conditions, negations, and uncertainty.
- Technical terms remain stable even when ordinary wording varies.
- Reported evidence and proposed explanations are distinguishable.
- Essential boundaries are available where a claim is read.
- The prose contains no assistant conversation or commentary about this revision.
- Material missing evidence is accounted for outside the manuscript.
- The revision improves clarity without adding unsupported confidence.

## 10. Task prompt: work from rough notes or revise a passage

Read ACADEMIC_WRITING.md. Draft or revise the requested passage from the supplied notes or text in natural academic English. Preserve my observations, intended emphasis, useful phrasing, and scientific meaning. Use the supplied or explicitly approved style samples when available. Let the material determine the information order; do not force every paragraph into the same template or replace plain technical English with inflated vocabulary.

Distinguish what I observed, what I implemented, what I plan to test, and what I am only proposing as an explanation. Preserve numbers, comparisons, technical terms, citations, and necessary qualifications. Remove commentary about how this text is being edited. Keep the work within the requested scope; perform a source or numerical audit when that audit is requested or a material inconsistency requires it.

When the task is a manuscript-only revision and the passage can be completed faithfully, return only the manuscript. If a material gap prevents completion, keep its minimal note separate and complete the supported parts. When I request a writing exercise, show the rough input, an appropriate revision, and the few decisions that matter.

## 11. Exercises and calibration cases

For requested examples and exercises, accept realistic, untidy starting material. Show what changes between a notebook explanation and the target genre. Include different paragraph purposes over time rather than repeating one formula. Label invented experimental settings and numbers as illustrative. Examples never supply evidence about the user's research.

### A. Spoken notes to a manuscript paragraph

The following notes, experiment, and counts are invented solely to demonstrate revision.

Raw notes:

> 先说结果吧，100 个模拟退款任务，同一个模型，两边最多 6 次工具调用，核对用掉的调用也算在里面。原来的 Agent 完成了 62 个，加了状态核对的是 74 个。这个只有一轮，别写稳定提升。我们是翻日志的时候发现，有些地方工具都返回新状态了，Agent 还按旧状态往下做，所以后来就只核对这次动作影响的字段。全量核对还没试。

One suitable manuscript version:

> The agent with state checking completed 74 of the 100 simulated refund tasks; the original agent completed 62. These counts come from a single run. Both agents used the same model and were allowed six tool calls per task, with calls for state checking included in that budget. We introduced the check after inspecting traces in which the agent kept using an outdated state despite receiving an update from a tool. The check covers the fields affected by the latest action.

The paragraph retains the author's decision to lead with the result and explains how trace inspection motivated the design. It neither invents a broad introduction nor claims statistical significance, stability, or a demonstrated causal explanation. Full-state checking is still untested; retain that item in the research notes and state it in the manuscript if a comparison or claim makes it material. The completion-rate difference is 12 percentage points, not a 12% relative improvement.

### B. Keep an intended experiment in the future

Raw note:

> 我想下一步只检查变化的字段，可能便宜一点，还没做。

Research-plan version:

> We plan to test whether checking only the affected fields reduces verification cost.

This belongs in a plan or relevant future-work passage. It does not support a results sentence claiming a cost reduction.

### C. Keep the evidence level when removing editorial framing

With only a design specification, write: "The controller is designed to inspect API state before choosing a recovery action." With implemented and confirmed behavior, write: "The controller inspects API state before choosing a recovery action." Neither sentence establishes a measured performance improvement.

## Reference context

Prepared as an operational writing module for the user's research workflow. Sources consulted:

- Codex instruction-file loading: https://learn.chatgpt.com/docs/agent-configuration/agents-md
- Paul Goldsmith-Pinkham, Writing & Thinking with AI Assistance: https://paulgp.substack.com/p/writing-and-thinking-with-ai-assistance
- Kiterlin, anti-defensive-writing: https://github.com/Kiterlin/anti-defensive-writing
- Adkid-Zephyr, anti-defensive-writing-Skill: https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill
- Gopen and Swan, The Science of Scientific Writing (1990), authorized reproduction: https://www.cs.tufts.edu/comp/150FP/archive/george-gopen/sci.html
- User-supplied workflow screenshots reviewed on 2026-10-19: IMG_2847.PNG (rough notes), IMG_2848.PNG (review), IMG_2849.PNG (alternative structures), IMG_2850.PNG (factual consistency). Their fixed quotas and outcome promises are not adopted.

Sources for questions about detection and provenance; these are background references, not instructions to add detector commentary to a manuscript:

- Turnitin, Using the AI Writing Report: https://guides.turnitin.com/hc/en-us/articles/22774058814093-Using-the-AI-Writing-Report
- Turnitin, Understanding the similarity score: https://guides.turnitin.com/hc/en-us/articles/23435833938701-Understanding-the-similarity-score
- Liang et al., GPT detectors are biased against non-native English writers (2023): https://arxiv.org/html/2304.02819v3
- Kirchenbauer et al., A Watermark for Large Language Models (ICML 2023): https://proceedings.mlr.press/v202/kirchenbauer23a.html
- OpenAI, Our approach to EU text provenance rules (2026-10-05): https://openai.com/index/eu-text-provenance/


