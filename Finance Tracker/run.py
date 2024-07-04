from app import create_app, db
from flask import current_app

app = create_app()

# Ensure the database is set up correctly
with app.app_context():
    db.create_all()  # Creates all tables if they don't already exist

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False for production use