""" Should not be executed more than once """

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if OPENAI_API_KEY is None:
    raise Exception("Missing OPENAI_API_KEY")

texts = [
    "This is unrelated to the second text",
    "This may relate to unsavory acts of violence",
]
db = FAISS.from_texts(texts, OpenAIEmbeddings())
db.save_local("faiss_index")