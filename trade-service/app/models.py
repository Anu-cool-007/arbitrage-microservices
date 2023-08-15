from . import db
from datetime import datetime


class Trade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    symbol = db.Column(db.String(255), unique=False, nullable=False)
    currency = db.Column(db.String(255), unique=False, nullable=False)
    buy_exchange = db.Column(db.String(3), unique=False, nullable=False)
    sell_exchange = db.Column(db.String(10), unique=False, nullable=False)
    buy_price = db.Column(db.Integer)
    sell_price = db.Column(db.Integer)

    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def to_json(self):
        return {
            "id": self.id,
            "user_id": self.name,
            "symbol": self.username,
            "currency": self.token,
            "buy_exchange": self.token,
            "sell_exchange": self.token,
            "buy_price": self.token,
            "sell_price": self.token,
        }
