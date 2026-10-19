### A

The agent with state checking completed 119 of 180 simulated inventory tasks, compared with 105 for the baseline, in a single run. Both agents used the same model and were allowed at most five tool calls per task, including calls used for state checking. We introduced the check after inspecting logs that showed the agent using an outdated state to choose its next action. The check covers only the fields affected by the preceding action. We hypothesize that maintaining state consistency contributed to the difference in completions, but we have not yet conducted an ablation study.

### B

The controller is designed to inspect API state before choosing a recovery action. We have not implemented the retry policy yet.

### C

**版本一：结果先行**

The completion counts in Lee et al.’s study were 41 with selective checks and 38 with full checks across 60 simulated scheduling tasks. These results came from a single run, and latency was not measured [R1].

这一版本先呈现两种核对方式的完成数量，再交代单轮实验和未测延迟的范围，强调已观察到的结果差异。

**版本二：评价范围先行**

Lee et al.’s evaluation of selective and full checks used one run of 60 simulated scheduling tasks and did not measure latency. They observed 41 successful completions with selective checks and 38 with full checks [R1].

这一版本先交代实验设置和未测量的指标，再报告完成数量，强调这项已有研究提供了哪些证据。
