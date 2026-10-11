import asyncio
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# 加载 .env 环境变量
load_dotenv()

async def main():
    print("🚀 1. 正在读取环境变量...")
    print(f"URL: {os.getenv('OPENAI_BASE_URL')}")
    print(f"LLM: {os.getenv('FAST_LLM')}")
    
    # 提取模型名称 (去掉 openai: 前缀)
    model_name = os.getenv('FAST_LLM', 'openai:qwen-plus').replace('openai:', '')
    
    print(f"\n🚀 2. 正在初始化模型 [{model_name}] ...")
    llm = ChatOpenAI(model=model_name, max_retries=0) # max_retries=0 强制它报错，不许无限重试！
    
    print("🚀 3. 正在向阿里云发送请求 (如果卡在这里说明网不通或Key有问题)...")
    try:
        response = await llm.ainvoke("你好，请做个简短的自我介绍。")
        print("\n🎉 4. 测试成功！收到回复：")
        print(response.content)
    except Exception as e:
        print("\n❌ 发生错误！真相大白：")
        print(e)

if __name__ == "__main__":
    asyncio.run(main())