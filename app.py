from quart import Quart, request, websocket
from llama_ind.app import main
from quart_cors import cors

app = cors(Quart(__name__), allow_origin="*")


@app.route("/")
def hello():
    return "wrong endpoint"


@app.websocket("/ws")
async def ws():
    while True:
        query = await websocket.receive()
        async for chunk in main(query):
            await websocket.send(chunk.delta)


if __name__ == "__main__":
    app.run(debug=True)
