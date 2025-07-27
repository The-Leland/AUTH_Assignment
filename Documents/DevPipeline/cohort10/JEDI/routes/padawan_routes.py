


from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from controllers.padawan_controller import *
from schemas.padawan_schema import padawan_schema, padawans_schema
from util.permissions import rank_required

padawan_bp = Blueprint("padawan_bp", __name__, url_prefix="/padawan")

@padawan_bp.route("", methods=["POST"])
@jwt_required()
@rank_required("Master")
def create():
    padawan = create_padawan(request.get_json())
    return padawan_schema.dump(padawan), 201

@padawan_bp.route("/<padawan_id>/promote", methods=["PUT"])
@jwt_required()
@rank_required("Council")
def promote(padawan_id):
    padawan = promote_padawan(padawan_id)
    if not padawan:
        return {"message": "Not found"}, 404
    return padawan_schema.dump(padawan), 200

@padawan_bp.route("/<padawan_id>", methods=["PUT"])
@jwt_required()
@rank_required("Master")
def update(padawan_id):
    updated = update_padawan(padawan_id, request.get_json())
    if not updated:
        return {"message": "Not found"}, 404
    return padawan_schema.dump(updated), 200

@padawan_bp.route("/<padawan_id>", methods=["DELETE"])
@jwt_required()
@rank_required("Council")
def delete(padawan_id):
    if not delete_padawan(padawan_id):
        return {"message": "Not found"}, 404
    return {"message": "Deleted"}, 200

