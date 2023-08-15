import sqlite3
from flask import Flask, Response, request, abort

# json dependencies
from flask import jsonify
from flask_restx import Api, Resource, fields


app = Flask(__name__)
api = Api(app)


@api.route("/hello")
class HelloWorld(Resource):
    def get(self):
        return {"hello": "world"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
