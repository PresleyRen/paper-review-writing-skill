# 独立安装与工具复测

日期：2026-10-19。使用隔离的虚构论文项目，没有修改真实论文。

## 1. 独立执行者的原版本复测

工作根目录：`/tmp/paper-install-independent-8srmdr6t`。
源码副本：`suite-copy`；安装目标：`existing-project`。

执行者从新的上下文读取安装器及测试，没有读取原 VALIDATION.md。提取器测试在脚本目录创建临时文件，因此两套测试均在 /tmp 的相同源码副本执行，保持原项目只读。

实际命令（在源码副本运行）：

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B tools/test_paper_tools.py -v
PYTHONDONTWRITEBYTECODE=1 python3 -B .agents/skills/paper-evidence-audit/scripts/test_extract_audit_items.py -v
```

结果：12项项目工具测试和8项提取器测试全部通过，退出码均为0。运行版本为 Python 3.12.14。

目标预置原 AGENTS.md、六个同名研究记录、额外笔记和已有稿件，共九个文件。使用实际安装器 CLI：

- dry-run：计划复制42个文件；目标文件集合和所有哈希保持不变，实际写入0。
- 首次安装：复制42个文件；安装后51个文件；八个非 AGENTS 原文件哈希不变，AGENTS 原文完整保留并追加一次工作流块。
- 再次安装：copy为空、merge_agents为false、无冲突；51个文件哈希不变。
- 八个技能均有 SKILL.md、agents/openai.yaml 和 implicit=true。
- 默认未复制 examples，未创建或启用目标 .codex 配置。

此阶段在新增指南之前运行，所以不把上述数字当作新版默认安装的固定文件数。

## 2. 更新后的定向核验

目标：`/tmp/paper-guide-install-tmcwhwoa`。预置自己的 AGENTS.md 和 research/state.json。

修正并新增文档后实际运行：

- 当前八个技能均通过 Skill Creator 的 quick_validate.py；元数据中的隐式调用设置与对应 default_prompt 核对通过。
- 当前 tools/test_paper_tools.py 的12项测试再次通过。
- 当前安装器 dry-run 保持目标0写入。
- 当前安装器首次复制49个文件；新增 SKILL_GUIDE.md、prompts/verify_installation.txt 与源文件逐字节一致。
- 原 AGENTS 内容和 state.json 保留。
- 再次安装没有新复制或 AGENTS 修改，目标文件哈希保持不变。
- git diff --check 通过。

两次安装的文件数不同，是因为套件版本与目标预置文件数量不同。判断依据是实际复制清单、保留内容和哈希，并非固定数量。

## 3. 环境边界

`command -v codex` 无输出、退出码1，当前 PATH 中没有可用 Codex CLI。本轮没有执行原生 /skills、真实 CLI 模型任务或 hook 生命周期。项目指南与核验 prompt 要求在目标客户端分别确认这些能力。

本地脚本测试不判断科学有效性、AI 检测指标或投稿结果。此前独立写作、审稿和修订的行为输出另见 VALIDATION.md；本轮新增的审计台账任务有单独报告。
