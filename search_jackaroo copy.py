from scrapegraphai.graphs import DepthSearchGraph
from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings
import json
import signal
import sys

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
        "model_instance": embedder_model_instance,
    },
    "verbose": True,
    "headless": True,
    
    # 限制爬取范围
    "depth": 2,                     # 减小搜索深度
    "max_pages": 5,                 # 限制页面数量
    "max_links_per_page": 10,       # 限制每页链接数
    
    # 过滤规则
    "only_inside_links": True,      # 只爬取站内链接
    "exclude_patterns": [           # 排除特定类型的URL
        "sitemap.xml",
        "robots.txt",
        "/api/",
        "/static/",
        "/assets/"
    ],
    
    # 超时设置
    "timeout": 10,                  # 减少单页超时
    "wait_time": 2,                 # 减少等待时间
    "retry_times": 1,               # 减少重试次数
    "total_timeout": 300,           # 添加总体超时限制（秒）
    
    # 添加错误处理
    "skip_on_error": True,          # 遇到错误时跳过继续执行
    "max_retries_per_page": 1,      # 每页最大重试次数
    "chunk_size": 1000
}

# 创建 DepthSearchGraph 实例
search_graph = DepthSearchGraph(
    prompt="分析 Jackaroo 游戏的下载量、收入、排名等数据，重点关注最近一个月的变化趋势。请提供具体的数据和分析。",
    source="https://app.diandian.com/",  # 设置起始URL
    config=graph_config
)

# 定义超时处理函数
def timeout_handler(signum, frame):
    print("爬虫执行超时，正在获取已收集的数据...")
    if 'search_graph' in globals():
        try:
            partial_result = search_graph.get_current_state()
            print(json.dumps(partial_result, indent=4, ensure_ascii=False))
        except:
            print("无法获取部分结果")
    sys.exit(1)

# 设置总体超时时间（例如5分钟）
signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(300)  # 300秒后触发超时

try:
    # 运行爬虫
    result = search_graph.run()
    print(json.dumps(result, indent=4, ensure_ascii=False))
except Exception as e:
    print(f"爬虫执行出错: {str(e)}")
    # 尝试获取部分结果
    try:
        partial_result = search_graph.get_current_state()
        print("已获取的部分数据:")
        print(json.dumps(partial_result, indent=4, ensure_ascii=False))
    except:
        print("无法获取部分结果")
finally:
    # 取消超时警报
    signal.alarm(0)