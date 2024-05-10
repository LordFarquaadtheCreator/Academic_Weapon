async def get_answer(query: str, context: any):
    from langchain_openai import ChatOpenAI
    from langchain_core.prompts.chat import ChatPromptTemplate
    from langchain_functions.llm_prompt import PROMPT

    llm = ChatOpenAI(model="gpt-3.5-turbo")

    chat_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", PROMPT),
            ("human", query),
        ]
    )

    response = llm.invoke(chat_prompt.format_prompt())
    return response


async def get_context(query: str, num_results: int, save=False):
    from langchain_functions.agents.query_rag.query_rag import query_db, add_to_db
    from langchain_functions.agents.internetSearch.internet import searchOrNot
    from langchain_functions.functions.needBing import need_bing

    results = []

    # check database
    try:
        results = query_db(query, num_results)
    except Exception as e:
        print(e)

    # calculate overall confidence
    confidence: int = sum(results[1]) / len(results[1])
    needs_bing = need_bing(confidence)

    if not needs_bing:
        try:
            res = searchOrNot(query)
            print("res", res)
            results.append(res)
        except Exception as e:
            print("Exception Occured", e)

    if save:
        try:
            await add_to_db(query)
        except Exception as e:
            print(e)

    return results[0]


async def get_response(query: str, context_count=5):
    context = await get_context(query, context_count)
    answer = await get_answer(query, context)
    return answer, context
