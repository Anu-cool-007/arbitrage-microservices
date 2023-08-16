from . import arbitrage_api_blueprint
from .api.AuthClient import AuthClient
from flask import session

from .. import sock
from flask import request
from flask_socketio import emit
import os
import json
from app.arbitrage_api.api.CryptoClient import get_crypto_data

from app.util.util import get_arbitrage


# Config Starts
API_KEY = "563c5dde1bdac6228e047bfffd62c13c6601e87fe4aec136f908f8270ac4179b"
symbols = ["BTC", "ETH", "USDT"]
currencies = ["USD", "EUR", "GBP"]
exchanges = ["Binance", "Coinbase", "Kraken", "Bitfinex"]
USE_LOCAL_DATA = True

# Config Ends

if os.path.isfile("./data.json") and USE_LOCAL_DATA:
    with open("data.json", "r") as data_file:
        crypto_data = json.load(data_file)
else:
    crypto_data = get_crypto_data(API_KEY, symbols, currencies, exchanges)
    json_object = json.dumps(crypto_data, indent=4)

    with open("data.json", "w") as data_file:
        data_file.write(json_object)

preferences: dict[str, str] = {}


def calc_arbitrage(threshold: int):
    emit(
        "arbitrage",
        json.dumps(
            [arbitrage.__dict__ for arbitrage in get_arbitrage(crypto_data, threshold)]
        ),
    )


@sock.on("threshold")
def test(threshold):
    threshold = int(threshold)
    session["threshold"] = threshold
    calc_arbitrage(threshold)
