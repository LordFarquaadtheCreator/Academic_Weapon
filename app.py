from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"
socketio = SocketIO(app)


@app.route("/")
@cross_origin()
def hello():
    return "wrong endpoint"


# socket.io connection
@socketio.on("message")
@cross_origin()
def handle_message(message):
    from flask_socketio import emit
    from llama_ind.app import main

    res = main(INDEX, message, sync=False, is_fahad=True)  # streamer

    for chunk in res:
        emit("message", chunk.delta)


@app.route("/query", methods=["GET"])
@cross_origin()
def query():
    from llama_ind.app import main
    from quart import request

    query_str = request.args.get("query")
    res = main(INDEX, query_str, sync=True, is_fahad=True)

    return str(res)


@app.route("/add_to_db", methods=["POST"])
@cross_origin()
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
    socketio.run(app, debug=True)
