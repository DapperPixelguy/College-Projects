import random

from project import create_app, db
from datetime import datetime
from project.models import Fixture, Team, Result, LeagueTable
import random

teams = [
    {'name': 'Barnfield RFC', 'logo': '/static/logos/Crediton.png'},
    {'name': 'Riverside Rangers', 'logo': '/static/logos/Brixham.png'},
    {'name': 'Hilltop Harriers', 'logo': '/static/logos/Barnstaple.png'},
    {'name': 'Westvale Wolves', 'logo': '/static/logos/Crediton.png'},
    {'name': 'Meadowbrook RFC', 'logo': '/static/logos/Brixham.png'},
    {'name': 'Trent Tigers', 'logo': '/static/logos/Barnstaple.png'},
    {'name': 'Eastgate Eagles', 'logo': '/static/logos/Brixham.png'},
    {'name': 'Northshore Knights', 'logo': '/static/logos/Crediton.png'},
    {'name': 'Springfield Sappers', 'logo': '/static/logos/Barnstaple.png'},
    {'name': 'Oakridge Orcas', 'logo': '/static/logos/Brixham.png'}
]


testFixtures = [
    {'team1': 'Meadowbrook RFC', 'team2': 'Trent Tigers', 'venue': 'Field House', 'date': '14/11/2025', 'time': '13:15'},
    {'team1': 'Westvale Wolves', 'team2': 'Barnfield RFC', 'venue': 'Community Ground', 'date': '14/11/2025', 'time': '15:00'},
    {'team1': 'Springfield Sappers', 'team2': 'Eastgate Eagles', 'venue': 'Another Example Venue', 'date': '14/11/2025', 'time': '12:00'},
    {'team1': 'Hilltop Harriers', 'team2': 'Northshore Knights', 'venue': 'Stadium Park', 'date': '14/11/2025', 'time': '18:30'},
    {'team1': 'Oakridge Orcas', 'team2': 'Riverside Rangers', 'venue': 'Example Venue', 'date': '14/11/2025', 'time': '12:00'}
]




with create_app().app_context():
    db.drop_all()
    db.create_all()
    for team in teams:
        data = Team()
        data.name= team['name']
        data.logo = team['logo']
        db.session.add(data)
    db.session.commit()

    for fixture in testFixtures:
        print(datetime.strptime(fixture['date'], '%d/%m/%Y').date())
        print(fixture)
        data = Fixture()
        data.team1 = Team.query.filter_by(name=fixture['team1']).first().id
        data.team2 = Team.query.filter_by(name=fixture['team2']).first().id
        data.date = datetime.strptime(fixture['date'], '%d/%m/%Y').date()
        data.venue = fixture['venue']
        data.time = datetime.strptime(fixture['time'], '%H:%M').time()
        print(data)
        db.session.add(data)
    db.session.commit()

    results = [{'team1_score': random.randint(0, 10), 'team2_score': random.randint(0, 10), 'fixture_id': x.id}
               for x in Fixture.query.all()]

    for result in results:
        data = Result()
        data.team1_score = result['team1_score']
        data.team2_score = result['team2_score']
        data.fixture_id = result['fixture_id']
        db.session.add(data)
    db.session.commit()

    for team in Team.query.all():
        table_entry = LeagueTable()
        table_entry.team_id = team.id
        db.session.add(table_entry)

    db.session.commit()
