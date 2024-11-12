import json
from scrapegraphai.graphs import SmartScraperGraph
from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings

embedder_model_instance = HuggingFaceInferenceAPIEmbeddings(
    api_key="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",
    model_name="sentence-transformers/all-MiniLM-l6-v2"
)

# 配置爬虫
graph_config = {
    "llm": {
        "model": "anthropic/claude-3-5-sonnet-20240620",  # 或使用其他 Groq 模型
        "api_key": "sk-lWSqoEVUO2wJPnMQzm4Xdb1I6wWRzjdsPROnFUPRTvxC53B3",  # 替换为您的 Groq API key
        "temperature": 0
    },
    "embeddings": {
        "model_instance": embedder_model_instance,  # Groq 不支持 embedding 模型，这里使用 Ollama
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
