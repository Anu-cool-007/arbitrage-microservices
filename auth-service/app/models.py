from . import db
from datetime import datetime
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    name = db.Column(db.String(255), unique=False, nullable=True)
    password = db.Column(db.String(255), unique=False, nullable=False)
    token = db.Column(db.String(255), unique=True, nullable=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def generate_token(self):
        self.token = self.username + str(
            datetime.strptime(
                "20.12.2016 09:38:42,76", "%d.%m.%Y %H:%M:%S,%f"
            ).timestamp()
            * 1000
        )

    def __repr__(self):
        return "<User %r>" % (self.username)

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "username": self.username,
            "token": self.token,
        }
