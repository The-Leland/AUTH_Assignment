


from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from controllers.crystal_controller import create_crystal, get_crystals_by_rarity
from schemas.crystal_schema import crystal_schema, crystals_schema
from util.permissions import rank_required

crystal_bp = Blueprint("crystal_bp", __name__, url_prefix="/crystal")

@crystal_bp.route("", methods=["POST"])
@jwt_required()
@rank_required("Master")
def create():
    crystal = create_crystal(request.get_json())
    return crystal_schema.dump(crystal), 201

@crystal_bp.route("/<rarity_level>", methods=["GET"])
@jwt_required()
@rank_required("Master")
def view_by_rarity(rarity_level):
    crystals = get_crystals_by_rarity(rarity_level)
    return crystals_schema.dump(crystals), 200

