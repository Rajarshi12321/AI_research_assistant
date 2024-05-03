from llama_index.core import VectorStoreIndex

from llama_index.vector_stores.pinecone import PineconeVectorStore
from pinecone import Pinecone


from research_assistant_app.constants import gemini_api_key, pinecone_api_key
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.llms.gemini import Gemini
import google.generativeai as genai
from llama_index.core import Settings

genai.configure(api_key=gemini_api_key)  # configuring api to run the pipeline
model = Gemini(models="gemini-pro", api_key=gemini_api_key, temperature=0.3)
gemini_embed_model = GeminiEmbedding(model_name="models/embedding-001")

embed_model = gemini_embed_model

Settings.llm = model
Settings.embed_model = gemini_embed_model
# Settings.node_parser = SentenceSplitter(chunk_size=512, chunk_overlap=20)
Settings.num_output = 512
Settings.context_window = 3900


pc = Pinecone(api_key=pinecone_api_key)
pinecone_index = pc.Index(
    "ai-research-assistant"
)  # `ai-research-assistant` is the index name

vector_store = PineconeVectorStore(pinecone_index=pinecone_index)

from llama_index.core.retrievers import VectorIndexRetriever

from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core import PromptTemplate

import google.generativeai as genai


def get_vector_retriever(Pinecone_vector_store):
    # Instantiate VectorStoreIndex object from your vector_store object
    vector_index = VectorStoreIndex.from_vector_store(
        vector_store=Pinecone_vector_store
    )

    print(vector_index, "check indexes")

    # Grab 5 search results
    retriever = VectorIndexRetriever(index=vector_index, similarity_top_k=5)

    # Pass in your retriever from above, which is configured to return the top 5 results
    query_engine = RetrieverQueryEngine(retriever=retriever)

    return query_engine, vector_index


def get_full_prompt_template(cur_instr: str, prompt_tmpl):
    tmpl_str = prompt_tmpl.get_template()
    new_tmpl_str = cur_instr + "\n" + tmpl_str
    new_tmpl = PromptTemplate(new_tmpl_str)
    return new_tmpl


def proper_prompting(my_query_enginge, my_vector_index):

    QA_PROMPT_KEY = "response_synthesizer:text_qa_template"

    # get the base qa prompt (without any instruction prefix)
    base_qa_prompt = my_query_enginge.get_prompts()[QA_PROMPT_KEY]

    initial_instr = """\
    You are a QA assistant specifically designed to help in reaserch work as and research assistant.
    ---------------------

    Context information is below. Given the context information and not prior knowledge, \
    "{context_str}\n"
    ---------------------
    answer the query. \
    
    It is very important that If the context is not relevant, 
    please answer the question by using your own knowledge about the topic

    """

    # this is the "initial" prompt template
    # implicitly used in the first stage of the loop during prompt optimization
    # here we explicitly capture it so we can use it for evaluation
    old_qa_prompt = get_full_prompt_template(initial_instr, base_qa_prompt)

    old_qa_prompt
    # Use the custom prompt when querying
    # genai.configure(api_key=gemini_api_key)
    query_engine = my_vector_index.as_query_engine(text_qa_template=old_qa_prompt)

    return query_engine


## This will be the main function that we would call for querying
def user_query(qus):
    genai.configure(api_key=gemini_api_key)

    my_query_enginge, my_vector_index = get_vector_retriever(vector_store)

    query_engine = proper_prompting(my_query_enginge, my_vector_index)

    response = query_engine.query(qus)

    return response.response
