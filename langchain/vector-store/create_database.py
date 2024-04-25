from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_env
import os
load_env()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") 
if OPENAI_API_KEY is None:
    raise Exception("Missing OPENAI_API_KEY")

db = FAISS(embedding_function = OpenAIEmbeddings())
db.save_local("faiss_index")