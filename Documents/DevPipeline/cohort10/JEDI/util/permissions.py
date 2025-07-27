

from flask_jwt_extended import get_jwt_identity
from functools import wraps
from flask import request, jsonify
from models.user import User

RANK_HIERARCHY = {
    "Youngling": 0,
    "Padawan": 1,
    "Knight": 2,
    "Master": 3,
    "Council": 4,
    "Grand Master": 5
}

def rank_required(required_rank):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            user_id = get_jwt_identity()
            user = User.query.get(user_id)
            if not user:
                return jsonify({"message": "User not found"}), 404

            user_rank = user.force_rank
            if RANK_HIERARCHY.get(user_rank, -1) < RANK_HIERARCHY.get(required_rank, 999):
                return jsonify({"message": f"{required_rank}+ required"}), 403

            return fn(*args, **kwargs)
        return wrapper
    return decorator

def self_or_rank(required_rank):
    def decorator(fn):
        @wraps(fn)
        def wrapper(user_id, *args, **kwargs):
            current_user_id = get_jwt_identity()
            user = User.query.get(current_user_id)
            if not user:
                return jsonify({"message": "User not found"}), 404

            if current_user_id != user_id and RANK_HIERARCHY.get(user.force_rank, 0) < RANK_HIERARCHY.get(required_rank, 0):
                return jsonify({"message": "Unauthorized"}), 403

            return fn(user_id, *args, **kwargs)
        return wrapper
    return decorator

def owner_only_or_rank(required_rank):
    def decorator(fn):
        @wraps(fn)
        def wrapper(saber_id, *args, **kwargs):
            from models.lightsaber import Lightsaber
            saber = Lightsaber.query.get(saber_id)
            if not saber:
                return jsonify({"message": "Saber not found"}), 404

            current_user_id = get_jwt_identity()
            user = User.query.get(current_user_id)

            if saber.owner_id != current_user_id and RANK_HIERARCHY.get(user.force_rank, 0) < RANK_HIERARCHY.get(required_rank, 0):
                return jsonify({"message": "Permission denied"}), 403

            return fn(saber_id, *args, **kwargs)
        return wrapper
    return decorator
