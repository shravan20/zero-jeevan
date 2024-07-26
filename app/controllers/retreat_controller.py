from flask import Blueprint, request, jsonify

retreat_bp = Blueprint('retreat', __name__)

@retreat_bp.route('/retreats', methods=['GET'])
def get_retreats():
    return jsonify({
        'message': 'retreat api'
    })


