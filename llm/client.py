from ollama import Client

from config import MODEL, OLLAMA_HOST


class LLMClient:

    def __init__(self):

        self.client = Client(host=OLLAMA_HOST)

        self.model = MODEL

    def generate(
        self,
        messages,
        schema=None,
        think=True,
    ):

        kwargs = {
            "model": self.model,
            "messages": messages,
            "think": think,
            "options": {
                "temperature": 0
            }
        }

        if schema is not None:
            kwargs["format"] = schema

        return self.client.chat(**kwargs)


llm = LLMClient()