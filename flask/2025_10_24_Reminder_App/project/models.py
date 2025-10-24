from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(1000), unique=True)
    password = db.Column(db.String(1000))
    reminders = db.relationship('Reminder', backref='user', lazy=True)

class Reminder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(1000))
    content = db.Column(db.String(5000))

