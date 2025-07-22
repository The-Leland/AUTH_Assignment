


import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, ForeignKey
from db import db

class Warranty(db.Model):
    __tablename__ = 'warranties'

    warranty_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    product_id = Column(UUID(as_uuid=True), ForeignKey('products.product_id'), nullable=False)
    warranty_months = Column(String, nullable=False)

