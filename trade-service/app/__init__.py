from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///auth.db"

    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        # Register blueprints
        from .trade_api import trade_api_blueprint

        app.register_blueprint(trade_api_blueprint)
        return app
