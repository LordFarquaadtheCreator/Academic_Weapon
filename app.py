from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "wrong endpoint"

@app.route("/query")
async def query(query):
    res = await langchain(query)
    return res

if __name__ == "__main__":
    app.run()