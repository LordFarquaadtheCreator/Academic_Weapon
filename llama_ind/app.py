def main():
    from llama_ind.get_db import get_db_index
    from llama_ind.init_db import create_db
    from llama_index.core.postprocessor import MetadataReplacementPostProcessor
    from llama_ind.query_rewrite import generate_queries

    try:
        res = generate_queries(
            "What's an LDNUM? How can I write a function to generate them. Who wrote the article?"
        )
        # index = create_db()
        index = get_db_index()
        query_engine = index.as_retriever(
            similarity_top_k=1,
            node_postprocessors=[
                MetadataReplacementPostProcessor(target_metadata_key="window"),
            ],
        )

        # query_engine = index.as_query_engine()
        for ques in res:
            response = query_engine.retrieve(ques)
            print(response)

    except Exception as e:
        print(e)
        exit()
