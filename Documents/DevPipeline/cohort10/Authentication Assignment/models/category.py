


import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String
from db import db

class Category(db.Model):
    __tablename__ = 'categories'

    category_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    category_name = Column(String, unique=True, nullable=False)
