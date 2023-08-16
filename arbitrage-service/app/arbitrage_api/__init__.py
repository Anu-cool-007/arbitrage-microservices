from flask_sock import Blueprint

arbitrage_api_blueprint = Blueprint("arbitrage_api", __name__)

from . import events
