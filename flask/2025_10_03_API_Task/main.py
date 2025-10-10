from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)

def get_fact():
    url = 'https://uselessfacts.jsph.pl/api/v2/facts/random'
    response = requests.get(url)
    data = response.json()
    return data['text']

def get_image(query):
    app_key = '_oXs4t9p9_i3Wf3e88XD6__7oExINVbRSBnCFe4B_2k'
    url = 'https://api.unsplash.com/search/photos'
    params = {
        'client_id': app_key,
        'query': query,
        'page': 1,
        'per_page': 1,
    }
    response = requests.get(url, params=params)
    image = response.json()['results'][0]['urls']['small']
    return image


@app.route('/')
def index():
    fact = get_fact()
    return render_template('index.html', fact=fact, image=get_image(fact))


app.run(debug=True)
#get_image('b')