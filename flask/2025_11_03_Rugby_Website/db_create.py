from project import create_app, db
from datetime import datetime
from project.models import Fixture

testFixtures = [{'team1': 'Norf fc', 'team2': 'souf fc', 'venue': 'down the pub', 'date': f'{datetime.now()}'},{'team1': 'Norf fc 2', 'team2': 'souf fc 2', 'venue': 'tobys', 'date': f'{datetime.now()}'}]

with create_app().app_context():
    db.drop_all()
    db.create_all()
    for fixture in testFixtures:
        print(fixture)
        data = Fixture()
        data.team1 = fixture['team1']
        data.team2 = fixture['team2']
        data.date = fixture['date']
        data.venue = fixture['venue']
        print(data)
        db.session.add(data)
    db.session.commit()
