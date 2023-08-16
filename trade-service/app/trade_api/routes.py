# application/user_api/routes.py
from . import trade_api_blueprint
from .. import db
from ..models import Trade
from flask import make_response, request, jsonify
from .api.AuthClient import AuthClient


@trade_api_blueprint.route("/api/trade", methods=["GET"])
def get_trades():
    token = request.headers.get("Authorization")

    response = AuthClient.get_user(token)
    print(token, response)
    if not response:
        return make_response(jsonify({"message": "Not logged in"}), 401)

    user = response["result"]

    trade_list = Trade.query.filter_by(user_id=user["id"]).all()

    response = jsonify(
        {"message": "Get Success", "result": [trade.to_json() for trade in trade_list]}
    )
    return response


@trade_api_blueprint.route("/api/trade/create", methods=["POST"])
def create_trade():
    token = request.headers.get("Authorization")

    response = AuthClient.get_user(token)

    if not response:
        return make_response(jsonify({"message": "Not logged in"}), 401)

    user = response["result"]

    user_id = user["id"]

    json = request.get_json()
    symbol = json["symbol"]
    currency = json["currency"]
    buy_exchange = json["buy_exchange"]
    sell_exchange = json["sell_exchange"]
    buy_price = json["buy_price"]
    sell_price = json["sell_price"]
    units = json["units"]

    trade = Trade()
    trade.user_id = user_id
    trade.symbol = symbol
    trade.currency = currency
    trade.buy_exchange = buy_exchange
    trade.sell_exchange = sell_exchange
    trade.buy_price = buy_price
    trade.sell_price = sell_price
    trade.units = units

    db.session.add(trade)
    db.session.commit()

    response = jsonify({"message": "Trade added", "result": trade.to_json()})

    return response
