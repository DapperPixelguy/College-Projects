from flask import Blueprint, render_template, jsonify
from .models import Fixture

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
    } for x in Fixture.query.all()]
    return jsonify(response)

@main.route('/league-table')
def league_table():
    return 'leeg table'

