


from utils.reflection import get_session, reflect_db
from flask_bcrypt import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import uuid

Base, engine = reflect_db()

User = Base.classes.user
AuthToken = Base.classes.authtoken

def create_user(data):
    session = get_session()
    hashed_password = generate_password_hash(data['password']).decode('utf-8')
    new_user = User()
    new_user.user_id = uuid.uuid4()
    new_user.email = data['email']
    new_user.password = hashed_password
    new_user.role = data.get('role', 'standard')
    session.add(new_user)
    session.commit()
    return {'user_id': str(new_user.user_id)}

def create_auth_token(data):
    session = get_session()
    user = session.query(User).filter_by(email=data['email']).first()
    if not user or not check_password_hash(user.password, data['password']):
        return {'error': 'Invalid credentials'}, 401
    token = AuthToken()
    token.auth_token = uuid.uuid4()
    token.user_id = user.user_id
    token.expiration = datetime.utcnow() + timedelta(hours=1)
    session.add(token)
    session.commit()
    return {'auth_token': str(token.auth_token), 'expires': token.expiration.isoformat()}

def update_user(current_user, user_id, data):
    session = get_session()
    if current_user.role != 'admin' and str(current_user.user_id) != user_id:
        return {'error': 'Unauthorized'}, 403
    target_user = session.query(User).get(user_id)
    if not target_user:
        return {'error': 'User not found'}, 404
    if 'email' in data:
        target_user.email = data['email']
    if 'password' in data:
        target_user.password = generate_password_hash(data['password']).decode('utf-8')
    session.commit()
    return {'updated_user_id': user_id}

def delete_user(user_id):
    session = get_session()
    user = session.query(User).get(user_id)
    if not user:
        return {'error': 'User not found'}, 404
    session.delete(user)
    session.commit()
    return {'deleted_user_id': user_id}

def get_users(current_user):
    session = get_session()
    if current_user.role != 'admin':
        return {'error': 'Not authorized'}, 403
    users = session.query(User).all()
    return [{'user_id': str(u.user_id), 'email': u.email, 'role': u.role} for u in users]

