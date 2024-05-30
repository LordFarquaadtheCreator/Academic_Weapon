from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS, cross_origin
import os

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
    

    PATH = os.path.join(os.getcwd(), "uploads")
    
    if not os.path.isdir("uploads"):
        os.mkdir(path=PATH)
    elif len(os.listdir(path=PATH)) != 0: #empty 
        print(f'DIRECTORY: {PATH} not empty.\nClearing directory...')
        for File in os.listdir(path=PATH): os.remove(os.path.join(PATH, File)) #delete the files
        
    try:
        file_payload = await request.files.getList('files') #recieve the file parts of the form

        data = await request.form #recieve the form data

        if len(data) > 0:
            for i, currFile in zip(data): ##here is where we want to cache the data
                print(currFile)
                await currFile.save(os.path.join(PATH, f'{i}{currFile.filename}'))

        add_to_db(INDEX, PATH) #add data to db after saving files
    except Exception as e:
        return jsonify(error=str(e)), 400
    else: #on success
        return jsonify(success=True)

    # try:
    #     data = await request.get_json()
    #     path = data["path"] # put the path in here

    #     add_to_db(INDEX, path)



if __name__ == "__main__":
    # from llama_ind.get_db import get_db_index

    INDEX = get_db_index()
    # app.run(debug=True)
    socketio.run(app, debug=True)
