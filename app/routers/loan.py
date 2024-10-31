from flask import jsonify, request
from flasgger import swag_from
from app import db
from app.models import Loan
from . import api_bp

@api_bp.route('/loans', methods=['GET'])
@swag_from({
    'responses': {
        200: {
            'description': 'List of loans',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {
                            'type': 'integer',
                            'example': 1
                        },
                        'book_id': {
                            'type': 'integer',
                            'example': 1
                        },
                        'user_id': {
                            'type': 'integer',
                            'example': 1
                        },
                        'loan_date': {
                            'type': 'string',
                            'format': 'date',
                            'example': '2024-10-31'
                        },
                        'return_date': {
                            'type': 'string',
                            'format': 'date',
                            'example': '2024-11-07'
                        },
                    }
                }
            }
        }
    }
})
def list_loans():
    loans = Loan.query.all()
    return jsonify([{
        'id': loan.id,
        'book_id': loan.book_id,
        'user_id': loan.user_id,
        'loan_date': loan.loan_date.isoformat(),
        'return_date': loan.return_date.isoformat() if loan.return_date else None
    } for loan in loans])

@api_bp.route('/loans', methods=['POST'])
@swag_from({
    'parameters': [
        {
            'name': 'body',
            'description': 'Loan data to create a new loan',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'book_id': {
                        'type': 'integer',
                        'example': 1
                    },
                    'user_id': {
                        'type': 'integer',
                        'example': 1
                    },
                    'loan_date': {
                        'type': 'string',
                        'format': 'date',
                        'example': '2024-10-31'
                    },
                    'return_date': {
                        'type': 'string',
                        'format': 'date',
                        'example': '2024-11-07'
                    },
                },
                'required': ['book_id', 'user_id', 'loan_date']
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Loan created successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {
                        'type': 'integer',
                        'example': 1
                    },
                    'book_id': {
                        'type': 'integer',
                        'example': 1
                    },
                    'user_id': {
                        'type': 'integer',
                        'example': 1
                    },
                    'loan_date': {
                        'type': 'string',
                        'format': 'date',
                        'example': '2024-10-31'
                    },
                    'return_date': {
                        'type': 'string',
                        'format': 'date',
                        'example': '2024-11-07'
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
                        'example': 'Invalid book or user ID'
                    }
                }
            }
        }
    }
})
def create_loan():
    data = request.get_json()
    if not data or 'book_id' not in data or 'user_id' not in data or 'loan_date' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    new_loan = Loan(
        book_id=data['book_id'],
        user_id=data['user_id'],
        loan_date=data['loan_date'],
        return_date=data.get('return_date')  # Optional field
    )
    db.session.add(new_loan)
    db.session.commit()

    return jsonify({
        'id': new_loan.id,
        'book_id': new_loan.book_id,
        'user_id': new_loan.user_id,
        'loan_date': new_loan.loan_date.isoformat(),
        'return_date': new_loan.return_date.isoformat() if new_loan.return_date else None
    }), 201
