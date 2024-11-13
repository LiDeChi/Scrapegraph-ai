import json
from scrapegraphai.graphs import SmartScraperGraph
from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings

# 创建 embeddings 实例
embedder_model_instance = HuggingFaceInferenceAPIEmbeddings(
    api_key="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",
    model_name="sentence-transformers/all-MiniLM-l6-v2"
)

# 配置爬虫
graph_config = {
    "llm": {
        "api_key": "sk-uIfCBXZD3IReex6jrZM0qVQ8V26wWlECLxsfRS3NLERwvpsG",
        "model": "oneapi/claude-3-sonnet-20240229",
        "base_url": "https://chat.cloudapi.vip/v1",
        "temperature": 0
    },
    "embeddings": {
        "model_instance": embedder_model_instance
    },
    "verbose": True,
    "headless": True
}

# 创建 SmartScraperGraph 实例
smart_scraper_graph = SmartScraperGraph(
    prompt="告诉我今天的游戏排名",
    source="https://appmagic.rocks/top-charts/apps",
    config=graph_config
)

# 运行爬虫
result = smart_scraper_graph.run()
print(json.dumps(result, indent=4))
