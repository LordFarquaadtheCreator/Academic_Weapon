def main():
    from llama_ind.get_db import get_db_index
    from llama_ind.init_db import create_db
    from llama_index.core.postprocessor import MetadataReplacementPostProcessor
    from llama_ind.query_rewrite import generate_queries

    try:
        # res = generate_queries(
        #     "What is a derivative??"
        # )
        res = "What is a derivative?"
        # index = create_db()
        index = get_db_index()
        query_engine = index.as_query_engine(
            similarity_top_k=1,
            node_postprocessors=[
                MetadataReplacementPostProcessor(target_metadata_key="window"),
            ],
            streaming=True
        )
        # streaming output:
        # https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/streaming/
        streaming_response = query_engine.query(res)

        response = ""
        for re in streaming_response.response_gen:
            response += re
            print(response)

    except Exception as e:
        print(e)
        exit()
