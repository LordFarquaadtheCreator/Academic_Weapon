import os
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
import json
import chromadb
from chromadb.utils import embedding_functions

# experiment with larger models 
MODEL_NAME = "mixedbread-ai/mxbai-embed-large-v1" # ~ 0.5 gb
embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=MODEL_NAME)

# Create Chroma Client
client = chromadb.PersistentClient(path="./chromadb/")
print(f'Number of active dbs: {client.count_collections()}')

# Create DB
academic_weapon_db = client.create_collection(
    name="academic_weapon", embedding_function=embedding_func
)