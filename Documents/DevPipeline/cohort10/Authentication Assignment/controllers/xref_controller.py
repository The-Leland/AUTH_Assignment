


from flask import jsonify
from db import db
from models.product_category_xref import ProductCategoryXref

def create_xref(data):
    xref = ProductCategoryXref(product_id=data['product_id'], category_id=data['category_id'])
    db.session.add(xref)
    db.session.commit()
    return jsonify({'message': 'xref created'})
