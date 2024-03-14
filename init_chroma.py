import os
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
import json
import chromadb
from chromadb.utils import embedding_functions

# experiment with larger models 
MODEL_NAME = "mixedbread-ai/mxbai-embed-large-v1" # ~ 0.5 gb
DISTANCE_FUNCTION = "cosine"
COLLECTION_NAME = "academic_weapon"
embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=MODEL_NAME)

def get_client() -> client:
    return chromadb.PersistentClient(path="./chromadb/")

def peek_db(db: chroma_collection) -> None:
    print(f"Peeking ...\n{collection.peek()}")


def create_collection() -> chroma_collection:
    print("Creating New Collection")
    academic_weapon_db = client.create_collection(
        name=COLLECTION_NAME, 
        embedding_function=embedding_func,
        metadata={"hnsw:space": DISTANCE_FUNCTION}
    )
    print(f"Number enteries in collection: {collection.count()}")
    return academic_weapon_db

def load_collection() -> chroma_collection:
    print("Loading Existing Collection")
    academic_weapon_db = client.get_collection(
        name=COLLECTION_NAME, 
        embedding_function=embedding_func,
        metadata={"hnsw:space": DISTANCE_FUNCTION}
    )
    print(f"Number enteries in collection: {collection.count()}")
    return academic_weapon_db
    
# saves to disk
def add_to_db(documents: list(str), ids: list(str), meta_data: dict(str), db: chroma_collection) -> None:
    print("Adding Data to Vector Database")
    db.add(
        documents=documents,
        metadatas=meta_data,
        id=ids,
    )

def get_n_results(db: chroma_collection, query: str, n: int, include: list = [], where: str = '', where_document: str = '') -> dict:
    db.query(
        query_texts=[str(query)],
        n_results=int(n),
        where={"metadata_field": str(where)},
        where_document={"$contains": str(where_document)},
        include=include
    )