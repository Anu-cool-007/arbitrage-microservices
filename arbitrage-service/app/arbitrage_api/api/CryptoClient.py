import requests

CMC_URL = "https://min-api.cryptocompare.com/data/v4/all/exchanges"


def get_crypto_data(
    api_key: str,
    symbols: list[str],
    currencies: list[str],
    exchanges: list[str],
):
    crypto_data: dict[str, dict[str, dict[str, int]]] = {}
    for symbol in symbols:
        symbol_data: dict[str, dict[str, int]] = {}
        for currency in currencies:
            currency_data: dict[str, int] = {}
            for exchange in exchanges:
                data = requests.get(
                    f"{CMC_URL}?fsym={symbol}&tsym={currency}&e={exchange}&api_key=={api_key}"
                ).json()
                if "Response" in data and data["Response"] == "Error":
                    continue
                currency_data[exchange] = data["RAW"]["PRICE"]
            symbol_data[currency] = currency_data
        crypto_data[symbol] = symbol_data
    return crypto_data
