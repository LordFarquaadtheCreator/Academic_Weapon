def main():
    from llama_ind.get_db import get_db_index
    from llama_ind.init_db import create_db
    from llama_index.core.postprocessor import MetadataReplacementPostProcessor
    from llama_ind.query_rewrite import generate_queries
    from llama_ind.get_window import get_window

    # query rewriter -> n-queries
    # n-queries -> database for #m results
    # rerank
    # prompt

    try:
        res = generate_queries("What is a derivative??")
        # exit()

        # index = create_db()
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

        print(data)
        # response = ""
        # for re in streaming_response.response_gen:
        #     response += re
        #     print(response)

    except Exception as e:
        print(e)
        exit()
