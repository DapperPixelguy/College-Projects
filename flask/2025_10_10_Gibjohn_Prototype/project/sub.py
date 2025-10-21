from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app
from flask_login import login_required, current_user
from . import db

sub = Blueprint('sub', __name__)

@sub.route('/our-tutors')
def our_tutors():
    return render_template('our_tutors.html')

@sub.route('/young-learners')
def young_learners():
    return render_template('young_learners.html')

@sub.route('/adult-learners')
def adult_learners():
    return render_template('adult_learners.html')

@sub.route('/help')
def help():
    return render_template('help.html')

@sub.route('/contact-us')
def contact_us():
    return render_template('contact_us.html')
