# CLAUDE.md

本文件为 AI 助手（Claude Code 等）提供本仓库的工作指南。开始任何改动前请通读一遍。
完整产品背景见 `docs/产品蓝图.md`，本文件是它的工程化速查版。

## 这是什么

**家庭学习门户（study-portal）**：把散落的学习资产收拢成一个"自家学习 App"，
全家任何设备打开网址即可使用。两个孩子各自独立：**Kenton（🦁 青蓝）** 与 **Eddey（🐯 珊瑚橙）**。

核心架构是**静态只读**：

```
展示层  GitHub Pages 静态站（孩子端只读打开）
数据层  仓库内 data/*.json（任务/软件/积分/播报索引）
生产层  爸爸电脑上的 Claude Code（改 JSON → git push → 约 1 分钟后网站自动更新）
```

> 关键认知：**孩子端永远只是打开看，所有数据更新都发生在爸爸电脑端。**
> 网站没有后端、没有账号系统、没有孩子端写入——不要尝试引入这些。

## 隐私红线（强制，最高优先级）

仓库是**公开**的（免费 GitHub Pages 要求），因此全网可见。任何改动都必须满足：

1. **只用英文小名 Kenton / Eddey**。绝不出现真实姓名、姓氏、学校、班级、地址、照片。
2. **敏感明细只存本地** `local-data/`（已被 `.gitignore` 屏蔽，永不上传）：
   错题原文、批改记录、成绩单等。网站上只放**匿名化统计**（如"小数除法正确率 62%→85%"）。
3. **永不提交任何账号、密码、密钥、token**。家长页也不放任何凭据。
4. 提交前自检：新增/修改内容是否泄露了上述任一项？有疑问就停下来问，不要先推送。

## 技术栈与约束

- **纯静态**：原生 HTML + CSS + 原生 JS（`fetch` + 模板字符串）。**无框架、无构建、无依赖、无 `package.json`、无 `node_modules`。**
- 不要引入打包器、npm 包、CSS 框架或 JS 框架。保持零依赖、可直接用浏览器打开。
- 所有页面共用 `assets/styles.css`（设计基线：**窄屏单列优先**、大按钮、糖果卡通风、孩子零打字）。
- 语言：界面与文档为中文；学习软件（`apps/`）内容可英文。

## 目录结构

| 路径 | 说明 |
|------|------|
| `index.html` | 首页：选择 Kenton / Eddey |
| `today.html` | 今日任务（读 `data/tasks.json`）+ 播报入口（读 `data/podcast.json`） |
| `apps.html` | 软件库（读 `data/apps.json`），支持 `?who=kenton\|eddey` 过滤 |
| `stars.html` | 星星榜（读 `data/scores.json`） |
| `parent.html` | 家长页：卷子下载 + 匿名化趋势（P1/P2 待接入，目前为占位） |
| `assets/styles.css` | 全站共享样式与 CSS 变量 |
| `data/*.json` | 唯一的"内容数据库"，日常更新主要改这里 |
| `apps/` | 学习软件（每个软件是一个自包含 HTML） |
| `papers/` | 卷子 PDF（家长页下载用） |
| `podcast/` | 每期播报页（一期一个 HTML） |
| `docs/产品蓝图.md` | 总施工图与分期计划（P0–P3） |
| `local-data/` | 🔒 本地敏感数据，**已 gitignore，永不上传**（仓库中不存在亦正常） |

## 页面如何读取数据

每个页面用 `fetch(..., { cache: "no-store" })` 读取对应 JSON 并渲染。约定：

- 孩子标识统一用 `who` 查询参数：`kenton` / `eddey`（如 `today.html?who=kenton`）。
- 两个孩子的主题色取自 CSS 变量 `--kenton` / `--eddey`，**内容与配色绝不混用**。
- 学科颜色/图标映射在 `apps.html` 的 `SUBJECT_META` 中（英语/语文/古诗/数学）。

## 数据文件格式（改动时严格遵守现有字段）

```jsonc
// data/tasks.json —— 今日任务（爸爸端每晚生成次日版）
{ "date": "2026-06-12",
  "kenton": [ { "type": "app", "title": "...", "link": "apps/xxx.html", "stars": 3 },
              { "type": "pdf", "title": "...", "link": "papers/xxx.pdf", "stars": 5 } ],
  "eddey":  [ ... ] }              // type 取 "app"(📖) 或 "pdf"(📄)

// data/apps.json —— 软件库索引（新软件入库时追加一条）
[ { "child": "kenton", "subject": "英语", "title": "...",
    "file": "apps/xxx.html", "added": "2026-06-11" } ]

// data/scores.json —— 积分（唯一可写来源：爸爸端汇总）
{ "updated": "2026-06-11", "kenton": { "week": 18, "total": 236 },
                           "eddey":  { "week": 21, "total": 214 } }

// data/podcast.json —— 播报索引（每期一条；today.html 取数组最后一条为"最新"）
[ { "date": "2026-06-11", "file": "podcast/2026-06-11.html", "topics": ["NBA", "太空"] } ]
```

约定：`child`/`who` 仅限 `kenton` 或 `eddey`；日期用 `YYYY-MM-DD`；
`link`/`file` 为相对仓库根的相对路径；JSON 必须合法（改完务必校验）。

## 常见任务做法（"更新门户"）

- **加今日任务** → 改 `data/tasks.json`（更新 `date` 与对应孩子数组）。
- **入库新软件** → 把 HTML 放进 `apps/`，在 `data/apps.json` 追加一条索引。
- **更新积分** → 改 `data/scores.json`（同时更新 `updated`）。
- **发布播报** → 在 `podcast/` 新建 `YYYY-MM-DD.html`，在 `data/podcast.json` 追加一条。
- **加卷子** → PDF 放进 `papers/`，在对应 `tasks.json` 用 `type:"pdf"` 链接到它。

新建软件/播报页时，复用现有页面的窄屏单列结构与 `assets/styles.css`，保持视觉一致。

## 验证

无构建、无测试框架。验证靠浏览器：

```bash
python3 -m http.server 8000   # 然后访问 http://localhost:8000/
```

改完自查清单：JSON 合法、相对路径正确、隐私红线无违反、窄屏（手机/平板竖屏）显示正常。

## Git 工作流

- 在指定特性分支开发并提交；除非用户明确要求，**不要创建 PR**。
- 提交信息用清晰的中文描述本次改了什么内容。
- 每一步开始前用一句中文说明意图（沿用蓝图里的协作习惯）。
- 任何一版改坏，靠 `git` 历史回退即可——这是该架构的安全网。
