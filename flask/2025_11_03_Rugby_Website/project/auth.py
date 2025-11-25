import flask
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db
from .wrappers import logged_out_required

auth = Blueprint('auth', __name__)

@auth.route('/login')
@logged_out_required
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
@logged_out_required
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = request.form.get('remember')

    user = User.query.filter_by(email=email).first()

    if not user:
        flash({'text': 'User does not exist. Check your details or', 'link': url_for('auth.signup'), 'linktext':'create an account'}, 'error')
        return redirect(url_for('auth.login'))

    if check_password_hash(user.password, password):
        login_user(user, remember=remember)
        return redirect(url_for('main.index'))
    else:
        flash({'text': 'Incorrect email or password'}, category='error')
        return redirect(url_for('auth.login'))


@auth.route('/signup')
@logged_out_required
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
@logged_out_required
def signup_post():
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('password-confirm')


    if User.query.filter_by(email=email).first():
        flash({'text': 'Email already registered'}, category='error')
        return redirect(url_for('auth.signup'))

    if password != confirm_password:
        flash({'text': 'Passwords do not match'}, category='error')
        return redirect(url_for('auth.signup'))


    if password == confirm_password:
        new_user = User()
        new_user.password = generate_password_hash(password, salt_length=5)
        new_user.name = email
        new_user.email = email
        new_user.accessLevel = 2
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user, remember=True)

        return redirect(url_for('main.index'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
