from llama_ind.timer import timer


@timer
def main(index, query: str, sync=False):
    """entry point for RAG"""
    from llama_index.core.postprocessor import MetadataReplacementPostProcessor
    from llama_ind.query_rewrite import generate_queries
    from llama_ind.get_window import get_window
    from llama_ind.rerank import rerank
    from llama_ind.llm import get_llm

    try:
        res = generate_queries(query)

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
        response = get_llm(query, str(data), sync)

        # for res in response:
        #     print(res.delta, end="")
        return response

    except Exception as e:
        print("Error!!", e)
        exit()
