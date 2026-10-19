# Codex 论文审稿与写作工具箱

用于**严格审稿、证据核查、论文写作和返修**的 Codex 项目工具箱，覆盖研究定位、口述起草、作者声音润色、问题复核与审稿回复。围绕作者提供的真实材料工作，保留主张的证据状态、数值、来源和必要边界，把审稿问题落实到可追溯的修改与复核。

仓库包含 **八个可独立使用的技能、17 组任务提示词、共享写作规则、研究记录模板、本地工具和验证案例**。建议完整保留套件，执行任务时只选择必要技能；一句话润色不需要启动完整论文流程。

版本：2026-10-19。本地 Python 工具面向 **Python 3.10+**，仅使用标准库；本次实测环境为 Python 3.12.14。技能正文和规则文件本身不依赖 Python。

## 文档入口

| 文档 | 什么时候读 |
| --- | --- |
| [SKILL_GUIDE.md](SKILL_GUIDE.md) | 首次使用：安装范围、按场景选择技能、方法整合、安装后核验。 |
| [AGENTS.md](AGENTS.md) | 项目入口：任务路由、授权范围、正文边界、审稿与问题关闭规则。 |
| [ACADEMIC_WRITING.md](ACADEMIC_WRITING.md) | 起草或改文：口述笔记、作者声音、证据保真、去自我防御表达。 |
| [RESEARCH_HARNESS.md](RESEARCH_HARNESS.md) | 多阶段任务：研究状态、角色协作、验收、恢复、可选 hooks 与 CLI。 |
| [PROMPTS.md](PROMPTS.md) | 直接复制 17 组任务提示词，并替换为真实材料路径。 |
| [VALIDATION.md](VALIDATION.md) | 查看已经执行的验证、实际输出与未验证的能力。 |
| [METHODS_AND_SOURCES.md](METHODS_AND_SOURCES.md) | 追查方法来源、整合取舍与配置依据。 |

## 快速开始：直接使用克隆的项目

### 1. 克隆仓库

```bash
git clone https://github.com/PresleyRen/codex-paper-review-writing.git
cd codex-paper-review-writing
```

仓库已包含项目级技能目录 [.agents/skills](.agents/skills) 和配套规则。打开这个目录作为 Codex 项目，检查当前客户端的技能列表是否能看到下表中的八个名称。CLI/IDE 可通过 `/skills` 检查，并用 `$paper-redteam` 等名称明确调用；具体选择方式与核验要求见 [技能指南](SKILL_GUIDE.md)。新增技能未出现时，重开会话后再检查。

技能文件存在、客户端能发现技能、技能在一次任务中表现正确，需要分别确认。无法观察客户端技能列表时，应将原生技能发现记为未验证。

### 2. 配置真实材料

按项目需要修改 [research/PROJECT.json](research/PROJECT.json)，设置稿件、结果、参考资料和笔记路径。默认的 `manuscript/main.md` 是路径示例，仓库没有附带真实论文。保留已有的正确配置和研究记录。

[examples](examples) 与 [evals](evals) 用于学习和复查虚构测试案例，不应作为真实研究结果。普通段落修改只需提供相应文字与来源；多阶段任务再使用研究台账。

### 3. 开始当前任务

可以先复制下面的请求，再从 [17 组提示词](PROMPTS.md) 中选择更具体的版本：

> 读取当前项目 AGENTS.md 和 SKILL_GUIDE.md。我的论文材料在【真实路径】，这次要完成【审稿 / 修稿 / 起草 / 核查】，交付【具体要求】。按请求动作选择最小所需技能，列出实际读取的材料后直接完成任务。保留已有研究记录，不把示例当成研究证据。

## 八个技能：按当前任务选择

