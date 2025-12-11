import requests

def ping():
    try:
        requests.get('https://college-projects-tslh.onrender.com')
        print('Ping sent')
    except Exception as e:
        print(e)
