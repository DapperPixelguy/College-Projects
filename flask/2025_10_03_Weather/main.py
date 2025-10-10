from flask import Flask, request, jsonify
from flask import render_template
import requests



app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    def get_weather(location='London'):
        url = 'http://api.weatherapi.com/v1/current.json'
        key = '76e28d4de7e044e99d6144910250310'
        params = {
            'key': key,
            'q': location
        }

        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            return data['location']['name'], data['current']['condition']['text']
        else:
            fallback = {
            'key': key,
            'q': 'London'
        }
            response = requests.get(url, params=fallback)
            data = response.json()
            return data['location']['name'], data['current']['condition']['text']

    def get_image(query='Sky'):
        app_key = '_oXs4t9p9_i3Wf3e88XD6__7oExINVbRSBnCFe4B_2k'
        url = 'https://api.unsplash.com/search/photos'
        params = {
            'client_id': app_key,
            'query': query,
            'page': 1,
            'per_page': 1,
        }
        response = requests.get(url, params=params)
        image = response.json()['results'][0]['urls']['raw']
        return image

    if request.method == 'POST':
        query = request.form.get('city').lower()

        location, weather = get_weather(query)
        return render_template('index.html', location=location, weather=weather, background=get_image(f'{weather} {location}'))
    else:
        location, weather = get_weather('London')
        return render_template('index.html', location=location, weather=weather, background=get_image(f'{weather} {location}'))

@app.route('/fetch')
def fetch_weather():
    city = request.args.get('city', 'London')

    def get_weather(location='London'):
        url = 'http://api.weatherapi.com/v1/current.json'
        key = '76e28d4de7e044e99d6144910250310'
        params = {
            'key': key,
            'q': location
        }

        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            return data['location']['name'], data['current']['condition']['text']
        else:
            fallback = {
            'key': key,
            'q': 'London'
        }
            response = requests.get(url, params=fallback)
            data = response.json()
            return data['location']['name'], data['current']['condition']['text']

    def get_image(query='Sky'):
        app_key = '_oXs4t9p9_i3Wf3e88XD6__7oExINVbRSBnCFe4B_2k'
        url = 'https://api.unsplash.com/search/photos'
        params = {
            'client_id': app_key,
            'query': query,
            'page': 1,
            'per_page': 1,
        }
        response = requests.get(url, params=params)
        image = response.json()['results'][0]['urls']['raw']
        return image

    location, weather = get_weather(city)
    background = get_image(f'{weather} {location}')
    return jsonify({'location': location, 'weather': weather, 'background': background})



app.run(debug=True)