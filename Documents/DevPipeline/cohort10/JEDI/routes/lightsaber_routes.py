


from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from controllers.lightsaber_controller import create_saber, update_saber, delete_saber
from models.lightsaber import Lightsaber
from schemas.lightsaber_schema import lightsaber_schema
from util.permissions import owner_only_or_rank

lightsaber_bp = Blueprint("lightsaber_bp", __name__, url_prefix="/lightsaber")

@lightsaber_bp.route("", methods=["POST"])
@jwt_required()
def create():
    data = request.get_json()
    data['owner_id'] = get_jwt_identity()
    saber = create_saber(data)
    return lightsaber_schema.dump(saber), 201

@lightsaber_bp.route("/<saber_id>", methods=["PUT"])
@jwt_required()
@owner_only_or_rank("Council")
def update(saber_id):
    saber = update_saber(saber_id, request.get_json())
    if not saber:
        return {"message": "Saber not found"}, 404
    return lightsaber_schema.dump(saber), 200

@lightsaber_bp.route("/<saber_id>", methods=["DELETE"])
@jwt_required()
@owner_only_or_rank("Council")
def delete(saber_id):
    if not delete_saber(saber_id):
        return {"message": "Not found"}, 404
    return {"message": "Saber destroyed"}, 200

@lightsaber_bp.route("/owner/<owner_id>", methods=["GET"])
@jwt_required()
def get_by_owner(owner_id):
    sabers = Lightsaber.query.filter_by(owner_id=owner_id).all()
    return lightsaber_schema.dump(sabers, many=True), 200
