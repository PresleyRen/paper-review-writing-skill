# 论文工作流 Harness

版本：2026-10-19。适用对象：有笔记、稿件、代码、实验记录或其中一部分材料的论文项目。

## 1. Harness 在这里负责什么

这里的 harness 是围绕模型任务建立的执行环境：明确输入、选择技能、维护研究状态、记录审稿问题、安排检查并控制结束条件。

| 层 | 负责的事 | 生效方式 |
| --- | --- | --- |
| AGENTS.md | 常驻项目规则与路由 | Codex 按项目指令加载规则发现。 |
| SKILL.md + description | 某项任务的具体方法 | 语义匹配或明确选择技能后读取。 |
| PROJECT.json、state.json、TSV | 输入路径、事实状态、问题状态、检查证据 | 本项目工作流和脚本读取；不是 Codex 内置科研格式。 |
| Python 工具 | 候选提取、文件冲突检查、记录与版本检查 | 实际执行命令才会运行。 |
| 可选本地 hook | 在受支持的生命周期事件做一次提示 | 需要配置并信任，不能只写进 Markdown。 |
| 可选 Codex CLI | 从 prompt 文件启动一次模型任务 | 需要已安装、可用且已登录的客户端。 |

这些层的边界要保持清楚。文档里写“执行审稿”不等于后台已经执行；记录里写 pass 也不等于脚本验证了科学结论。

## 2. 入口由当前任务决定

| 用户当前任务 | 路径 | 默认结束点 |
| --- | --- | --- |
| 只改一段语法 | voice | 保真检查后交付段落。 |
| 乱序笔记成稿 | draft → 局部 voice 检查 | 交付有证据支持的正文。 |
| 规范改写来源段落 | rewrite → 来源/原意核对 | 交付改文与所需引用。 |
| 检查研究论证 | positioning | 给出主张边界、竞争解释和判别办法。 |
| 只做审稿 | redteam，必要时 audit | 交付审稿意见，不擅自改稿。 |
| 按意见修稿 | revision → 受影响内容 audit/voice | 完成可支持的改动，明确未完成证据任务。 |
| 全面审稿并改稿 | redteam → revision → affected audit → voice | 关闭可关闭的问题，保留精确阻塞项。 |
| 投稿前全面检查 | 上述必要阶段 + 全稿事实/引用/数值/正文检查 | 记录当前检查结果并运行项目 gate。 |

从已有研究状态继续，不每次重开选题、文献检索和实验设计。

## 3. 从主张开始建立可追溯关系

每个关键主张至少回答：

1. 论文究竟说了什么？定位到段落、表格、公式或标题。
2. 哪个原始记录、实现事实、文献或推导支持它？
3. 证据到结论之间依赖什么推理与假设？
4. 有没有同样能解释现象的替代解释？
5. 哪个最小检查能区分这些解释？
6. 检查缺失时，当前可写的结论边界在哪里？

预算、模型、任务集合、重试、信息权限、评测器、分母和聚合方式应与结果绑定。不能把 “74%” 当作脱离实验条件的独立数字。

一个问题可能同时影响摘要、主表和结论。建立依赖关系，修改它们；不要把同一个根因拆成多个拒稿理由来凑数。

## 4. 文件与状态

### PROJECT.json

这是本套件的自定义配置。最小配置已经提供在 research/PROJECT.json。

- manuscript_paths：真实稿件文件列表，包含需要核查的附录、表图文本或导出的核查材料。
- evidence_roots：帮助 agent 找相关证据的目录。
- evidence_files：需要随本次检查绑定版本的具体证据文件，可选；大目录不会自动递归哈希。
- claims_file、issues_file、sources_file、state_file：已有记录的位置。
- required_checks：至少包含 claims、numbers、citations、manuscript_boundary。
- review_language、manuscript_language：本项目的默认语言。

路径使用项目内相对路径。外部来源仍可在 sources.tsv 中记录 URL；需要文件新鲜度检查时，保留适合核查的本地证据版本并记入 evidence_files。不要为了符合模板复制大型数据集或改动原始记录。

### Claims ledger

表头：

    claim_id | location | claim | evidence_status | evidence | boundary | disposition

evidence_status：

| 状态 | 必须有的实际基础 |
| --- | --- |
| proposed | 已提出的想法或解释；不是结果。 |
| planned | 已说明准备做的测试；不是运行记录。 |
| implemented | 代码或系统行为已确认；不是性能提升。 |
| measured | 有可追溯的观测或实验记录。 |
| derived | 从明确资料计算或推导得出。 |
| verified | 完成了明确范围的核对；在 evidence 说明核对了什么。 |

