from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
import os
load_dotenv()

async def query(query: str):
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    if OPENAI_API_KEY is None:
        raise Exception("Missing OPENAI_API_KEY")

    db = FAISS.load_local(
        "faiss_index", OpenAIEmbeddings(), allow_dangerous_deserialization=True
    )

    docs = await db.similarity_search(query)

    return docs