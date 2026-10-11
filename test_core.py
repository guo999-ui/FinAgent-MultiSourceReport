import asyncio
from gpt_researcher import GPTResearcher
import os
from dotenv import load_dotenv

# 强行加载 .env 里的环境变量
load_dotenv()

async def main():
    print("🚀 1. 正在初始化 Researcher (测试大模型配置)...")
    query = "苹果公司的现任CEO是谁？"
    
    try:
        # 绕开网页，直接在本地运行核心框架
        researcher = GPTResearcher(query=query, report_type="research_report")
        print("✅ 2. 初始化成功！正在去网上搜索和抓取数据 (测试搜索引擎和爬虫bs4)...")
        
        # 测试搜索和抓取
        research_result = await researcher.conduct_research()
        print("✅ 3. 数据收集完毕！开始让大模型写报告...")
        
        # 测试大模型总结能力
        report = await researcher.write_report()
        print("🎉 4. 测试成功！整个链路完全打通。报告内容如下：\n")
        print("==================================================")
        print(report)
        print("==================================================")
        
    except Exception as e:
        print(f"❌ 发生致命错误: {e}")

if __name__ == "__main__":
    asyncio.run(main())