from quart import Quart, request
from langchain_functions import base_agent
from quart_cors import cors

app = cors(Quart(__name__), allow_origin="http://localhost:5173/")


@app.route("/")
def hello():
    return "wrong endpoint"


@app.route("/query", methods=["GET"])
async def query():
    query = request.args.get("query")
    res = await base_agent(query, 1)
    return res


if __name__ == "__main__":
    app.run(debug=True)
