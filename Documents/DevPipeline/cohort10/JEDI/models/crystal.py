


from db import db
from marshmallow import Schema, fields
from uuid import uuid4

class Crystal(db.Model):
    __tablename__ = "crystals"
    crystal_id = db.Column(db.String, primary_key=True, default=lambda: str(uuid4()))
    crystal_type = db.Column(db.String, unique=True)
    origin_planet = db.Column(db.String)
    rarity_level = db.Column(db.String)
    force_amplify = db.Column(db.Float)

    sabers = db.relationship("Lightsaber", backref="crystal")

class CrystalSchema(Schema):
    crystal_id = fields.String(dump_only=True)
    crystal_type = fields.String(required=True)
    origin_planet = fields.String()
    rarity_level = fields.String()
    force_amplify = fields.Float()

crystal_schema = CrystalSchema()
crystals_schema = CrystalSchema(many=True)
