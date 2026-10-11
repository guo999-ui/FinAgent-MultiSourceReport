import requests
import json

# 1. 门牌号：指向你 main.py 启动的服务地址
URL = "http://localhost:8000/api/do_research"

# 2. 菜单：你想让 AI 调研的内容
data = {
    "task": "2024年新能源汽车电池技术突破",
    "report_type": "research_report" # 确保是这个类型以触发微信模式
}

print("📡 正在发送请求到后端，请观察【终端 A】的日志输出...")

try:
    # 发送 POST 请求
    response = requests.post(URL, json=data, timeout=300)
    
    if response.status_code == 200:
        result = response.json()
        print("\n✅ 调研成功！报告预览：\n")
        print(result["report_content"][:500] + "...") # 只打印前500字
    else:
        print(f"❌ 请求失败，状态码：{response.status_code}")
        print(response.text)

except Exception as e:
    print(f"❌ 无法连接到后端，请确保 main.py 正在运行！错误: {e}")