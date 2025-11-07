from project import create_app, db

with create_app().app_context():
    db.drop_all()
    db.create_all()