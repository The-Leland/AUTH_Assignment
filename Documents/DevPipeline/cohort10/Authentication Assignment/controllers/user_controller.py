


import uuid
from flask import jsonify
from db import db
from models.user import User
from models.authtoken import AuthToken
from flask_bcrypt import generate_password_hash, check_password_hash
from datetime import datetime, timedelta

def create_user(data):
    hashed_password = generate_password_hash(data['password']).decode('utf-8')
    new_user = User(email=data['email'], password=hashed_password, role=data.get('role', 'standard'))
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'user_id': str(new_user.user_id)})

def create_auth_token(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({'error': 'Invalid credentials'}), 401
    token = AuthToken(user_id=user.user_id)
    db.session.add(token)
    db.session.commit()
    return jsonify({'auth_token': str(token.auth_token), 'expires': token.expiration.isoformat()})

def update_user(user, user_id, data):
    if user.role != 'admin' and str(user.user_id) != user_id:
        return jsonify({'error': 'Unauthorized'}), 403
    target_user = User.query.get(user_id)
    if not target_user:
        return jsonify({'error': 'User not found'}), 404
    if 'email' in data:
        target_user.email = data['email']
    if 'password' in data:
        target_user.password = generate_password_hash(data['password']).decode('utf-8')
    db.session.commit()
    return jsonify({'updated_user_id': user_id})

def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({'deleted_user_id': user_id})

def get_users(user):
    if user.role != 'admin':
        return jsonify({'error': 'Not authorized'}), 403
    users = User.query.all()
    return jsonify([{'user_id': str(u.user_id), 'email': u.email, 'role': u.role} for u in users])
