"""RAG Application Chat Section"""

from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI

load_dotenv()

# Vector Embeddings
gemini_client = OpenAI()
embedding_model = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview")
vector_db = QdrantVectorStore.from_existing_collection(
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="learning_rag",
)

# Take user input
user_query = input("Ask something: ")

# Relevant chunks from the vector db
search_results = vector_db.similarity_search(user_query)

CONTEXT = "\n\n\n".join(
    [
        f"""Page Content: {result.page_content}
        \nPage Number: {result.metadata["page_label"]}
        \nFile Location: {result.metadata["source"]}"""
        for result in search_results
    ]
)

# System Prompt
SYSTEM_PROMPT = f"""
 You are a helpfull AI Assistant who answeres user query based on the available context retrieved from a PDF file along with page_contents and page number.
 You should only ans the user based on the following context and navigate the user to open the right page number to know more.
 Context:
 {CONTEXT}
"""

# Chat Completion
response = gemini_client.chat.completions.create(
    model="gemini-3.1-pro",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_query},
    ],
)
