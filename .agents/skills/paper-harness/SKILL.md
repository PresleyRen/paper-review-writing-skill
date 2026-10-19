---
name: paper-harness
description: "Set up or coordinate a project-wide academic writing, rigorous review, revision and evidence-audit workflow. 用于安装论文工作流、论文项目初始化、完整审稿修稿闭环、投稿前全面检查。Use for explicit setup or a multi-stage paper task. Do not initialize files or run a full pipeline for an isolated paragraph edit, translation or general writing question."
---

# Paper Harness

Coordinate the requested work through clear inputs, stage ownership and checkable outputs.
Use only the stages needed for the user's task.

## Read the project context

Read applicable AGENTS.md instructions, the task and current manuscript or notes.
If present, read research/PROJECT.json and research/state.json.
For project setup or a full cycle, read the project RESEARCH_HARNESS.md; use references/workflow-contract.md when no project manual exists.
For a question about which skills to install or use, consult SKILL_GUIDE.md when present. Explain the relevant choice without initializing a paper workflow merely to answer that question.

Do not ask the author to restate materials already available. Infer routine paths from the actual project. A template path is not evidence that a manuscript exists there.

## Select the entry point

| Task | Entry point and necessary follow-through |
| --- | --- |
| “Set this up for my project” | Install/merge the project rules and selected skills; preserve existing files; show the actual changes. |
| “Is this claim worth a paper?” | paper-positioning; obtain evidence for a novelty claim before asserting it. |
| “Write from these notes” | paper-draft; finish with a proportionate meaning and language check. |
| “Only polish this paragraph” | paper-voice; no full review, new ledgers or new experiments. |
| “Rewrite this matched paragraph” | paper-rewrite; preserve attribution and distinguish report types. |
| “Review this manuscript” | paper-redteam; use paper-evidence-audit for evidence needed to assess a concrete issue. Do not rewrite unless requested. |
| “Review and fix the paper” | Review, triage, paper-revision, then recheck affected claims and evidence. |
| “Prepare for submission” | Perform the requested final scope: substantive review, supported repairs, evidence/numerical/citation audit and final text check. |

Read a selected skill before applying it. Do not load all references by default.
An automatic match is a routing aid, not proof that a workflow executed.

## Coordinate independent roles

When tools support delegation and the task benefits from it:

- Give a skeptical reviewer the manuscript, research question, relevant methods and evidence.
- Give an evidence reviewer the original records and exact claims to verify.
- Give the editor accepted findings, source material and the writing rules.
- Keep the reviewer independent of the editor's self-assessment; do not prime reviewers with a desired decision.
- Assign one owner for shared manuscript edits. Others return located findings.
- Make dependencies sequential: do not let an editor invent evidence while waiting for an auditor.

For small tasks or without delegation tools, perform separate sequential passes and describe them honestly. Do not claim multiple independent agents ran if they did not.

## Maintain durable state proportionately

For multi-stage project work, update only relevant records:

- research/claims.tsv: claim text, location, evidence status, support and boundary.
- research/issues.tsv: located issue, basis, consequence, repair and closure.
- research/state.json: current stage, actual checks, remaining blockers and the version of checked inputs.
- research/sources.tsv: citation source, locator and what it supports.

Use these project templates if present; otherwise use a concise equivalent.
Keep records outside manuscript prose. Do not create paperwork for a clean sentence edit.

## Execute the authorized repairs

Complete edits that existing evidence supports.
A missing control can lead to a design task, a narrower claim or an explicitly unresolved issue.
A test plan is not a completed test. Do not run costly or destructive experiments merely because a review suggested them.

Keep the original notes and raw evidence intact. Preserve unrelated user changes.
Do not stop after a plan when supported work remains.

## Exit and verification

Use the exit criteria in the project harness. For a submission task, verify sources, numerical associations, claim boundaries, citations and the final manuscript separately from prose polish.

When available, run the project's paper_gate.py to check record completeness and snapshot freshness. It cannot establish scientific truth, detect all errors or predict acceptance. Never make a missing gate pass by deleting a finding, fabricating a record or changing a status without its evidence.

Stop when the requested work is complete or the remaining task specifically needs unavailable evidence. Report that exact gap and deliver the supported work.

If setting up this starter project, use its tools/install_project.py with --dry-run first and then the authorized installation. Do not infer that this skill alone contains or installed all companion skills. If the complete project source is unavailable, use assets/project-rules.md as a minimal instruction fragment and state which companion files are still absent.
