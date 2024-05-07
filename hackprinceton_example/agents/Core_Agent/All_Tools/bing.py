import os
from dotenv import load_dotenv
from langchain_community.utilities import BingSearchAPIWrapper
from langchain_openai import OpenAI
from langchain.agents import Tool

load_dotenv()

os.environ["BING_SUBSCRIPTION_KEY"] = os.getenv("BingAPI")
os.environ["BING_SEARCH_URL"] = "https://api.bing.microsoft.com/v7.0/search"




# Initialize the BingSearchAPIWrapper
search = BingSearchAPIWrapper(k=1)

# Initialize the OpenAI language model if needed
# llm = OpenAI(model_name="gpt-4-0125-preview", temperature=0.2)

BingAPI = Tool(
        name="Intermediate Answer",
        func=search.run,
        description="useful for when you need to ask with search"
    )
