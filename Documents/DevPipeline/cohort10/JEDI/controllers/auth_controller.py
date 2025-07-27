


from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash
from models.user import User
from datetime import timedelta

def get_token_expiration(rank):
    if rank == "Grand Master":
        return timedelta(days=30)
    elif rank == "Council":
        return timedelta(days=14)
    elif rank == "Master":
        return timedelta(days=7)
    else:
        return timedelta(hours=2)

def authenticate_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        expires = get_token_expiration(user.force_rank)
        token = create_access_token(identity=user.user_id, expires_delta=expires)
        return token, user
    return None, None
