from langchain_openai import ChatOpenAI
from langchain.agents import tool
from langchain_community.utilities import BingSearchAPIWrapper
from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import tool
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor
from typing import List
import json
from langchain_core.agents import AgentActionMessageLog, AgentFinish
from langchain.agents.format_scratchpad import format_to_openai_function_messages
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv, find_dotenv
import os

#load the enviornment variables...
load_dotenv(find_dotenv('.env'))
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
BING_API_KEY = os.getenv('BING_API_KEY')

"""
TO DO: Prompt engineering for the output of the LLM [X] (Explain the structure of the output)
TO DO: generate file which will be used to populate DB [X]
"""
#Constants
URL = 'https://api.bing.microsoft.com/v7.0/search'
MODEL = ChatOpenAI(model= "gpt-3.5-turbo", api_key= OPENAI_API_KEY, temperature=0.1)
prompt = ChatPromptTemplate.from_messages([
    ("system", "you don't know current events beyond the year 2022! You are assisting a user with queries they have about homework"),
    ("user", "{userQuery}"),
    MessagesPlaceholder(variable_name="agent_scratchpad")
])


# tool and response descriptions
class SearchInput(BaseModel): 
    query: str = Field(description='This should be a search query')

class Response(BaseModel):
    """Final response to the question being asked"""

    sources_desc = "List of URL's, snippets, and titles which provide sources to help answer the question. \
        Do not include under any circumstance title or snippet, \
        only include only eight of the links from this list of dictionaries"

    searchedAnswer: str = Field(description="The final answer that the user will recieve")
    sources: List = Field(description=sources_desc)

# helper functions...
def outputParser(output): # parse the output
    # the data was found in the vector store or the Model is capable without the tool
    if "function_call" not in output.additional_kwargs:
        return AgentFinish(return_values={"storedAnswer": output.content}, log=output.content)

    # Parse out the function call
    function_call = output.additional_kwargs["function_call"]
    name = function_call["name"]
    inputs = json.loads(function_call["arguments"])

    # If the Response function was invoked, return to the user with the function inputs
    if name == "Response": return AgentFinish(return_values=inputs, log=str(function_call))
    
    # Otherwise, return an agent action
    return AgentActionMessageLog(tool=name, tool_input=inputs, log="", message_log=[output])

def writeToFiles(source: list[dict[str]]) -> None:
    path = os.path.join(os.getcwd(), "files_with_sources")
    if not os.path.isdir("files_with_sources"):
        os.mkdir(path=path)
    elif len(os.listdir(path=path)) != 0: #empty 
        print(f'DIRECTORY: {path} not empty.\nClearing directory...')
        for File in os.listdir(path=path): os.remove(os.path.join(path, File)) #delete the files
    for i, src in enumerate(source):
        #we have the index and the link as well...
        with open(file=f"{path}/searched_source_{i + 1}.txt", mode='w', encoding="UTF-8") as cache_search:
            res = requests.get(url=src['link'])
            if res.status_code != 200:
                print(f'there was an error of status code: {res.status_code}')
                continue
            doc = res.content
            soup = BeautifulSoup(doc, 'html.parser') #use beautiful soup to only get the text and title
            content = soup.get_text(separator="\n", strip=True)
            content_split = content.split('\n')
            cache_search.writelines(content_split)

# defining the tools the GPT LLM can use
@tool("search-tool", args_schema=SearchInput) # don't think this is necessary since bing search is a built in tool
def searchBing(query: str) -> list[dict[str]]:
    """a tool to look search online with the bing api"""
    SEARCH = BingSearchAPIWrapper(bing_subscription_key = BING_API_KEY, bing_search_url = URL, )
    return SEARCH.results(query, 100)



#exports
def searchOrNot(userIn: str) -> List[dict]: 
    #Binding the tools
    model_with_tools = MODEL.bind_functions([searchBing, Response])

    #Building the agent
    agent = (
        {
            "userQuery": lambda x: x["userQuery"],
            "agent_scratchpad": lambda x: format_to_openai_function_messages(x["intermediate_steps"])
        }
        | prompt
        | model_with_tools
        | outputParser
    )

    #Prepping execution and executing
    agent_executor = AgentExecutor(agent=agent, tools=[searchBing], verbose=False)
    out = agent_executor.invoke({"userQuery": userIn})
    if "storedAnswer" not in out.keys():
        writeToFiles(source=out['sources'])

    return out


if __name__ == "__main__":
    userIn = input("What would you like to search today?: ")
    print(searchOrNot(userIn=userIn))
