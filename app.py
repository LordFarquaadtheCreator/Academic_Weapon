from quart import Quart, request, make_response, websocket
from langchain_functions.base_agent import get_response
from quart_cors import cors
import asyncio


app = cors(Quart(__name__), allow_origin="*")


@app.route("/")
def hello():
    return "wrong endpoint"


@app.route("/query", methods=["GET"])
async def query():
    query = request.args.get("query")
    #formerly context = int(request.args.get("content")) or 5
    context = 5
    res = await get_response(query=query, context_count=context)
    #'>' not supported between instances of 'str' and 'int'
    #this error is caused by the context being a string and not an integer in previous res = await get_response(query, str(context))
    return str(res)


@app.route("/upload", methods=["POST"]) #for the most part the posting of the file is done just need a location for the file to be stored for the moment before being passed into the vector store.
async def upload():
    try:
        text_payload = await request.form #recieve other parts of the form
        file_payload = await request.files #recieve the file parts of the form
        for name, data in text_payload.items(): ##here is where we want to process and save the data...
            print(name, data)
        for name, currFile in file_payload.items():
            print(name, currFile.read())

    except Exception as e:
        return await make_response(f'Error {e}', 500)
    else: #on success
        return await make_response(f'successfully uploaded data!', 200)

#websocket helpers
#this allows sending and recieving messages from the websocket independently without having to wait on the client
async def send_message(message):
    await websocket.send("STARTED WEBSOCKET CONNECTION WITH QUART SERVER")

async def recieve_message():
    data = await websocket.receive()
    return data

# async def close_connection():
#     await websocket.close()

# working on the websocket implementation
# @app.websocket("/ws")
# async def ws():
#     sender = asyncio.create_task(send_message())
#     reciever = asyncio.create_task(recieve_message())
#     await asyncio.gather(sender, reciever)

# https://pgjones.gitlab.io/quart/how_to_guides/websockets.html



# https://stackoverflow.com/questions/70138056/json-server-access-to-localhost-was-denied-in-chrome
#possible reason why this port keeps disconneting 
#is because of the cors policy and the airplay on port 5000 for apple devices
#however the issue is definetly apparent if the 
#if you are having issues with access to localhost being denied visit chrome://net-internals/#sockets and flush the sockets.
#last alternative would be to switch the port.
#basically DO NOT START THE VITE SERVER BEFORE THE QUART SERVER.


### For a websocket implementation.....

# @app.websocket("/ws")
# async def ws():
#     websocket.headers
#     while True:
#         try:
#             data = await websocket.receive()
#             await websocket.send(f"Echo {data}")
#         except asyncio.CancelledError:
#             # Handle disconnect
#             raise

if __name__ == "__main__":
    app.run(debug=True)
