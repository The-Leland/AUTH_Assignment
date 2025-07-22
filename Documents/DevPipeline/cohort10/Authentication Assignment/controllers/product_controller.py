


import uuid
from flask import jsonify
from db import db
from models.product import Product
from models.warranty import Warranty
from models.product_category_xref import ProductCategoryXref
from models.category import Category

def create_product(data):
    new_product = Product(
        company_id=data['company_id'],
        company_name=data['company_name'],
        price=data['price'],
        description=data['description'],
        active=data.get('active', True)
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'product_id': str(new_product.product_id)})

def get_products():
    products = Product.query.all()
    result = []
    for p in products:
        warranty = Warranty.query.filter_by(product_id=p.product_id).first()
        xrefs = ProductCategoryXref.query.filter_by(product_id=p.product_id).all()
        categories = [str(x.category_id) for x in xrefs]
        result.append({
            'product_id': str(p.product_id),
            'company_id': str(p.company_id),
            'company_name': p.company_name,
            'price': p.price,
            'description': p.description,
            'active': p.active,
            'warranty': warranty.warranty_months if warranty else None,
            'categories': categories
        })
    return jsonify(result)

def get_product(product_id):
    p = Product.query.get(product_id)
    if not p:
        return jsonify({'error': 'Product not found'}), 404
    warranty = Warranty.query.filter_by(product_id=product_id).first()
    xrefs = ProductCategoryXref.query.filter_by(product_id=product_id).all()
    categories = [str(x.category_id) for x in xrefs]
    return jsonify({
        'product_id': str(p.product_id),
        'company_id': str(p.company_id),
        'company_name': p.company_name,
        'price': p.price,
        'description': p.description,
        'active': p.active,
        'warranty': warranty.warranty_months if warranty else None,
        'categories': categories
    })

def get_active_products():
    products = Product.query.filter_by(active=True).all()
    return jsonify([{'product_id': str(p.product_id)} for p in products])

def get_products_by_company(company_id):
    products = Product.query.filter_by(company_id=company_id).all()
    return jsonify([{'product_id': str(p.product_id)} for p in products])

def update_product(product_id, data):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    for field in ['company_id', 'company_name', 'price', 'description', 'active']:
        if field in data:
            setattr(product, field, data[field])
    db.session.commit()
    return jsonify({'updated_product_id': product_id})

def delete_product(product_id):
    ProductCategoryXref.query.filter_by(product_id=product_id).delete()
    Warranty.query.filter_by(product_id=product_id).delete()
    Product.query.filter_by(product_id=product_id).delete()
    db.session.commit()
    return jsonify({'deleted_product_id': product_id})
