import os
from dotenv import load_dotenv
from pathlib import Path

# 获取项目根目录
BASE_DIR = Path(__file__).resolve().parent.parent
env_path = BASE_DIR / '.env'

# 加载环境变量
load_dotenv(env_path)

# API 配置
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
ANTHROPIC_API_BASE = "https://chat.cloudapi.vip/v1"  # 添加自定义 API 基础URL

if not ANTHROPIC_API_KEY:
    raise ValueError(f"ANTHROPIC_API_KEY not found in environment variables. Please check {env_path}")

# 基础配置
BASE_CONFIG = {
    "llm": {
        "model": "anthropic/claude-3-sonnet-20240229",
        "api_key": ANTHROPIC_API_KEY,
        "api_base": ANTHROPIC_API_BASE,  # 添加自定义 API 端点
        "temperature": 0
    },
    "verbose": True,
    "headless": True
} 