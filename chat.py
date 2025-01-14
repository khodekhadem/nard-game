from flask import Flask, render_template, request, jsonify
import socket
import os,sys
import random
import sender

def send_message(msg,myserver):
    #myserver.send(f'{msg}'.encode())
    sender.start(msg,myserver,'router1')
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, parent_dir)
from sender import start  as senderstart

app = Flask(__name__)
messages = []

@app.route("/")
def index():
    return render_template("/index.html")

@app.route("/send_message", methods=["POST"])
def send_message():
    msg = request.form.get("message", "")
    if msg:
        messages.append(msg)
    return jsonify({"messages": messages})

@app.route("/get_messages", methods=["GET"])
def get_messages():
    return jsonify({"messages": messages})

@app.route("/roll_dice", methods=["GET"])
def roll_dice():
    try:
        server =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sender.start('dice',server,'router1')
        tmp1 = server.recv(1024).decode()
        sender.start('dice',server,'router1')
        tmp2 = server.recv(1024).decode()
        dice=[tmp1,tmp2]
        return jsonify({"dice": dice})
    except:
        dice = [random.randint(1, 6), random.randint(1, 6)]
        #return jsonify({"dice": dice})
        return jsonify({"dice": [9,9]})

def start():
    #start the app with ip 0.0.0.0
    app.run(host="0.0.0.0", port=5000)

if __name__ == "__main__":
    #senderstart('hello',socket.socket(socket.AF_INET, socket.SOCK_STREAM),'router1')
    app.run(host="0.0.0.0", port=5005,debug=True)
