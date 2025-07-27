
from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request
from functools import wraps
from models.user import User
from db import db
from flask import jsonify

RANKS = ["Youngling", "Padawan", "Knight", "Master", "Council", "Grand Master"]

def rank_required(min_rank):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            user_id = get_jwt_identity()
            user = db.session.get(User, user_id)
            if not user:
                return jsonify({"message": "User not found"}), 404

            if RANKS.index(user.force_rank) < RANKS.index(min_rank):
                return jsonify({"message": f"{min_rank}+ rank required"}), 403

            return fn(*args, **kwargs)
        return decorator
    return wrapper
