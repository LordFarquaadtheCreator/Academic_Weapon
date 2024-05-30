from llama_index.core.node_parser import SentenceWindowNodeParser
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core import Document
from llama_index.embeddings.huggingface import HuggingFaceEmbedding


def init_defaults():
    from llama_index.core import Settings

    node_parser = SentenceWindowNodeParser.from_defaults(
        window_size=3,
        window_metadata_key="window",
        original_text_metadata_key="original_text",
    )

    Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

    text_splitter = SentenceSplitter()

    Settings.text_splitter = text_splitter

    return node_parser, text_splitter


def sentence_window_setup(documents: Document) -> Document:
    from llama_ind.remove_stop import remove_stop_words

    node_parser, text_splitter = init_defaults()

    nodes = node_parser.get_nodes_from_documents(documents)

    for node in nodes:
        node.metadata["original_text"] = remove_stop_words(
            node.metadata["original_text"]
        )

    return nodes
