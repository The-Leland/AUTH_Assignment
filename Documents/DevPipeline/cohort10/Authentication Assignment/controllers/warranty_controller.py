


from utils.reflection import get_session, reflect_db
import uuid

Base, engine = reflect_db()
Warranty = Base.classes.warranty

def create_warranty(data):
    session = get_session()
    warranty = Warranty()
    warranty.warranty_id = uuid.uuid4()
    warranty.product_id = data['product_id']
    warranty.warranty_months = data['warranty_months']
    session.add(warranty)
    session.commit()
    return {'warranty_id': str(warranty.warranty_id)}

def get_warranty(warranty_id):
    session = get_session()
    w = session.query(Warranty).get(warranty_id)
    if not w:
        return {'error': 'Warranty not found'}, 404
    return {'warranty_id': str(w.warranty_id), 'warranty_months': w.warranty_months}

def update_warranty(warranty_id, data):
    session = get_session()
    w = session.query(Warranty).get(warranty_id)
    if not w:
        return {'error': 'Warranty not found'}, 404
    if 'warranty_months' in data:
        w.warranty_months = data['warranty_months']
    session.commit()
    return {'updated_warranty_id': warranty_id}

def delete_warranty(warranty_id):
    session = get_session()
    session.query(Warranty).filter_by(warranty_id=warranty_id).delete()
    session.commit()
    return {'deleted_warranty_id': warranty_id}
