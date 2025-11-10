from flask import Blueprint, render_template
from .models import Fixture

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/fixtures')
def fixtures():
    return render_template('fixtures.html', data=Fixture.query.all())

@main.route('/league-table')
def league_table():
    return 'leeg table'

