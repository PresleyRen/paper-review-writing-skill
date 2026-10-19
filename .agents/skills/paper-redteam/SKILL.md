---
name: paper-redteam
description: "毒舌/毒蛇式审稿、拒稿理由、逻辑漏洞、实验与实现疑点、论证盲区；give a targeted adversarial paper review grounded in exact claims, artifacts, and evidence. Use for critical review, reviewer-style assessment, or substantive checks of a revision. Distinguish confirmed defects from suspicions and missing evidence. Do not trigger for ordinary polishing, style extraction, a numerical audit alone, or drafting a response to known comments without a new review."
---

# Targeted Paper Red Team

Give a demanding, specific assessment of what the supplied paper establishes.
Make criticism useful through evidence, consequences, and a decisive repair.
Do not equate an aggressive tone with a strong review.

## Fix the review boundary

1. Identify the requested scope: one claim, a section, a full paper,
   an implementation concern, or a check of a particular revision.
2. Identify any supplied venue criteria and the paper's actual contribution.
3. Inspect the relevant manuscript and available supporting artifacts.
   A review request alone does not authorize rewriting them or running experiments.
4. Read the project-root ACADEMIC_WRITING.md if it exists.
5. In project mode, read relevant existing research/PROJECT.json,
   research/claims.tsv, and research/issues.tsv.
   Inspect actual fields and preserve existing identifiers and decisions.
6. Do not require project files or ledgers for a chat-only review.
7. Use the requested language; Chinese is suitable for editorial analysis
   when no different preference is established.

Read [agent-review-lenses.md](references/agent-review-lenses.md)
for LLM/Agent-specific implementation and experimental questions.
Select the relevant lenses; do not run every question against every paper.

## Establish the claim chain

Locate the main research question and the claims that support the contribution.
For each material claim, identify the supplied definition, method, experiment,
result, interpretation, and conclusion that depend on it.

Use short exact quotations, section names, table cells, code locations,
run identifiers, or other recoverable anchors.
Do not invent locations or imply access to an artifact that was not inspected.
Keep a supplied claim distinct from a fact independently checked.

Trace only the implementation path relevant to the claim under review:
input, available information, decision, tool action, state update,
termination, recorded outcome, and scoring.
Compare that path with the paper's description when code or traces are available.

A missing repository does not prove that the implementation is incorrect.
An absent control can establish a gap in the current argument without proving
that the proposed method itself fails.

## Test the argument

Ask the questions that could change the reader's interpretation:

- Does the evidence answer the paper's actual question?
- Do definitions and metrics measure the claimed property?
- Does the comparison isolate the proposed mechanism?
- Could extra information, compute, retries, or selection explain the result?
- Are plans, implementation behavior, and observed outcomes distinguished?
- Does a conclusion extend beyond the evaluated setting?
- Does the nearest cited work actually support the claimed distinction?
- Does an important assumption fail in the task the paper says it addresses?

Investigate a material uncertainty using available sources and artifacts.
Use primary literature for claims about prior work.
Keep an unresolved lookup unresolved rather than asserting a novelty defect.
Do not replace targeted investigation with an unbounded general literature search.

## Investigate implementation and experimental doubts

Choose doubts connected to the specific architecture or evaluation.

1. Check task success against the intended external state or objective criterion.
2. Inspect how failure, timeout, partial completion, and invalid output are scored.
3. Compare actual information and budgets across conditions.
4. Check whether a verifier or judge uses privileged labels or method identity.
5. Inspect whether a claimed ablation changes the executed path.
6. Check whether trials, templates, tasks, and repetitions are being conflated.
7. Compare method descriptions with available configuration, code, and logs.

Do not assert every risk in this list is present.
For a suspected issue, name the observation that motivates it
and the smallest check that would distinguish it from a correct implementation.
A static read or existing-log rescore may be sufficient.
Do not demand a costly new benchmark when a smaller check resolves the question.

## Write evidence-grounded findings

Use one record per distinct problem.
Merge symptoms that share the same cause and repair.

Include:
- A stable issue identifier when project records already supply one.
- The exact affected location and claim.
- The inspected evidence or the particular missing evidence.
- The reason this matters for the claim or review judgment.
- The finding type, severity, and any remaining uncertainty.
- The smallest useful validation or repair.
- The observable condition for closing the issue.

Use these finding kinds:
- confirmed: An inspected artifact establishes the contradiction or defect.
- suspected: A concrete observation supports a plausible problem not yet checked.
- missing-evidence: A material claim lacks the required support in inspected material.
- preference: An editorial choice without a demonstrated substantive defect.

Use blocking, major, minor, or editorial severity.
Tie severity to the main conclusion and the effort needed to establish it.
Do not label an ordinary missing attachment as a confirmed scientific failure.
Do not accuse authors of fabrication or infer intent from inconsistent records.

State a rejection reason as a conditional assessment of the supplied submission:
identify the claim the current evidence cannot establish and why it matters.
Do not predict an editor's decision or assign unsupported acceptance probabilities.
Do not default to rejection before reading the evidence.

## Find material blind spots

Look for an omitted question that could change the contribution,
such as deployability of the available information, the true task outcome,
a failure branch excluded from scoring, or a simpler competing explanation.

Require a concrete connection to the paper.
Explain what observation would make the concern more or less credible.
Do not invent objections to reach a requested number.
If fewer substantial issues are supported, return those with their evidence.

Keep strengths when they affect the assessment:
a sound control, an explicit boundary, or a useful result can defeat an objection.
Do not preserve an accusation after its premise has been disproved.

## Keep review and manuscript separate

Put findings in the review output or authorized review record.
Do not insert reviewer dialogue, generic disclaimers, or editorial instructions
into the manuscript during a review-only task.

Recommend a content repair:
correct a metric, explain an implementation detail, add the missing comparison,
or narrow a claim to the evidence.
Adding "may" or a broad limitations paragraph is not a repair for an invalid metric.

Distinguish resolving an overclaim by narrowing it from demonstrating
the original broader claim with new evidence.
A proposed experiment is an action item, not a completed result.

## Use project records when appropriate

Follow the existing issue headers:
issue_id, location, claim_id, severity, kind, finding, basis,
status, resolution, recheck, closed_at.

Use open, in-progress, closed, deferred, or disputed accurately.
A review-only task normally reads existing records and returns a report;
write issue records only when requested or part of the authorized project workflow.
Keep resolution and recheck evidence for a material issue before closing it.
Never fill closed_at for an unresolved or merely planned repair.

Respect prior closures.
Reopen a closed issue only when new relevant evidence appears,
including a relevant change to the manuscript, implementation, or result.
Do not reopen it merely because a new review pass would phrase it differently.

## Deliver a useful assessment

Lead with the most consequential evidence-based finding.
Report material rejection risks, implementation doubts, blind spots,
and prioritized minimum actions without forcing those categories to be nonempty.
If an overall recommendation is requested, justify it against the inspected scope
and supplied criteria rather than treating it as a real journal decision.

State which necessary evidence remains unavailable.
Do not claim that the paper is guaranteed to pass formal review.
If no material defect is found within the inspected scope, say so directly.
Stop after the requested review; do not start unrelated rewrites or experiments.
