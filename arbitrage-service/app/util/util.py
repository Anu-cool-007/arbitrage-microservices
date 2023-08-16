from itertools import combinations
import math

from app.models.models import Arbitrage


def get_arbitrage(
    data: dict[str, dict[str, dict[str, int]]], threshold: int
) -> list[Arbitrage]:
    arbitrage_list: Arbitrage = []
    for symbol in data:
        for currency in data[symbol]:
            currency_data = [
                [exchange, data[symbol][currency][exchange]]
                for exchange in data[symbol][currency]
            ]
            pairs = list(combinations(currency_data, 2))
            print(symbol, currency, pairs)
            for pair in pairs:
                if pair[0][1] > pair[1][1]:
                    arbitrage = Arbitrage(
                        symbol=symbol,
                        currency=currency,
                        buy_exchange=pair[1][0],
                        sell_exchange=pair[0][0],
                        buy_price=pair[1][1],
                        sell_price=pair[0][1],
                        units=math.ceil(threshold / (pair[0][1] - pair[1][1])),
                    )
                    arbitrage_list.append(arbitrage)
                elif pair[0][1] < pair[1][1]:
                    arbitrage = Arbitrage(
                        symbol=symbol,
                        currency=currency,
                        buy_exchange=pair[0][0],
                        sell_exchange=pair[1][0],
                        buy_price=pair[0][1],
                        sell_price=pair[1][1],
                        units=math.ceil(threshold / (pair[1][1] - pair[0][1])),
                    )
                    arbitrage_list.append(arbitrage)
    return arbitrage_list
