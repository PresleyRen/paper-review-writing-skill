---
name: paper-revision
description: "审稿修订、处理 reviewer comments、修订计划与 response letter；turn known review findings into evidence-grounded manuscript changes and traceable responses. Use when the user asks to address comments, apply revisions, plan repairs, draft a rebuttal, or verify issue closure. Respect review-only and plan-only requests. Do not trigger for a first independent review, ordinary polishing without review findings, style extraction, or a new research-positioning task."
---

# Paper Revision

Translate review findings into specific, authorized repairs.
Keep the manuscript accurate and natural while making the status of each action clear.
Treat a review as evidence to assess, not an instruction that is automatically correct.

## Establish the requested action

Identify whether the task is:
- Review-only: assess the supplied comments and findings without changing the manuscript.
- Plan-only: propose decisions and repairs without claiming they were applied.
- Apply revisions: perform the changes authorized by the user's request.
- Response-only: draft a reply consistent with the work actually completed.
- Closure check: verify the named issues against the changed artifacts.

A request to revise authorizes ordinary supported edits within its scope.
Do not ask again for permission already given.
A suggestion in a review does not itself authorize a new experiment,
an unsupported result, or a change to the central research objective.

Read the requested manuscript, review, and available evidence.
Read the project-root ACADEMIC_WRITING.md if it exists.
In project mode, inspect relevant existing research/PROJECT.json,
research/claims.tsv, and research/issues.tsv before changing project records.
Read actual paths, headers, and required checks; do not invent configuration fields.
Use a concise issue record in chat when no project files are involved.

Read [repair-and-response.md](references/repair-and-response.md)
for repair decisions, closure examples, and evidence-grounded response patterns.

## Reconstruct the issue accurately

1. Locate the review comment and the exact affected claim or artifact.
2. Identify the evidence the reviewer inspected and any unstated assumption.
3. Check whether the problem is confirmed, suspected, missing evidence,
   or an editorial preference.
4. Separate multiple independent problems hidden in one comment.
5. Merge duplicate comments that have the same cause and repair.
6. Preserve existing issue identifiers and previous decisions.

Do not manufacture a flaw simply because the reviewer demanded a change.
Do not dismiss a substantive problem merely because the review sounds harsh.
If the comment rests on a mistaken reading, identify the relevant evidence
and decide whether a clearer explanation would prevent that reading.

## Choose a repair and its authority

Distinguish the decision from its execution.

- Accept: the concern is supported and the requested repair is appropriate.
- Adapt: address the valid concern with a smaller or better-supported repair.
- Dispute: explain the evidence or reasoning that defeats the objection.
- Defer: the required evidence or decision is not currently available.

These are decision labels for the working record, not new ledger status values.
Map them to the existing project fields without changing the schema.

Apply local factual corrections, clearer definitions, and supported wording changes
when the user has requested revision.
Preserve relevant negative findings and essential scope conditions.
If a proposal changes the paper's core question, contribution, task population,
or evaluation objective, surface that specific decision before implementing it
unless the existing task already authorizes the change.
Complete unrelated authorized repairs while that decision remains open.

## Build the minimum action

For each material issue, identify:
- The manuscript or implementation change needed.
- The evidence required to justify it.
- Any dependent tables, figures, captions, abstract, or conclusion.
- The smallest check that can establish the repair.
- The condition under which the issue can close.

Prefer checking existing code or rescoring existing records when that resolves the issue.
Do not require a new study when the defect is arithmetic or a misreported setting.
Do not substitute a sentence about limitations for a missing control or invalid metric.

Keep a planned experiment explicitly planned.
Do not fabricate runs, seed counts, labels, statistics, citations, or logs.
Implement and execute experiments only within the task's authorization
and available resources; an unapproved proposal remains an action item.
A passing unit test does not demonstrate a paper-level performance improvement.

## Make the authorized changes

Preserve the author's intended meaning, useful phrasing, and appropriate voice.
Do not import generic reviewer language into the prose.

For every changed claim, preserve or explicitly resolve:
subject, comparator, outcome, numbers, direction, conditions, uncertainty,
evidence status, technical terms, and source support.

Keep observations separate from explanations and intended future work.
Do not convert association into causation or a limited result into a broad guarantee.
A material qualification belongs next to the claim it qualifies.
Remove redundant defensive framing once the actual problem has been repaired.

When editing a file, keep working notes outside the manuscript.
Do not overwrite original research notes unless an in-place rewrite was requested.
Make changes only within the requested scope and preserve unrelated work.

## Verify the changed claim and its dependencies

Check the actual resulting artifact, not a plan to change it.
Compare affected numbers and statements with the identified source.
Recheck dependent summaries after changing a result or metric.
Do not restart an unrelated full-paper audit after a local correction.

Use claim evidence statuses accurately:
proposed, planned, implemented, measured, derived, or verified.
A recalculated quantity may be derived from identified observations.
A verified status must state the executed check and its scope.
Do not imply that checking a percentage verified the original data collection.

Use active, narrowed, or withdrawn for claim disposition.
Narrowing a claim does not retroactively validate the broader version.
If the accepted repair removes a central contribution, report that consequence;
do not quietly present the remaining paper as satisfying the original objective.

## Close issues with evidence

Use the project issue headers when the ledger exists:
issue_id, location, claim_id, severity, kind, finding, basis,
status, resolution, recheck, closed_at.

Use open, in-progress, closed, deferred, or disputed as documented.
For blocking or major issues, require a concrete resolution and a recheck
before setting closed and recording the actual closure time.
A promised future experiment is insufficient.
An unresolved disagreement is disputed, not silently closed.

Record whether closure came from:
- Correcting an error and checking the corrected artifact.
- Obtaining new evidence and checking the associated claim.
- Clarifying an implementation or assumption with a verified source.
- Narrowing or withdrawing an authorized claim and checking dependent text.

Resolve an overclaim by removing its unsupported part when authorized.
Keep a separate unanswered scientific question open if it still requires evidence.
Reopen a closed issue only for new relevant evidence or a relevant artifact change.
Do not reopen it just to produce another review cycle.

## Write a response consistent with the work

Explain what changed, why it addresses the concern, and where it can be found.
Use completed-action language only for changes and checks actually completed.
For pending work, label the proposed action and the evidence still needed.
Do not invent a commitment the author has not made.

A response letter may explain a decision or disagree with a reviewer.
Use specific evidence and a direct, professional tone.
Do not copy that exchange into the manuscript.
Do not claim that a response guarantees acceptance.

## Deliver in the requested format

For review-only or plan-only work, return findings or actions without changing the paper.
For a manuscript-only revision, return the revised prose when it can be completed faithfully.
Keep any material blocker separate and minimal; ordinary uncertainty is not a blocker.
For a response letter, include only truthful change descriptions and requested context.
For project work, update authorized records using their existing schema.
Do not create ledgers or a report for a routine chat edit with no material issues.

State material work left pending without treating supported edits as unfinished.
Stop after the affected issues are resolved or a concrete missing input blocks them.
