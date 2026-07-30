from types import SimpleNamespace
from typing import Any

from huggingface_hub import InferenceClient

from config import HF_MODEL, HF_PROVIDER, HF_TOKEN


class LLMClient:
    """
    Hugging Face Inference Providers üzerinden sohbet tamamlama
    ve structured output üretir.

    Dönen veri yapısı, eski Ollama istemcisiyle uyumludur:

        response.message.content
        response.message.thinking
    """

    def __init__(self) -> None:
        client_kwargs: dict[str, Any] = {
            "provider": HF_PROVIDER,
        }

        if HF_TOKEN:
            client_kwargs["api_key"] = HF_TOKEN

        self.client = InferenceClient(**client_kwargs)
        self.model = HF_MODEL

    @staticmethod
    def _create_response(
        content: str,
        thinking: str = "",
    ) -> SimpleNamespace:
        return SimpleNamespace(
            message=SimpleNamespace(
                content=content,
                thinking=thinking,
            )
        )

    def generate(
        self,
        messages: list[dict[str, str]],
        schema: dict[str, Any] | None = None,
        think: bool = True,
    ) -> SimpleNamespace:
        """
        Modele mesaj gönderir.

        `think` parametresi, mevcut Planner ve Responder kodlarıyla
        geriye dönük uyumluluk için korunmuştur. Hugging Face üzerinde
        kullanılan instruct model ayrı bir thinking alanı döndürmez.
        """

        request_kwargs: dict[str, Any] = {
            "model": self.model,
            "messages": messages,
            "temperature": 0.0,
            "max_tokens": 2048,
        }

        if schema is not None:
            request_kwargs["response_format"] = {
                "type": "json_schema",
                "json_schema": {
                    "name": "tool_plan",
                    "schema": schema,
                    "strict": True,
                },
            }

        try:
            response = self.client.chat_completion(
                **request_kwargs
            )
        except Exception as exc:
            raise RuntimeError(
                "Hugging Face LLM çağrısı başarısız oldu. "
                "HF_TOKEN, HF_MODEL ve Inference Provider "
                f"ayarlarını kontrol edin. Hata: {exc}"
            ) from exc

        content = response.choices[0].message.content

        if content is None:
            content = ""

        return self._create_response(
            content=content,
            thinking="",
        )


llm = LLMClient()