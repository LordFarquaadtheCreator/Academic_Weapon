from agents.query_rag.query_rag import query_db, add_to_db
from agents.internetSearch.internet import searchOrNot
from functions import needBing

async def langchain(query: str, num_results: int, save = False):
    results = []
    
    # check database
    try:
        results = query_db(query, num_results)
    except Exception as e:
        print(e)

    # calculate overall confidence
    confidence: int = sum(results[1])
    if(needBing(confidence)):
        # search on the internet
        try:
            results.append(await searchOrNot(query))
        except Exception as e:
            print(e)


    if save:
        try:
            await add_to_db(query)
        except Exception as e:
            print(e)

    return results


if __name__ == "__main__":
    import asyncio 

    async def main():
        print(await langchain("im gonna  ", 4))
    
    asyncio.run(main())