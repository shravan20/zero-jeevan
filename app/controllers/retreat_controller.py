from flask import Blueprint, request, jsonify
from app.services.retreat_service import RetreatService
from marshmallow.exceptions import ValidationError

from app.validations.retreat_schema import RetreatSchema

retreat_bp = Blueprint('retreat', __name__)
retreat_schema = RetreatSchema()
service = RetreatService()

@retreat_bp.route('/retreats', methods=['GET'])
def get_retreats():
    filters = {}
    search = request.args.get('search')
    if search:
        filters['title'] = search

    location = request.args.get('location')
    if location:
        filters['location'] = location
    
    filter_criteria = {k: v for k, v in filters.items() if v}

    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))

    result, status_code = service.get_retreats(filters=filter_criteria, page=page, limit=limit)
    return jsonify(result), status_code

@retreat_bp.route('/retreats/<int:retreat_id>', methods=['GET'])
def get_retreat_by_id(retreat_id):
    result, status_code = service.get_retreat_by_id(retreat_id)
    return jsonify(result), status_code


@retreat_bp.route('/retreats', methods=['POST'])
def create_retreat():
    if request.content_type != 'application/json':
        return jsonify({"message": "Content-Type must be application/json"}), 415

    data = request.get_json()
    try:
        retreat_schema.load(data)
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400


    data = request.get_json()
    result, status_code = service.create_retreat(data)
    return jsonify(result), status_code