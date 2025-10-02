from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/spain')
def index_spain():
    return 'spanish'


app.run(debug=True)