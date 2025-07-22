


import uuid
from flask import jsonify
from db import db
from models.company import Company
from models.product import Product
from models.product_category_xref import ProductCategoryXref

def create_company(data):
    new_company = Company(company_name=data['company_name'])
    db.session.add(new_company)
    db.session.commit()
    return jsonify({'company_id': str(new_company.company_id)})

def get_companies():
    companies = Company.query.all()
    return jsonify([{'company_id': str(c.company_id), 'company_name': c.company_name} for c in companies])

def get_company(company_id):
    company = Company.query.get(company_id)
    if not company:
        return jsonify({'error': 'Company not found'}), 404
    return jsonify({'company_id': str(company.company_id), 'company_name': company.company_name})

def update_company(company_id, data):
    company = Company.query.get(company_id)
    if not company:
        return jsonify({'error': 'Company not found'}), 404
    if 'company_name' in data:
        company.company_name = data['company_name']
    db.session.commit()
    return jsonify({'updated_company_id': company_id})

def delete_company(company_id):
    products = Product.query.filter_by(company_id=company_id).all()
    for p in products:
        ProductCategoryXref.query.filter_by(product_id=p.product_id).delete()
        db.session.delete(p)
    Company.query.filter_by(company_id=company_id).delete()
    db.session.commit()
    return jsonify({'deleted_company_id': company_id})
