import os
import asyncio
import sys
from dotenv import load_dotenv

# ==========================================
# 🟢 1. 环境配置加载
# ==========================================
env_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(env_path):
    load_dotenv(dotenv_path=env_path)

from gpt_researcher import GPTResearcher

# ===================================================================
# 🟢 2. 魔法时刻：【内存补丁】(Tavily + Nodriver)
# ===================================================================

# ---------------------------------------------------------
# 补丁 1：Tavily 侦察兵
# ---------------------------------------------------------
from gpt_researcher.retrievers.tavily.tavily_search import TavilySearch
original_tavily_init = TavilySearch.__init__ 

def wechat_tavily_init(self, query, headers=None, topic="general", query_domains=None, **kwargs):
    if "微信" in query or "公众号" in query:
        query_domains = ["mp.weixin.qq.com"]
        print("\n🕵️ [Tavily 侦察兵] 已限制只搜索微信公众号")
    original_tavily_init(self, query=query, headers=headers, topic=topic, query_domains=query_domains, **kwargs)

TavilySearch.__init__ = wechat_tavily_init

# ---------------------------------------------------------
# 补丁 2：Nodriver 互斥锁适配器 (绝对排队机制)
# ---------------------------------------------------------
# 🔑 定义全局互斥锁：确保同一时刻只有 1 个浏览器在运行
wechat_scrape_lock = asyncio.Lock()

class WeChatNodriverScraper:
    def __init__(self, link, session=None):
        self.link = link  
        self.session = session

    async def scrape_async(self):
        from gpt_researcher.scraper.browser.nodriver_scraper import NoDriverScraper
        
        # ⛔ 关键修改：所有并发任务在这里被“互斥锁”拦截，必须排队一个一个进
        async with wechat_scrape_lock:
            print(f"\n🔒 [获取通行证] 开始专注抓取 -> {self.link}")
            
            scraper = NoDriverScraper(url=self.link)
            try:
                text, image_urls, title = await scraper.scrape_async()
                
                # 抓取完成后，强制让程序（以及微信的防火墙）休息 3 秒，再放下一个任务进来
                print("⏳ [冷却中] 抓取完成，休息 3 秒防风控...")
                await asyncio.sleep(3)
                
                if text and len(text) > 100 and "zendriver package is required" not in text:
                    print(f"✅ [提取成功] 获取到《{title}》正文 {len(text)} 字！")
                    return text, image_urls, title
                else:
                    print("⚠️ [无效网页] 内容过短，已被微信屏蔽或为协议页面。")
                    return "", [], ""
            except Exception as e:
                print(f"❌ [抓取失败] {e}")
                return "", [], ""

# ---------------------------------------------------------
# 补丁 3：全局路由拦截
# ---------------------------------------------------------
from gpt_researcher.scraper.scraper import Scraper as CoreScraper
original_get_scraper = CoreScraper.get_scraper

def wechat_get_scraper(self, link):
    if "mp.weixin.qq.com" in link:
        return WeChatNodriverScraper
    return original_get_scraper(self, link)

CoreScraper.get_scraper = wechat_get_scraper

# ===================================================================
# 🟢 3. 端到端测试流程代码
# ===================================================================

async def run_wechat_research():
    # 我们换一个更有意思的话题测试
    query = "请总结近期微信公众号上关于【分析霍尔木兹海峡局势对中国A股市场的影响，重点关注石油、航运及化工板块。】的深度分析文章"
    report_type = "detailed_report"

    print("\n" + "="*50)
    print("🚀 启动【Tavily + Nodriver】单线防封锁流水线")
    print("="*50)

    try:
        # ⚠️ 关键修改：detailed_report 需要使用专门的 DetailedReport 类
        from backend.report_type.detailed_report.detailed_report import DetailedReport
        
        researcher = DetailedReport(
            query=query,
            report_type=report_type,
            report_source="web"
        )
        
        print("\n🔍 [阶段 1] 正在进行深度研究...")
        report = await researcher.run()

        print("\n🎉 测试成功！报告生成完毕！\n")
        
        file_name = "wechat_ultimate_report.md"
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(report)
        print(f"💾 完整报告已保存: {file_name}")

    except Exception as e:
        print(f"\n❌ 测试过程中发生错误: {e}")

if __name__ == "__main__":
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    try:
        asyncio.run(run_wechat_research())
    except SystemExit:
        pass
    except Exception as e:
        if "Executor shutdown" not in str(e) and "no close frame" not in str(e):
            pass