from quart import Quart, request
from langchain_functions.base_agent import get_response
from quart_cors import cors

app = cors(Quart(__name__), allow_origin="http://localhost:5173/")


@app.route("/")
def hello():
    return "wrong endpoint"


@app.route("/query", methods=["GET"])
async def query():
    query = request.args.get("query")
    context = request.args.get("content") or 5
    
    res = await get_response(query, str(context))
    return str(res)


if __name__ == "__main__":
    app.run(debug=True)
