import os

import flask
from flask import Blueprint, render_template, jsonify, redirect, url_for, request, flash, current_app
from flask_login import login_required
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename
from sqlalchemy import or_
from .wrappers import *
from .models import Fixture, Result, Team, User, LeagueTable, League
from datetime import datetime
from . import db
from db_create import db_create

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/fixtures')
def fixtures():
    return render_template('fixtures.html', data=Fixture.query.all(), leagues=League.query.all(), teams=Team.query.order_by(Team.name).all())

@main.route('/fixtures/fetch')
def fetch_fixtures():

    team_filter = request.args.get('team')
    league_filter = request.args.get('league')

    if team_filter != 'all':
        if league_filter != 'all':
            fixture_list = (
                Fixture.query
                .filter(or_(Fixture.team1 == team_filter, Fixture.team2 == team_filter), Fixture.league_id==league_filter)
                .order_by(Fixture.date, Fixture.time)
                .all()
            )
        elif league_filter == 'all':
            fixture_list = (
                Fixture.query
                .filter(or_(Fixture.team1 == team_filter, Fixture.team2 == team_filter))
                .order_by(Fixture.date, Fixture.time)
                .all()
            )
    elif team_filter == 'all':
        if league_filter != 'all':
            fixture_list = (
                Fixture.query
                .filter(Fixture.league_id==league_filter)
                .order_by(Fixture.date, Fixture.time)
                .all()
            )
        elif league_filter == 'all':
            fixture_list = Fixture.query.order_by(Fixture.date, Fixture.time).all()


    response = [{
        'id': x.id,
        'league': {
          'name': x.league.name,
        },
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
    } for x in fixture_list]
    return jsonify(response)


@main.route('/league-table/update')
def update_league_table():

    fixtures = Fixture.query.all()

    results = [r.result for r in fixtures if r.result]

    teams = Team.query.all()

    try:
        LeagueTable.__table__.drop(db.engine, checkfirst=True)
        LeagueTable.__table__.create(db.engine)

        for fixture in Fixture.query.all():
            league1 = LeagueTable(team_id=fixture.team1, league_id=fixture.league.id)
            db.session.add(league1)
            league2 = LeagueTable(team_id=fixture.team2, league_id=fixture.league.id)
            db.session.add(league2)

        db.session.commit()

        for result in results:
            team1 = LeagueTable.query.filter_by(team_id=result.fixture.team1, league_id=result.fixture.league.id).first()
            team2 = LeagueTable.query.filter_by(team_id=result.fixture.team2, league_id=result.fixture.league.id).first()

            print(team1.played)

            team1_score = result.team1_score
            team2_score = result.team2_score

            team1.pf += team1_score
            team1.pa += team2_score

            team1.pd = team1.pf - team1.pa

            team2.pf += team2_score
            team2.pa += team1_score

            team2.pd = team2.pf - team2.pa

            # If not draw
            if team1_score > team2_score or team2_score > team1_score:
                winner, loser = (team1, team2) if team1_score > team2_score else (team2, team1)
                winner_score, loser_score = (team1_score, team2_score) if team1_score > team2_score else (team2_score, team1_score)

                winner.played += 1
                loser.played += 1

                winner.won += 1
                loser.lost += 1

                winner.points += 4

                if (winner_score - loser_score) <= 7:
                    loser.bonus += 1

            # If draw
            if team1_score == team2_score:
                team1.points += 2
                team2.points += 2

                team1.played += 1
                team2.played += 1

                team1.draw += 1
                team2.draw += 1

        db.session.commit()

    except Exception as e:
        current_app.logger.error(f'Error updating league table: {e}. League entries remain unchanged.')

    return redirect(url_for('main.league_table'))

@main.route('/fixtures/create-result', methods=['POST'])
@login_required
@access_level_required(2, requestonly=True)
def create_result():
    data = request.get_json()

    fixture_id = data['id']
    team1_score = int(data['team1_score'])
    team2_score = int(data['team2_score'])

    fixture = Fixture.query.filter_by(id=fixture_id).first()

    fixture.result = Result(team1_score=team1_score, team2_score=team2_score)
    db.session.commit()

    update_league_table()

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
        'venue': fixture.venue,
        'league': {
            'name': fixture.league.name
        }
    }

    return jsonify(response)



@main.route('/league-table')
def league_table():
    return render_template('league_table.html', teams=Team.query.all(), leagues=League.query.all())

@main.route('/league-table/fetch')
def fetch_league_table():
    sort = request.args.get('sort', 'points')
    asc = request.args.get('asc', 'false').lower() == 'true'
    league = request.args.get('league', 'league1').lower()



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
    sort_col2 = LeagueTable.pd.asc() if asc else LeagueTable.pd.desc()


    teams = Team.query.join(LeagueTable).join(League).filter(League.id == league).order_by(sort_col, sort_col2).all()
    print('-------------team-----------------')

    response = []
    for team in teams:
        standing = LeagueTable.query.filter_by(team_id=team.id, league_id=league).first()
        print(standing.won, team.name)
        response.append(
        {
        'name': team.name,
        'standing': {
            'played': standing.played,
            'won':    standing.won,
            'draw':   standing.draw,
            'lost':   standing.lost,
            'pf':     standing.pf,
            'pa':     standing.pa,
            'pd':     standing.pd,
            'bonus':  standing.bonus,
            'points': standing.points
        }
        })

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
    teams = Team.query.order_by(Team.name).all()
    return render_template('admin.html', teams=teams, leagues=League.query.all())

@main.route('/admin/fixture_create', methods=['GET', 'POST'])
@login_required
@access_level_required(2)
def fixture_create():

    team1 = request.form.get('team1')
    team2 = request.form.get('team2')
    date = request.form.get('date')
    time = request.form.get('time')
    venue = request.form.get('venue')
    league = request.form.get('league')

    for key in request.form.keys():
        if not request.form.get(key):
            flash({'text': 'Some fields were left empty'}, 'error')
            return redirect(url_for('main.admin'))

    print(date,time)
    fixture = Fixture()

    fixture.team1 = team1
    fixture.team2 = team2
    fixture.date = datetime.strptime(date, '%Y-%m-%d').date()
    fixture.time = datetime.strptime(time, '%H:%M').time()
    fixture.venue = venue
    fixture.league_id = int(league)

    # Check if league entries already exist

    if not LeagueTable.query.filter_by(team_id=team1, league_id=league).first():
        new_league = LeagueTable(team_id=team1, league_id=league)
        db.session.add(new_league)

    if not LeagueTable.query.filter_by(team_id=team2, league_id=league).first():
        new_league = LeagueTable(team_id=team2, league_id=league)
        db.session.add(new_league)


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

    if email:
        user_check = User.query.filter_by(email=email).first()

        if not user_check:
            user.email = email
            db.session.commit()
        else:
            flash({'text': 'User with that email already exists'}, 'error')

    if password:
        if len(password) > 3:
            user.password = generate_password_hash(password)
            db.session.commit()
        else:
            flash({'text': 'Password must be at least 3 characters long'}, 'error')



    return redirect(url_for('main.profile'))

@main.route('/photo-fetch')
def photo_fetch():
    response = []

    for filename in os.listdir('project/static/photos'):
        response.append(f'static/photos/{filename}')

    return jsonify(response)

@main.route('/feedback')
def feedback():
    return render_template('feedback.html')


@main.route('/database-create')
def db_create_route():
    db.create_all()

    if not Team.query.first():
        db_create()

