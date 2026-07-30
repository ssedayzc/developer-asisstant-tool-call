import os

from dotenv import load_dotenv


load_dotenv()


HF_TOKEN = os.getenv("HF_TOKEN", "")

HF_MODEL = os.getenv(
    "HF_MODEL",
    "Qwen/Qwen3-4B-Instruct-2507",
)

HF_PROVIDER = os.getenv(
    "HF_PROVIDER",
    "auto",
)

GITHUB_TOKEN = os.getenv(
    "GITHUB_TOKEN",
    "",
)

PYPI_API = "https://pypi.org/pypi"
GITHUB_API = "https://api.github.com"
STACKEXCHANGE_API = "https://api.stackexchange.com/2.3"