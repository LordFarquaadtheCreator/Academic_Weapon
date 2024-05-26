import os
import logging
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from sentence_window import sentence_window_setup

PERSIST_DIR = "./db"
DATA_DIR = "data"

logging.basicConfig(level=logging.INFO)

def create_db():
    if not os.path.exists(PERSIST_DIR):
        try:
            documents = SimpleDirectoryReader(DATA_DIR).load_data()
            documents = sentence_window_setup(documents)
            index = VectorStoreIndex(documents)
            index.storage_context.persist(persist_dir=PERSIST_DIR)

            logging.info("Vector database created successfully.")
        except Exception as e:
            logging.error(f"Failed to create vector database: {e}")
    else:
        logging.info("Vector database already exists!")

if __name__ == "__main__":
    create_db()
