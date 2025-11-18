from flask import Blueprint, render_template, jsonify, redirect, url_for, request
from flask_login import login_required
from .wrappers import *
from .models import Fixture, Result, Team, User
from datetime import datetime
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/fixtures')
def fixtures():
    return render_template('fixtures.html', data=Fixture.query.all())

@main.route('/fixtures/fetch')
def fetch_fixtures():
    response = [{
        'team1': {
            'name': x.team1_rel.name,
            'logo': x.team1_rel.logo
        },
        'team2': {
            'name': x.team2_rel.name,
            'logo': x.team2_rel.logo
        },
        'venue': x.venue,
        'date': str(x.date),
        'time': str(x.time)
    } for x in Fixture.query.order_by(Fixture.date, Fixture.time).all()]
    return jsonify(response)

@main.route('/league-table')
def league_table():
    return redirect(url_for('main.index'))

@main.route('/results')
def results():
    return render_template('results.html', results=Result.query.all())

@main.route('/results/fetch')
def results_fetch():
    results = (
        Result.query
        .join(Fixture)
        .order_by(Fixture.date, Fixture.time)
        .all()
    )

    response = [{
        'team1_results': r.team1_score,
        'team2_results': r.team2_score,
        'fixture_id': r.fixture_id,
        'fixture': {
            'time': r.fixture.time.strftime('%H:%M'),
            'date': r.fixture.date.strftime('%Y-%m-%d'),
            'venue': r.fixture.venue,
            'team1_rel': {
                'logo': r.fixture.team1_rel.logo,
                'name': r.fixture.team1_rel.name
            },
            'team2_rel': {
                'logo': r.fixture.team2_rel.logo,
                'name': r.fixture.team2_rel.name
            }
        }
    } for r in results]

    return jsonify(response)


@main.route('/admin')
@login_required
@access_level_required(2)
def admin():
    teams = Team.query.all()
    return render_template('admin.html', teams=teams)

@main.route('/admin/fixture_create', methods=['GET', 'POST'])
@login_required
@access_level_required(2)
def fixture_create():

    team1 = request.form.get('team1')
    team2 = request.form.get('team2')
    date = request.form.get('date')
    time = request.form.get('time')
    venue = request.form.get('venue')

    print(date,time)
    fixture = Fixture()

    fixture.team1 = team1
    fixture.team2 = team2
    fixture.date = datetime.strptime(date, '%Y-%m-%d').date()
    fixture.time = datetime.strptime(time, '%H:%M').time()
    fixture.venue = venue

    db.session.add(fixture)
    db.session.commit()

    return redirect(url_for('main.fixtures'))
    # return 'Bello! I am a minion!'

