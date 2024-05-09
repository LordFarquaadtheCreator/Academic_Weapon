from agents.query_rag.vector_store.similarity_search import query
from agents.query_rag.vector_store.add_data import add_file, add_text


def query_db(query_str: str, num_results: int = 1):
    res: object = query(query_str, num_results)
    confidence = []
    documents = []
    
    for elem in res:
        documents.append(elem[0])
        confidence.append(elem[1])

    return [documents, confidence]


async def add_to_db(data: any):
    if isinstance(data, str):
        res = await add_text(data)
    else:
        res = await add_file(data)
    return res


# if __name__ == "__main__":
#     import asyncio

#     async def main():
#         # res = await add_to_db("im gonna add this to the db")
#         res = query_db("im gonna add this to the ")
#         print(res)

#     asyncio.run(main())
