from flask import session, current_app

from .. import sock
from flask_socketio import emit
import os
import json
from app.arbitrage_api.api.CryptoClient import get_crypto_data

from app.util.util import get_arbitrage


# Check if local crypto data is present and app is configured to load from it
if os.path.isfile("./data.json") and current_app.config["USE_LOCAL_DATA"]:
    with open("data.json", "r") as data_file:
        crypto_data = json.load(data_file)
else:
    crypto_data = get_crypto_data(
        current_app.config["API_KEY"],
        current_app.config["SYMBOLS"],
        current_app.config["CURRENCIES"],
        current_app.config["EXCHANGES"],
    )
    json_object = json.dumps(crypto_data, indent=4)

    with open("data.json", "w") as data_file:
        data_file.write(json_object)

# User threshold preference. Can be stored in db or flask session
preferences: dict[str, str] = {}


# on new threshold, get new arbitrage list and emit back
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
