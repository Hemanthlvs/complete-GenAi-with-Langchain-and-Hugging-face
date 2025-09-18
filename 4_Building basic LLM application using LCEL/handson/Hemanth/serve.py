import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langserve import add_routes
from fastapi import FastAPI


load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

model = ChatGroq(model="Gemma2-9b-It", groq_api_key=GROQ_API_KEY)

### Prompt Templates
generic_template = "You are now a translator. So please translate the below text to {language}"

prompt = ChatPromptTemplate.from_messages(
    [
        ("system",generic_template),
        ("user","{input_text}")
    ]
)

input = "Hey Hi! How are you?"

parser = StrOutputParser()

chain = prompt | model | parser

#chain.invoke({"language":"Telugu","input_text":input})


## App definition
app=FastAPI(title="Langchain Server",
            version="1.0",
            description="A simple API server using Langchain runnable interfaces")


## Adding chain routes
add_routes(
    app,
    chain,
    path="/chain"
)

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8000)
