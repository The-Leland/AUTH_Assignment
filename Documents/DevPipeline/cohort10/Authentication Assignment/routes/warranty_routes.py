


from flask import Blueprint, request
from controllers import warranty_controller
from lib.authenticate import auth_required, admin_required
bp = Blueprint('warranties', __name__)

@bp.route('/warranty', methods=['POST'])
@admin_required
def create_warranty(current_user):
    return warranty_controller.create_warranty(request.json)

@bp.route('/warranty/<id>', methods=['GET'])
def get_warranty(id):
    return warranty_controller.get_warranty(id)

@bp.route('/warranty/<id>', methods=['PUT'])
@admin_required
def update_warranty(current_user, id):
    return warranty_controller.update_warranty(id, request.json)

@bp.route('/warranty/delete', methods=['DELETE'])
@admin_required
def delete_warranty(current_user):
    return warranty_controller.delete_warranty(request.args.get('id'))
