import requests
import time
import os

from dotenv import load_dotenv

load_dotenv()

OLLAMA_HOST = os.getenv("OLLAMA_HOST")
MODEL = os.getenv("MODEL")


class LLMClient:

    def chat(self, prompt, system="", temp=0.5):

        url = f"{OLLAMA_HOST}/api/chat"

        body = {
            "model": MODEL,
            "messages": [
                {
                    "role": "system",
                    "content": system
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "stream": False
        }

        inicio = time.time()

        response = requests.post(
            url,
            json=body
        )

        print(response.text)

        data = response.json()

        fim = time.time()

        resposta = data["message"]["content"]

        return {
            "resposta": resposta,
            "tempo_ms": round((fim - inicio) * 1000, 2)
        }