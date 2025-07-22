


from flask import Blueprint, request
from controllers import user_controller
from lib.authenticate import auth_required
bp = Blueprint('users', __name__)

@bp.route('/user', methods=['POST'])
def create_user():
    return user_controller.create_user(request.json)

@bp.route('/auth', methods=['POST'])
def create_auth():
    return user_controller.create_auth_token(request.json)

@bp.route('/users', methods=['GET'])
@auth_required
def get_users(current_user):
    return user_controller.get_users(current_user)

@bp.route('/user/<id>', methods=['PUT'])
@auth_required
def update_user(current_user, id):
    return user_controller.update_user(current_user, id, request.json)

@bp.route('/user/delete', methods=['DELETE'])
@auth_required
def delete_user(current_user):
    return user_controller.delete_user(str(current_user.user_id))
