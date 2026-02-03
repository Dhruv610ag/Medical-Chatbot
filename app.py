from flask import Flask, render_template, request
from dotenv import load_dotenv
import os

from src.helper import download_embeddings
from src.prompt import *

from langchain_pinecone import PineconeVectorStore
from langchain_groq import ChatGroq
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate

app = Flask(__name__)
load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not PINECONE_API_KEY:
    raise RuntimeError("PINECONE_API_KEY not set")

if not GROQ_API_KEY:
    raise RuntimeError("GROQ_API_KEY not set")

# Load embeddings
embeddings = download_embeddings()

index_name = "medicoai-chatbot"

# Load existing Pinecone index
docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)

retriever = docsearch.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    groq_api_key=GROQ_API_KEY,
    temperature=0.2
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

qa_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, qa_chain)

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/get", methods=["POST"])
def chat():
    msg = request.form.get("msg", "")
    if not msg:
        return "Please enter a question."

    response = rag_chain.invoke({"input": msg})
    return response["answer"]

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
