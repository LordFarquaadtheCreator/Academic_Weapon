from llama_ind.timer import timer


@timer
def add_to_db(db, path: str) -> bool:
    try:
        from llama_index.core import SimpleDirectoryReader
        from llama_ind.sentence_window import sentence_window_setup

        documents = SimpleDirectoryReader(path).load_data()
        nodes = sentence_window_setup(documents)

        db._add_nodes_to_index(nodes)
        return True

    except Exception as e:
        raise Exception(f"Failed to add to vector database: {e}")
