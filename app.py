from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from openai import OpenAI
import streamlit as st
import os
from dotenv import load_dotenv

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
## Langmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
LANGCHAIN_API_KEY = os.environ["LANGCHAIN_API_KEY"]

load_dotenv()  #


prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

## streamlit framework

st.title('VedDarpan Chatbot')
input_text=st.text_input("Search the topic u want")

# openAI LLm 
llm=ChatOpenAI(model="llama-3-sonar-large-32k-online", base_url="https://api.perplexity.ai")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))