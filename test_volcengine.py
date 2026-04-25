#!/usr/bin/env python3
"""测试火山方舟 LLM 连接"""

import os
from langchain_openai import ChatOpenAI

# 火山方舟配置
API_KEY = "ddfb0bcd-95d2-452b-a51b-1cdbad6c2e64"
BASE_URL = "https://ark.cn-beijing.volces.com/api/coding/v3"
MODEL = "ark-code-latest"

print("=" * 60)
print("火山方舟 LLM 连接测试")
print("=" * 60)
print(f"Model: {MODEL}")
print(f"Base URL: {BASE_URL}")
print()

llm = ChatOpenAI(
    model=MODEL,
    base_url=BASE_URL,
    api_key=API_KEY,
    temperature=0.3,
)

try:
    print("正在发送测试请求...")
    response = llm.invoke("你好，请用中文简单介绍一下你自己，不超过50字")
    print()
    print("✅ 连接成功！")
    print(f"响应: {response.content}")
    print()
    print("=" * 60)
    print("测试通过！火山方舟配置正确。")
except Exception as e:
    print(f"❌ 连接失败: {str(e)}")
    import traceback
    traceback.print_exc()
