def get_db_index():
    """Returns the database for direct queries"""
    import chromadb
    from llama_index.vector_stores.chroma import ChromaVectorStore
    from llama_index.core import VectorStoreIndex
    from llama_index.embeddings.huggingface import HuggingFaceEmbedding

    PERSIST_DIR = "db"
    EMBED_MODEL = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
    DB_NAME = "academic"

    db = chromadb.PersistentClient(path=PERSIST_DIR)
    chroma_collection = db.get_collection(DB_NAME)

    return chroma_collection