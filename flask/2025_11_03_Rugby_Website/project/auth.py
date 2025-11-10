from flask import Blueprint, render_template, redirect, url_for, flash, request

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    print(email, password)
    return redirect(url_for('auth.login'))

@auth.route('/signup')
def signup():
    return 'Signup'
