


from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from controllers.species_controller import create_species
from models.species import Species
from schemas.species_schema import species_schema, species_list_schema
from util.permissions import rank_required

species_bp = Blueprint("species_bp", __name__, url_prefix="/species")

@species_bp.route("", methods=["POST"])
@jwt_required()
@rank_required("Master")
def create():
    species = create_species(request.get_json())
    return species_schema.dump(species), 201

@species_bp.route("/<species_id>", methods=["GET"])
@jwt_required()
def get(species_id):
    species = Species.query.get(species_id)
    if not species:
        return {"message": "Species not found"}, 404
    return species_schema.dump(species), 200

@species_bp.route("", methods=["GET"])
@jwt_required()
def all_species():
    return species_list_schema.dump(Species.query.all()), 200
