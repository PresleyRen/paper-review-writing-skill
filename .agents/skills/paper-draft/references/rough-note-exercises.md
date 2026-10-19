# Rough notes and faithful prose

All research settings and numbers in this reference are fictional teaching material.

## Result first, with a real change of mind

Raw notes:

> 先别写那个“大幅提高”。我们这次是 100 个模拟退款任务，baseline 做成 62 个，加核对是 74 个。两边同一个模型，最多 6 次工具调用，核对也占这个次数。其实我是翻日志才注意到，它有几步还在用旧状态，工具明明已经返回新的了。后来才加了这个检查，只看上一步影响的字段。就一轮，重复实验还没跑。

One manuscript version:

> The agent with state checking completed 74 of the 100 simulated refund tasks; the baseline completed 62. These counts come from a single run. Both agents used the same model and had a six-call tool budget, including calls used for checking. We added the check after inspecting traces in which the agent continued to use an outdated state despite receiving a tool update. The check covers the fields affected by the preceding action.

The author leads with the result; the draft preserves that choice. It retains the single-run setting and budget definition. It reports why the check was added without claiming a demonstrated causal mechanism. If a difference is needed, it is 12 percentage points; the relative increase is 12/62, approximately 19.4%, with the comparator stated.

## A plan stays a plan

Raw notes:

> 我想把全量核对换成只核对变动字段，应该能便宜一点吧。这个没写完，更没测，先别当贡献。

Suitable plan:

> We plan to compare full-state verification with checking only the affected fields and measure their verification cost.

Do not write “Our selective verification reduces cost.” Neither implementation nor measurement is available.

## Discussion with uneven emphasis

Raw notes:

> 超时这个得说。主表好看一点，但慢任务还是慢，主要是工具卡住时多了一次查询。平均值变化不大，我们现在还没有尾延迟的完整统计。别把“平均差不多”写成“没有额外延迟”。

Suitable discussion, if those observations are the supplied record:

> The mean latency changed little in this evaluation. Some tool stalls nevertheless triggered an additional query, so the mean alone does not establish that the method adds no latency. We have not yet completed the analysis of tail latency.

The qualification conveys a specific measurement boundary. It is not an apology or a promise about future results. If exact mean estimates become available, name them and their evaluation setting.

## What to learn from an author sample

Learn paragraph purposes, where an author places the key fact, how they introduce terms, acceptable first-person usage and characteristic transitions. Keep technical vocabulary stable.

Do not infer an English author profile solely from Chinese chat. Do not copy another paper's distinctive phrasing, findings or experiences into the current manuscript. Preserve useful wording from the current draft and notes.