| 技能 | 适合的请求 | 主要产出与范围 | 对应 Prompt |
| --- | --- | --- | --- |
| [paper-harness](.agents/skills/paper-harness/SKILL.md) | 建立流程；审稿并修稿；投稿前完整检查 | 调度必要阶段，整合产物与检查记录。 | 1、8、12 |
| [paper-positioning](.agents/skills/paper-positioning/SKILL.md) | 创新点是否成立；如何排除竞争解释 | 主张边界、最近工作差异、最小判别检查或实验设计。计划保持为计划。 | 10 |
| [paper-draft](.agents/skills/paper-draft/SKILL.md) | 将乱序口述、笔记或已知结果写成新段落 | 忠实的新正文，区分观察、实现、假设与未来工作。 | 2 |
| [paper-voice](.agents/skills/paper-voice/SKILL.md) | 去套话和自我防御；保留作者声音；只改语法 | 修改已有正文，保持事实、术语、数值和必要限定。 | 3、4、13 |
| [paper-rewrite](.agents/skills/paper-rewrite/SKILL.md) | 对照来源重组段落；处理真实相似度报告 | 来源清楚的改写或结构习作，保留归属与引用。 | 5、6 |
| [paper-redteam](.agents/skills/paper-redteam/SKILL.md) | 严苛审稿；找拒稿理由和论证盲区 | 有定位与依据的问题、影响、最小检查和关闭条件。只审稿时保留原文。 | 7 |
| [paper-evidence-audit](.agents/skills/paper-evidence-audit/SKILL.md) | 对照原始记录核查数字、表图、主张与引用 | 可追溯的核查记录；缺少来源的项目保持无法核验。 | 11 |
| [paper-revision](.agents/skills/paper-revision/SKILL.md) | 根据已有意见修稿、回复；复核已关闭问题 | 实际修订、关闭依据与如实回复，不把待做实验写成已完成。 | 9、15 |

每个技能均包含 `SKILL.md`、`agents/openai.yaml` 和按需读取的参考资源。技能配置允许隐式调用，实际选择取决于任务与技能描述的匹配；重要任务可以明确指定主技能。

