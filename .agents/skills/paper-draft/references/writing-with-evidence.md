# 从已有实验写论文

## 先分清三种职责

| 职责 | 读取什么 | 给作者的结果 |
| --- | --- | --- |
| 期刊要求 | 确认目标刊、稿型和当前作者指南。查看该稿型的结构、字数、图表、补充材料及数据/代码声明。若给了本次决定信或评语，再对照其具体要求 | 记下适用条目、出处、查看日期和对应章节。分别标记“必须”“建议”“未核实”。给了多个候选期刊时分别记录。未定刊时按领域惯例起草，保留可迁移的大纲 |
| 写作指导 | 根据问题、材料和读者安排论证顺序，选择下表所需的编辑或教学方法。先读该体裁作者认可的样稿 | 确定每节要回答什么、展示哪项证据、怎样让下一节接得上。按已确认的目标稿型呈现。例如同刊的 Article 和 Brief Communication 可能要求不同的标题层级 |
| 证据与读者检查 | 按适用的评审标准检查贡献是否清楚，观察能否支撑推断，其他人能否核查结果。作者的实测数据、证明、文献原文决定科学陈述 | 把会改变判断的问题还给写作者修正。只有真实审稿意见才进入逐点回复。一次任务可顺序完成这三种职责；记录实际工作 |

## 实验完成后先提取什么

以研究问题为单位读已有数据说明、代码与配置、运行记录、逐例输出、图表源和原文。先找现有项目记录。短段落只取必要字段；整篇论文可用现有 research/claims.tsv 保存贡献、证据位置与范围。

1. **问题和预期。** 作者想检验什么？什么结果会削弱这一预期？区分事先定义的指标、事后发现和计划。已有假设与观察不符时保留这个发现。
2. **研究对象和观察单位。** 数据版本、取样、标签含义、时间与分组切分、排除项及原因、可见输入、独立单位、样本数和分母。目标若是回答正确率，只有检索相关性标签就只能回答排序问题。
3. **实际比较。** 对照与变体、改变的因素、相同或不同的预算、模型与工具版本、提示及重试、随机性、指标定义。把原定设计与实际运行分开。公式与代码不一致时追查生成表格的版本。
4. **结果和不确定性。** 提取主结果、负面或无定论结果、有依据的子组和敏感性检查；逐项记基准、方向、差值、单位、条件和可用的不确定性。按合适的独立单位复算，不从均值猜方差。
5. **可追溯的证据。** 为每个核心主张保留文件/版本、运行 ID 或日志、表行或图源，以及对应方法。外部文献保留页、节、表或定理并指出支持哪个分句。注明缺失、版本冲突或只读到摘要的位置。
6. **允许的推断。** 为主结果写一句有数据支持的观察，再写一句可能的解释。标出哪一种解释经对照检验。先决定这条结果回答哪个问题，再决定它进主文、附录还是作者备注。

可直接采用这一行工作底稿：研究问题 | 受测对象与单位 | 比较与指标 | 结果及不确定性 | 证据定位 | 可写主张 | 未解决问题。不要把工作表标签搬进论文。

实证研究用“观察到、支持、提示”等与设计匹配的动词。单次基准比较能支持该配置下的差异；主张某组件造成差异，需要能辨别该组件的对照。区间跨零可报告方向仍不确定。等效或非劣需要相应设计和界值。理论证明单独检查假设与推导，若结果偏离原假设，保留原假设和不符之处，将新问题标为探索性。

有目标期刊时，在安排段落前执行[同刊证据与表达学习](target-journal-papers.md)。将相应引文放到它所支持的论点，把观察到的术语及段落动作交给主写作者。

## 从材料到每一节

对整篇实证稿，先把主要图表与数字对齐，再起草方法、结果与讨论，回填引言，最后核摘要与标题。对已写到一半的稿，从现有断点继续。最终章节和排列依目标稿型。独立综述按问题与文献综合组织；理论论文按假设、命题和证明组织；系统论文区分实现与评估。仅按稿型和读者需要增设独立的 Related Work、Limitations 或 Conclusion。

