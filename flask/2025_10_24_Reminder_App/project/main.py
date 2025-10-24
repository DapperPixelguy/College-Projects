from flask import Blueprint, render_template, redirect, url_for, request, session, abort, flash

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

