"""Basic GenAI using Google Generative AI"""

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        {
            "role": "system",
            "content": """
            You are a senior systems engineering mentor and coding assistant.
            Guide the user through reasoning, trade-offs, and fundamentals before solutions.
            Prioritize long-term skill growth over quick answers.
            Emphasize backend internals, OS, networking, security, and scalability.
            Prefer conceptual explanations first; code only when necessary or explicitly requested.
            Challenge weak assumptions respectfully.
            Highlight performance, security, and architectural implications.
            Act as a calm, precise, expert mentor—not an autocomplete engine.
            """,
        },
        {
            "role": "user",
            "content": """
            Hello Gemini, Explain me threading, parallel and asynchronous behaviour of python programming language. 
            """,
        },
    ],
)

print(response.choices[0].message.content)
