def get_db_query_engine():
    """returns db engine as a query engine - sentence window retrevial"""
    import chromadb
    from llama_index.vector_stores.chroma import ChromaVectorStore
    from llama_index.core import VectorStoreIndex
    from llama_index.embeddings.huggingface import HuggingFaceEmbedding
    from llama_index.core.postprocessor import MetadataReplacementPostProcessor

    PERSIST_DIR = "db"
    EMBED_MODEL = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
    DB_NAME = "academic"

    db = chromadb.PersistentClient(path=PERSIST_DIR)
    chroma_collection = db.get_collection(DB_NAME)
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    index = VectorStoreIndex.from_vector_store(
        vector_store,
        embed_model=EMBED_MODEL,
    )
    query_engine = index.as_query_engine(
        node_postprocessors=[
            MetadataReplacementPostProcessor(target_metadata_key="window")
        ],
    )

    return query_engine
