---
name: paper-evidence-audit
description: "Audit academic manuscript claims, numbers, figures, and citations against supplied evidence. 用于数字单位核查、引用核验、终稿降维核查和投稿前事实检查。Use for a requested evidence audit or a concrete contradiction. Keep contradiction checks local; do not launch a full audit for ordinary language editing."
---

# Paper Evidence Audit

核查论文里的主张是否得到现有材料支持，把确认的问题变成具体修改。
按用户要求用中文讨论核查结果，保留英文论文的写作语言。

## 确定本次范围

1. 明确待查文件、论文版本和核查对象。完整投稿前核查覆盖全文；单个矛盾只追查关联主张及其来源。
2. 读取项目已有的 ACADEMIC_WRITING.md（如果存在），并遵守适用的项目指令。缺少该文件不阻塞本技能独立运行。
3. 列出实际可用的记录：实验原始输出、分析脚本、配置、表格源文件、图源和文献原文。区分已读取、仅提供摘要、不可访问。
4. 读取 references/audit_protocol.md，按与当前任务有关的部分执行。不要因本技能存在而重新审查每次语言润色。

## 提取候选核查项

材料较多时，运行随附脚本建立索引。在项目根目录调用：

    python3 .agents/skills/paper-evidence-audit/scripts/extract_audit_items.py \
      paper/main.tex results/summary.csv \
      --output reports/audit_candidates.tsv

使用 Python 3.10 或更高版本，无第三方依赖。
脚本只接收本地 UTF-8 的 .md、.txt、.tex、.csv、.tsv、.json 文件。
默认拒绝覆盖已有输出；有意更新报告时才使用 --overwrite。
无论是否使用该选项，都拒绝把输出写到任一输入或其文件别名。

TSV 保留 source_path、line、column、context、raw_token、kind、status。
所有候选项初始且固定为 unverified；同一数字在不同位置分别保留。
context 是单行片段，行列编号从 1 开始。核查前回到完整原文，避免漏掉片段之外的条件。

把脚本输出当作定位索引。它不会读取 PDF、图像、扫描件或手写数学，不会执行公式，
也不会判断数字、引用键、统计结论或图表是否正确。
CSV、JSON 和 TeX 按文本扫描，不进行完整语法解析；复杂公式、多行引用、表格结构可能漏检。
需要这些材料时，使用相应阅读工具并记录实际读取范围。

## 对照证据

- 主张：明确研究对象、改变的因素、比较基线、成立条件、证据位置和论证强度。
- 数字：核对数值、符号、单位、分母、统计口径、样本筛选、模型版本、任务划分和舍入。
- 改善幅度：区分百分点与相对百分比，写出计算基准；基准为零时不要计算相对变化。
- 证据状态：区分提出、计划、实现、测量、推导和限定范围的已核查。模拟属于实验条件；未经检验的机制解释另记为假设。写入项目台账时遵循 RESEARCH_HARNESS.md 的 evidence_status 枚举，按 references/audit_protocol.md 区分候选状态、核查结果与台账状态。
- 图表：核对表格单元格、图源、坐标、误差条、图例、注释与正文指向。
- 引用：解析引用键到实际来源，核查被引用材料是否支持附近的具体主张。找到键或 DOI 不等于读过文献。
- LLM/Agent：核对模型、提示、工具、检索材料、重试、预算、评测器和种子。把结果归到实际受测配置。
- 因果与泛化：实验比较支持什么就写什么；消融、相关关系或单个案例不能自动推出机制因果或普遍适用。

对于本项目的实验数值和性能结论，未经原始记录核查，只能报告内部一致性或来源缺口。
正文、表格和模型回复互相一致，不能作为独立验证。不擅自启动新实验，不修改原始证据来让核查通过。
如任务已授权检索引用原文，可另用检索工具核对来源；本地提取脚本始终不联网。

## 交付与修订

给出范围、实际读取的证据和具体发现。每条发现包含：

    位置 | 主张 | 证据位置 | 核查状态 | 问题 | 建议修改或缺少的材料

使用 supported、internal_consistency_only、contradicted、missing_source、
needs_interpretation 标记人工核查结果；保留原始候选 TSV 的 unverified 状态。
只有实际完成相应比对才能写 supported，并说明支持范围。

用户要求修订时，完成有证据的修改；缺证据的部分单独列出具体缺口。
在投稿前核查发现已知错误时，明确标记该错误；不要把“未发现矛盾”写成“论文已证实正确”。
保持论文正文面向读者，把核查说明放进核查报告。
不把每个可选实验写成正文局限，不隐藏影响结论的负面结果。

## 本地自测

    python3 .agents/skills/paper-evidence-audit/scripts/test_extract_audit_items.py

测试覆盖候选提取和输入保护；不验证任何真实论文的科学结论。
