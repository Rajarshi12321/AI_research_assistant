import streamlit as st
from pathlib import Path

import os

import google.generativeai as genai

from research_assistant_app.components.data_ingestion import (
    get_cleaned_dir_docs,
    get_cleaned_input_docs,
)

from research_assistant_app.components.data_querying import user_query
from research_assistant_app.components.data_indexing import run_indexing_pipeline


from dotenv import load_dotenv

load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


st.set_page_config("Chat PDF")

st.header("Your research assistant here to help💁 (Powered by Gemini)")


user_question = st.text_input(
    "Chat with existing Pdfs in Pinecone data base or Your added PDF"
)

if user_question:
    response = user_query(user_question)

    st.write(response)


File = st.file_uploader(
    "Upload Your new PDF file to store in Pinecone DB", type=("pdf"), key="pdf"
)

if File:  # Save uploaded file to 'Data/' folder.
    save_folder = "Data"
    save_path = Path(save_folder, File.name)
    with open(save_path, mode="wb") as w:
        w.write(File.getvalue())

    if save_path.exists():
        st.success(f"File {File.name} is successfully saved!")

    file_dir = f"Data/{File.name}"

    res = get_cleaned_input_docs(file_dir)

    print(res, "cleaned docs")

    index_stats = run_indexing_pipeline(res)

    print(index_stats, "checking indexes")

    if index_stats != None:
        st.success(f"File {File.name} is successfully upserted in Pinecone DB!")

    user_question_pdf = st.text_input("Ask a Question from the PDF File")

    if user_question_pdf:
        response = user_query(user_question_pdf)

        st.write(response)

    File = None
