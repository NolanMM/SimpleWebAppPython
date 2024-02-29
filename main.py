from app import app, db

# Use app context
with app.app_context():
    # Create all tables
    db.create_all()
    db.session.commit()
