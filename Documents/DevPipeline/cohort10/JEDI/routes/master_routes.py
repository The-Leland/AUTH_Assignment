


from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from controllers.master_controller import *
from schemas.master_schema import master_schema, masters_schema
from util.permissions import rank_required

master_bp = Blueprint("master_bp", __name__, url_prefix="/master")

@master_bp.route("", methods=["POST"])
@jwt_required()
@rank_required("Council")
def promote():
    master = create_master(request.get_json())
    return master_schema.dump(master), 201

@master_bp.route("/<master_id>", methods=["PUT"])
@jwt_required()
@rank_required("Council")
def update(master_id):
    updated = update_master(master_id, request.get_json())
    if not updated:
        return {"message": "Not found"}, 404
    return master_schema.dump(updated), 200

@master_bp.route("/<master_id>", methods=["DELETE"])
@jwt_required()
@rank_required("Grand Master")
def delete(master_id):
    if not delete_master(master_id):
        return {"message": "Not found"}, 404
    return {"message": "Deleted"}, 200

@master_bp.route("s", methods=["GET"])
@jwt_required()
@rank_required("Padawan")
def list_masters():
    return masters_schema.dump(get_masters()), 200
