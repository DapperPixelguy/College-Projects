from flask import Blueprint, redirect, url_for, request, render_template, flash
from flask_login import logout_user, login_user, login_required, current_user
from . import db
from .models import User

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    user = User.query.filter_by(email='test@test.com').first()
    login_user(user)
    flash({'text': 'You have been logged in.'}, 'Success')
    return redirect(url_for('main.index'))

@auth.route('/signup')
def signup():
    return 'Sign up'

@auth.route('/logout')
def logout():
    logout_user()
    flash({'text': 'You have been logged out.'}, 'Success')
    return redirect(url_for('main.index'))