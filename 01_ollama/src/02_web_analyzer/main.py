"""Web Analyzer Agent"""

import requests
from bs4 import BeautifulSoup
from openai import OpenAI, OpenAIError


def scrape_webpage(url: str) -> str:
    """Fetches a webpage and returns clean, stripped text content."""
    try:
        # Add a user-agent header to avoid getting blocked by websites
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        # Parse HTML and extract raw text strings
        soup = BeautifulSoup(response.text, "html.parser")

        # Remove script, style, and navigation blocks to clean the data
        for element in soup(["script", "style", "nav", "footer", "header"]):
            element.decompose()

        # Get text and clean up whitespace gaps
        clean_text = soup.get_text(separator=" ")
        lines = (line.strip() for line in clean_text.splitlines())
        chunks = (phrase for line in lines for phrase in line.split("  "))
        return "\n".join(chunk for chunk in chunks if chunk)

    except requests.RequestException as e:
        return f"Error scraping the website: {e}"


def analyze_with_ollama(webpage_content: str, model_name: str = "deepseek-r1:8b"):
    """Sends the scraped text to Ollama to generate a markdown description."""

    client = OpenAI(base_url="http://localhost:11434/v1/", api_key="_")

    # Define strict system instructions for Markdown layout
    system_prompt = (
        "You are an expert web content analyzer. Your task is to describe and summarize "
        "the provided webpage content. You must reply strictly using clean Markdown formatting. "
        "Include a title, a high-level summary, key bullet points, and any primary themes found."
    )

    user_prompt = f"Here is the raw content of the webpage:\n\n{webpage_content}"

    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.3,  # Lower temperature keeps the summary factual
        )
        return response.choices[0].message.content
    except (
        OpenAIError
    ) as e:  # pragma: no cover - handle SDK/runtime errors from the OpenAI client
        # The OpenAI SDK may raise various errors (network, auth, etc.). Propagate a clear message.
        return f"Error communicating with Ollama: {e}"


# --- Execution Flow ---
if __name__ == "__main__":
    # Target URL to analyze
    TARGET_URL = "https://kashfulquraan.com"

    print(f"1. Scraping text from: {TARGET_URL}...")
    SCRAPED_DATA = scrape_webpage(TARGET_URL)

    # Simple check to verify we got actual content
    if SCRAPED_DATA.startswith("Error"):
        print(SCRAPED_DATA)
    else:
        print(f"2. Successfully extracted {len(SCRAPED_DATA)} characters.")
        print("3. Sending content to Ollama for Markdown generation...\n")

        markdown_summary = analyze_with_ollama(
            SCRAPED_DATA, model_name="deepseek-r1:8b"
        )

        print("--- Ollama Markdown Report ---")
        print(markdown_summary)
