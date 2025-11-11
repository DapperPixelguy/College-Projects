from project import create_app, db
from datetime import datetime
from project.models import Fixture, Team

teams = [{'name': 'Norf fc', 'logo': '/static/england-rugby.svg'}, {'name': 'Souf fc', 'logo': '/static/daom-rugby.svg'}]

testFixtures = [{'team1': 'Norf fc', 'team2': 'Souf fc', 'venue': 'Example venue', 'date': datetime.today().strftime('%d/%m/%Y'), 'time': '12:00'},{'team1': 'Souf fc', 'team2': 'Norf fc', 'venue': 'Another example venue', 'date': datetime.today().strftime('%d/%m/%Y'), 'time': '13:15'},{'team1': 'Norf fc', 'team2': 'Norf fc', 'venue': 'Final example venue', 'date': datetime.today().strftime('%d/%m/%Y'), 'time': '00:01'}]


with create_app().app_context():
    db.drop_all()
    db.create_all()
    for team in teams:
        data = Team()
        data.name= team['name']
        data.logo = team['logo']
        db.session.add(data)

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
