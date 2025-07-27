


from db import db
from marshmallow import Schema, fields
from uuid import uuid4

class Lightsaber(db.Model):
    __tablename__ = "lightsabers"
    saber_id = db.Column(db.String, primary_key=True, default=lambda: str(uuid4()))
    owner_id = db.Column(db.String, db.ForeignKey("users.user_id"))
    crystal_id = db.Column(db.String, db.ForeignKey("crystals.crystal_id"))
    saber_name = db.Column(db.String, unique=True)
    hilt_material = db.Column(db.String)
    blade_color = db.Column(db.String)
    is_completed = db.Column(db.Boolean)

class LightsaberSchema(Schema):
    saber_id = fields.String(dump_only=True)
    owner_id = fields.String(required=True)
    crystal_id = fields.String(required=True)
    saber_name = fields.String()
    hilt_material = fields.String()
    blade_color = fields.String()
    is_completed = fields.Boolean()

lightsaber_schema = LightsaberSchema()

