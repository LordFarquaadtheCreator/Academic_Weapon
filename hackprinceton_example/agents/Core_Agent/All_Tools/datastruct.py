from langchain_community.utilities import StackExchangeAPIWrapper
from langchain.agents import load_tools

stackexchange = StackExchangeAPIWrapper()
tools = load_tools(["stackexchange"])


stackexchange.run("zsh: command not found: python")

tools = [
     {
        "name": "stackexchange",
        "description": "Stack Exchange API Wrapper",
        "type": "tool",
        "tool": stackexchange,
    }
]
