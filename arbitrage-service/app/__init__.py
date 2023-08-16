from flask import Flask
from flask_socketio import SocketIO

# app = Flask(__name__)
# sock = SocketIO(app, cors_allowed_origins="*")

sock = SocketIO()


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "gjr39dkjn344_!67#"

    with app.app_context():
        # Register blueprints
        from .arbitrage_api import arbitrage_api_blueprint

        app.register_blueprint(arbitrage_api_blueprint)
        sock.init_app(app, cors_allowed_origins="*")
        return app
