from agents.query_rag.query_rag import query_db, add_to_db
from agents.internetSearch.internet import searchOrNot
from functions.needBing import need_bing

async def langchain(query: str, num_results: int, save = False):
    results = []

    # check database
    try:
        results = query_db(query, num_results)
    except Exception as e:
        print(e)

    # calculate overall confidence
    confidence: int = sum(results[1])/len(results[1])
    needs_bing = need_bing(confidence)

    if(not needs_bing):
        try:
            res = searchOrNot(query)
            print("res", res)
            results.append(res)
        except Exception as e:
            print("Exception Occured",  e)

    if save:
        try:
            await add_to_db(query)
        except Exception as e:
            print(e)

    return results[0]


if __name__ == "__main__":
    import asyncio 

    async def main():
        res = await langchain("the mitocondria is the powerhouse of the cell  ", 4)
        print(res)
    
    asyncio.run(main())
