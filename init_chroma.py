import os
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
import json
import chromadb
from chromadb.utils import embedding_functions

# experiment with larger models 
MODEL_NAME = "mixedbread-ai/mxbai-embed-large-v1" # ~ 0.5 gb
COLLECTION_NAME = "academic_weapon"
embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=MODEL_NAME)

# Create Chroma Client
client = chromadb.PersistentClient(path="./chromadb/")
print(f'Number of active dbs: {client.count_collections()}')

def create_collection() -> collection:
    academic_weapon_db = client.create_collection(
        name=COLLECTION_NAME, embedding_function=embedding_func
    )
    return academic_weapon_db

def load_collection() -> collection:
    academic_weapon_db = client.create_collection(
        name=COLLECTION_NAME, embedding_function=embedding_func
    )
    return academic_weapon_db

db = load_collection() if (client.count_collections() != 0) else create_collection()