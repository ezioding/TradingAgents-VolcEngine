#!/usr/bin/env python3
"""使用火山方舟运行 TradingAgents 测试"""

import os
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

print("=" * 70)
print("TradingAgents + 火山方舟 集成测试")
print("=" * 70)

# 设置 API Key
os.environ["VOLCENGINE_API_KEY"] = "ddfb0bcd-95d2-452b-a51b-1cdbad6c2e64"

# 创建自定义配置
config = DEFAULT_CONFIG.copy()
config["llm_provider"] = "volcengine"
config["deep_think_llm"] = "ark-code-latest"
config["quick_think_llm"] = "ark-code-latest"
config["max_debate_rounds"] = 1
config["max_risk_discuss_rounds"] = 1
config["output_language"] = "Chinese"
config["checkpoint_enabled"] = False

print(f"LLM Provider: {config['llm_provider']}")
print(f"Deep Think Model: {config['deep_think_llm']}")
print(f"Quick Think Model: {config['quick_think_llm']}")
print(f"Output Language: {config['output_language']}")
print()

try:
    print("正在初始化 TradingAgents 图谱...")
    ta = TradingAgentsGraph(debug=True, config=config)
    print("✅ 初始化成功！")
    print()

    print("正在运行股票分析 (NVDA, 2024-05-10)...")
    print("=" * 70)
    print()

    _, decision = ta.propagate("NVDA", "2024-05-10")

    print()
    print("=" * 70)
    print("✅ 分析完成！")
    print("=" * 70)
    print()
    print("最终交易决策:")
    print(decision)

except Exception as e:
    print(f"❌ 运行失败: {str(e)}")
    import traceback
    traceback.print_exc()
