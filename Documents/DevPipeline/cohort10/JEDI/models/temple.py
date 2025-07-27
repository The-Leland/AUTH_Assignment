


from db import db
from marshmallow import Schema, fields
from uuid import uuid4

class Temple(db.Model):
    __tablename__ = "temples"
    temple_id = db.Column(db.String, primary_key=True, default=lambda: str(uuid4()))
    temple_name = db.Column(db.String, unique=True, nullable=False)
    planet = db.Column(db.String)
    master_count = db.Column(db.Integer)
    padawan_limit = db.Column(db.Integer)
    is_active = db.Column(db.Boolean, default=True)

    users = db.relationship("User", backref="temple")

class TempleSchema(Schema):
    temple_id = fields.String(dump_only=True)
    temple_name = fields.String(required=True)
    planet = fields.String()
    master_count = fields.Integer()
    padawan_limit = fields.Integer()
    is_active = fields.Boolean()

temple_schema = TempleSchema()
temples_schema = TempleSchema(many=True)
