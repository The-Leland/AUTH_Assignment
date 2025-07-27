


from db import db
from models.user import User
from models.auth_token import AuthToken
from models.lightsaber import Lightsaber

def create_user(data):
    user = User(**data)
    db.session.add(user)
    db.session.commit()
    return user

def get_all_users():
    return User.query.all()

def get_user(user_id):
    return db.session.get(User, user_id)

def update_user(user_id, updates):
    user = get_user(user_id)
    if not user:
        return None
    for key, value in updates.items():
        setattr(user, key, value)
    db.session.commit()
    return user

def delete_user(user_id):
    user = get_user(user_id)
    if not user:
        return False
    AuthToken.query.filter_by(user_id=user_id).delete()
    Lightsaber.query.filter_by(owner_id=user_id).delete()
    db.session.delete(user)
    db.session.commit()
    return True
