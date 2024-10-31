# app/schemas.py
from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    email = fields.Str(required=True)

class BookSchema(Schema):
    id = fields.Int(required=True)
    title = fields.Str(required=True)
    author = fields.Str(required=True)

class LoanSchema(Schema):
    id = fields.Int(required=True)
    book_id = fields.Int(required=True)
    user_id = fields.Int(required=True)
    loan_date = fields.Date(required=True)
    return_date = fields.Date()
