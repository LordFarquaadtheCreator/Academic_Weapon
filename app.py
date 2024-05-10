# doc: https://pgjones.gitlab.io/quart/reference/cheatsheet.html#cheatsheet
from quart import Quart, Response, request, jsonify
from langchain_functions.base_agent import get_answer, get_context

app = Quart(__name__)


@app.route("/")
def hello():
    return "wrong endpoint"


@app.route("/query")
async def query():
    query = request.args.get("query", default="", type=str)
    if not query:
        return jsonify({"error": "Query parameter is required"}), 400

    context_count = request.args.get("context_count", default=5, type=int)

    response = await get_answer(query, context_count)

    return response.content


if __name__ == "__main__":
    app.run(debug=True)
