


from functools import wraps
from flask import request, jsonify
from models.authtoken import AuthToken
from models.user import User
from db import db
from datetime import datetime

def get_user_from_token():
    token = request.headers.get('Authorization')
    if not token:
        return None
    token_obj = db.session.query(AuthToken).filter_by(auth_token=token).first()
    if token_obj and token_obj.expiration > datetime.utcnow():
        return token_obj.user
    return None

def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        user = get_user_from_token()
        if not user:
            return jsonify({'error': 'Unauthorized'}), 401
        return f(user, *args, **kwargs)
    return decorated

def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        user = get_user_from_token()
        if not user or user.role != 'admin':
            return jsonify({'error': 'Admin privileges required'}), 403
        return f(user, *args, **kwargs)
    return decorated
