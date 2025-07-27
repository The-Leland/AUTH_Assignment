


from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from util.decorators import rank_required
from models.course import CourseSchema
from controllers.course_controller import create_course, get_courses_by_difficulty

course_bp = Blueprint("course_routes", __name__, url_prefix="/courses")
course_schema = CourseSchema()
course_list_schema = CourseSchema(many=True)

@course_bp.route("", methods=["POST"])
@jwt_required()
@rank_required("Master")
def add_course():
    data = request.get_json()
    course = create_course(data)
    return course_schema.dump(course), 201

@course_bp.route("/<difficulty>", methods=["GET"])
@jwt_required()
def get_by_difficulty(difficulty):
    courses = get_courses_by_difficulty(difficulty)
    return course_list_schema.dump(courses), 200
