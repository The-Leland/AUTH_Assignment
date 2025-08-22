


from utils.reflection import get_session, reflect_db

Base, engine = reflect_db()
ProductCategoryXref = Base.classes.product_category_xref

def create_xref(data):
    session = get_session()
    xref = ProductCategoryXref()
    xref.product_id = data['product_id']
    xref.category_id = data['category_id']
    session.add(xref)
    session.commit()
    return {'message': 'xref created'}


