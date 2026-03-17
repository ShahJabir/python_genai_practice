"""FastAPI GenAI App"""

import os
from openai import OpenAI
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

app = FastAPI()


class PromptModel(BaseModel):
    """prompt pydantic model"""

    user: str
    prompt: str


@app.get("/")
def read_root():
    """Root Endpoint"""
    return {"Hello": "World"}


@app.post("/weather")
def read_weather(prompt: PromptModel):
    """Weather Endpoint"""
    response = client.chat.completions.create(
        model="gemini-3-flash-preview",
        messages=[
            {
                "role": "user",
                "content": prompt.prompt,
            },
        ],
    )
    return response.choices[0].message.content
