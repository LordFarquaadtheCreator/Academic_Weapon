from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os


async def upload_to_db(doc):
    """takes in documents and uploads to db"""
    load_dotenv()
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    if OPENAI_API_KEY is None:
        raise Exception("Missing OPENAI_API_KEY")

    db = FAISS.load_local(
        "faiss_index", OpenAIEmbeddings(), allow_dangerous_deserialization=True
    )

    db.add_documents(doc)

    db.save_local("faiss_index")


async def upload_text(text: str):
    load_dotenv()
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    if OPENAI_API_KEY is None:
        raise Exception("Missing OPENAI_API_KEY")

    db = FAISS.load_local(
        "faiss_index", OpenAIEmbeddings(), allow_dangerous_deserialization=True
    )

    db.add_texts([text])

    db.save_local("faiss_index")
