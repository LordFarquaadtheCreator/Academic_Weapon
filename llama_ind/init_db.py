import os
import logging
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_ind.sentence_window import sentence_window_setup
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
import chromadb
import shutil

PERSIST_DIR = "db"
DATA_DIR = "data"
EMBED_MODEL = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
DB_NAME = "academic"
logging.basicConfig(level=logging.INFO)


def init_chroma():
    chroma_client = chromadb.PersistentClient(path=PERSIST_DIR)
    chroma_collection = chroma_client.create_collection(DB_NAME)
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    return storage_context


def create_db():
    """return index of vector database"""
    if not os.path.exists(PERSIST_DIR):
        os.mkdir(PERSIST_DIR)
        try:
            # process data
            documents = SimpleDirectoryReader(DATA_DIR).load_data()
            # documents = sentence_window_setup(documents)
            # ^^^ breaks

            # create vector database
            storage_context = init_chroma()

            index = VectorStoreIndex.from_documents(
                documents, storage_context=storage_context, embed_model=EMBED_MODEL
            )

            logging.info("Vector database created successfully.")

            return index
        except Exception as e:
            logging.error(f"Failed to create vector database: {e}")
            raise Exception(f"Failed to create vector database: {e}")
    else:
        logging.info("Vector database already exists! Trying to delete")
        shutil.rmtree(PERSIST_DIR)
        raise Exception("Vector database already exists!")


if __name__ == "__main__":
    create_db()
