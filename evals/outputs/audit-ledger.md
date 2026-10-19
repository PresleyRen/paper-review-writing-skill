本文件为本轮独立执行者在虚构案例中的实际输出；用于核对审计台账接口与任务边界，不是用户的真实研究结果。

# 论文证据核查报告

核查日期：2026-10-19（UTC）
项目：`/tmp/paper-audit-followup-2ofjcoi8`
任务：依据 `$paper-evidence-audit` 核查现有稿件与指定记录；仅更新核查记录。

## 一、结论与核查范围

**在本次指定材料与稿件现有措辞范围内，未发现需要记入问题表的实质矛盾。** 稿件把单轮模拟观测、机制假设和未来重复计划分开表述。记录中的成功数为 26，全部分配任务为 40，复算成功率为 65%；8 次失败和 6 次超时包含在分母内。以上结论对应 `manuscript.md` 第 3 行和 `records.json` 第 2–14 行。

“state checking prevented stale-state errors”仍是作者明确提出的假设，当前记录没有证明该因果机制；“Five independent repetitions”仍是计划，现有完成记录只有一轮。这两点已经由正文中的 “We hypothesize” 和 “are planned” 正确限定，因此本次不把未完成的机制检验或未来运行本身记作已确认错误，也不把它们升级为已测量或已验证的结果。

本次覆盖 `research/PROJECT.json` 指定的全部稿件与证据：`manuscript.md` 第 1–3 行、`records.json` 第 1–15 行。实际逐句核查了主张、数字、分母、观测与计划的区别、因果解释边界、引用和正文边界。没有进行论文改写或新实验，也没有把当前核查标记为投稿就绪。

## 二、实际读取的材料及其证据能力

| 材料 | 实际读取范围 | 用途与可支持范围 |
| --- | --- | --- |
| `AGENTS.md` | 全文 | 确定任务路由、保留原稿与原始记录、问题分级和报告要求。 |
| `ACADEMIC_WRITING.md` | 全文 | 核对证据层级、主张保真及正文边界规则；其中示例未当作本项目证据。 |
| `RESEARCH_HARNESS.md` | 全文 | 使用项目主张、问题与状态记录的合法字段和枚举。 |
| `.agents/skills/paper-evidence-audit/SKILL.md` | 全文 | 执行所选技能的核查和交付要求。 |
| `.agents/skills/paper-evidence-audit/references/audit_protocol.md` | 全文 | 区分候选提取状态、人工核查结果与项目台账状态。 |
| `research/PROJECT.json` | 全文 | 指定 `manuscript.md` 和 `records.json`；证据目录与笔记目录均为空。 |
| `manuscript.md` | 第 1–3 行，全文 | 一段先导观测的三个句子；无表图、引用、显著性检验或比较基线主张。 |
| `records.json` | 第 1–15 行，全文 | 一轮模拟库存任务的结构化运行计数、种子、指标定义、计划数量及消融完成标记。 |
| `research/claims.tsv`、`research/issues.tsv`、`research/sources.tsv` | 更新前均只有表头 | 确认没有可继承或需重开的既有主张、问题或来源记录。 |
| `research/state.json` | 更新前全文 | 初始状态为 `setup`，没有既有已完成检查。 |
| `tools/paper_gate.py` | 全文 | 核对项目状态与快照接口；此工具不提供实验事实证据。 |

`records.json` 是本次提供并实际检查的运行记录，但内容粒度是单轮汇总，未包含逐任务执行轨迹、成功判定器输出、模型与提示配置、预算或消融日志。因此，本报告对运行结果的支持范围是“稿件与这份指定记录相符，且算术可复算”；没有独立确认 26 个任务的成功判定，也没有重新执行控制器。缺少这些更细记录不自动构成当前三句话的矛盾，但它们限制了可声称的核查深度。

正文没有引用键、文献条目或需要本次逐篇核对的引文；未开展外部文献检索。研究判断仅使用以上指定稿件和记录，没有引入其他项目的材料。

## 三、逐项主张核查

人工核查结果使用 `supported`、`internal_consistency_only`、`contradicted`、`missing_source`、`needs_interpretation`。项目 `claims.tsv` 的 `evidence_status` 使用另一套项目枚举，不能将前述结果标签直接写入该字段。

