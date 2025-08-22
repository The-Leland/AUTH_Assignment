


import uuid
from flask import jsonify
from utils.reflection import get_session, reflect_db

Base, _ = reflect_db()
Company = Base.classes.companies
Product = Base.classes.products
ProductCategoryXref = Base.classes.product_category_xref

def create_company(data):
    session = get_session()
    new_company = Company(company_name=data['company_name'])
    session.add(new_company)
    session.commit()
    return jsonify({'company_id': str(new_company.company_id)})

def get_companies():
    session = get_session()
    companies = session.query(Company).all()
    return jsonify([
        {'company_id': str(c.company_id), 'company_name': c.company_name}
        for c in companies
    ])

def get_company(company_id):
    session = get_session()
    company = session.query(Company).get(company_id)
    if not company:
        return jsonify({'error': 'Company not found'}), 404
    return jsonify({
        'company_id': str(company.company_id),
        'company_name': company.company_name
    })

def update_company(company_id, data):
    session = get_session()
    company = session.query(Company).get(company_id)
    if not company:
        return jsonify({'error': 'Company not found'}), 404
    if 'company_name' in data:
        company.company_name = data['company_name']
    session.commit()
    return jsonify({'updated_company_id': company_id})

def delete_company(company_id):
    session = get_session()
    products = session.query(Product).filter_by(company_id=company_id).all()
    for product in products:
        session.query(ProductCategoryXref).filter_by(product_id=product.product_id).delete()
        session.delete(product)
    session.query(Company).filter_by(company_id=company_id).delete()
    session.commit()
    return jsonify({'deleted_company_id': company_id})
