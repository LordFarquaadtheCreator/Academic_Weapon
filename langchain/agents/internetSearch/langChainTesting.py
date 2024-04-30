# from langchain_core.prompts import ChatPromptTemplate, BasePromptTemplate
# from langchain_openai import ChatOpenAI
# from langchain_core.output_parsers import StrOutputParser
# from dotenv import dotenv_values
# CONFIG = dotenv_values('../../../.env')
# OPENAI_API_KEY = CONFIG['OPENAI_API_KEY']



# MODEL = ChatOpenAI(model= "gpt-3.5-turbo", api_key= OPENAI_API_KEY)

# prompt = ChatPromptTemplate.from_messages([
#     ("system", "you have a texan accent and don't speak much!"),
#     ("user", "{userQuery}"),  
# ])



# prompt_value = prompt.invoke({"userQuery": "What is the size of the eiffel tower?"}) # this part basically injects into the template of the Prompt

# print(prompt_value.to_json())

# res = MODEL.invoke(prompt_value)

# print(res + "\n\n") #pass in the prompt to the model and get a response

# print(StrOutputParser().invoke(input=res))


# #so essentially we want the code above to become the code at the bottom!

# #This can all be done by using the below method and the widely used one notice that the | are used much like piping in the CLI
# chain = prompt | MODEL | StrOutputParser()
# chain.invoke({"userQuery": "What is the size of the eiffel tower?"})
# print(chain.invoke({"userQuery": "What is the size of the eiffel tower?"}))


from internet import searchOrNot

print(searchOrNot(userIn='How many pokemon games have been released up until 2023?'))