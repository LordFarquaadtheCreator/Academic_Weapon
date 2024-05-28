def main():
    # documents = SimpleDirectoryReader("data").load_data()

    # Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

    # sentence_index = sentence_window_setup(documents)
    # exit()
    # ollama
    # Settings.llm = Ollama(model="phi3", request_timeout=360.0)
    # needs more ram!!!!

    from llama_ind.get_db import get_db_index
    from llama_ind.init_db import create_db
    from llama_index.core.postprocessor import MetadataReplacementPostProcessor

    try:
        index = create_db()
        # index = get_db_index()
        # query_engine = index.as_query_engine(
        #     similarity_top_k=5,
        #     node_postprocessors=[
        #         MetadataReplacementPostProcessor(target_metadata_key="window")
        #     ],
        # )

        # index = create_db()
    except Exception as e:
        print(e)
        exit()

    query_engine = index.as_query_engine()
    response = query_engine.query("what is an ld?")
    print(response)