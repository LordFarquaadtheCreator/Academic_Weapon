from llama_ind.timer import timer
from llama_index.core import PromptTemplate

QUERY_GEN_PROMPT = PromptTemplate(
    """\
    You are a helpful assistant that generates multiple search queries for a vector database 
    based on a single input query. These queries must look like incomplete text found in a textbook
    so the database can easily find the appropiate data. They must be constructed in a way that it helps
    break down the large, complex input query into smaller, more specific queries - like divide and conquer.
    Seperate each query with a newline character '\n'
    Generate {num_queries} search queries, one on each line, related to the following input query:
    Query: {query}
    Queries:
    """
)
QUERRY_WRAPPER_PROMPT = PromptTemplate(
    "Below is an instruction that describes a task. "
    "Write a response that appropriately completes the request.\n\n"
    "### Instruction:\n{query_str}\n\n### Response:"
)


@timer
def generate_queries(query: str, num_queries: int = 4):
    from llama_index.llms.huggingface import HuggingFaceLLM
    import torch

    llm = HuggingFaceLLM(
        context_window=514,
        max_new_tokens=256,
        generate_kwargs={"temperature": 0.25, "do_sample": True},
        query_wrapper_prompt=QUERRY_WRAPPER_PROMPT,
        tokenizer_name="BAAI/bge-reranker-base",
        model_name="BAAI/bge-reranker-base",
        device_map="auto",
        tokenizer_kwargs={"max_length": 514},
        model_kwargs={"torch_dtype": torch.float16},  # may or may not work on mac
    )

    response = llm.predict(QUERY_GEN_PROMPT, num_queries=num_queries, query=query)
    queries = response.split("\n")
    return queries
