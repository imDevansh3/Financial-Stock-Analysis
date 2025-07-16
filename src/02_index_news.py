import os
import openai
from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

# Load environment variables
load_dotenv()

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Load documents
documents = SimpleDirectoryReader('articles').load_data()

# Build index
index = VectorStoreIndex.from_documents(documents)

# Persist the index to disk
index.storage_context.persist()