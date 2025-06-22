# app/chat.py

import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def chat_with_openai(history: list[dict]) -> str:
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=history,
            temperature=0.7,
            max_tokens=1000,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"
