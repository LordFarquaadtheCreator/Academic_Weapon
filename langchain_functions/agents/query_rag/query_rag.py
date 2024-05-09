# query the FAISS database
from langchain_functions.vector-store.similarity_serch import query
from langchain_community.vector-store.add_data import *
import asyncio

async def query_db(query_str: str):
    return await query(query_str)

async def add_to_db(data: any):
    pass

if __name__ == "__main__":
    async def main():
        print(query_db("test"))

    asyncio.run(main())