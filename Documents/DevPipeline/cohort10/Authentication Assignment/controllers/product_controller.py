


from utils.reflection import get_session, reflect_db
import uuid

Base, engine = reflect_db()

Product = Base.classes.product
Warranty = Base.classes.warranty
ProductCategoryXref = Base.classes.product_category_xref
Category = Base.classes.category

def create_product(data):
    session = get_session()
    new_product = Product()
    new_product.product_id = uuid.uuid4()
    new_product.company_id = data['company_id']
    new_product.company_name = data['company_name']
    new_product.price = data['price']
    new_product.description = data['description']
    new_product.active = data.get('active', True)
    
    session.add(new_product)
    session.commit()
    return {'product_id': str(new_product.product_id)}

def get_products():
    session = get_session()
    products = session.query(Product).all()
    result = []
    for p in products:
        warranty = session.query(Warranty).filter_by(product_id=p.product_id).first()
        xrefs = session.query(ProductCategoryXref).filter_by(product_id=p.product_id).all()
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
    return result

def get_product(product_id):
    session = get_session()
    p = session.query(Product).get(product_id)
    if not p:
        return {'error': 'Product not found'}, 404
    warranty = session.query(Warranty).filter_by(product_id=product_id).first()
    xrefs = session.query(ProductCategoryXref).filter_by(product_id=product_id).all()
    categories = [str(x.category_id) for x in xrefs]
    return {
        'product_id': str(p.product_id),
        'company_id': str(p.company_id),
        'company_name': p.company_name,
        'price': p.price,
        'description': p.description,
        'active': p.active,
        'warranty': warranty.warranty_months if warranty else None,
        'categories': categories
    }

def get_active_products():
    session = get_session()
    products = session.query(Product).filter_by(active=True).all()
    return [{'product_id': str(p.product_id)} for p in products]

def get_products_by_company(company_id):
    session = get_session()
    products = session.query(Product).filter_by(company_id=company_id).all()
    return [{'product_id': str(p.product_id)} for p in products]

def update_product(product_id, data):
    session = get_session()
    product = session.query(Product).get(product_id)
    if not product:
        return {'error': 'Product not found'}, 404
    for field in ['company_id', 'company_name', 'price', 'description', 'active']:
        if field in data:
            setattr(product, field, data[field])
    session.commit()
    return {'updated_product_id': str(product_id)}

def delete_product(product_id):
    session = get_session()
    session.query(ProductCategoryXref).filter_by(product_id=product_id).delete()
    session.query(Warranty).filter_by(product_id=product_id).delete()
    session.query(Product).filter_by(product_id=product_id).delete()
    session.commit()
    return {'deleted_product_id': str(product_id)}
