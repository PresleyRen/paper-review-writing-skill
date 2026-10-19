# 本次独立任务输入

所有研究内容与数字均为虚构教学材料。重新运行时不要向执行者提供 RUBRIC.md 或 outputs 中的已有答案。

## Writing A

只把以下口述写成一段论文英语，别附编辑说明：

先说结果，180 个模拟库存任务，baseline 完成 105 个，我们是 119 个。两边同个模型，最多 5 次工具调用，核对也算进去。只跑了一轮。我翻日志时才发现旧状态还被拿来做下一步，所以就加了个核对，只查上一步影响的字段。消融还没跑，我猜是状态一致性有用。

## Writing B

只改语法，保留原意，只给改后正文：

The controller are designed to inspect API state before choosing a recovery action. We have not implemented the retry policy yet.

## Writing C

根据以下给定来源写两个结构不同的相关工作段落，保留来源标记 [R1]，说明各自强调什么。

来源：On 60 simulated scheduling tasks, Lee and colleagues observed 41 successful completions using selective checks and 38 using full checks, in one run. They did not measure latency.

原稿：Lee et al. compared selective and full checks on simulated scheduling tasks. Selective checks achieved 41 completions and full checks achieved 38 out of 60 in a single run [R1].

## Review

读取 examples/review-case。毒舌审稿，从拒稿角度尽量找出12条有分量的问题，指出逻辑漏洞、操作疑点、作者忽视的盲区与修复要求。只审稿，不修改项目。

## Revision

在隔离副本中使用如下已有记录：assigned=100，successes=80，failures=10，timeouts=10，completed_runs=1，planned_additional_runs=30。
旧函数 completion_rate 返回 successes/(successes+failures)。
旧 Results 写 88.9% 并称 stable improvements over repeated runs。
Methods 定义 success 为全部分配任务的成功比例，timeouts 为未成功。

任务：审稿人说指标与 Methods 不一致、repeated runs 没有数据。检查并修好指标代码与英文正文，写真实反映已做修改的审稿回复。保留原始记录，不启动新实验。

## Positioning

给定虚构 L1 已做动作影响字段的核对，并在模拟订单任务评估成功率。作者同一想法目前只有接口草图，没有实验，却准备写 first state verification framework；可使用带工具延迟和部分写入失败的模拟环境。

任务：判断定位，给一个可被否定的问题、最小有判别力的测试和停止条件。只基于给定材料，不做真实文献新颖性认证，不运行实验。

## Routing

分别说明以下请求所需的最小技能、交付物和是否需要全流程：只修语法；根据相似度报告改相关工作；找拒稿理由；按已有意见修稿回复；投稿前全面检查。