| 位置 | 写进去什么 | 完成时怎样互查 |
| --- | --- | --- |
| 标题和摘要 | 对象及任务、关键做法、最主要发现及适用条件。有明确比较时保留比较对象和指标。按目标刊的摘要栏目和字数重排 | 摘要中的每一项贡献都能定位到正文，结论强度与结果一致 |
| 引言 | 从一个具体问题或有根据的观察开始，交代前人解决了什么、仍存的困难、研究问题、本文做法和贡献 | 对每条贡献指出哪项比较、证明或产物能兑现；“首次”需专门查新 |
| 相关工作 | 按研究问题、评测条件或技术分歧比较原始工作，说明局限在哪些条件下发生，落到本文解决的差异 | 逐条核对文献的实际任务、数据与结论。只支持半句就拆句 |
| 数据与方法 | 对象、来源、采样、切分、标签、算法和可用输入，说明为何这样设计，写出复现所需细节 | 表图中的方法和设置能回到实现；正文与附录对同一方法用同一名称 |
| 实验设置 | 研究问题对应的对照、基线、预算、指标、独立单位、重复策略、分析程序和选择模型的规则 | 识别混杂因素与信息泄漏；“同预算”要核对实际口径；只选过一次参数的事后分析如实说明 |
| 结果与图表 | 依次回答研究问题。给比较条件、主要数值、方向、幅度和重要不确定性。解释数字说明了哪项观测，明确关键的反向或无定论结果。图注给对象、单位、误差定义和图例 | 用表或图源校正文中数值，保留实际分母和有科学意义的差异；未做的消融不能解释机制 |
| 讨论和局限 | 先回答开头的问题，再解释相对已有工作增加了哪些认识。写出对读者有实际后果的替代解释、条件和限制。只有能区分两种解释的后续实验才值得展开 | 采用下方的异议处理表。直接影响核心结论的证据同步回到 Results、摘要和引言 |
| 结论与补充材料 | 用研究范围内最清楚的答案收束。按稿型放复现细节、附加分析、数据/代码声明及其他必需项目 | 重要反例在主文可见。没有对应结果的外推不进入结论，未运行的工作保持将来时 |

论证段写不顺时，可按“观点 → 证据 → 解释这项证据如何支持观点 → 按需承接下一段”组织（Rutgers 的 PIER 教法）。方法段按实际步骤写；单个结果常用两句即可。写第一版前读取适用的作者声音规则，保留术语和负面结果；去掉替读者设想反驳、重复免责、无依据的强化词。

## 遇到反例和不同解释时怎样写

| 看到什么 | 怎么处理 |
| --- | --- |
| 猜测审稿人也许会批评，提不出证据或影响 | 用作内部自查。若不会改变结果、解释或读者的使用决定，直接写研究发现 |
| 同一结果有两种合理机制 | 在 Results 写观测。Discussion 比较解释，各自给出来源或判断依据、已经排除了什么、哪项检验可以区分。对未检验的机制保持假设语气 |
| 发现子组反向或已有论文结果不同 | 本研究实测反向时，交代子组、样本量与分析属性；在 Results 报告影响总体判断的例外。对外部文献先核对任务、预算和度量，在 Discussion 解释可比性及剩余分歧 |
| 证据推翻主张、存在分母错误、基线预算足以混淆归因 | 回到来源，纠正数字或缩小/撤回主张，连同摘要、引言、图表、讨论一起更新。已有证据不能恢复原主张时，给作者一个最小判别实验。保留仍成立的实测贡献 |
| 收到真实审稿意见或右侧评分 | 取原稿、评语和原量表，定位到具体句子，核实依据再修改；给审稿人的回应放回复信。只有同一量表实际复评才能报告提分 |

## 何时用哪个技能或工具

先读当前可用技能入口和必需的附属文件。内置技能按同套件的 sibling 目录解析。外部技能可通过当前宿主提供的技能名、作者提供的本地路径或获准读取的上游入口使用。需要执行脚本时检查依赖、输入和实际输出。只读公开方法时，据实记为参考。外部技能缺失时使用表中本地路径完成能做的部分。一次只选能改变当前写作决策的工具。

