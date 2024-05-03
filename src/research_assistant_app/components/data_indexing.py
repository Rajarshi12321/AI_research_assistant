from llama_index.core import StorageContext

from llama_index.vector_stores.pinecone import PineconeVectorStore
from pinecone import Pinecone


from llama_index.core.node_parser import SemanticSplitterNodeParser
from llama_index.core.ingestion import IngestionPipeline

from research_assistant_app.constants import gemini_api_key, pinecone_api_key
from research_assistant_app.components.data_ingestion import get_cleaned_dir_docs


from research_assistant_app.constants import gemini_api_key, pinecone_api_key
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.llms.gemini import Gemini
import google.generativeai as genai
from llama_index.core import Settings
from llama_index.core.node_parser import SentenceSplitter


genai.configure(api_key=gemini_api_key)  # configuring api to run the pipeline
model = Gemini(models="gemini-pro", api_key=gemini_api_key, temperature=0.3)
gemini_embed_model = GeminiEmbedding(model_name="models/embedding-001")

embed_model = gemini_embed_model

Settings.llm = model
Settings.embed_model = gemini_embed_model
Settings.node_parser = SentenceSplitter(chunk_size=512, chunk_overlap=20)
Settings.num_output = 512
Settings.context_window = 3900


# Define the initial pipeline
pipeline = IngestionPipeline(
    transformations=[
        SemanticSplitterNodeParser(
            buffer_size=1,
            breakpoint_percentile_threshold=95,
            embed_model=embed_model,
        ),
        embed_model,
    ],
)


pc = Pinecone(api_key=pinecone_api_key)
pinecone_index = pc.Index(
    "ai-research-assistant"
)  # `ai-research-assistant` is the index name

vector_store = PineconeVectorStore(pinecone_index=pinecone_index)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

# cleaned_docs = get_cleaned_dir_docs()
# print(cleaned_docs, "Check 1")

pipeline = IngestionPipeline(
    transformations=[
        SemanticSplitterNodeParser(
            buffer_size=1,
            breakpoint_percentile_threshold=95,
            embed_model=embed_model,
        ),
        embed_model,
    ],
    vector_store=vector_store,  # Our new addition
)


# Now we run our pipeline!
def run_indexing_pipeline(docs):
    genai.configure(api_key=gemini_api_key)  # configuring api to run the pipeline

    pipeline.run(documents=docs)

    # print(pinecone_index.describe_index_stats(), "pincone index")
    return pinecone_index.describe_index_stats()


# >>> {'dimension': 1536,
# >>> 'index_fullness': 0.0,
# >>> 'namespaces': {'': {'vector_count': 46}},
# >>> 'total_vector_count': 46}

if __name__ == "__main__":
    cleaned_docs = get_cleaned_dir_docs("Data")

    index_stats = run_indexing_pipeline(cleaned_docs[:3])

    print(index_stats, "pincone index")
