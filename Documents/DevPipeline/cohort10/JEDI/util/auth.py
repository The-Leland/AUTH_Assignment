

from flask_jwt_extended import create_access_token
from datetime import timedelta

def generate_token(user):
    rank_expirations = {
        "Youngling": 15,
        "Padawan": 30,
        "Knight": 60,
        "Master": 120,
        "Council": 240,
        "Grand Master": 360
    }
    minutes = rank_expirations.get(user.force_rank, 15)
    expires = timedelta(minutes=minutes)
    return create_access_token(identity=user.user_id, expires_delta=expires)
