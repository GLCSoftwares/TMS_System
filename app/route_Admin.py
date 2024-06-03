from flask import Blueprint, request, jsonify

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin', methods=['GET'])
def admin_example():
    return jsonify({'message': 'Admin respones'}), 200
