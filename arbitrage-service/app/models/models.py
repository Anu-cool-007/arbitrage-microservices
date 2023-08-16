from dataclasses import dataclass


@dataclass
class Arbitrage:
    symbol: str
    currency: str
    buy_exchange: str
    sell_exchange: str
    buy_price: int
    sell_price: int
    units: int
