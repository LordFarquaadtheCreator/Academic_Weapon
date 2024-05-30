from llama_ind.timer import timer

QUERY_GEN_TEMPLATE = """\
    You are a helpful assistant that generates multiple search queries for a vector database 
    based on a single input query. These queries must look like incomplete text found in a textbook
    so the database can easily find the appropiate data. They must be constructed in a way that it helps
    break down the large, complex input query into smaller, more specific queries - like divide and conquer.
    Seperate each query with a newline character '\n'
    Generate {num_queries} search queries, one on each line, related to the following input query:
    Query: {query}
    Queries:
"""


@timer
def generate_queries(query: str, num_queries: int = 4):
    from llama_index.core import PromptTemplate
    from llama_index.llms.openai import OpenAI

    query_gen_prompt = PromptTemplate(QUERY_GEN_TEMPLATE)
    llm = OpenAI(model="gpt-3.5-turbo")

    response = llm.predict(query_gen_prompt, num_queries=num_queries, query=query)
    queries = response.split("\n")
    return queries
