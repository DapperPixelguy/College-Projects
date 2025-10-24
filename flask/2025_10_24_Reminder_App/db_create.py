from project import db, create_app
from project.models import User

testing = User(email='test@test.com', password='test')

app = create_app()
if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
        db.session.add(testing)
        db.session.commit()
