from flask import Flask, jsonify, request

app = Flask(__name__)

@server.route("/")
def hello():
    return "Hello World"

if __name__ == "__main__":
    app.run()
