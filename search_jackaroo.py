from scrapegraphai.graphs import ScriptCreatorMultiGraph
from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings
import json

# 创建 embeddings 实例
embedder_model_instance = HuggingFaceInferenceAPIEmbeddings(
    api_key="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",
    model_name="sentence-transformers/all-MiniLM-l6-v2"
)

# 配置爬虫
graph_config = {
    "llm": {
        "api_key": "sk-uIfCBXZD3IReex6jrZM0qVQ8V26wWlECLxsfRS3NLERwvpsG",
        "model": "oneapi/claude-3-5-sonnet-20241022",
        "base_url": "https://chat.cloudapi.vip/v1",
        "temperature": 0
    },
    "embeddings": {
        "model_instance": embedder_model_instance
    },
    "library": "beautifulsoup"
}

# 定义要爬取的URL列表
urls = [
    "https://www.qimai.cn/",
    "https://www.data.ai/",
    "https://app.diandian.com/"
]

# 创建 ScriptCreatorMultiGraph 实例
script_creator_graph = ScriptCreatorMultiGraph(
    prompt="分析 Jackaroo 游戏的下载量、收入、排名等数据，重点关注最近一个月的变化趋势。请提供具体的数据和分析。",
    source=urls,
    config=graph_config
)

# 运行爬虫
result = script_creator_graph.run()
print(json.dumps(result, indent=4, ensure_ascii=False))