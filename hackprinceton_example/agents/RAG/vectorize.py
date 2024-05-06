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


os.environ["OPENAI_API_KEY"] =os.getenv('OPENAI_API_KEY')

# loader = TextLoader(r"/Users/fahadfaruqi/Desktop/HackPrinceton/backend/agents/RAG/dsa.txt")
# data = loader.load()
# text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
# docs = text_splitter.split_documents(data)
query = "How do I do binary search"

db3 = Chroma(persist_directory="./chroma_db", embedding_function=OpenAIEmbeddings())
db3.get() 
vector_search = db3
# docs = db3.similarity_search(query)
# vector_search = Chroma.from_documents(persist_directory="./chroma_db")

#embedding_vector = OpenAIEmbeddings().embed_query(query)
# results = vector_search.similarity_search(query)
# print(docs[0].page_content)