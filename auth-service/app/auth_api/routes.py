# application/user_api/routes.py
from . import auth_api_blueprint
from .. import db, login_manager
from ..models import User
from flask import make_response, request, jsonify
from flask_login import current_user, login_user, login_required

# Flask login manager to load user by user_id
@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()

# flask login manager to fetch user from request using auth token
@login_manager.request_loader
def load_user_from_request(request):
    token = request.headers.get("Authorization")
    if token:
        token = token.replace("Basic ", "", 1)
        user = User.query.filter_by(token=token).first()
        if user:
            return user
    return None


# Fetch all users
@auth_api_blueprint.route("/api/users", methods=["GET"])
def get_users():
    data = []
    for row in User.query.all():
        data.append(row.to_json())

    response = jsonify(data)
    return response


# Sign in API
@auth_api_blueprint.route("/api/user/create", methods=["POST"])
def post_register():
    json = request.get_json()
    name = json["name"]
    username = json["username"]
    password = json["password"]
    user = User.query.filter_by(username=username).first()
    if not user:
        user = User()
        user.name = name
        user.username = username
        user.password = password

        user.generate_token()

        db.session.add(user)
        db.session.commit()

        response = jsonify({"message": "User added", "result": user.to_json()})
    else:
        response = make_response(jsonify({"message": "User already present"}), 500)

    return response

# Log in API. Returns updated token
@auth_api_blueprint.route("/api/user/login", methods=["POST"])
def post_login():
    json = request.get_json()
    username = json["username"]
    user = User.query.filter_by(username=username).first()
    if user:
        if json["password"] == user.password:
            user.generate_token()
            db.session.commit()
            login_user(user)

            return make_response(
                jsonify({"message": "Logged in", "result": user.to_json()})
            )

    return make_response(jsonify({"message": "Not logged in"}), 401)

# API for internal services to fetch user from user request
@auth_api_blueprint.route("/api/user", methods=["GET"])
def get_user():
    user: User = load_user_from_request(request=request)
    if user:
        return make_response(jsonify({"result": user.to_json()}))

    return make_response(jsonify({"message": "Not logged in"})), 401
