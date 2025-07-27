


from db import db
from marshmallow import Schema, fields
from uuid import uuid4

class Course(db.Model):
    __tablename__ = "courses"
    course_id = db.Column(db.String, primary_key=True, default=lambda: str(uuid4()))
    instructor_id = db.Column(db.String, db.ForeignKey("masters.master_id"))
    course_name = db.Column(db.String, unique=True)
    difficulty = db.Column(db.String)
    duration_weeks = db.Column(db.Integer)
    max_students = db.Column(db.Integer)

    enrollments = db.relationship("PadawanCourse", backref="course", cascade="all, delete")

class CourseSchema(Schema):
    course_id = fields.String(dump_only=True)
    instructor_id = fields.String(required=True)
    course_name = fields.String(required=True)
    difficulty = fields.String()
    duration_weeks = fields.Integer()
    max_students = fields.Integer()

course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)

