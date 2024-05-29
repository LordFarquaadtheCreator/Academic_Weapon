def main(query: str):
    from llama_ind.get_db import get_db_index
    from llama_ind.init_db import create_db
    from llama_index.core.postprocessor import MetadataReplacementPostProcessor
    from llama_ind.query_rewrite import generate_queries
    from llama_ind.get_window import get_window
    from llama_ind.rerank import rerank
    from llama_ind.llm import get_llm

    # [x] query rewriter -> n-queries
    # [x] n-queries -> database for #m results
    # [x] rerank
    # prompt

    try:
        res = generate_queries(query)

        # index = create_db()

        # init db
        index = get_db_index()
        query_engine = index.as_retriever(
            similarity_top_k=1,
            node_postprocessors=[
                MetadataReplacementPostProcessor(target_metadata_key="window"),
            ],
        )

        # extract window
        data = []
        for question in res:
            query_response = query_engine.retrieve(question)
            data.append(get_window(query_response))

        # rerank
        data = rerank(data)

        # prompt
        response = get_llm(query, str(data))

        for r in response:
            print(r.delta, end="")

    except Exception as e:
        print("Error!!", e)
        exit()
