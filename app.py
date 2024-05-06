from quart import Quart, request
from lang import langchain

app = Quart(__name__)


@app.route("/")
def hello():
    return "wrong endpoint"

@app.route("/query", methods=["GET"])
async def query():
    query = request.args.get("query")
    res = await langchain(query)
    return res

if __name__ == "__main__":
    app.run(debug=True)
