from llama_index.llms.ollama import Ollama
from llama_index.core.llms import ChatMessage


def get_llm(query, context):
    llm = Ollama(model="gemma:2b", request_timeout=30.0)

    messages = [
        ChatMessage(
            role="system",
            content="You are a helpful assistant knowledgable in mathamatics.",
        ),
        ChatMessage(role="user", content=context),
        ChatMessage(role="user", content=query),
    ]

    return llm.stream_chat(messages)
