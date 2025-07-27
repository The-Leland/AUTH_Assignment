


from db import db
from marshmallow import Schema, fields
from uuid import uuid4
from datetime import datetime

class AuthToken(db.Model):
    __tablename__ = "authtokens"
    auth_token = db.Column(db.String, primary_key=True, default=lambda: str(uuid4()))
    user_id = db.Column(db.String, db.ForeignKey("users.user_id"))
    expiration_date = db.Column(db.DateTime, nullable=False)

class AuthTokenSchema(Schema):
    auth_token = fields.String(dump_only=True)
    user_id = fields.String(required=True)
    expiration_date = fields.DateTime()

auth_token_schema = AuthTokenSchema()