| 主张 ID／稿件位置 | 当前主张 | 证据位置 | 人工核查结果 | 问题或支持边界 | 建议修改或缺少的材料 |
| --- | --- | --- | --- | --- | --- |
| C001；`manuscript.md` 第 3 行，第 1 句 | 一轮模拟运行中，控制器完成 40 个分配任务中的 26 个。 | `records.json` 第 2 行 `setting`；第 3–11 行 `completed_runs` 只有一个元素；第 5–9 行：seed=11、assigned=40、successes=26、failures=8、timeouts=6。 | `supported` | 与提供的模拟库存任务运行记录相符。台账为 `measured`，边界保留单轮、模拟、seed=11 和汇总记录粒度；没有证据用于推广到独立重复、真实部署或相对其他控制器的改善。 | 当前数值与范围不需修改。若要独立核验成功标签，需相应逐任务轨迹与判定记录；本次未要求这些新的验证。 |
| C002；`manuscript.md` 第 3 行，第 1 句括号内 | 26/40 对应 65% 成功率。 | `records.json` 第 6–9 行计数；第 13 行指标定义为 successes / all assigned tasks，包含失败及超时。 | `supported` | 已实际复算 `26 / 40 × 100 = 65%`；`26 + 8 + 6 = 40`。台账为 `derived`。65% 是该轮成功率，正文没有将其写成改善幅度。 | 不需修正。分母应保持 40，不能排除 6 次超时后改用 34；也没有基线可据此推导相对改善或百分点提升。 |
| C003；`manuscript.md` 第 3 行，第 2 句 | “We hypothesize that state checking prevented stale-state errors.” | 主张及假设限定见该句；`records.json` 第 14 行 `ablation_completed=false`。提供的计数字段中没有 stale-state 错误类别或机制对照。 | `needs_interpretation` | 待检验的是假设的因果内容；它不是当前已经确认的研究结果。台账为 `proposed`。没有消融也不能反向推出该假设为假。现有 “We hypothesize” 已正确说明证据层级，因此不据此制造实质问题。 | 当前假设措辞可保留。若以后要写成已证明的机制，需要能识别 stale-state 错误的轨迹及隔离 state checking 因素的适当比较；此处仅记录升级主张所需证据，不启动实验。 |
| C004；`manuscript.md` 第 3 行，第 3 句 | “Five independent repetitions are planned.” | `records.json` 第 12 行 `planned_additional_runs=5`；第 3–11 行仅有一轮已完成记录。 | `supported`（计划数量与未来时态） | 记录支持另计划 5 次，稿件没有把它们计入已完成结果。台账为 `planned`。“independent”在当前句中是计划目标；记录未提供后续种子、重置策略或独立性方案，故本次不确认将来运行的独立性。 | 不需要把计划改写为已完成结果，也不应凭计划产生均值、方差或显著性。未来报告重复结果时，再核查实际运行及独立性设计。 |

四项主张均保持 `disposition=active`：本次没有改写、收窄或撤回正文。C001 与 C002 分开，是为了把来自记录的观测计数和本次复算的比率分别记为 `measured` 与 `derived`；C003 的未检验机制不因表达了一个推测就变成 `derived`。

## 四、数字与条件的实际复算

已用 Python 读取当前 `records.json`，以精确分数执行下列算术核对。这属于对已有记录的复算，不是运行新实验。

| 核查项 | 记录与计算 | 结果 |
| --- | --- | --- |
| 已完成运行数 | `len(completed_runs)=1`，唯一记录 seed=11 | 与 “In one simulated run” 相符。 |
| 任务数守恒 | 成功 26 + 失败 8 + 超时 6 = 分配 40 | 各类计数合计覆盖 40 个分配任务。 |
| 成功率 | `26/40=0.65`；`0.65×100=65%` | 稿件 65% 正确，不涉及舍入误差。 |
| 分母口径 | 第 13 行明确包括全部 assigned tasks、失败和超时 | 没有排除超时；复算与指定口径一致。 |
| 未来运行数量 | `planned_additional_runs=5` | 与未来计划的 Five 一致，不属于 completed_runs。 |
| 消融状态 | `ablation_completed=false` | 不能据此声称已完成机制检验。 |

稿件没有提供或声称基线差异、成本、延迟、均值与标准差、置信区间或 p 值，本次没有推算或补造这些结果。没有表格、图像或图源可供视觉核查。

## 五、问题判定与正文边界

**本次新增实质问题 0 条，`research/issues.tsv` 保留原有表头，未伪造问题或关闭记录。** 判定依据如下：

- 26、40、65% 均有对应记录并通过复算；失败和超时没有被从成功率分母中隐藏。
- 已完成运行数为 1，正文没有声称完成五次重复或稳定改善。
- 机制句明确是 hypothesis，未写成已经验证的因果结论。
- 五次重复明确为 planned；计划尚无结果不等于稿件把计划冒充结果。
- 三句正文均为观测、假设或计划内容，没有助手对话、审查过程说明、TODO 或宣传性编辑说明混入正文。

这里的“无实质问题”只描述当前指定材料与现有窄范围主张，不代表因果机制、重复稳定性或真实部署效果已经通过验证。尚未发生的验证继续保留在主张证据边界中，不转写为无依据的已确认缺陷。

## 六、更新的记录与版本保留

- 新建 `research/audit-report.md`：本报告。
- 更新 `research/claims.tsv`：C001=`measured`、C002=`derived`、C003=`proposed`、C004=`planned`，附稿件位置、证据位置与范围。
- 更新 `research/sources.tsv`：记录此次实际读取的本地来源与对应主张，不声称已读取不存在的文献或任务轨迹。
- 更新 `research/state.json`：登记当前范围内的 claims、numbers、citations、manuscript_boundary 检查及文件快照；保持 `submission_requested=false`，阶段为 `auditing`。
- `research/issues.tsv` 没有新增行；`manuscript.md`、`records.json`、`research/PROJECT.json` 和项目规则不作修改。

稿件与证据的核查版本采用 SHA-256 标识：

| 文件 | SHA-256 |
| --- | --- |
| `manuscript.md` | `fd449dc41d70d961a1c2ec0fdf210bcdd687926cd7ee78cef1311f580edc3de3` |
| `records.json` | `a26c142941bcefa32e985bdb2c2d31c3bb8ba82dfcd69b7b76df6af13214d9ff` |

写入后复读台账并核对合法枚举、行结构、上述输入哈希和快照一致性。未运行投稿级 gate；本任务没有请求投稿就绪判定。哈希和记录检查也不替代科研证据判断。