`paper-harness` 是调度入口，单独复制它不会安装另外七个技能。下方安装器负责复制完整套件。此前参考的 anti-defensive-writing、Writing & Thinking with AI Assistance 和图片方法已按用途整合为规则；使用本套件无需另行安装这些方法来源。对应关系见 [技能指南的整合对照表](SKILL_GUIDE.md#3-之前的方法整合到哪里了)。

## 17 组可复制提示词

完整文本在 [PROMPTS.md](PROMPTS.md)。先选任务，再把占位符换成真实路径、材料和交付要求。

| 编号 | 任务 |
| --- | --- |
| 1 | [安装到项目](PROMPTS.md#1-安装到项目) |
| 2 | [从真实乱序口述起草](PROMPTS.md#2-从真实乱序口述起草) |
| 3 | [去自我防御，保留作者声音](PROMPTS.md#3-去自我防御保留作者声音) |
| 4 | [只改语法](PROMPTS.md#4-只改语法) |
| 5 | [来源改写与结构习作](PROMPTS.md#5-来源改写与结构习作) |
| 6 | [按真实相似度报告处理](PROMPTS.md#6-按真实相似度报告处理) |
| 7 | [毒舌审稿](PROMPTS.md#7-毒舌审稿) |
| 8 | [审稿并实际修稿](PROMPTS.md#8-审稿并实际修稿) |
| 9 | [针对已有意见修订并回复](PROMPTS.md#9-针对已有意见修订并回复) |
| 10 | [找论证盲区与最小补充实验](PROMPTS.md#10-找论证盲区与最小补充实验) |
| 11 | [终稿降维核查](PROMPTS.md#11-终稿降维核查) |
| 12 | [投稿前完整检查](PROMPTS.md#12-投稿前完整检查) |
| 13 | [学习我自己的写法](PROMPTS.md#13-学习我自己的写法) |
| 14 | [核验路由是否合适](PROMPTS.md#14-核验路由是否合适) |
| 15 | [仅检查某个已关闭问题](PROMPTS.md#15-仅检查某个已关闭问题) |
| 16 | [安装后的核验与试用](PROMPTS.md#16-安装后的核验与试用) |
| 17 | [我不知道该用哪个技能](PROMPTS.md#17-我不知道该用哪个技能) |

[prompts](prompts) 另提供口述起草、只审稿、按意见修稿和安装核验四份独立 `.txt` 文件。首次安装用第 1 组的路径式请求，不要求目标会话已经识别技能。

## 安装到已有论文项目

保留克隆后的套件目录。目标论文项目目录需已存在；将下面两条命令中的路径换成实际绝对路径，按顺序执行。

先预览安装计划：

```bash
python3 /完整路径/codex-paper-review-writing/tools/install_project.py --project /你的论文项目 --dry-run
```

检查输出中的目标文件与 `conflicts`；无冲突后执行安装：

```bash
python3 /完整路径/codex-paper-review-writing/tools/install_project.py --project /你的论文项目
```

[安装器](tools/install_project.py) 会复制八个技能、共享规则、工作流、提示词、工具与记录模板，并向已有 `AGENTS.md` 追加带标记的工作流块。相同文件保持不变，已有 `research` 记录保留。发现不同的技能、规则或工具文件时，会在写入前报告冲突，供人工合并。

安装器检测文件差异，合并后仍需阅读项目规则，处理含义上的冲突。`AGENTS.override.md` 或更深目录规则也可能影响实际加载。

默认不复制虚构案例；学习时可以添加 `--include-examples`。开发验证记录保留在套件源目录。安装完成后，在目标项目配置 [材料路径](research/PROJECT.json)，打开或重开 Codex 会话，并按 [Prompt 16](PROMPTS.md#16-安装后的核验与试用) 分别核验文件完整性、客户端可见性与实际任务表现。已有足够记录的检查无需重复运行。

需要团队共享的规则、技能和工具，可以纳入目标项目的版本管理；论文、数据与密钥的跟踪规则由该项目决定。详细步骤见 [安装与验收指南](SKILL_GUIDE.md)。

## 研究记录与本地工具

| 入口 | 用途与边界 |
| --- | --- |
| [research](research) | 稿件与证据路径、主张、问题、来源、检查状态及作者风格模板。按任务需要使用。 |
| [tools/paper_gate.py](tools/paper_gate.py) | 检查记录完整性、严重未关闭问题、复查记录和文件版本变化；不判断科学结论是否成立。 |
| [extract_audit_items.py](.agents/skills/paper-evidence-audit/scripts/extract_audit_items.py) | 提取数字、统计标记与引用键候选，输出均保持 `unverified`，等待来源核查。 |
| [optional](optional) | 自定义审稿角色与 Stop hook 模板；需要在实际环境配置后才会执行。 |

多阶段流程与具体命令见 [RESEARCH_HARNESS.md](RESEARCH_HARNESS.md)。只处理一段文字时，使用对应技能和必要材料即可。

## 已经验证什么

截至 2026-10-19，仓库中的 [验证记录](VALIDATION.md) 记载了以下实际检查：

- **技能结构与配置：**八个技能通过结构校验；元数据、被引用的本地资源、可选 TOML 与 JSON 配置已核对。
- **本地工具：**20 项测试通过，包括 8 项候选提取器测试和 12 项项目工具测试。安装实测覆盖预检查不写入、保留已有规则与研究记录、重复安装无变化和文件冲突阻止写入。
- **隔离的虚构任务：**执行了口述起草、语法修改、来源改写、严苛审稿、实际修订、研究定位、任务路由和审计台账检查。输入、评价要求与实际输出分别保存在 [evals/TASKS.md](evals/TASKS.md)、[evals/RUBRIC.md](evals/RUBRIC.md) 和 [evals/outputs](evals/outputs)。

这些记录支持相应工具行为和给定案例的结果。它们不是有统计功效的对照实验，没有测量安装前后错误率差异，也不能代表任意真实论文的表现。Python 3.10 与 3.11 未在本次环境逐个实测。

原生 Codex CLI 技能发现、真实 CLI 任务、Skills UI 安装以及 hook 信任与生命周期执行，仍需在实际使用的客户端核验。结构校验和本地脚本测试不能替代这些集成检查。

本套件提供技能规则与工具，没有训练或微调模型，也没有内置付费查重或 AI 检测服务。可以对照用户提供的真实相似度报告处理匹配段落；没有实际检测与复测报告时，不推算检测分数变化。它不检测或移除水印，也不预测期刊录用。

## 可选：从 Git bundle 恢复

如果另行拿到了配套的 `codex-paper-project.bundle`，可以用它恢复离线项目快照：

```bash
git clone /你保存的路径/codex-paper-project.bundle codex-paper-review-writing
cd codex-paper-review-writing
```

恢复后按上面的项目使用说明继续，或通过安装器复制到已有论文项目。Bundle 内容对应生成快照时的版本；它是 GitHub 克隆之外的可选交付路径，不是使用本仓库的前置要求。
