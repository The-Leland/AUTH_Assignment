


from flask import Blueprint, request
from controllers import xref_controller
from lib.authenticate import auth_required, admin_required
bp = Blueprint('xref', __name__)

@bp.route('/product/category', methods=['POST'])
@admin_required
def create_xref(current_user):
    return xref_controller.create_xref(request.json)
