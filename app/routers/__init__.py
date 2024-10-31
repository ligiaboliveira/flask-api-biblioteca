# app/routers/__init__.py
from flask import Blueprint

# Create a blueprint for the API
api_bp = Blueprint('api', __name__)

# Import routes to register them without causing circular imports
from .book import list_books
from .user import list_users
from .loan import list_loans

# Register routes to the blueprint
api_bp.add_url_rule('/books', view_func=list_books, methods=['GET'])
api_bp.add_url_rule('/users', view_func=list_users, methods=['GET'])
api_bp.add_url_rule('/loans', view_func=list_loans, methods=['GET'])
