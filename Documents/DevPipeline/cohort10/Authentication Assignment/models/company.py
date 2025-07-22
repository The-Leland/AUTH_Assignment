


import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String
from db import db

class Company(db.Model):
    __tablename__ = 'companies'

    company_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    company_name = Column(String, unique=True, nullable=False)
