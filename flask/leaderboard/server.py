from flask import Flask, request, render_template, jsonify
import pandas as pd

df = pd.read_csv('leaderboard.csv').sort_values(by=['Score'], ascending=False)

app = Flask(__name__)

@app.route('/')
def index():
    names = df.loc[:, 'Name']
    scores = df.loc[:, 'Score']
    data=zip(names,scores)
    return render_template('index.html', data=data)

@app.route('/submit', methods=['POST'])
def receive_json():
    global df
    response=request.get_json()
    new_data = pd.DataFrame([{'Name': response.get('name'), 'Score': int(response.get('score'))}])
    print(new_data)
    df = pd.concat([df, new_data], ignore_index=True).sort_values(by=['Score'], ascending=False)
    print(df)
    df.to_csv('leaderboard.csv', index=False)
    return 'Received!'

@app.route('/raw')
def raw_data():
    df = pd.read_csv('leaderboard.csv').sort_values(by=['Score'], ascending=False)
    return df.to_json(orient='records')

if __name__ == '__main__':
    app.run(debug=True)