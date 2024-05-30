from quart import Quart, request, make_response, websocket
from quart import Quart, request, websocket
# from llama_ind.app import main
from quart_cors import cors

from flask import Flask
from flask_socketio import SocketIO

# app = cors(Quart(__name__), allow_origin="*")
app = Flask(__name__)
socketio = SocketIO(app)


@app.route("/")
def hello():
    return "wrong endpoint"


# ws/127.0.0.1:5000/ws
# @app.websocket("/ws")
# async def ws():
#     from llama_ind.app import main

#     while True:
#         query = await websocket.receive()
#         async for chunk in query:
#             await websocket.send(chunk)
#         # async for chunk in main(INDEX, query):
#         #     await websocket.send(chunk.delta)


# @app.websocket("/ws")
# async def ws():
#     while True:
#         query = await websocket.receive()
#         async for chunk in query:
#             await websocket.send(chunk)


@socketio.on("message")
def handle_message(message):
    from flask_socketio import emit
    from llama_ind.app import main

    res = main(INDEX, message, sync=False, is_fahad=True)  # streamer

    for chunk in res:
        # print(chunk.delta, end="")
        emit(chunk.delta)


@socketio.on("query")
def query(message):
    from flask_socketio import send

    # from llama_ind.app import main

    # print(message)
    # # res = main(INDEX, message, sync=False, is_fahad=True)  # streamer

    # # for chunk in res:
    # #     send(chunk)
    send(message)

    # return


# @app.route("/query", methods=["GET"])
# def query():
#     from llama_ind.app import main
#     from quart import request

#     query_str = request.args.get("query")
#     res = main(INDEX, query_str, sync=True, is_fahad=True)

#     return str(res)


# @app.route("/add_to_db", methods=["POST"])
# async def db():
# from quart import request, jsonify
# from llama_ind.add_to_db import add_to_db

# try:
#     data = await request.get_json()
#     path = data["path"]

#     add_to_db(INDEX, path)

#     return jsonify(success=True)
# except Exception as e:
#     return jsonify(error=str(e)), 400
@app.route("/upload", methods=["POST"]) #for the most part the posting of the file is done just need a location for the file to be stored for the moment before being passed into the vector store.
async def upload():
    PATH = os.path.join(os.getcwd(), "uploads")

    if not os.path.isdir("uploads"):
        os.mkdir(path=PATH)
    elif len(os.listdir(path=PATH)) != 0: #empty 
        print(f'DIRECTORY: {PATH} not empty.\nClearing directory...')
        for File in os.listdir(path=PATH): os.remove(os.path.join(PATH, File)) #delete the files
        
    try:
        text_payload = await request.form #recieve other parts of the form
        file_payload = await request.files #recieve the file parts of the form

        if len(text_payload) > 0:
            for key, data in text_payload.items(): ##here is where we want to process and save the data...
                print(key, data)
        if len(file_payload) > 0:
            for key, currFile in file_payload.items(): ##here is where we want to cache the data
                print(key, currFile)
                await currFile.save(os.path.join(PATH, f'{key}{currFile.filename}'))

    except Exception as e:
        return await make_response(f'Error {e}', 500)
    else: #on success
        return await make_response(f'successfully uploaded data!', 200)

#websocket helpers
#this allows sending and recieving messages from the websocket independently without having to wait on the client
async def send_message(): #whatever you want to be returned to the client goes here
    await websocket.send('Hello from the server!')

async def recieve_message() -> None:
    data = await websocket.receive()
    print(data, type(data))
    

async def close_connection():
    await websocket.close()
    return 'sucessfully closed websocket connection!'

@app.websocket("/ws")
async def ws():
    sender = asyncio.create_task(send_message())
    reciever = asyncio.create_task(recieve_message())

    await asyncio.gather(sender, reciever)

# https://pgjones.gitlab.io/quart/how_to_guides/websockets.html



# @app.websocket("/ws")
# async def ws():
#     while True:
#         query = await websocket.receive()
#         await websocket.send(f'The websocket connection was successfule with the query: {query}')
#         async for chunk in main(query):
#             await websocket.send(chunk.delta)


if __name__ == "__main__":
    # from llama_ind.get_db import get_db_index

    # INDEX = get_db_index()
    # app.run(debug=True)
    socketio.run(app, debug=True)
