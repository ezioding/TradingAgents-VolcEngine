# TradingAgents + 火山方舟

基于 TradingAgents 多智能体交易框架，集成火山方舟（VolcEngine）LLM 支持。

## 快速开始

### 前置要求

- Python 3.10+
- [uv](https://github.com/astral-sh/uv) 包管理器
- 火山方舟 API Key

### 安装与运行

```bash
# 1. Clone 仓库
git clone https://github.com/ezioding/TradingAgents-VolcEngine.git
cd TradingAgents-VolcEngine

# 2. 创建 .env 文件并添加火山方舟 API Key
echo "VOLCENGINE_API_KEY=你的_api_key" > .env

# 3. 创建虚拟环境并安装依赖
uv venv
source .venv/bin/activate
uv pip install -e .

# 4. 运行交互式 CLI
tradingagents
```

### 使用说明

运行 `tradingagents` 后，按提示选择：
1. 股票代码（如 `NVDA`、`AAPL`、`TSLA`）
2. 分析日期
3. 分析师团队
4. 研究深度
5. **LLM Provider 选择 "火山方舟 (VolcEngine)"**
6. 模型选择 `ark-code-latest`
7. 输出语言（推荐选择 "Chinese"）

### Python 代码调用

```python
import os
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

# 设置火山方舟 API Key（或在 .env 文件中配置）
os.environ["VOLCENGINE_API_KEY"] = "你的_api_key"

config = DEFAULT_CONFIG.copy()
config["llm_provider"] = "volcengine"
config["deep_think_llm"] = "ark-code-latest"
config["quick_think_llm"] = "ark-code-latest"
config["output_language"] = "Chinese"

ta = TradingAgentsGraph(debug=True, config=config)
_, decision = ta.propagate("NVDA", "2024-05-10")
print(decision)
```

## 项目来源

基于 [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) 二次开发，添加了火山方舟 LLM 提供商支持。
