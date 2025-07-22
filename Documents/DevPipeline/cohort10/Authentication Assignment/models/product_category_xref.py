


from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from db import db

class ProductCategoryXref(db.Model):
    __tablename__ = 'productscategoriesxref'

    product_id = Column(UUID(as_uuid=True), ForeignKey('products.product_id'), primary_key=True)
    category_id = Column(UUID(as_uuid=True), ForeignKey('categories.category_id'), primary_key=True)

