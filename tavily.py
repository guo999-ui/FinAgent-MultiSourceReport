#!/usr/bin/env python3
"""
微信公众号研究测试脚本（使用核心代码中的微信模式）
"""
import os
import asyncio
import sys
from dotenv import load_dotenv

# 加载环境配置
env_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(env_path):
    load_dotenv(dotenv_path=env_path)

from gpt_researcher import GPTResearcher

async def run_wechat_research():
    # 微信模式查询（会自动触发 .env 中配置的 RESEARCH_MODE）
    query = "请总结一下近期微信公众号上关于【AI大模型应用落地案例】的深度分析文章"
    report_type = "research_report"

    print("\n" + "="*50)
    print("🚀 启动【微信模式】研究流程")
    print("📋 当前模式: " + os.getenv("RESEARCH_MODE", "original"))
    print("="*50)

    try:
        researcher = GPTResearcher(query=query, report_type=report_type)
        
        print("\n🔍 [阶段 1] 正在搜集资料...")
        await researcher.conduct_research()

        print("\n✍️ [阶段 2] 正在撰写报告...")
        report = await researcher.write_report()

        print("\n🎉 测试成功！报告生成完毕！")
        
        # 保存报告
        file_name = "wechat_report.md"
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(report)
        print(f"💾 报告已保存至: {file_name}")

    except Exception as e:
        print(f"\n❌ 测试失败: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(run_wechat_research())
