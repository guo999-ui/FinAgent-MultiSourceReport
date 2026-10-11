import requests
import time

print("📡 正在发送请求到深度研究API...")
print("=" * 60)


try:
    start_time = time.time()
    
    # 使用POST请求调用深度研究API
    response = requests.post(
        "http://localhost:8000/api/deep_research",
        json={
            "query": "分析霍尔木兹海峡局势对中国A股市场的影响",
            "research_mode": "hybrid"  # 可选：original（默认）、wechat、hybrid
        },
        timeout=3000  # 50分钟超时
    )

    elapsed_time = time.time() - start_time
    print(f"✅ 请求成功，耗时: {elapsed_time:.1f} 秒")
    print("-" * 60)

    result = response.json()
    
    print(f"状态: {result.get('status')}")
    print(f"消息: {result.get('message')}")
    print(f"大模型: {result.get('llm_model')}")
    print(f"Markdown文件: {result.get('md_file_path')}")
    print(f"Word文件: {result.get('docx_file_path')}")
    
    if result.get('report_content'):
        print("\n📄 报告内容预览（前100字）:")
        print("-" * 60)
        print(result['report_content'])
        print("\n" + "=" * 60)
        print("💡 完整报告已保存到文件，可通过md_file_path查看")

except requests.exceptions.Timeout:
    elapsed_time = time.time() - start_time
    print(f"❌ 请求超时！已等待 {elapsed_time:.1f} 秒")
    print("建议: 深度研究需要较长时间，可以增加timeout参数")
except requests.exceptions.ConnectionError:
    print("❌ 连接失败！请确保服务器已启动并运行在 http://localhost:8000")
except Exception as e:
    print(f"❌ 请求出错: {str(e)}")
