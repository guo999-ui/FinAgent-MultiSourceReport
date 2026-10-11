# 多数据源智能研究代理

基于 LLM 的自主研究代理，融合 **Tavily 网络搜索**、**微信公众号** 和 **本地文档** 三大数据源，对任意主题进行深度研究并生成带引用的综合报告。

## 核心特性

- 🌐 **Tavily 搜索**：实时网络信息检索
- 💬 **微信公众号**：针对 `mp.weixin.qq.com` 链接的专项抓取与防封锁处理
- 📂 **本地文档**：支持本地文件作为研究知识源
- 🤖 **多智能体协作**：基于 LangGraph 的多角色分工，深度研究与质量校验
- 📝 **报告生成**：自动汇总多源信息，输出 Markdown / PDF / Word 格式报告
- 🖥️ **前端界面**：提供 Web 交互界面（Next.js）

## 快速开始

### 环境要求

- Python 3.11+
- Node.js 18+（使用前端界面时）

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置环境变量

复制 `.env.example` 为 `.env` 并填入你的 API Key：

```bash
cp .env.example .env
```

```env
OPENAI_API_KEY=your_openai_key
TAVILY_API_KEY=your_tavily_key
DOC_PATH=./my-docs
```

### 3. 运行

启动后端服务：

```bash
python main.py
```

启动前端界面（可选）：

```bash
cd frontend/nextjs
npm install
npm run dev
```

### Docker 部署

```bash
docker-compose up
```

## 项目结构

```
├── backend/            # 后端服务（FastAPI + WebSocket）
├── frontend/           # 前端界面（Next.js）
├── gpt_researcher/     # 核心研究引擎
├── multi_agents/       # 多智能体协作模块
├── outputs/            # 生成的报告输出目录
└── my-docs/            # 本地文档目录
```

## 多智能体协作

基于 [LangGraph](https://python.langchain.com/docs/langgraph) 构建的多智能体研究系统，通过专业化分工提升研究的深度与质量。灵感来自 [STORM](https://arxiv.org/abs/2402.14207) 论文，由一组 AI 代理协同完成从规划到发布的完整研究流程。

### 智能体角色

| 角色 | 职责 |
|------|------|
| 👤 **Human** | 人类在环，监督流程并提供反馈 |
| 📋 **Chief Editor** | 主编，统筹全局并协调各智能体 |
| 🔍 **Researcher** | 研究员，对各子主题进行深度研究并撰写初稿 |
| ✏️ **Editor** | 编辑，规划报告大纲与结构 |
| ✅ **Reviewer** | 审稿人，校验研究结果的正确性 |
| 🔧 **Revisor** | 修订者，根据审稿反馈修改内容 |
| 📖 **Writer** | 作者，汇总撰写最终报告 |
| 📤 **Publisher** | 发布者，将报告导出为多种格式 |

### 工作流程

1. **规划阶段**：Browser 浏览互联网收集初始信息，Editor 规划报告大纲
2. **研究阶段**：各子主题并行执行 Researcher → Reviewer → Revisor 的循环
3. **撰写阶段**：Writer 汇总所有研究成果，撰写包含引言、结论和引用的最终报告
4. **发布阶段**：Publisher 输出 Markdown / PDF / Word 等格式

### 运行多智能体

```bash
cd multi_agents
pip install -r requirements.txt
python main.py
```

通过编辑 `multi_agents/task.json` 自定义研究主题、模型、报告格式等参数。

## 声明

本项目基于 [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher) 二次开发，原始代码遵循 Apache License 2.0。
