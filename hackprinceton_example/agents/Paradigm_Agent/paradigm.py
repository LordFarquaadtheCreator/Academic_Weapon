from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.agents import Tool, AgentType
from langchain.agents import initialize_agent
from langchain.chains import ConversationChain
import os
from typing import List, Union
from agents.Paradigm_Agent.para_tools import tools
from agents.Paradigm_Agent.para_prompt import template_prompt
from langchain.prompts import StringPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.agents import Tool
from langchain.agents import AgentExecutor, create_react_agent

from dotenv import load_dotenv

load_dotenv()
llm = ChatOpenAI(model_name="gpt-4-0125-preview", openai_api_key=os.environ["OPENAI_API_KEY"])

prompt=PromptTemplate.from_template(template_prompt)

agent = create_react_agent(llm, tools, prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)

# input = "How do I code a factorial function in js?"

# print(agent_executor.invoke({"input":input}))