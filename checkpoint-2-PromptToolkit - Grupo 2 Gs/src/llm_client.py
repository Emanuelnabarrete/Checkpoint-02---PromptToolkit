import os
import time
import requests

from dotenv import load_dotenv

load_dotenv()

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
MODEL = os.getenv("MODEL", "gpt-oss:120b")


class LLMClient:
    def chat(self, prompt, system="", temperature=0.5, max_tokens=20):
        url = f"{OLLAMA_HOST}/api/chat"

        payload = {
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
            "stream": False,
            "options": {
                "temperature": temperature,
                "num_predict": max_tokens
            }
        }

        start_time = time.time()

        try:
            response = requests.post(
                url,
                json=payload,
                timeout=120
            )

            response.raise_for_status()

            data = response.json()

            answer = data["message"]["content"].strip()

        except Exception as error:
            answer = f"ERROR: {error}"

        end_time = time.time()

        return {
            "answer": answer,
            "time_ms": round((end_time - start_time) * 1000, 2)
        }