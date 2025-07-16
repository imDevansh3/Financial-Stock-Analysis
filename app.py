import os
from dotenv import load_dotenv
import openai
from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage
from llama_index.llms.openai import OpenAI
import streamlit as st
from llama_index.core import Settings


load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

llm = OpenAI(
    model_name = 'gpt-3.5-turbo',
    max_tokens = 4096
    )

Settings.llm = llm

storage_context = StorageContext.from_defaults(
    persist_dir="./storage"
)

index = load_index_from_storage(storage_context)

query_engine = index.as_query_engine()

st.title('Financial Stock Analysis using LlamaIndex')

st.header("Reports:")

report_type = st.selectbox(
    'What type of report do you want?',
    ('Single Stock Outlook', 'Competitor Analysis')
)

if report_type == 'Single Stock Outlook':
    symbol = st.text_input("Stock Symbol")

    if symbol:
        with st.spinner(f'Generating Report for {symbol}...'):
            response = query_engine.query(f"Write a report on the outlook for {symbol} stock from the years 2023-2027. Be sure to include potential risks and headwinds.")
            print(type(response))

            st.write(str(response))



if report_type == "Competitor Analysis":
    symbol1 = st.text_input("Stock Symbol 1")
    symbol2 = st.text_input("Stock Symbol 2")

    if symbol1 and symbol2:
        with st.spinner(f'Generating report for {symbol1} vs. {symbol2}...'):
            response = query_engine.query(f"Write a report on the competition between {symbol1} stock and {symbol2} stock.")

            st.write(str(response))