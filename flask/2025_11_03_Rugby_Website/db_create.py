import random

from project import create_app, db
from datetime import datetime
from project.models import Fixture, Team, Result, LeagueTable
import os
import re

# teams = [
#     {'name': 'Barnfield RFC', 'logo': '/static/logos/Crediton.png'},
#     {'name': 'Riverside Rangers', 'logo': '/static/logos/Brixham.png'},
#     {'name': 'Hilltop Harriers', 'logo': '/static/logos/Barnstaple.png'},
#     {'name': 'Westvale Wolves', 'logo': '/static/logos/Crediton.png'},
#     {'name': 'Meadowbrook RFC', 'logo': '/static/logos/Brixham.png'},
#     {'name': 'Trent Tigers', 'logo': '/static/logos/Barnstaple.png'},
#     {'name': 'Eastgate Eagles', 'logo': '/static/logos/Brixham.png'},
#     {'name': 'Northshore Knights', 'logo': '/static/logos/Crediton.png'},
#     {'name': 'Springfield Sappers', 'logo': '/static/logos/Barnstaple.png'},
#     {'name': 'Oakridge Orcas', 'logo': '/static/logos/Brixham.png'}
# ]

teams = [
]

for file in os.listdir('project/static/logos'):
    if file.endswith('.png'):
        team = {'name': '', 'logo': ''}
        name = os.fsdecode(file).split('.')[0]
        print(name)
        name = re.findall('[A-Z][^A-Z]*', name)
        name = ' '.join(name)
        print(name)
        logo = file

        team['name'] = name
        team['logo'] = f'static/logos/{logo}'

        teams.append(team)

# testFixtures = [
#     {'team1': 'Meadowbrook RFC', 'team2': 'Trent Tigers', 'venue': 'Field House', 'date': '14/11/2025', 'time': '13:15'},
#     {'team1': 'Westvale Wolves', 'team2': 'Barnfield RFC', 'venue': 'Community Ground', 'date': '14/11/2025', 'time': '15:00'},
#     {'team1': 'Springfield Sappers', 'team2': 'Eastgate Eagles', 'venue': 'Another Example Venue', 'date': '14/11/2025', 'time': '12:00'},
#     {'team1': 'Hilltop Harriers', 'team2': 'Northshore Knights', 'venue': 'Stadium Park', 'date': '14/11/2025', 'time': '18:30'},
#     {'team1': 'Oakridge Orcas', 'team2': 'Riverside Rangers', 'venue': 'Example Venue', 'date': '14/11/2025', 'time': '12:00'}
# ]




with create_app().app_context():
    db.drop_all()
    db.create_all()
    for team in teams:
        data = Team()
        data.name= team['name']
        data.logo = team['logo']
        db.session.add(data)
    db.session.commit()

    teams_db = Team.query.all()
    team_names = [t.name for t in teams_db]

    venues = [
        "Field House",
        "Community Ground",
        "Stadium Park",
        "Example Venue",
        "Another Example Venue"
    ]

    testFixtures = []

    for i in range(5):  # generate 5 fixtures
        team1, team2 = random.sample(team_names, 2)  # ensures no duplicates

        testFixtures.append({
            'team1': team1,
            'team2': team2,
            'venue': random.choice(venues),
            'date': '14/11/2025',  # or randomise later if you want
            'time': '13:15'  # placeholder; can also randomise
        })

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

    # results = [{'team1_score': random.randint(0, 10), 'team2_score': random.randint(0, 10), 'fixture_id': x.id}
    #            for x in Fixture.query.all()]
    #
    # for result in results:
    #     data = Result()
    #     data.team1_score = result['team1_score']
    #     data.team2_score = result['team2_score']
    #     data.fixture_id = result['fixture_id']
    #     db.session.add(data)
    # db.session.commit()

    for team in Team.query.all():
        # won = random.randint(0, 20)
        # draw = random.randint(0, 20 - won)
        # lost = random.randint(0, 20 - won - draw)
        #
        # pf = random.randint(50, 500)  # points for
        # pa = random.randint(50, 500)  # points against
        # pd = pf - pa  # points difference
        #
        # bonus = random.randint(0, 5)  # bonus points
        #
        # played = won + draw + lost
        #
        # points = (won * 2) + (draw * 1) + bonus  # Or whatever scoring system you use
        #
        # table_entry = LeagueTable(
        #     team_id=team.id,
        #     played=played,
        #     won=won,
        #     draw=draw,
        #     lost=lost,
        #     pf=pf,
        #     pa=pa,
        #     pd=pd,
        #     bonus=bonus,
        #     points=points
        # )
        table_entry = LeagueTable(team_id=team.id)
        db.session.add(table_entry)

    db.session.commit()
