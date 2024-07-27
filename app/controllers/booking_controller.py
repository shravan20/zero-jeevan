from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from app.services.booking_service import BookingService
from app.validations.booking_schema import BookingSchema

booking_bp = Blueprint('booking', __name__)
booking_schema = BookingSchema()
booking_service = BookingService()

@booking_bp.route('/booking', methods=['GET'])
def book_retreat():
    data = request.json
    return jsonify({'test':'success'})

@booking_bp.route('/booking', methods=['POST'])
def add_book_retreat():
    data = request.get_json()
    if request.content_type != 'application/json':
        return jsonify({"message": "Content-Type must be application/json"}), 415
    try:
        data = booking_schema.load(data)
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    result, status_code = booking_service.create_booking(data)
    return jsonify(result), status_code