| 信号 | 优先使用 | 给正文带回什么 |
| --- | --- | --- |
| 核心贡献和竞争解释尚未分清 | paper-positioning；实验设计或统计问题复杂时按需读 [Paper Review Atlas](https://github.com/PresleyRen/paper-review-atlas/blob/main/skills/paper-review-atlas/SKILL.md) 对应模块 | 可检验的陈述及辨别条件。确需新实验且作者授权时交 [Agent Research Atlas](https://github.com/PresleyRen/agent-research-atlas/blob/main/skills/agent-research-atlas/SKILL.md)；写作继续使用已完成结果 |
| 要写数字、表、差值或公平比较 | paper-evidence-audit，读原始输出，以本地 Python 和适用统计单位复算。提取脚本只定位。存在预算、标签或切分疑问时定向审查 | 证据支持的数字、比较范围和区间。只能核到汇总表时说明核到哪层 |
| 要写“已有研究发现”、比较或文献空白 | paper-evidence-audit + 原文；可用 [citation-management](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/citation-management/SKILL.md) 或 [Crossref](https://www.crossref.org/documentation/retrieve-metadata/rest-api/) 核 DOI、题名、版本 | 来源定位及它真正支持的那部分。元数据查询不验证论文里的结论 |
| 写完整综述或跨文献综合 | [ReviewCraft](https://github.com/PresleyRen/reviewcraft-skill/blob/main/SKILL.md)；已有[方法整合记录](https://github.com/PresleyRen/reviewcraft-skill/blob/main/references/skill-adapters.md)可复用。缺失时按主题、原文及适用条件综合。系统综述另核检索、筛选和纳入记录 | 来源覆盖、异同与证据边界。独立综述交其主导；实证论文的一段 Related Work 只借相关模块 |
| 需要作者语气、避免空话和防御性写作 | 起草前读 paper-voice 的适用原则。已配置 [ClearWeave](https://github.com/PresleyRen/clearweave-skill/blob/main/skills/clearweave/SKILL.md) 时先读其 references/preservation.md 与 [references/drafting.md](https://github.com/PresleyRen/clearweave-skill/blob/621c1584af2f248dec18ecb0cb16f947d67a04a0/skills/clearweave/references/drafting.md)，依目标语言加载对应 Humanizer。英语论文选其固定的英文来源，中文学术论文选反防御写作与学术规则，离线按上游回退 | 在第一版就用作者能接受的句子。修改后核对数值、主语、否定、条件和确定性；只改语法保持局部 |
| 需要另一种叙事结构或期刊风格 | 可选社区 [nature-writing / nature-polishing](https://github.com/Yuan1z0825/nature-skills)。分别用于结构和已有措辞；检查同级 nature-shared 与入口要求的资源。使用实投稿型的官方指南裁决 | 可逐句对照的写法；保留原有贡献和范围。依赖不齐时用本页章节指导和作者指南 |
| 需要重画图、选刊或执行返修 | [FigureFoundry](https://github.com/PresleyRen/figurefoundry-scientific-figures/blob/main/skills/figurefoundry/SKILL.md) 从数据绘图；[ScholarRoute](https://github.com/PresleyRen/scholar-route/blob/main/skills/scholar-route/SKILL.md) 核刊与稿型；paper-revision 处理决定信。只审稿才走 paper-redteam，来源重组可用 paper-rewrite | 源数据一致的图注、带出处的栏目要求或逐点修订。图表可直接用项目现有绘图工具；未指定期刊按稿型先起草 |

读取项目数据、公共文献、写草稿与本地复算按当前授权执行。保留原始记录。付费实验、向外上传未发表材料或投稿需要相应授权。把实际使用的来源位置、计算和未决问题记在作者备注或现有记录中，遵守仅正文的交付要求。若恢复一个跨章任务，先核稿件和证据版本，更新依赖同一主张的全部位置。

## 给不同任务选用的一手来源

- **稿型要求示例。** 用目标期刊相应稿型的页面确定最终章节；同刊不同稿型也能有不同规则。[Nature Methods, Content Types](https://www.nature.com/nmeth/content)
- **编辑论写作。** 结果交代证据和直接发现，讨论放更深入的解释与相关研究；新实测数据应在结果部分出现。[Nature Methods 编辑部，So you’re writing a paper](https://www.nature.com/articles/nmeth.4532)
- **先整理实验再动笔。** Ángel Borja 从作者、编辑经验建议先准备图表、写方法与结果，最后写摘要；作为可选起草顺序，用当前期刊指南确定刊出结构。[Elsevier 刊载的署名教程](https://www.elsevier.com/connect/11-steps-to-structuring-a-science-paper-editors-will-take-seriously)
- **教授与研究者的方法。** 把引言的每条贡献指向证据；用一系列有数据支撑的结果搭成中心论证；按句段、方法、结果、摘要的不同职责训练表达。[Simon Peyton Jones 讲义](https://simon.peytonjones.org/great-research-paper/) · [Mensh 与 Kording，PLOS Computational Biology](https://doi.org/10.1371/journal.pcbi.1005619) · [Kristin Sainani，Stanford](https://web.stanford.edu/~kcobb/courses/writing/)
- **章节教程。** MIT 的两份写作课适合判断哪些内容写成结果、哪些讨论比较和局限。Rutgers 的段落模板可用于整合文献。[MIT Results](https://mitcommlab.mit.edu/be/commkit/journal-article-results/) · [MIT Discussion](https://mitcommlab.mit.edu/be/commkit/journal-article-discussion/) · [Rutgers 文献综述教程](https://openpub.libraries.rutgers.edu/irphabcd/chapter/chapter-5-literature-reviews/)
- **机器学习报告与评审。** 按适用项核数据划分、评测单位、基线、独立测试与主张范围。正式投稿时查当年当刊/会议的具体版本，既有年份的评审指南可作阅读角度。[Nature 机器学习报告清单](https://www.nature.com/documents/ML-reporting-summary.pdf) · [NeurIPS 论文清单](https://neurips.cc/public/guides/PaperChecklist) · [NeurIPS 2025 评审指南](https://neurips.cc/Conferences/2025/ReviewerGuidelines)
