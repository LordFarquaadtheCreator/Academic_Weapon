from langchain_community.utilities import BingSearchAPIWrapper
from dotenv import dotenv_values
from langchain.tools import BaseTool, StructuredTool, tool
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.pydantic_v1 import BaseModel, Field
import json
import requests
import openmeteo_requests
from retry_requests import retry
import requests_cache

URL = f'https://api.bing.microsoft.com/v7.0/search'
CONFIG = dotenv_values('../.env')
BING_API_KEY = CONFIG['BING_API_KEY']
query = 'Best GPU\'s in 2024'


#WORKING ON....

cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)



def searchBing(query: str, numRes: int) -> list[dict[str]]:
    SEARCH = BingSearchAPIWrapper(bing_subscription_key = BING_API_KEY, bing_search_url = URL, )
    return SEARCH.results(query, numRes)

#custom tools

class WeatherSearch(BaseModel):
    query: str = Field(description="This is a query to the weather api")


@tool
def searchCurrentWeather(query: str):
    """Get the latest news on weather given a location"""
    requests.get()
    

if __name__ == "__main__":
    print(json.dumps(obj=searchBing(query=query, numRes=100)[::2], indent=6))
