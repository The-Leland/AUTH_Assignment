


from db import db
from marshmallow import Schema, fields
from uuid import uuid4

class Species(db.Model):
    __tablename__ = "species"
    species_id = db.Column(db.String, primary_key=True, default=lambda: str(uuid4()))
    species_name = db.Column(db.String, unique=True)
    homeworld = db.Column(db.String)
    forse_sensitive = db.Column(db.Boolean)
    avg_lifespan = db.Column(db.Integer)

    padawans = db.relationship("Padawan", backref="species")

class SpeciesSchema(Schema):
    species_id = fields.String(dump_only=True)
    species_name = fields.String(required=True)
    homeworld = fields.String()
    forse_sensitive = fields.Boolean()
    avg_lifespan = fields.Integer()

species_schema = SpeciesSchema()
species_list_schema = SpeciesSchema(many=True)
