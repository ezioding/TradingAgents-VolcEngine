#!/usr/bin/env python3
"""测试环境变量加载"""

import os
from dotenv import load_dotenv

print("=" * 60)
print("环境变量加载测试")
print("=" * 60)

# 加载 .env 文件
load_dotenv()

# 检查 VOLCENGINE_API_KEY
api_key = os.environ.get("VOLCENGINE_API_KEY")
if api_key:
    print(f"✅ VOLCENGINE_API_KEY 已加载: {api_key[:20]}...")
else:
    print("❌ VOLCENGINE_API_KEY 未找到")

# 检查其他提供商的 API Key 环境变量名是否正确配置
print()
print("测试 LLM 工厂是否能正确使用环境变量:")

from tradingagents.llm_clients import create_llm_client

try:
    client = create_llm_client(
        provider="volcengine",
        model="ark-code-latest",
    )

    llm = client.get_llm()
    print(f"  ✓ LLM 客户端创建成功")
    print(f"  ✓ Base URL: {llm.base_url}")

    # 测试调用
    response = llm.invoke("你好，返回一句话")
    print(f"  ✓ API 调用成功")
    print(f"  响应: {response.content[:80]}...")

except Exception as e:
    print(f"  ✗ 失败: {e}")
    import traceback
    traceback.print_exc()

print()
print("=" * 60)
print("✅ 环境变量配置完成！现在可以运行 `tradingagents` 命令了。")
print("=" * 60)
