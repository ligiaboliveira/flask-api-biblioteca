from flask import request, jsonify
from flasgger import swag_from
from app import db
from app.models import Book
from . import api_bp

@api_bp.route('/books', methods=['GET'])
@swag_from({
    'responses': {
        200: {
            'description': 'List of books',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {
                            'type': 'integer',
                            'example': 1
                        },
                        'title': {
                            'type': 'string',
                            'example': 'The Great Gatsby'
                        },
                        'author': {
                            'type': 'string',
                            'example': 'F. Scott Fitzgerald'
                        },
                    }
                }
            }
        }
    }
})
def list_books():
    books = Book.query.all()
    return jsonify([{'id': book.id, 'title': book.title, 'author': book.author} for book in books])

@api_bp.route('/books', methods=['POST'])
@swag_from({
    'parameters': [
        {
            'name': 'book',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'title': {
                        'type': 'string',
                        'example': 'The Great Gatsby'
                    },
                    'author': {
                        'type': 'string',
                        'example': 'F. Scott Fitzgerald'
                    }
                },
                'required': ['title', 'author']
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Book created',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {
                        'type': 'integer',
                        'example': 1
                    },
                    'title': {
                        'type': 'string',
                        'example': 'The Great Gatsby'
                    },
                    'author': {
                        'type': 'string',
                        'example': 'F. Scott Fitzgerald'
                    }
                }
            }
        },
        400: {
            'description': 'Invalid input'
        }
    }
})
def create_book():
    data = request.json
    if not data or 'title' not in data or 'author' not in data:
        return jsonify({"error": "Invalid input"}), 400

    new_book = Book(title=data['title'], author=data['author'])
    db.session.add(new_book)
    db.session.commit()

    return jsonify({'id': new_book.id, 'title': new_book.title, 'author': new_book.author}), 201
