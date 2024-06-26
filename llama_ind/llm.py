from llama_ind.timer import timer
from llama_index.core import PromptTemplate

QA_PROMPT = PromptTemplate(
    """\
    Context information is below.
    _____________________________
    {context_str}
    Given the context information and not prior knowledge, answer the query.
    Query: {query}
    Answer: \    
    """
)


@timer
def get_llm(query, context, sync=False):
    from llama_index.llms.ollama import Ollama
    from llama_index.core.llms import ChatMessage

    llm = Ollama(model="gemma:2b", request_timeout=30.0)

    formatted_qa = QA_PROMPT.format(context_str=context, query=query)

    messages = [
        ChatMessage(
            role="system",
            content="You are a helpful assistent knowldege in mathamatics",
        ),
        ChatMessage(role="user", context=str(formatted_qa)),
    ]

    return llm.complete(formatted_qa) if sync else llm.stream_chat(messages)
