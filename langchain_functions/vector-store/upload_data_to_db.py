from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv
import os

def upload_to_db(doc):
    """ takes in documents and uploads to db"""
    load_dotenv()
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    if OPENAI_API_KEY is None:
        raise Exception("Missing OPENAI_API_KEY")

    db = FAISS.load_local(
        "faiss_index", OpenAIEmbeddings(), allow_dangerous_deserialization=True
    )

    db.add_documents(doc)

    db.save_local("faiss_index")
