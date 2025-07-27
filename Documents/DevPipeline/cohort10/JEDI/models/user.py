


from db import db
from marshmallow import Schema, fields, validates, ValidationError
from uuid import uuid4
from datetime import datetime

class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.String, primary_key=True, default=lambda: str(uuid4()))
    temple_id = db.Column(db.String, db.ForeignKey("temples.temple_id"))
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    force_rank = db.Column(db.String, nullable=False)
    midi_count = db.Column(db.Integer, nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    joined_date = db.Column(db.DateTime, default=datetime.utcnow)

    padawan = db.relationship("Padawan", backref="user", uselist=False)
    master = db.relationship("Master", backref="user", uselist=False)
    lightsabers = db.relationship("Lightsaber", backref="owner")
    tokens = db.relationship("AuthToken", backref="user", cascade="all, delete")

class UserSchema(Schema):
    user_id = fields.String(dump_only=True)
    temple_id = fields.String(required=True)
    username = fields.String(required=True)
    email = fields.Email(required=True)
    force_rank = fields.String(required=True)
    midi_count = fields.Integer(required=True)
    is_active = fields.Boolean()
    joined_date = fields.DateTime(dump_only=True)

    @validates("force_rank")
    def validate_rank(self, value):
        valid_ranks = ["Youngling", "Padawan", "Knight", "Master", "Council", "Grand Master"]
        if value not in valid_ranks:
            raise ValidationError("Invalid Force rank.")

user_schema = UserSchema()
users_schema = UserSchema(many=True)

