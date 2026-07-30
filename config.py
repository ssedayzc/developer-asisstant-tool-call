import os

from dotenv import load_dotenv


load_dotenv()


MODEL = os.getenv(
    "MODEL",
    "qwen3:4b",
)

OLLAMA_HOST = os.getenv(
    "OLLAMA_HOST",
    "http://localhost:11434",
)

GITHUB_TOKEN = os.getenv(
    "GITHUB_TOKEN",
    "",
)

PYPI_API = "https://pypi.org/pypi"

GITHUB_API = "https://api.github.com"

STACKEXCHANGE_API = "https://api.stackexchange.com/2.3"