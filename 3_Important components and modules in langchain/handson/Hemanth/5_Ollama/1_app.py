import os
from dotenv import load_dotenv

from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

#langsmith Tracking
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_PROJECT'] = os.getenv('LANGCHAIN_PROJECT')

#prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpul assistant. Please help me with the following question."),
        ("user","Question:{question}")
    ]
)

# Streamlit framework
st.title("welcome our Ollama")
input_text = st.text_input("what question you have in mind?")

llm = Ollama(model="gemma:2b")
str_output = StrOutputParser()
chain = prompt | llm | str_output

if input_text:
    st.write(chain.invoke({"question":input_text}))

