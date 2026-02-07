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
- example_request (string curl command)
- possible_errors (array of strings)

Return ONLY a valid JSON array.
No markdown.
No explanation.
No code blocks.

Endpoints:
{endpoints}
"""

    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost:8000",
            "X-Title": "AI API Doc Generator"
        },
        json={
            "model": "mistralai/mistral-7b-instruct",
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.1
        },
        timeout=60,
    )

    data = response.json()

    if "choices" not in data:
        return {"error": data}
    
    content = data["choices"][0]["message"]["content"].strip()

    # Remove markdown if present
    content = content.replace("```json", "").replace("```", "").strip()

    try:
        # First attempt
        return json.loads(content)
    except:
        try:
            # If it’s a stringified JSON, decode again
            cleaned = content.encode().decode("unicode_escape")
            return json.loads(cleaned)
        except:
            return {
                "error": "Failed to parse AI output",
                "raw_output": content
            }
