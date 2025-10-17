from project import db, models, create_app

with create_app().app_context():
    db.drop_all()
    db.create_all()