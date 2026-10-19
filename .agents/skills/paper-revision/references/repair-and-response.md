# Repair Decisions and Response Patterns

Use the smallest repair that addresses the actual finding.
Keep editorial decisions separate from manuscript prose.

## Choose the repair

| Finding | Appropriate repair | Insufficient replacement |
| --- | --- | --- |
| Arithmetic or denominator error | Recompute from identified observations; update dependent text and tables. | Retaining the error and adding a cautionary sentence. |
| Method differs from implementation | Inspect the executed path; correct the account or the authorized implementation. | Rewriting the method to sound more rigorous without checking code. |
| Mechanism is not isolated | Add the relevant control if authorized, or narrow the mechanism claim if authorized. | Declaring the same result merely suggestive without addressing what it establishes. |
| Scope exceeds evaluation | Name the actual setting and revise dependent claims. | Hiding the boundary only at the end of the paper. |
| Novelty overlaps prior work | Verify the overlap; clarify a supported distinction or propose a substantive repositioning. | Renaming the method and preserving the same novelty assertion. |
| Reviewer misreads an existing control | Cite its actual location and result; clarify the manuscript if helpful. | Accepting an incorrect criticism or attacking the reviewer. |
| Required source is unavailable | Mark the exact unresolved evidence need; complete independent repairs. | Treating missing material as confirmed failure or claiming it was verified. |
| Reviewer prefers a different sentence | Apply it when useful and within scope; otherwise explain the editorial choice if requested. | Treating a preference as a scientific defect. |

## Truthful response patterns

Use these only when their factual conditions hold.
They are adaptable patterns, not mandatory opening formulas.

Completed wording correction:
"Section 3 now specifies that evaluation used simulated API failures.
The abstract and conclusion use the same scope."

Completed numerical correction:
"Table 2 now reports the success rate over all 100 attempted tasks.
The calculation includes the 10 timed-out tasks in the denominator."

Completed new comparison:
"The revised experiment compares both conditions under the stated call budget.
Table 3 reports the new comparison, and Section 4 describes its configuration."

Use the last pattern only after the comparison actually ran and its outputs were checked.

Supported disagreement:
"The reported metric includes all attempted tasks, including timeouts.
We have clarified the denominator in Section 4."

Use completed-action wording only if that clarification was made.
If it was not, describe the evidence and propose the clarification without claiming it exists.

Pending work in an editorial plan:
"Pending: run the matched-budget comparison before retaining the causal claim."

A pending item belongs in the plan or issue record.
It must not become "We performed the requested comparison" in a rebuttal.

## Worked closure: a denominator error

The following example is hypothetical.

Source observations:
100 attempted tasks; 80 successful, 10 failed, and 10 timed out.
The stated metric uses all attempted tasks.
The current script excludes timeouts and reports 80 / 90 = 88.9%.

Repair:
Recompute 80 / 100 = 80%.
Correct the scorer when code changes are authorized.
Update affected manuscript, table, caption, and summary statements.

Recheck:
Compare the resulting denominator and result with the source observations.
Check that timeouts remain recorded as attempted tasks.
Do not claim that recomputation validates the original outcome labels.

Closure:
Record the actual correction and recheck before closing the metric issue.
The value is derived from the identified observations.
Any verified status must identify the particular check performed.

## Worked closure: an unsupported mechanism

The paper attributes an observed improvement to collaboration.
The existing evaluation changes both collaboration and computation.

If a matched comparison is authorized and completed:
Check the result and revise the mechanism claim accordingly.

If the author authorizes narrowing:
Report the observed system-level comparison under its actual budgets.
Remove unsupported mechanism assertions from dependent passages.
Record disposition as narrowed for the affected claim.

The narrowed claim can resolve the overstatement.
It does not establish the original mechanism or close a separate task to test it.
If the central contribution depends on that mechanism, report the remaining consequence.

## Recheck only what changed

A numerical correction requires checking dependent numbers and interpretations.
A clarification requires checking the relevant meaning and reference.
A new experiment requires checking its records and the claims based on them.
A change that invalidates an earlier closure is new evidence for that issue.
A fresh stylistic preference does not by itself reopen a closed scientific issue.
