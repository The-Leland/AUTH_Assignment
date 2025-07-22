


from flask import Blueprint, request
from controllers import category_controller
from lib.authenticate import auth_required, admin_required
bp = Blueprint('categories', __name__)

@bp.route('/category', methods=['POST'])
@admin_required
def create_category(current_user):
    return category_controller.create_category(request.json)

@bp.route('/categories', methods=['GET'])
def get_categories():
    return category_controller.get_categories()

@bp.route('/category/<id>', methods=['GET'])
def get_category(id):
    return category_controller.get_category(id)

@bp.route('/category/<id>', methods=['PUT'])
@admin_required
def update_category(current_user, id):
    return category_controller.update_category(id, request.json)

@bp.route('/category/delete', methods=['DELETE'])
@admin_required
def delete_category(current_user):
    return category_controller.delete_category(request.args.get('id'))