disposition 使用 active、narrowed、withdrawn。状态属于具体主张，不能把整个项目写成 verified 后让所有结论自动继承。

模拟属于实验条件，写在 boundary 或 evidence；不要把 simulated 当作 evidence_status。候选提取器的 unverified、核查报告的 supported/contradicted 等状态各有用途，不能直接填进 claims.tsv。未检验的机制假设与观测结果应分成不同主张。

### Issues ledger

表头：

    issue_id | location | claim_id | severity | kind | finding | basis | status | resolution | recheck | closed_at

severity 使用 blocking、major、minor、editorial。
kind 使用 confirmed、suspected、missing-evidence、preference。
status 使用 open、in-progress、closed、deferred、disputed。

“有疑点”与“已经证实有错”必须分开。审稿意见没有依据时，也可以被证据驳回；不能把每条苛刻意见都升级成论文的永久局限。

closed 必须记录修复方式、实际复查及日期。真实研究记录初始为空；示例不是已完成项目的记录。

### state.json

stage 使用 setup、drafting、reviewing、revising、auditing、ready。
submission_requested 仅在当前确实要求投稿级检查时设为 true。

checks 中的每项记录：

    {
      "status": "pass",
      "basis": "实际完成的检查及范围",
      "artifacts": ["research/review/本次检查报告.md"]
    }

未执行为 not_run，有阻塞为 blocked。numbers 或 citations 的 not_applicable 需要明确理由和检查记录；不能用它们跳过实际存在的数字或引用。claims 与 manuscript_boundary 不允许 not_applicable。

remaining_blockers 记录尚未解决的实质障碍。
checked_artifact_sha256 绑定已经检查过的具体文件版本，不包含 state.json 自己。

## 5. 严苛审稿的交付契约

每条有分量的问题至少给出：

- 原句/位置和涉及的主张；
- 检查过的记录、代码、原文来源，或明确缺什么材料；
- 有问题的推理步骤；
- 为什么足以影响该稿件的审稿判断；
- 已证实、疑点、缺证据或偏好；
- 最小判别检查或修复；
- 关闭条件。

不写“实验不充分”就结束。例如：

> 你把收益归因于协作，但协作组可用 16 次模型调用，单 Agent 只有 4 次。现有实验没有区分协作机制与额外推理预算；论文中的“相同预算”还与配置直接冲突。先修正预算描述，并做同预算对照，或把当前主张收窄为这两种配置的观测差异。

这里可确认的是配置差异与表述冲突。协作是否无效仍不知道。不要从一个混杂因素跳到“方法完全没用”或指控作者造假。

关注 LLM/Agent 论文的实际操作：成功是否来自外部目标状态、超时是否被排出分母、核对/重试是否计入预算、是否读取 oracle 信息、消融开关是否真正生效、评判器是否与方法循环自证、离线模拟条件是否能支持部署结论。按具体主张选择，避免通用清单淹没关键问题。

## 6. 修稿怎样真正关闭问题

| 问题 | 可关闭的行动 | 不构成关闭 |
| --- | --- | --- |
| 百分比计算错误 | 对照原始计数修正计算，更新依赖文本与表图，复算。 | 加一句“应谨慎解释”。 |
| 缺同预算对照 | 完成授权对照并核查；或收窄/撤回机制主张。 | 换几个更弱的形容词，仍保留同一因果解释。 |
| 引用不支撑主张 | 找到真实支持来源，或改写/删除依赖该来源的主张。 | 只删除未核验标记。 |
| 重复实验只在计划中 | 改正结果表述，把计划留在计划位置。 | 编造均值、方差、显著性。 |
| 审稿人误解实现 | 给出实际代码/日志，必要时澄清方法，核对改文。 | 只回复“我们不同意”。 |

修复结果进入论文；辩论、证据缺口、关闭理由留在审稿记录。
关闭后只对相关变动重查，不无限循环全稿审判。

## 7. 角色与并行

主代理负责范围、整合和最终稿。
审稿者负责论证链、拒稿条件与盲区。
核查者负责证据、数值与实现对应。
编辑者负责把已接受的修复写进正文，并保持作者声音。

给独立审稿者原稿与证据，避免先告诉它“这篇应该接收”或“这里一定有 12 个问题”。不要把编辑者的自我解释当作证据。

共享稿件只由一个整合者写。多个只读分析可以并行，依赖新的数值或审查结论的修改顺序执行。没有子代理能力时做分离的顺序审查，不假称多人独立审核。

