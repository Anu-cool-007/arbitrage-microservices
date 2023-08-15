from flask import Blueprint

auth_api_blueprint = Blueprint("auth_api", __name__)

from . import routes
