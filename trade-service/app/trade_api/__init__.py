from flask import Blueprint

trade_api_blueprint = Blueprint("trade_api", __name__)

from . import routes
