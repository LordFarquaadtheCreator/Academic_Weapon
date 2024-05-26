def main():
    # documents = SimpleDirectoryReader("data").load_data()

    # Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

    # sentence_index = sentence_window_setup(documents)
    # exit()
    # ollama
    # Settings.llm = Ollama(model="phi3", request_timeout=360.0)
    # needs more ram!!!!

    from llama_ind.get_db import get_db
    index = get_db()

    query_engine = index.as_query_engine()
    response = query_engine.query("what is an ldnum?")
    print(response)

