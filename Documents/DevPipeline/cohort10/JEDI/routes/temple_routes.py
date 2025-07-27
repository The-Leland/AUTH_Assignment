


from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from controllers.temple_controller import *
from schemas.temple_schema import temple_schema
from util.permissions import rank_required

temple_bp = Blueprint("temple_bp", __name__, url_prefix="/temple")

@temple_bp.route("", methods=["POST"])
@jwt_required()
@rank_required("Grand Master")
def create():
    temple = create_temple(request.get_json())
    return temple_schema.dump(temple), 201

@temple_bp.route("/<temple_id>", methods=["GET"])
@jwt_required()
def view(temple_id):
    temple = get_temple(temple_id)
    if not temple:
        return {"message": "Not found"}, 404
    return temple_schema.dump(temple), 200

@temple_bp.route("/<temple_id>", methods=["PUT"])
@jwt_required()
@rank_required("Grand Master")
def update(temple_id):
    updated = update_temple(temple_id, request.get_json())
    if not updated:
        return {"message": "Not found"}, 404
    return temple_schema.dump(updated), 200

@temple_bp.route("/<temple_id>", methods=["DELETE"])
@jwt_required()
@rank_required("Grand Master")
def deactivate(temple_id):
    if not delete_temple(temple_id):
        return {"message": "Not found"}, 404
    return {"message": "Deactivated"}, 200
