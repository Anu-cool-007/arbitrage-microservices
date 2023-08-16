from app import create_app, sock

app = create_app()

if __name__ == "__main__":
    sock.run(app, host="0.0.0.0", port=5001, debug=True)
