from . import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    picture = db.Column(db.String(30))
    accessLevel = db.Column(db.Integer, default=0)

    @property
    def access_name(self):
        return {
            0: '',
            1: 'Admin',
            2: 'Super Admin'
        }.get(self.accessLevel, 'Unknown')
