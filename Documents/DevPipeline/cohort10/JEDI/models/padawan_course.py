


from db import db
from marshmallow import Schema, fields
from datetime import datetime

class PadawanCourse(db.Model):
    __tablename__ = "padawan_courses"
    padawan_id = db.Column(db.String, db.ForeignKey("padawans.padawan_id"), primary_key=True)
    course_id = db.Column(db.String, db.ForeignKey("courses.course_id"), primary_key=True)
    enrollment_date = db.Column(db.DateTime, default=datetime.utcnow)
    completion_date = db.Column(db.DateTime)
    final_score = db.Column(db.Float)

class PadawanCourseSchema(Schema):
    padawan_id = fields.String(required=True)
    course_id = fields.String(required=True)
    enrollment_date = fields.DateTime()
    completion_date = fields.DateTime()
    final_score = fields.Float()

padawan_course_schema = PadawanCourseSchema()
padawan_courses_schema = PadawanCourseSchema(many=True)

