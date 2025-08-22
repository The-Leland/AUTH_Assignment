


import uuid
from flask import jsonify
from utils.reflection import get_session, reflect_db

Base, _ = reflect_db()
Category = Base.classes.categories
ProductCategoryXref = Base.classes.product_category_xref

def create_category(data):
    session = get_session()
    category = Category(category_name=data['category_name'])
    session.add(category)
    session.commit()
    return jsonify({'category_id': str(category.category_id)})

def get_categories():
    session = get_session()
    categories = session.query(Category).all()
    return jsonify([{'category_id': str(c.category_id), 'category_name': c.category_name} for c in categories])

def get_category(category_id):
    session = get_session()
    category = session.query(Category).get(category_id)
    if not category:
        return jsonify({'error': 'Category not found'}), 404
    return jsonify({'category_id': str(category.category_id), 'category_name': category.category_name})

def update_category(category_id, data):
    session = get_session()
    category = session.query(Category).get(category_id)
    if not category:
        return jsonify({'error': 'Category not found'}), 404
    category.category_name = data['category_name']
    session.commit()
    return jsonify({'updated_category_id': category_id})

def delete_category(category_id):
    session = get_session()
    session.query(ProductCategoryXref).filter_by(category_id=category_id).delete()
    session.query(Category).filter_by(category_id=category_id).delete()
    session.commit()
    return jsonify({'deleted_category_id': category_id})
