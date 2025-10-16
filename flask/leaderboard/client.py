import requests

name = input('Name >> ')
score = input('Score >> ')

url = 'http://127.0.0.1:5000/submit'

data = {
    'name': name,
    'score': score
}

response = requests.post(url, json=data)

print(f'Sent {data}')
print(response.status_code)

