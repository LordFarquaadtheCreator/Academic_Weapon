from llama_ind.timer import timer


@timer
def add_to_db(db, path: str) -> None:
    try:
        from llama_index.core import SimpleDirectoryReader
        # from llama_index import StorageContext
        from llama_ind.sentence_window import sentence_window_setup

        documents = SimpleDirectoryReader(path).load_data()
        nodes = sentence_window_setup(documents)

        db.insert_nodes(nodes)
        db.storage_context.persist(persist_dir="db")

    except Exception as e:
        print("hellooooo error on add to db")
        raise Exception(f"Failed to add to vector database: {e}")
