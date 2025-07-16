import os
import openai
from dotenv import load_dotenv
from llama_index.core import StorageContext, load_index_from_storage

# Load environment variables
load_dotenv()

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Load persisted index from disk
storage_context = StorageContext.from_defaults(persist_dir="./storage")
index = load_index_from_storage(storage_context)

# Create a query engine and ask a question
query_engine = index.as_query_engine()

response = query_engine.query("Tell me about Google's new supercomputer.")

# Print only the response text
print(str(response))