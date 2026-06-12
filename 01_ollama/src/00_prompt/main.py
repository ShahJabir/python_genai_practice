"""A custom system prompt for Shah Jabir Taqi."""

from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1/",
    api_key="_",  # A dummy key is required by the SDK but ignored by Ollama
)

prompt = input("Enter your message: ")

response = client.chat.completions.create(
    model="deepseek-r1:8b",
    messages=[
        {"role": "user", "content": prompt},
    ],
)

# Extract the response text
print("--- Response ---")
print(response.choices[0].message.content)
print("\n--- Token Usage ---")

# Access the usage data fields
usage = response.usage
print(f"Input (Prompt) Tokens:  {usage.prompt_tokens}")
print(f"Output (Completion) Tokens: {usage.completion_tokens}")
print(f"Total Tokens Used:       {usage.total_tokens}")
