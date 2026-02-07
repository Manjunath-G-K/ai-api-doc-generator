import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")


def generate_docs(endpoints):
    prompt = f"""
You are an API documentation generator.

For each endpoint, generate:
- method
- path
- description
- example_request (curl)
- possible_errors (2–3 items)

Return as JSON array.

Endpoints:
{endpoints}
"""

    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": "mistralai/mistral-7b-instruct",
            "messages": [
                {"role": "user", "content": prompt}
            ],
        },
        timeout=60,
    )

    data = response.json()
    print("OPENROUTER RESPONSE:", data)

    if "choices" not in data:
        return {"error": data}

    return data["choices"][0]["message"]["content"]

