import requests
from app.models.models import Arbitrage
import dataclasses


# API client for Trade service
class TradeClient:
    @staticmethod
    def create_trade(token, arbitrage: Arbitrage):
        headers = {"Authorization": token}
        response = requests.request(
            method="POST",
            url="http://localhost:5002/api/trade/create",
            headers=headers,
            json=dataclasses.asdict(arbitrage),
        )
        if response.status_code == 401:
            return False
        trade = response.json()
        return trade
