# app/routers/book.py
from flask import jsonify
from flasgger import swag_from
from app import db
from app.models import Book
from app.schemas import BookSchema
from . import api_bp

@api_bp.route('/books', methods=['GET'])
@swag_from({
    'responses': {
        200: {
            'description': 'List of books',
            'schema': BookSchema(many=True).fields,  # Correctly reference schema fields
        }
    }
})
def list_books():
    books = Book.query.all()
    book_schema = BookSchema(many=True)
    output = book_schema.dump(books)  # Serialize the books
    print(output)  # Log the output for debugging
    return jsonify(output)  # Return the serialized data
