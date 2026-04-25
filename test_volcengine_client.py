#!/usr/bin/env python3
"""测试火山方舟 LLM 客户端集成"""

import os

# 设置 API Key
os.environ["VOLCENGINE_API_KEY"] = "ddfb0bcd-95d2-452b-a51b-1cdbad6c2e64"

print("=" * 60)
print("TradingAgents 火山方舟客户端集成测试")
print("=" * 60)
print()

# 测试 1: 直接使用工厂创建客户端
print("测试 1: 通过 LLM 工厂创建 VolcEngine 客户端")
try:
    from tradingagents.llm_clients import create_llm_client

    client = create_llm_client(
        provider="volcengine",
        model="ark-code-latest",
    )

    print(f"  ✓ 客户端类型: {type(client).__name__}")
    print(f"  ✓ Provider: {getattr(client, 'provider', 'N/A')}")
    print(f"  ✓ Model: {client.model}")
    print("  ✓ 客户端创建成功")
except Exception as e:
    print(f"  ✗ 失败: {e}")
    import traceback
    traceback.print_exc()
    exit(1)

print()

# 测试 2: 获取 LLM 实例并调用
print("测试 2: 调用 LLM 实例")
try:
    llm = client.get_llm()
    print(f"  ✓ LLM 类型: {type(llm).__name__}")

    response = llm.invoke("请用一句话介绍TradingAgents")
    print(f"  ✓ LLM 调用成功")
    print(f"  响应: {response.content[:100]}...")
except Exception as e:
    print(f"  ✗ 失败: {e}")
    import traceback
    traceback.print_exc()
    exit(1)

print()

# 测试 3: 验证模型
print("测试 3: 模型验证")
try:
    is_valid = client.validate_model()
    print(f"  ✓ 模型验证结果: {is_valid}")
    client.warn_if_unknown_model()
    print("  ✓ 警告检查完成")
except Exception as e:
    print(f"  ✗ 失败: {e}")

print()

# 测试 4: 检查 CLI 选项注册
print("测试 4: CLI 提供商选项注册")
try:
    from cli.utils import select_llm_provider
    from tradingagents.llm_clients.model_catalog import MODEL_OPTIONS, get_model_options

    # 检查 volcengine 是否在模型目录中
    if "volcengine" in MODEL_OPTIONS:
        print("  ✓ volcengine 已注册到模型目录")
        quick_models = get_model_options("volcengine", "quick")
        deep_models = get_model_options("volcengine", "deep")
        print(f"  ✓ Quick 模型数量: {len(quick_models)}")
        print(f"  ✓ Deep 模型数量: {len(deep_models)}")
        for name, mid in quick_models:
            print(f"    - {name}: {mid}")
    else:
        print("  ✗ volcengine 未在模型目录中找到")
except Exception as e:
    print(f"  ✗ 失败: {e}")

print()
print("=" * 60)
print("✅ 所有测试通过！火山方舟 LLM 集成配置完成。")
print("=" * 60)
print()
print("使用方法:")
print("  1. CLI: 运行 `tradingagents`，选择 '火山方舟 (VolcEngine)'")
print("  2. Python:")
print("     config['llm_provider'] = 'volcengine'")
print("     config['deep_think_llm'] = 'ark-code-latest'")
print("     config['quick_think_llm'] = 'ark-code-latest'")
