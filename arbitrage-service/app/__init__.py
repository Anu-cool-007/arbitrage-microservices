from flask import Flask
from flask_socketio import SocketIO, emit


app = Flask(__name__)
sock = SocketIO(app, cors_allowed_origins="*")
