


import uuid
from flask import jsonify
from db import db
from models.warranty import Warranty

def create_warranty(data):
    warranty = Warranty(product_id=data['product_id'], warranty_months=data['warranty_months'])
    db.session.add(warranty)
    db.session.commit()
    return jsonify({'warranty_id': str(warranty.warranty_id)})

def get_warranty(warranty_id):
    w = Warranty.query.get(warranty_id)
    if not w:
        return jsonify({'error': 'Warranty not found'}), 404
    return jsonify({'warranty_id': str(w.warranty_id), 'warranty_months': w.warranty_months})

def update_warranty(warranty_id, data):
    w = Warranty.query.get(warranty_id)
    if not w:
        return jsonify({'error': 'Warranty not found'}), 404
    if 'warranty_months' in data:
        w.warranty_months = data['warranty_months']
    db.session.commit()
    return jsonify({'updated_warranty_id': warranty_id})

def delete_warranty(warranty_id):
    Warranty.query.filter_by(warranty_id=warranty_id).delete()
    db.session.commit()
    return jsonify({'deleted_warranty_id': warranty_id})
