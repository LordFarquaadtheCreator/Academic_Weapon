from quart import Quart, request
from langchain_functions.base_agent import get_response
from quart_cors import cors

app = cors(Quart(__name__), allow_origin="*")


@app.route("/")
def hello():
    return "wrong endpoint"


@app.route("/query", methods=["GET"])
async def query():
    query = request.args.get("query")
    context = int(request.args.get("content")) or 5
    res = await get_response(query=query, context_count=context)
    #'>' not supported between instances of 'str' and 'int'
    #this error is caused by the context being a string and not an integer in previous res = await get_response(query, str(context))
    return str(res)

# https://stackoverflow.com/questions/70138056/json-server-access-to-localhost-was-denied-in-chrome
#possible reason why this port keeps disconneting 
#is because of the cors policy and the airplay on port 5000 for apple devices
#however the issue is definetly apparent if the 
#if you are having issues with access to localhost being denied visit chrome://net-internals/#sockets and flush the sockets.
#last alternative would be to switch the port.
#basically DO NOT START THE VITE SERVER BEFORE THE QUART SERVER.

if __name__ == "__main__":
    app.run(debug=True)
