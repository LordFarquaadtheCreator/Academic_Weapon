#making a custom agent that uses the bingSearch tool found in ./bingSearchTool.py
from dotenv import dotenv_values
from langchain_openai import ChatOpenAI
from langchain.agents import tool
from langchain_community.utilities import BingSearchAPIWrapper
from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import BaseTool, StructuredTool, tool
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain.agents.format_scratchpad.openai_tools import format_to_openai_tool_messages
from langchain.agents.output_parsers.openai_tools import OpenAIToolsAgentOutputParser
from langchain.agents import AgentExecutor

#creating a custom tool: https://python.langchain.com/docs/modules/tools/custom_tools/
#creating an agent: https://python.langchain.com/docs/expression_language/get_started/ 

URL = f'https://api.bing.microsoft.com/v7.0/search'
CONFIG = dotenv_values('../../../.env')
#add error handling...
BING_API_KEY = CONFIG['BING_API_KEY']
OPENAI_API_KEY = CONFIG['OPENAI_API_KEY']
MODEL = ChatOpenAI(model= "gpt-3.5-turbo", api_key= OPENAI_API_KEY, temperature=0)


prompt = ChatPromptTemplate.from_messages([
    ("system", "you have a texan accent and don't know current events beyond the year 2022!"),
    ("user", "{userQuery}"),
    MessagesPlaceholder(variable_name="agent_scratchpad")
])

class SearchInput(BaseModel): #further add description to args
    query: str = Field(description='This should be a search query')


#defining the tools the GPT LLM can use
@tool("search-tool", args_schema=SearchInput) # don't think this is necessary since bing search is a built in tool
def searchBing(query: str) -> list[dict[str]]:
    """look up things online with bing api"""
    SEARCH = BingSearchAPIWrapper(bing_subscription_key = BING_API_KEY, bing_search_url = URL, )
    return SEARCH.results(query, 100)


#Binding the tools
tools = [searchBing] 
model_with_tools = MODEL.bind_tools(tools)

#Building the agent
agent = (
    {
        "userQuery": lambda x: x["userQuery"],
        "agent_scratchpad": lambda x: format_to_openai_tool_messages(x["intermediate_steps"])
    }
    | prompt
    | model_with_tools
    | OpenAIToolsAgentOutputParser()
) # literally almost like doing the standard chaining/piping all that is missing is the .invoke

#Prepping execution and executing
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=False)

# list(agent_executor.stream({"userQuery": userIn}))
# https://python.langchain.com/docs/modules/agents/how_to/agent_structured/
# To Do: Look over at the above documentation so that I can return the agent with structured output. i.e. 
# I want the sources used as well to be returned not just the input and output.
# The resources could either be used for the 

if __name__ == "__main__":
    userIn = input("What would you like to search today?: ")
    print(agent_executor.invoke({"userQuery": userIn}))
