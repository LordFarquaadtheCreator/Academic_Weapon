from vector_store.similarity_search import query
from vector_store.add_data import add_file, add_text


def query_db(query_str: str, num_results: int = 1):
    res = query(query_str, num_results)
    confidence = res[0][1]
    documents = res[0][0]
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
