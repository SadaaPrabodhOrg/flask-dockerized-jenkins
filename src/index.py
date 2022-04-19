import os
import socket

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/status", methods=["GET"])
def hello():
    return jsonify({"status": "UP"})


@app.route('/')
def hello2():
    html = "<h3>Hello ferozekhan {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>"
    return html.format(name=os.getenv("NAME", " ferozekhan world"), hostname=socket.gethostname())


if __name__ == "__main__":
    app.run(port=5000, host="127.0.0.1", debug=True)
