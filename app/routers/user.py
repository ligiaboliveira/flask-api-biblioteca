# app/routers/user.py
from flask import jsonify
from flasgger import swag_from
from app import db
from app.models import User
from app.schemas import UserSchema  # Import the UserSchema
from . import api_bp

@api_bp.route('/users', methods=['GET'])
@swag_from({
    'responses': {
        200: {
            'description': 'List of users',
            'schema': UserSchema(many=True).fields,  # Use the schema
        }
    }
})
def list_users():
    users = User.query.all()
    user_schema = UserSchema(many=True)  # Initialize schema for multiple users
    return jsonify(user_schema.dump(users))  # Serialize and return
