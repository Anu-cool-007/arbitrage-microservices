# from app import app, sock
# from flask import request
# from flask_socketio import emit
# import os
# import json
# from app.arbitrage_api.api.CryptoClient import get_crypto_data

# from app.models.models import Arbitrage

# URL = "https://min-api.cryptocompare.com/data/generateAvg"
# API_KEY = "563c5dde1bdac6228e047bfffd62c13c6601e87fe4aec136f908f8270ac4179b"
# symbols = ["BTC", "ETH", "USDT"]
# currencies = ["USD", "EUR", "GBP"]
# exchanges = ["Binance", "Coinbase", "Kraken", "Bitfinex"]

# USE_LOCAL_DATA = True
# if os.path.isfile("./data.json") and USE_LOCAL_DATA:
#     with open("data.json", "r") as data_file:
#         crypto_data = json.load(data_file)
# else:
#     crypto_data = get_crypto_data(URL, API_KEY, symbols, currencies, exchanges)
#     json_object = json.dumps(crypto_data, indent=4)

#     with open("data.json", "w") as data_file:
#         data_file.write(json_object)

# preferences: dict[str, str] = {}


# def calc_arbitrage(threshold: int):
#     emit("reverse", "test lol")


# @sock.on("threshold")
# def test(data):
#     preferences[data["user_id"]] = data["threshold"]
#     print(preferences)
#     calc_arbitrage(data["threshold"])


# if __name__ == "__main__":
#     sock.run(app, host="0.0.0.0", port=5001, debug=True)

from app import create_app, sock

app = create_app()

if __name__ == "__main__":
    sock.run(app, host="0.0.0.0", port=5001, debug=True)
