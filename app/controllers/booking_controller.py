from flask import Blueprint, request, jsonify

booking_bp = Blueprint('booking', __name__)

@booking_bp.route('/booking', methods=['GET'])
def book_retreat():
    data = request.json
    return jsonify({'test':'success'})