from flask_login import UserMixin
from . import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))


class Fixture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    venue = db.Column(db.String(100), nullable=False)

    team1 = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    team2 = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)

    team1_rel = db.relationship('Team', foreign_keys=[team1], back_populates='home_fixtures')
    team2_rel = db.relationship('Team', foreign_keys=[team2], back_populates='away_fixtures')

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    logo = db.Column(db.String(100))

    home_fixtures = db.relationship('Fixture', back_populates='team1_rel', foreign_keys='Fixture.team1')
    away_fixtures = db.relationship('Fixture', back_populates='team2_rel', foreign_keys='Fixture.team2')