optional/agents/ 提供官方格式的自定义角色示例。复制到实际项目 .codex/agents/ 后按客户端支持使用；没有在本环境执行真实 Codex 子代理配置安装。角色写“只读”是行为要求，不能替代实际权限限制。

## 8. 本地脚本的使用与含义

### 候选提取

    python3 .agents/skills/paper-evidence-audit/scripts/extract_audit_items.py manuscript/main.tex results/summary.csv --output research/audit_candidates.tsv

支持 UTF-8 的 .md、.txt、.tex、.csv、.tsv、.json。输出来源路径、行列、上下文、原始 token、类型与 unverified 状态。它不解析所有数学语义、PDF 或图片，也不证明候选项正确。PDF/图片需实际阅读与适当提取，再做人工或模型对应核查。

### 记录快照

完成实际检查并写出报告、更新 ledgers 后：

    python3 tools/paper_gate.py snapshot --project . --files results/summary.csv

命令只打印哈希，不改状态、不批准检查。将实际检查覆盖的哈希写入 state.json 的 checked_artifact_sha256。项目配置、稿件、三张 ledger、check artifacts 以及 evidence_files 都纳入所需快照。

### 投稿级 gate

    python3 tools/paper_gate.py check --project . --submission

BLOCKED 返回码为 2；记录通过返回 RECORDED_CHECKS_CURRENT，码为 0。没要求投稿级核查且不加 --submission 时，返回 NOT_REQUESTED。

检查的内容是字段/状态合法性、严重问题是否仍打开、关闭记录是否完整、检查说明与报告是否存在，以及文件是否在核查后变化。

脚本不会判断审稿报告写得对不对、证据是否足够、统计推断是否有效，也不会凭关键词扫描决定文风。不要把机器记录通过写成“论文已通过科学验证”。

检查后只要相关正文、表格、指标代码或记录变化，就更新受影响的检查及快照。不要只刷新哈希以掩盖没有复查。

## 9. 可选本地 Stop hook

默认交付不安装 hook。完整模板在 optional/hooks.template.json。

将 command 中的脚本路径改为实际绝对路径，并将配置合并到项目 .codex/hooks.json。已有 hooks 需要保留。当前官方要求通过 /hooks 审阅并信任定义；项目配置层也须被信任。客户端不支持该功能时用上面的显式命令。

本套件 wrapper 仅在 submission_requested=true 且 stage 为 auditing/ready 时运行记录检查。发现问题输出 systemMessage，退出码仍为 0。不返回 decision:block，不用退出码 2 触发 Stop 续跑；不会自动启动模型、实验或循环修改。

这只是结束时的提示，不拦截你手工发送文件、推送仓库或提交期刊。云端编排不支持此处的本地命令 hook。具体支持范围按官方当前文档核对。

## 10. 可选非交互审稿

先在 research/PROJECT.json 配置真实稿件与证据路径；需要指定特殊范围时再编辑 prompts/review_only.txt。然后在已可用的本地 Codex CLI 中执行：

    codex exec --sandbox read-only - < prompts/review_only.txt

此命令实际启动一次模型任务，会使用客户端配置的模型服务。只读审稿与本地 Python gate 是不同操作。不要将付费模型任务放进每次自动 Stop 的脚本。

官方 CLI、子代理和 hooks 可能变化；实现依据与核验日期见 METHODS_AND_SOURCES.md。本交付没有编造最低版本号，也没有假称真实客户端命令已经跑过。

## 11. 中断恢复与停止

重新进入项目时先读 state、未关闭的重大问题和最后检查报告，核对当前文件。
沿原任务继续，不覆盖原始笔记、不重复启动已完成实验。
只有相关产物变更或新证据才重开已关闭问题。

小修改结束于局部保真检查。完整修稿结束于完成可支持的修改并明确真正剩余的证据需求。投稿前检查结束于当前范围被实查且无重大未解决问题；它仍不能保证实际审稿接受。

## 12. 评价这套工作流

用真实失败用例评价：是否改动事实、是否把计划当结果、是否发现预算/分母问题、是否定位来源、是否真的关闭问题、是否污染正文、是否在只改语法时过度行动。

套件源目录中的 examples/ 是虚构练习；验证方法和本次结果在源目录的 VALIDATION.md，二者默认不复制到普通目标项目。目标项目的安装、选择与核验入口见 SKILL_GUIDE.md。不要用单一 AI 检测分数替代这些质量检查。
