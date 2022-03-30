from ctypes.wintypes import MSG
from flask import Flask, render_template
from flask_socketio import SocketIO
import requests

app = Flask(__name__)
app.config["SECRET_KEY"] = "de16b73459bbfeceb67a01773f6684e7909e14d1ff61e5789a4c40067cb1a33c"
socketio = SocketIO(app)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def get():
    return render_template("get.html")


@socketio.on("led")
def handle_message(msg):
    ########## get two data : led number and status ###########
    
    # print('Message: ' + msg["led"] + )
    # r = requests.get('https://n64522.alavischool.ir/')
    # print(r)
    socketio.emit("led1", {"data": "Led is on"}, broadcast=True)
    print("send message")


if __name__ == '__main__':
    socketio.run(app, port=8080, debug=True)
