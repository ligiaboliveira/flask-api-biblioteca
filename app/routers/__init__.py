from flask import Blueprint

# Create a blueprint for the API
api_bp = Blueprint('api', __name__)

# Import routes to register them without causing circular imports
from .book import list_books, create_book
from .user import list_users, create_user
from .loan import list_loans, create_loan

# Register routes to the blueprint
api_bp.add_url_rule('/books', view_func=list_books, methods=['GET'])
api_bp.add_url_rule('/books', view_func=create_book, methods=['POST'])
api_bp.add_url_rule('/users', view_func=list_users, methods=['GET'])
api_bp.add_url_rule('/users', view_func=create_user, methods=['POST'])
api_bp.add_url_rule('/loans', view_func=list_loans, methods=['GET'])
api_bp.add_url_rule('/loans', view_func=create_loan, methods=['POST'])  # Register the create_loan route
