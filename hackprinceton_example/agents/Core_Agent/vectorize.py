import os
# from langchain_community.vectorstores import MongoDBAtlasVectorSearch
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
load_dotenv()
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import DatabricksVectorSearch
from langchain_community.vectorstores import Chroma
from langchain.agents import Tool


os.environ["OPENAI_API_KEY"] =os.getenv('OPENAI_API_KEY')
loader = TextLoader("dsa.txt")
data = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
docs = text_splitter.split_documents(data)
  


vector_search = Chroma.from_documents(docs, OpenAIEmbeddings())

# query = "How do I do binary search"
# embedding_vector = OpenAIEmbeddings().embed_query(query)
# results = vector_search.similarity_search(query)
# print(results[0].page_content)

# results = vector_search.similarity_search(query)
# the above is the function for api. add the result of the function to the start of the
# input query. the purpose is to give extra context for layla without taking away the code context
# edge cas that can be omitted is going out of toke max limit