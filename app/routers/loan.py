from flask import jsonify
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
                            'example': 101
                        },
                        'user_id': {
                            'type': 'integer',
                            'example': 1001
                        },
                        'loan_date': {
                            'type': 'string',
                            'format': 'date',
                            'example': '2024-10-30'
                        },
                        'return_date': {
                            'type': 'string',
                            'format': 'date',
                            'example': '2024-11-30'
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
        'loan_date': loan.loan_date.isoformat() if loan.loan_date else None,
        'return_date': loan.return_date.isoformat() if loan.return_date else None
    } for loan in loans])
