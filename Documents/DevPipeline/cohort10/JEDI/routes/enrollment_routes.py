


from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from controllers.padawan_course_controller import *
from schemas.padawan_course_schema import padawan_course_schema
from util.permissions import rank_required

enroll_bp = Blueprint("enroll_bp", __name__, url_prefix="/enrollment")

@enroll_bp.route("", methods=["POST"])
@jwt_required()
@rank_required("Master")
def enroll():
    enrollment = enroll_padawan(request.get_json())
    return padawan_course_schema.dump(enrollment), 201

@enroll_bp.route("/<padawan_id>/<course_id>", methods=["DELETE"])
@jwt_required()
@rank_required("Master")
def remove(padawan_id, course_id):
    if not remove_enrollment(padawan_id, course_id):
        return {"message": "Not found"}, 404
    return {"message": "Removed"}, 200
