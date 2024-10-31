from flask import jsonify, request
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

@api_bp.route('/users', methods=['POST'])
@swag_from({
    'parameters': [
        {
            'name': 'body',
            'description': 'User data to create a new user',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {
                        'type': 'string',
                        'example': 'John Doe'
                    },
                    'email': {
                        'type': 'string',
                        'example': 'johndoe@example.com'
                    },
                },
                'required': ['name', 'email']
            }
        }
    ],
    'responses': {
        201: {
            'description': 'User created successfully',
            'schema': {
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
        },
        400: {
            'description': 'Invalid input',
            'schema': {
                'type': 'object',
                'properties': {
                    'error': {
                        'type': 'string',
                        'example': 'Invalid email format'
                    }
                }
            }
        }
    }
})
def create_user():
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    new_user = User(name=data['name'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        'id': new_user.id,
        'name': new_user.name,
        'email': new_user.email
    }), 201
