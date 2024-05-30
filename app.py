from quart import Quart, websocket
from llama_ind.app import main
from quart_cors import cors

app = cors(Quart(__name__), allow_origin="*")


@app.route("/")
def hello():
    return "wrong endpoint"


# ws/127.0.0.1:5000/ws
@app.websocket("/ws")
async def ws():
    while True:
        query = await websocket.receive()
        async for chunk in main(INDEX, query):
            await websocket.send(chunk.delta)


@app.route("/add_to_db", methods=["POST"])
async def db():
    from quart import request, jsonify
    from llama_ind.add_to_db import add_to_db

    try:
        data = await request.get_json()
        path = data["path"]

        add_to_db(INDEX, path)

        return jsonify(success=True)
    except Exception as e:
        return jsonify(error=str(e)), 400


if __name__ == "__main__":
    from llama_ind.get_db import get_db_index

    INDEX = get_db_index()
    app.run(debug=True)
