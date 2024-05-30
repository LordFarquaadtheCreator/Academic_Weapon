from llama_ind.timer import timer


@timer
def rerank(data: object):
    """takes in array of documents & sorts based on score - returns window only"""
    try:
        sorted_dicts = sorted(data, key=lambda x: x["score"], reverse=True)
        return [d["data"] for d in sorted_dicts]
    except Exception as e:
        raise Exception("Reranking falled", e)
