from collections import UserList

from flask_login import UserMixin
from . import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    picture = db.Column(db.String(100), default='uploads/blank_profile.png')
    accessLevel = db.Column(db.Integer, default=0)


class Fixture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    venue = db.Column(db.String(100), nullable=False)

    team1 = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    team2 = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)

    team1_rel = db.relationship('Team', foreign_keys=[team1], back_populates='home_fixtures')
    team2_rel = db.relationship('Team', foreign_keys=[team2], back_populates='away_fixtures')

class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team1_score = db.Column(db.Integer, nullable=False)
    team2_score = db.Column(db.Integer, nullable=False)
    fixture_id = db.Column(db.Integer, db.ForeignKey('fixture.id'), nullable=False)

    fixture = db.relationship('Fixture', backref='results')

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    logo = db.Column(db.String(100))

    home_fixtures = db.relationship('Fixture', back_populates='team1_rel', foreign_keys='Fixture.team1')
    away_fixtures = db.relationship('Fixture', back_populates='team2_rel', foreign_keys='Fixture.team2')

    standing = db.relationship('LeagueTable', back_populates='team', uselist=False)

class LeagueTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False, unique=True)

    played = db.Column(db.Integer, default=0)
    won = db.Column(db.Integer, default=0)
    draw = db.Column(db.Integer, default=0)
    lost = db.Column(db.Integer, default=0)

    pf = db.Column(db.Integer, default=0)
    pa = db.Column(db.Integer, default=0)
    pd = db.Column(db.Integer, default=0)
    bonus = db.Column(db.Integer, default=0)
    points = db.Column(db.Integer, default=0)

    team = db.relationship('Team', back_populates='standing')
