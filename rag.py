from langchain import hub
from langchain_chroma import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_groq import ChatGroq
from langchain_ollama import OllamaEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

loader = TextLoader("output.txt")
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)
local_embeddings = OllamaEmbeddings(model="nomic-embed-text")
vectorstore = Chroma.from_documents(documents=splits, embedding=local_embeddings)

retriever = vectorstore.as_retriever()
# prompt = hub.pull("rlm/rag-prompt")

llm = ChatGroq(model="llama3-8b-8192")

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

prompt = hub.pull("rlm/rag-prompt")

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

while True:
    print("Type 'exit' to quit")
    question = input("User's Question: ")
    if question == "exit":
        break
    response = rag_chain.invoke(question)
    print("AI Answer: ", response)

print("Good Bye")
# response = rag_chain.invoke("When the idea of establishing a textile institute come from group of industrialists?")
# print("Answer: ", response)