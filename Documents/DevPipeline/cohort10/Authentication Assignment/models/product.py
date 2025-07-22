


import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from db import db

class Product(db.Model):
    __tablename__ = 'products'

    product_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    company_id = Column(UUID(as_uuid=True), ForeignKey('companies.company_id'), nullable=False)
    company_name = Column(String, nullable=False)
    price = Column(Integer)
    description = Column(String)
    active = Column(Boolean, default=True)
