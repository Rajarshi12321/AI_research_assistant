# loading secret key
import os
from dotenv import load_dotenv

from llama_index.core import VectorStoreIndex
from llama_index.core import ServiceContext
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.llms.gemini import Gemini
import google.generativeai as genai

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
pinecone_api_key = os.getenv("PINECONE_API_KEY")
