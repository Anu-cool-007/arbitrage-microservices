from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///auth.db"

    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        # Register blueprints
        from .auth_api import auth_api_blueprint

        app.register_blueprint(auth_api_blueprint)
        return app
