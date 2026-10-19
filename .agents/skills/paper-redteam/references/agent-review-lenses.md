# LLM and Agent Review Lenses

Use a lens only when its subject affects the paper's claim.
Turn a question into a finding only after locating its evidentiary basis.

## Select the relevant lens

| Claim or component | Inspect | Smallest useful discriminator |
| --- | --- | --- |
| Task success | Actual world or database state, success definition, invalid actions, and timeouts. | Rescore available traces against the stated outcome criterion. |
| Planning or reasoning | Model, information, prompt, budget, attempts, and stopping differences. | Identify the changed factor and add the necessary matched comparison. |
| Tool recovery | Partial commits, retries, idempotency, stale state, and termination. | Inspect a relevant failure trace and its executed recovery path. |
| State verification | Inputs available to the verifier, cost accounting, and independent error labels. | Check for oracle information and compare predicted errors with external labels. |
| Multi-agent collaboration | Total computation, communication, sampling, aggregation, and judge visibility. | Compare with a suitable single-agent budget control and inspect scoring inputs. |
| RAG | Retrieval, evidence support, answer correctness, corpus version, and access scope. | Inspect failed cases at each layer rather than relying on one end-to-end score. |
| Long-term memory | Task boundaries, retained information, stale entries, and split design. | Trace whether a held-out answer or task-specific state entered memory. |
| Knowledge graphs | Schema validity, entity resolution, relation direction, truth, and source support. | Separate constraint checks from factual evidence checks on selected records. |
| Efficiency | Quality level, token and call counts, latency, retries, and orchestration. | Recompute the named measure with omitted costs included. |
| Robustness or generalization | Evaluation diversity, repeated templates, noise source, and aggregation. | Check whether the evaluated variation matches the claimed boundary. |
| LLM-based evaluation | Rubric, order, identity cues, reference answers, and calibration. | Inspect judge inputs; use an objective check where the task permits one. |
| Algorithm-to-code fidelity | Entry point, defaults, ablations, terminal conditions, and scorer. | Follow the actual executed configuration through the claimed component. |

A method can legitimately use more resources or information if that is part of
the design and the claim reports the trade-off accurately.
A fixed-budget or mechanism-isolation claim needs the corresponding controls.
Do not demand identical inputs where the intended contribution changes access;
instead test whether that access is realistic and described honestly.

## Evidence and interpretation

A trace showing a timeout omitted from a denominator is evidence of that omission.
It does not establish why the omission occurred.
A missing matched-budget baseline establishes an unresolved competing explanation.
It does not prove that collaboration has no value.
A schema-valid graph can still contain factual errors.
A failed test can reflect the implementation, evaluation setup, or research idea;
inspect the layer that failed before assigning the conclusion.

## Worked finding: unmatched computation

The following records are hypothetical and illustrate review structure.

Anchor:
The abstract claims a collaboration gain under an equal model-call budget.
The run record contains 16 calls for the multi-agent condition and 4 for the baseline.

Kind and severity:
confirmed; major, or blocking if the equal-budget mechanism claim is central.

Finding:
The stated equal-budget condition conflicts with the recorded executions.
The result cannot isolate collaboration from additional computation.

Minimum repair:
Correct the budget description.
For the mechanism claim, add a suitable same-budget control or remove that claim
with the author's authorization if it changes the paper's central positioning.

Close when:
The wording matches the runs and the resulting claim is supported by the comparison.
Record separately whether new evidence was obtained or the original claim narrowed.

## Worked finding: uninspected verifier inputs

Anchor:
The method says that a verifier compares predicted state with "ground truth."
No input construction or deployable source is supplied.

Kind:
missing-evidence, with a specific oracle-information concern still suspected.

Finding:
The available material does not establish whether the verifier can operate
with information available at intended deployment time.

Minimum check:
Inspect the function that constructs verifier inputs and the source of each field.

Close when:
The input path is documented and checked, or the claim is explicitly restricted
to an oracle-assisted setting that the author accepts.

Do not report hidden-label leakage as confirmed until the input path supports it.

## Closed-issue discipline

A rewritten paragraph is new relevant evidence only for claims it changes.
A new code branch or scorer configuration can invalidate a previous check.
A different reviewer's wording preference does not invalidate a resolved result.
Recheck affected dependencies rather than restarting the entire review.
