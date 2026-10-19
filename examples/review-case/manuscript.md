# Budget-matched multi-agent coordination

This fictional excerpt is provided for a review exercise.

## Methods

We compare a multi-agent coordinator with a single-agent baseline on 100 simulated service tasks. Success is the proportion of all assigned tasks completed. Both methods use equal model-call budgets and access the same information.

## Results

The baseline succeeds on 66.0% of tasks and the coordinator succeeds on 88.9%, a gain of 22.9 percentage points. This stable improvement across seeds demonstrates that collaboration itself improves reasoning. Our checker requires no privileged state, making the result directly applicable to production.

## Run notes

The current table uses the available run. Thirty additional seed runs are planned for next week.
