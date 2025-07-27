


from db import db
from marshmallow import Schema, fields
from uuid import uuid4
from datetime import datetime

class Padawan(db.Model):
    __tablename__ = "padawans"
    padawan_id = db.Column(db.String, primary_key=True, default=lambda: str(uuid4()))
    master_id = db.Column(db.String, db.ForeignKey("masters.master_id"))
    user_id = db.Column(db.String, db.ForeignKey("users.user_id"))
    species_id = db.Column(db.String, db.ForeignKey("species.species_id"))
    padawan_name = db.Column(db.String, unique=True, nullable=False)
    age = db.Column(db.Integer)
    training_level = db.Column(db.Integer)
    graduation_date = db.Column(db.DateTime)

    courses = db.relationship("PadawanCourse", backref="padawan", cascade="all, delete")

class PadawanSchema(Schema):
    padawan_id = fields.String(dump_only=True)
    master_id = fields.String(required=True)
    user_id = fields.String(required=True)
    species_id = fields.String(required=True)
    padawan_name = fields.String(required=True)
    age = fields.Integer()
    training_level = fields.Integer()
    graduation_date = fields.DateTime()

padawan_schema = PadawanSchema()
padawans_schema = PadawanSchema(many=True)
