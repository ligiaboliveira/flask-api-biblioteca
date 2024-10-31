# app/routes.py
from flask import Blueprint, jsonify
from flasgger import Swagger, swag_from
from app import db
from app.models import User, Book, Loan

# Create a blueprint for routes
api_bp = Blueprint('api', __name__)

# Initialize Swagger
swagger = Swagger(api_bp)

@api_bp.route('/users', methods=['GET'])
@swag_from({
    'responses': {
        200: {
            'description': 'List of users',
            'schema': User.__name__
        }
    }
})
def list_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'name': user.name, 'email': user.email} for user in users])

@api_bp.route('/books', methods=['GET'])
@swag_from({
    'responses': {
        200: {
            'description': 'List of books',
            'schema': Book.__name__
        }
    }
})
def list_books():
    books = Book.query.all()
    return jsonify([{'id': book.id, 'title': book.title, 'author': book.author} for book in books])

@api_bp.route('/loans', methods=['GET'])
@swag_from({
    'responses': {
        200: {
            'description': 'List of loans',
            'schema': Loan.__name__
        }
    }
})
def list_loans():
    loans = Loan.query.all()
    return jsonify([{'id': loan.id, 'book_id': loan.book_id, 'user_id': loan.user_id, 'loan_date': loan.loan_date, 'return_date': loan.return_date} for loan in loans])

# Register the blueprint with the main app
def register_routes(app):
    app.register_blueprint(api_bp, url_prefix='/api')
