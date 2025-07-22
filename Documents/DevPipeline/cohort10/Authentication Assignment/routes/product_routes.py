


from flask import Blueprint, request
from controllers import product_controller
from lib.authenticate import auth_required, admin_required
bp = Blueprint('products', __name__)

@bp.route('/product', methods=['POST'])
@admin_required
def create_product(current_user):
    return product_controller.create_product(request.json)

@bp.route('/products', methods=['GET'])
def get_products():
    return product_controller.get_products()

@bp.route('/product/<id>', methods=['GET'])
def get_product(id):
    return product_controller.get_product(id)

@bp.route('/products/active', methods=['GET'])
def get_active_products():
    return product_controller.get_active_products()

@bp.route('/product/company/<id>', methods=['GET'])
def get_by_company(id):
    return product_controller.get_products_by_company(id)

@bp.route('/product/<id>', methods=['PUT'])
@admin_required
def update_product(current_user, id):
    return product_controller.update_product(id, request.json)

@bp.route('/product/delete', methods=['DELETE'])
@admin_required
def delete_product(current_user):
    return product_controller.delete_product(request.args.get('id'))
