from langchain_community.vectorstores import MongoDBAtlasVectorSearch
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import MongoDBAtlasVectorSearch
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import DatabricksVectorSearch
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from databricks.vector_search.client import VectorSearchClient
import os
from langchain_mongodb.cache import MongoDBCache
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()

from langchain_mongodb import MongoDBAtlasVectorSearch
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from databricks.vector_search.client import VectorSearchClient

# Configure the Databricks CLI
os.system("databricks configure")


os.environ["OPENAI_API_KEY"] = os.getenv('openai_api_key')

loader = TextLoader(r"C:\Users\David Mazur\Documents\HackPrinceton\backend\agents\RAG\Etymology.txt")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()
emb_dim = len(embeddings.embed_query("hello"))
vsc = VectorSearchClient()
print(emb_dim)

"""

vsc.create_endpoint(name="vector_search_demo_endpoint", endpoint_type="STANDARD")

vector_search_endpoint_name = "vector_search_demo_endpoint"
index_name = "ml.llm.demo_index"

index = vsc.create_direct_access_index(
    endpoint_name=vector_search_endpoint_name,
    index_name=index_name,
    primary_key="id",
    embedding_dimension=emb_dim,
    embedding_vector_column="text_vector",
    schema={
        "id": "string",
        "text": "string",
        "text_vector": "array<float>",
        "source": "string",
    },
)

index.describe()


dvs = DatabricksVectorSearch(
    index, text_column="text", embedding=embeddings, columns=["source"]
)

dvs.add_documents(docs)############

query = "What did the president say about Ketanji Brown Jackson"
dvs.similarity_search(query)
print(docs[0].page_content)"""