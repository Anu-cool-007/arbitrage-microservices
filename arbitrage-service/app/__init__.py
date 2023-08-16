from flask import Flask
from flask_socketio import SocketIO

sock = SocketIO()


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "gjr39dkjn344_!67#"
    app.config["USE_LOCAL_DATA"] = True
    app.config[
        "API_KEY"
    ] = "563c5dde1bdac6228e047bfffd62c13c6601e87fe4aec136f908f8270ac4179b"
    app.config["SYMBOLS"] = ["BTC", "ETH", "USDT"]
    app.config["CURRENCIES"] = ["USD", "EUR", "GBP"]
    app.config["EXCHANGES"] = ["Binance", "Coinbase", "Kraken", "Bitfinex"]

    with app.app_context():
        # Register blueprints
        from .arbitrage_api import arbitrage_api_blueprint

        app.register_blueprint(arbitrage_api_blueprint)
        sock.init_app(app, cors_allowed_origins="*")
        return app
