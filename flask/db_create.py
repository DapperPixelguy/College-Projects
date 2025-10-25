from . import db, models, create_app

with create_app().app_context():
    db.create_all()