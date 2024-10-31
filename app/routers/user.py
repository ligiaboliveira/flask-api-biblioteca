from flask import jsonify
from flasgger import swag_from
from app import db
from app.models import User
from . import api_bp

@api_bp.route('/users', methods=['GET'])
@swag_from({
    'responses': {
        200: {
            'description': 'List of users',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {
                            'type': 'integer',
                            'example': 1
                        },
                        'name': {
                            'type': 'string',
                            'example': 'John Doe'
                        },
                        'email': {
                            'type': 'string',
                            'example': 'johndoe@example.com'
                        },
                    }
                }
            }
        }
    }
})
def list_users():
    users = User.query.all()
    return jsonify([{
        'id': user.id,
        'name': user.name,
        'email': user.email
    } for user in users])
