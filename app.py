# doc: https://pgjones.gitlab.io/quart/reference/cheatsheet.html#cheatsheet
from quart import Quart, request
from langchain_functions.base_agent import langchain
from langchain_functions.agents.internetSearch import *

app = Quart(__name__)


@app.route("/")
def hello():
    return "wrong endpoint"

@app.route("/query", methods=["GET"])
async def query():
    query = request.args.get("query")
    res = await langchain(query, 1)
    print(f'The response was {res} \n\n')
    return res

@app.route("/upload", methods=["POST"])
async def uploadFile():
    return request.body
    

if __name__ == "__main__":
    app.run(debug=True)
