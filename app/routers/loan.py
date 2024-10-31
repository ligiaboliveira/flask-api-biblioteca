from flask import jsonify
from flasgger import swag_from
from app import db
from app.models import Loan
from app.schemas import LoanSchema  # Import the LoanSchema
from . import api_bp

@api_bp.route('/loans', methods=['GET'])
@swag_from({
    'responses': {
        200: {
            'description': 'List of loans',
            'schema': LoanSchema(many=True).fields,  # Use the schema
        }
    }
})
def list_loans():
    loans = Loan.query.all()
    loan_schema = LoanSchema(many=True)  # Initialize schema for multiple loans
    return jsonify(loan_schema.dump(loans))  # Serialize and return
