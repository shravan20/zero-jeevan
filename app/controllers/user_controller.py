from flask import Blueprint, request, jsonify
from app.services.user_service import UserService

user_bp = Blueprint('user', __name__)
service = UserService()

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.json
    result = service.create_user(data)
    return jsonify(result)

@user_bp.route('/users', methods=['GET'])
def get_users():
    result, status_code = service.get_users()
    return jsonify(result)
