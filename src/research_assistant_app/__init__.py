import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[logging.FileHandler(log_filepath), logging.StreamHandler(sys.stdout)],
)

logger = logging.getLogger("research_assistantLogger")


from research_assistant_app.constants import gemini_api_key, pinecone_api_key
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.llms.gemini import Gemini
import google.generativeai as genai
from llama_index.core import Settings
from llama_index.core.node_parser import SentenceSplitter

model = Gemini(models="gemini-pro", api_key=gemini_api_key, temperature=0.3)

gemini_embed_model = GeminiEmbedding(model_name="models/embedding-001")

embed_model = gemini_embed_model

Settings.llm = model
Settings.embed_model = gemini_embed_model
Settings.node_parser = SentenceSplitter(chunk_size=512, chunk_overlap=20)
Settings.num_output = 512
Settings.context_window = 3900

genai.configure(api_key=gemini_api_key)
