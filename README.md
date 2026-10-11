# 多数据源智能研究代理

基于 LLM 的自主研究代理，融合 **Tavily 网络搜索**、**微信公众号** 和 **本地文档** 三大数据源，对任意主题进行深度研究并生成带引用的综合报告。

## 核心特性

- 🌐 **Tavily 搜索**：实时网络信息检索
- 💬 **微信公众号**：针对 `mp.weixin.qq.com` 链接的专项抓取与防封锁处理
- 📂 **本地文档**：支持本地文件作为研究知识源
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

## 声明

本项目基于 [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher) 二次开发，原始代码遵循 Apache License 2.0。
