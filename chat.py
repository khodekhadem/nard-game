from flask import Flask, render_template, request, jsonify
import socket
import os, sys
import random
import sender

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, parent_dir)
from sender import start as senderstart

app = Flask(__name__)
messages = []
backgammon_numbers = [[5,0,0,0,3,0,5,0,0,0,0,2], [5,0,0,0,3,0,5,0,0,0,0,2]]  # Initial numbers
#backgammon_numbers = [[i for i in range(1, 13)], [i for i in range(13, 25)]]  # Initial numbers

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
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sender.start('dice', server, 'router1')
        tmp1 = server.recv(1024).decode()
        sender.start('dice', server, 'router1')
        tmp2 = server.recv(1024).decode()
        dice = [tmp1, tmp2]
        return jsonify({"dice": dice})
    except:
        dice = [random.randint(1, 6), random.randint(1, 6)]
        return jsonify({"dice": [9, 9]})

@app.route("/get_numbers", methods=["GET"])
def get_numbers():
    return jsonify({"numbers": backgammon_numbers})

@app.route("/update_number", methods=["POST"])
def update_number():
    row = int(request.form.get("row"))
    index = int(request.form.get("index"))
    new_value = int(request.form.get("value"))
    backgammon_numbers[row][index] = new_value
    return jsonify({"numbers": backgammon_numbers})

def start():
    app.run(host="0.0.0.0", port=5000)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)