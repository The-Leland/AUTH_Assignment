


from flask import Blueprint, request
from controllers import company_controller
from lib.authenticate import auth_required, admin_required
bp = Blueprint('companies', __name__)

@bp.route('/company', methods=['POST'])
@admin_required
def create_company(current_user):
    return company_controller.create_company(request.json)

@bp.route('/companies', methods=['GET'])
def get_companies():
    return company_controller.get_companies()

@bp.route('/company/<id>', methods=['GET'])
def get_company(id):
    return company_controller.get_company(id)

@bp.route('/company/<id>', methods=['PUT'])
@admin_required
def update_company(current_user, id):
    return company_controller.update_company(id, request.json)

@bp.route('/company/delete', methods=['DELETE'])
@admin_required
def delete_company(current_user):
    return company_controller.delete_company(request.args.get('id'))
