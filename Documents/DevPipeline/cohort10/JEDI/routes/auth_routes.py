


from flask import Blueprint, request
from controllers.auth_controller import authenticate_user
from schemas.user_schema import user_schema

auth_bp = Blueprint("auth_bp", __name__, url_prefix="/user")

@auth_bp.route("/auth", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    token, user = authenticate_user(username, password)
    if not token:
        return {"message": "Invalid credentials"}, 401
    return {
        "access_token": token,
        "user": user_schema.dump(user)
    }, 200
