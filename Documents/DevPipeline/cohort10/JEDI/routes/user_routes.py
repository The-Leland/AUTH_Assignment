


from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from controllers.user_controller import *
from schemas.user_schema import user_schema, users_schema
from util.permissions import rank_required

user_bp = Blueprint("user_bp", __name__, url_prefix="/user")

@user_bp.route("", methods=["POST"])
def create():
    data = request.get_json()
    user = create_user(data)
    return user_schema.dump(user), 201

@user_bp.route("/profile", methods=["GET"])
@jwt_required()
def get_profile():
    user = get_user(get_jwt_identity())
    return user_schema.dump(user), 200

@user_bp.route("/<user_id>", methods=["PUT"])
@jwt_required()
@rank_required("Council")
def update(user_id):
    data = request.get_json()
    updated = update_user(user_id, data)
    if not updated:
        return {"message": "User not found"}, 404
    return user_schema.dump(updated), 200

@user_bp.route("/<user_id>", methods=["DELETE"])
@jwt_required()
@rank_required("Grand Master")
def delete(user_id):
    if not delete_user(user_id):
        return {"message": "User not found"}, 404
    return {"message": "User deleted"}, 200

@user_bp.route("s", methods=["GET"])
@jwt_required()
@rank_required("Council")
def get_all():
    return users_schema.dump(get_all_users()), 200
