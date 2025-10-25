from flask import Flask, request, render_template, session
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
db = SQLAlchemy

app.secret_key = b'be4d5f71c519cdf5154688def5b11ac8d7533584fe80dbfab49d033e81d2f562'

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route('/')
def index():
    return render_template('index.html')


app.run(debug=True)