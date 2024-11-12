import json
from scrapegraphai.graphs import SmartScraperGraph

# 配置爬虫
graph_config = {
    "llm": {
        "model": "ollama/llama3.2",
        "temperature": 0.0,
        "format": "json",
    },
    "embeddings": {
        "model": "nomic-embed-text",
    },
    "verbose": True,
    "headless": False,
}

# 创建 SmartScraperGraph 实例
smart_scraper_graph = SmartScraperGraph(
    prompt="找出公司做什么的，公司名称和联系邮箱。",
    source="https://scrapegraphai.com/",
    config=graph_config
)

# 运行爬虫
result = smart_scraper_graph.run()
print(json.dumps(result, indent=4))
