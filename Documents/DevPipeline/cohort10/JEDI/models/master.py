


from db import db
from marshmallow import Schema, fields
from uuid import uuid4

class Master(db.Model):
    __tablename__ = "masters"
    master_id = db.Column(db.String, primary_key=True, default=lambda: str(uuid4()))
    user_id = db.Column(db.String, db.ForeignKey("users.user_id"))
    master_name = db.Column(db.String, unique=True, nullable=False)
    specialization = db.Column(db.String)
    years_training = db.Column(db.Integer)
    max_padawans = db.Column(db.Integer)

    padawans = db.relationship("Padawan", backref="master")
    courses = db.relationship("Course", backref="instructor")

class MasterSchema(Schema):
    master_id = fields.String(dump_only=True)
    user_id = fields.String(required=True)
    master_name = fields.String(required=True)
    specialization = fields.String()
    years_training = fields.Integer()
    max_padawans = fields.Integer()

master_schema = MasterSchema()
masters_schema = MasterSchema(many=True)

