# seed.py
from app import app, db
from app.models import User, Book, Loan
from datetime import datetime

# Ensure app context for database operations
with app.app_context():
    # Drop all tables (optional, if you want to reset the database)
    db.drop_all()
    # Create tables
    db.create_all()

    # Seed Users
    user1 = User(name="Alice Johnson", email="alice@example.com")
    user2 = User(name="Bob Smith", email="bob@example.com")

    # Seed Books
    book1 = Book(title="The Great Gatsby", author="F. Scott Fitzgerald")
    book2 = Book(title="To Kill a Mockingbird", author="Harper Lee")

    # Seed Loans
    loan1 = Loan(book=book1, user=user1, loan_date=datetime(2024, 10, 1))
    loan2 = Loan(book=book2, user=user2, loan_date=datetime(2024, 10, 2), return_date=datetime(2024, 10, 20))

    # Add to session and commit
    db.session.add_all([user1, user2, book1, book2, loan1, loan2])
    db.session.commit()

    print("Database seeded successfully!")
