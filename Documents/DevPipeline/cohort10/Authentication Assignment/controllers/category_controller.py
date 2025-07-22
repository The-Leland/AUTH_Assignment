


import uuid
from flask import jsonify
from db import db
from models.category import Category
from models.product_category_xref import ProductCategoryXref

def create_category(data):
    category = Category(category_name=data['category_name'])
    db.session.add(category)
    db.session.commit()
    return jsonify({'category_id': str(category.category_id)})

def get_categories():
    categories = Category.query.all()
    return jsonify([{'category_id': str(c.category_id), 'category_name': c.category_name} for c in categories])

def get_category(category_id):
    category = Category.query.get(category_id)
    if not category:
        return jsonify({'error': 'Category not found'}), 404
    return jsonify({'category_id': str(category.category_id), 'category_name': category.category_name})

def update_category(category_id, data):
    category = Category.query.get(category_id)
    if not category:
        return jsonify({'error': 'Category not found'}), 404
    category.category_name = data['category_name']
    db.session.commit()
    return jsonify({'updated_category_id': category_id})

def delete_category(category_id):
    ProductCategoryXref.query.filter_by(category_id=category_id).delete()
    Category.query.filter_by(category_id=category_id).delete()
    db.session.commit()
    return jsonify({'deleted_category_id': category_id})
