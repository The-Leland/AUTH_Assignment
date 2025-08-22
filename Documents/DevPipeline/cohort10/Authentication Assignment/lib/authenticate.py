


from functools import wraps
from flask import request, jsonify
from datetime import datetime
from utils.reflection import get_session, reflect_db

Base, engine = reflect_db()
AuthToken = Base.classes.authtoken
User = Base.classes.user

def get_user_from_token():
    token = request.headers.get('Authorization')
    if not token:
        return None
    session = get_session()
    token_obj = session.query(AuthToken).filter_by(auth_token=token).first()
    if token_obj and token_obj.expiration > datetime.utcnow():
        user = session.query(User).get(token_obj.user_id)
        return user
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
