---
name: paper-positioning
description: "研究定位、选题收敛、创新点与贡献边界、竞争解释、最小判别实验；position a paper, narrow a research question, assess a contribution, or design evidence that can distinguish a hypothesis from alternatives. Use for substantive research positioning and experiment design, including rough ideas. Do not trigger for language-only polishing, a numerical audit alone, a request only to learn writing style, or a full reviewer report without a positioning task."
---

# Paper Positioning

Turn a research interest, observation, or draft claim into a specific question,
a defensible contribution boundary, and a feasible way to test it.
Make progress with the available material; do not require a polished outline.

## Establish the task and available context

1. Identify the requested deliverable: candidate directions, contribution analysis,
   a hypothesis, a comparison with prior work, or an experiment plan.
2. Recover the actual research objective and any decisions already accepted.
   Continue the current project rather than restarting topic discovery.
3. Locate the project root from the task or workspace when using project files.
4. Read the root ACADEMIC_WRITING.md if it exists.
   Apply its evidence and manuscript-boundary rules to any proposed paper wording.
5. In project mode, inspect research/PROJECT.json, research/claims.tsv,
   and research/issues.tsv only if they exist and matter to this task.
   Read the actual configuration and headers; preserve unrelated entries.
6. Use file paths, language choices, and required checks actually supplied.
   Do not assume undocumented configuration fields.
7. In chat-only work, use a concise explanation or table.
   Do not create configuration files or ledgers merely to use this skill.

Read [claim-experiment-cards.md](references/claim-experiment-cards.md)
when building a contribution card, choosing controls, or preparing a pilot.

## Establish what is known

Separate observations, author-supplied claims, implementation facts,
measured results, derived quantities, explanations, and future plans.
Preserve the scope in which each statement is supported.

- Treat a supplied draft as the author's account, not independent corroboration.
- Do not invent a failure trace, dataset, baseline, citation, result, or deployment.
- Label a thought experiment or synthetic example as such.
- Keep the observed phenomenon distinct from the proposed reason for it.
- Use an explicit unknown when evidence is unavailable.
- Do not turn plausible reasoning into a promised positive result.

If a material ambiguity changes the proposed question, explain that ambiguity
and complete the work that does not depend on it.
Ask only for information needed to choose between materially different paths.

## Find a research-sized question

Start with a concrete failure, tension, or unexplained result.

1. Specify the task, environment, available information, and relevant constraints.
2. Identify the current method and the exact behavior that fails.
3. Identify who or what is affected and why the failure matters.
4. Separate a reproducible observation from an anecdote or assumed problem.
5. Isolate an intervention small enough to explain and evaluate.
6. State what would count as an informative answer, including a negative answer.

When exploring directions, produce a small, task-proportional shortlist.
Do not fill a quota with weak variants of the same idea.
Prefer questions with available evidence, accessible implementations,
and a decisive small test over impressive names for large systems.

Do not assume that every engineering feature is a new research contribution.
A contribution may concern a mechanism, evaluation method, measured boundary,
or an informative system result; explain the specific knowledge it would add.

## Check the claimed distinction

Identify the closest actual work or existing baseline, rather than comparing
only with a vague category such as conventional agents.

- Inspect primary sources when making literature or novelty claims.
- Distinguish material read in full from abstracts or search snippets.
- Record the source and the precise problem, mechanism, and evaluation compared.
- Keep citation support separate from a paper's promotional framing.
- Do not infer that a method does not exist because a search did not find it.
- Report the searched scope and unresolved novelty questions outside the manuscript.
- Continue design work when source access is unavailable, without certifying novelty.

Bound the search to the contribution under consideration.
Expand it only when a concrete nearby result could change the decision.
If a close method already answers the question, explain the overlap and propose
a genuine remaining distinction or recommend abandoning that candidate.
Do not rename the same method and call the renamed version novel.

## Build a claim and its competing explanations

State the proposed claim with its task, intervention, comparator, outcome,
conditions, and current evidence status.
Use an ordinary sentence before introducing a project acronym.

Ask what else could produce the same observation.
Select alternatives that the actual intervention might have changed, such as:

- More model calls, tokens, retries, time, or external information.
- A stronger model, better prompt, or different stopping policy.
- Different task difficulty, filtering, or benchmark construction.
- A scorer that rewards the proposed format or sees method identity.
- Oracle information or answer leakage unavailable during intended use.

Connect each material alternative to a control or a narrower claim.
Do not list generic threats that have no identifiable connection to this method.

## Design the smallest discriminating check

Define the prediction before describing a large experimental suite.

1. Specify the primary question and observable endpoint.
2. State the intervention and a meaningful comparison.
3. Identify the independent evaluation unit and the available task source.
4. Define success, failure, timeout, exclusion, and missing-result handling.
5. Match the relevant budget or report the quality-cost trade-off explicitly.
6. Include the smallest control that distinguishes the key competing explanation.
7. Specify required logs, labels, configuration, and scorer behavior.
8. State what outcome would support, weaken, or contradict the hypothesis.
9. Separate exploratory tuning from the later evaluation used for the claim.

Choose task counts, repetitions, and analysis methods for the concrete uncertainty.
Do not impose a universal seed count, significance test, or model count.
Do not tune the benchmark or primary metric after seeing results merely to win.

A static implementation inspection, existing-log rescore, or toy counterexample
may settle a preliminary question before a costly new run.
Describe which uncertainty that check can and cannot resolve.
A plan to run an experiment does not authorize or record its execution.

## Decide and hand off

Classify the candidate using evidence: ready for a small test,
needs a specific prerequisite, overlaps existing work, or should be dropped.
These are working judgments, not promises about publication.

Give the user a concrete next action and its decision criterion.
If the main uncertainty is empirical, name the smallest test that addresses it.
If the idea fails logically under its assumptions, explain the contradiction.
Do not keep broadening a weak direction indefinitely.

For project records, follow the existing headers:
claim_id, location, claim, evidence_status, evidence, boundary, disposition.
Use proposed, planned, implemented, measured, derived, or verified accurately.
Use active, narrowed, or withdrawn for disposition.
A verified entry must name the executed check and its limited scope.
Do not change an accepted central research objective without authorization.

## Deliver

Return the requested analysis or experiment plan, usually in Chinese.
Include proposed English claim wording only when useful to the requested task.
Keep search notes, weaknesses, and decisions outside any manuscript passage.
Preserve essential qualifications inside the claim where interpretation needs them.

Make the result concrete: question, evidence, distinction, competing explanation,
minimal test, and the decision that test enables.
Cite sources for literature-dependent assertions.
Do not claim guaranteed feasibility, novelty, SCI acceptance, or experimental success.
