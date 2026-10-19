# Claim and Experiment Cards

Use only the fields needed for the current research decision.
These are working records, not mandatory manuscript headings.

## Contribution card

| Item | Record |
| --- | --- |
| Observed problem | Specific behavior and its source, or mark it hypothetical. |
| Task and setting | Inputs, environment, information available, and constraints. |
| Current approach | A real implementation or accurately described baseline. |
| Proposed change | The smallest intervention under investigation. |
| Expected mechanism | Why that intervention might change the outcome. |
| Competing explanation | A different cause that could explain the same result. |
| Nearest work | Source, actual overlap, and remaining distinction. |
| Main claim | Comparator, outcome, conditions, and evidence status. |
| Falsifying observation | A result that would defeat or materially narrow the claim. |
| Next check | Smallest useful inspection, rescore, or experiment. |
| Prerequisites | Data, labels, implementation, access, time, and allowed budget. |
| Decision | Continue, revise, defer for a named prerequisite, or abandon. |

Keep novelty and feasibility as separate questions.
A method can be feasible but already known, or distinctive but presently untestable.

## Match the check to the claim

| Proposed claim | Discriminating evidence | Inadequate substitute |
| --- | --- | --- |
| State checking improves recovery | Same tasks with and without checking; objective final-state assessment; relevant budget accounting. | A trace in which the checker correctly diagnoses one error. |
| Collaboration explains an improvement | A suitable single-agent comparison at comparable budget, with the actual coordination change identified. | More agents also receiving more calls and more source information. |
| Retrieval improves factual support | Source-grounded assessment plus task correctness, with retrieval conditions recorded. | A fluent answer or a citation that exists but does not support the claim. |
| A memory policy generalizes | Evaluation with separation appropriate to the task and inspection for cross-task information leakage. | Repeating near-identical templates already stored in memory. |
| Ontology constraints improve factual quality | Separate constraint validity from entity, relation, and evidence correctness. | Passing a schema validator alone. |
| A method reduces cost | A named cost measure at an explicitly compared quality level, including orchestration and retries. | Counting only the main model call. |

Treat these as diagnostic patterns.
Choose the checks relevant to the actual claim rather than requiring every row.

## Pilot card

Record the question, dataset or task source, evaluation unit,
conditions, baseline, intervention, budget, and primary endpoint.
Record all exclusions in advance where practical.
Retain failed and timed-out attempts according to the stated endpoint.

Specify the result that would justify a larger study.
Specify the result that would make the current explanation doubtful.
Specify how an ambiguous pilot would be distinguished from a negative one.

A pilot may reveal that the benchmark is insensitive or the implementation fails.
Do not interpret those outcomes automatically as proof against the research idea.
Diagnose the relevant layer before deciding what to test next.

## Hypothetical example: stale task state

The following is an invented design example, not evidence about a user's system.

Observation:
Some inspected traces continue from an old task state after a tool returns an update.

Candidate claim:
Checking fields affected by the latest action may reduce stale-state errors.

Key alternative:
The new agent may simply receive extra calls or more current information.

First checks:
Inspect whether the proposed checker uses deployable information.
Confirm that checking calls count toward the reported budget.
Define a stale-state error independently of the checker's own output.

Small comparison:
Evaluate the original agent, the agent with the proposed check,
and a relevant control for any extra budget or information introduced.
Use the same task source and a common objective success definition.

Useful negative result:
If the budget-matched control explains the improvement,
the claim about the special checking mechanism is not established.
Do not hide that result; revise the explanation or the study.

Boundary:
A change in a simulator does not itself establish performance during live outages.
A causal explanation requires evidence that distinguishes it from material alternatives.

## Evidence statuses in project records

- proposed: A claim or mechanism has been suggested.
- planned: A specific check has been designed but not completed.
- implemented: The relevant behavior exists and its implementation is confirmed.
- measured: An execution produced a traceable observed result.
- derived: A quantity was calculated from identified source observations.
- verified: An explicitly identified check was actually performed.

Verification applies to its stated scope.
Recomputing a percentage does not verify the original data collection.
Use disposition to distinguish active, narrowed, and withdrawn claims.
