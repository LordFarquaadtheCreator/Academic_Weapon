from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from dotenv import load_env
import os
load_dotenv()

DATA_PATH = "../data"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") 

if OPENAI_API_KEY is None:
    raise Exception("Missing OPENAI_API_KEY")

db = FAISS.load_local("faiss_index", OpenAIEmbeddings())

for entry in os.listdir(DATA_PATH):
    loader = TextLoader(entry) #must be txt file
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)

    db.add_documents(docs)