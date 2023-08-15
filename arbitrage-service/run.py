from app import app, sock
from flask_socketio import emit


@sock.on("reverse")
def test(message):
    print(message)
    emit("reverse", message[::-1])


if __name__ == "__main__":
    sock.run(app, host="0.0.0.0", port=5001, debug=True)
