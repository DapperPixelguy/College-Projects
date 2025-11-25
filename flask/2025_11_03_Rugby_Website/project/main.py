import os

import flask
from flask import Blueprint, render_template, jsonify, redirect, url_for, request, flash, current_app
from flask_login import login_required
from werkzeug.utils import secure_filename

from .wrappers import *
from .models import Fixture, Result, Team, User, LeagueTable
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
        'id': x.id,
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
        'time': str(x.time),
        **({
            'result': {
                'team1': x.result.team1_score,
                'team2': x.result.team2_score
            }
        } if x.result else {})
    } for x in Fixture.query.order_by(Fixture.date, Fixture.time).all()]
    return jsonify(response)

@main.route('/fixtures/create-result', methods=['POST'])
@login_required
@access_level_required(2, requestonly=True)
def create_result():
    data = request.get_json()

    fixture_id = data['id']
    team1_score = data['team1_score']
    team2_score = data['team2_score']

    fixture = Fixture.query.filter_by(id=fixture_id).first()

    fixture.result = Result(team1_score=team1_score, team2_score=team2_score)

    db.session.commit()

    print(fixture_id, team1_score, team2_score)

    print(fixture.venue)

    response = {
        'id': fixture.id,
        'team1': {
            'name': fixture.team1_rel.name,
            'logo': fixture.team1_rel.logo,
            'score': fixture.result.team1_score
        },
        'team2': {
            'name': fixture.team2_rel.name,
            'logo': fixture.team2_rel.logo,
            'score': fixture.result.team2_score
        },
        'date': str(fixture.date),
        'venue': fixture.venue
    }

    return jsonify(response)

@main.route('/league-table')
def league_table():
    return render_template('league_table.html', teams=Team.query.all())

@main.route('/league-table/fetch')
def fetch_league_table():
    sort = request.args.get('sort', 'points')
    asc = request.args.get('asc', 'false').lower() == 'true'

    sortable = {
            'name': Team.name,
            'played': LeagueTable.played,
            'won':    LeagueTable.won,
            'draw':   LeagueTable.draw,
            'lost':   LeagueTable.lost,
            'pf':     LeagueTable.pf,
            'pa':     LeagueTable.pa,
            'pd':     LeagueTable.pd,
            'bonus':  LeagueTable.bonus,
            'points': LeagueTable.points
    }

    sort_col = sortable.get(sort.lower(), LeagueTable.points)

    sort_col = sort_col.asc() if asc else sort_col.desc()


    teams = Team.query.join(LeagueTable).order_by(sort_col, LeagueTable.pd.desc()).all()
    for team in teams:
        print(team.standing.won, team.name)
    response = [
        {
        'name': team.name,
        'standing': {
            'played': team.standing.played,
            'won':    team.standing.won,
            'draw':   team.standing.draw,
            'lost':   team.standing.lost,
            'pf':     team.standing.pf,
            'pa':     team.standing.pa,
            'pd':     team.standing.pd,
            'bonus':  team.standing.bonus,
            'points': team.standing.points 
        }
    } for team in teams]

    return jsonify(response)

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

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html')


@main.route('/profile/update', methods=['POST'])
@login_required
def profile_update():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    picture = request.files.get('picture')

    allowed_files = ['png', 'jpg', 'jpeg']

    if picture:
        print(picture.filename)
        file = request.files['picture']
        filename = secure_filename(file.filename)
        if filename.split('.')[-1] in allowed_files:
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            current_user.picture=f'uploads/{filename}'
            db.session.commit()
        else:
            return redirect(url_for('main.profile'))


    user = User.query.filter_by(email=current_user.email).first()

    print(user.name)

    if name:
        user.name = name.title()
        db.session.commit()

    return redirect(url_for('main.profile'))

@main.route('/photo-fetch')
def photo_fetch():
    response = []

    for filename in os.listdir('project/static/photos'):
        response.append(f'static/photos/{filename}')

    return jsonify(response)


