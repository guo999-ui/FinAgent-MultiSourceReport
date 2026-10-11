import requests

response = requests.post(
    "http://localhost:8000/api/deep_research",
    json={
        "query": "测试中文查询",
        "report_source": "web",
        "research_mode": "hybrid"
    }
)

print("状态码:", response.status_code)
result = response.json()
print("状态:", result.get("status"))
print("消息:", result.get("message"))
