# doc: https://pgjones.gitlab.io/quart/reference/cheatsheet.html#cheatsheet
# doc for requests: https://pgjones.gitlab.io/quart/tutorials/api_tutorial.html
from quart import Quart, request
from langchain_functions.base_agent import langchain
from langchain_functions.agents.internetSearch import *
from langchain_functions.agents.query_rag.vector_store.add_data import add_text

app = Quart(__name__)


@app.route("/")
def hello():
    return "wrong endpoint"

@app.route("/query", methods=["GET"])
async def query():
    query = request.args.get("query")
    res = await langchain(query, 1)
    return res

# @app.route("/upload", methods=["POST"])
# async def uploadFile():
#     try:
        
#     except Exception as err:
#         print(f'There was an error: {err}')
#         return "An error occurred"
#     else:
#         return "Data recieved successfully"
    

if __name__ == "__main__":
    app.run(debug=True)
