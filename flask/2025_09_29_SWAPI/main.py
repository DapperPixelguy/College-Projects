from math import isnan

from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)

def get_character_height():
    url = 'https://swapi.info/api/people'
    all_data = []

    try:
        response = requests.get(url)
        data = response.json()


        for item in data:
            #print(item)
            name = item.get('name')
            height = item.get('height')
            try:
                height = int(height)
            except:
                height= 0



            all_data.append({'name': name,
                             'height': height
                             })
        print(sorted(all_data, key=lambda d: d['height'], reverse=True))
        all_data = sorted(all_data, key=lambda d: d['name'])
        return all_data
    except requests.exceptions.RequestException as e:
        print(f'Error fetching data {e}')
        return None

get_character_height()

@app.route('/')
def index():
    return render_template('index.html', data=get_character_height())



app.run(debug=True)