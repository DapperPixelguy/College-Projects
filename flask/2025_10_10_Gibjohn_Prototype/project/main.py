import werkzeug.security
from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
import os
from . import db
from .decorators import access_required
from .models import User

main = Blueprint('main', __name__)
allowed_extensions = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/profile', methods=['POST'])
@login_required
def profile_update():
    if 'file' not in request.files:
        flash('No file')
        return redirect(url_for('main.profile'))

    file = request.files['file']
    email = request.form.get('email')
    name = request.form.get('name')
    old_password = request.form.get('old-password')
    new_password = request.form.get('new-password')

    if file.filename == '':
        file = None

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        current_user.picture = filename

    if email and email != current_user.email:
        if 2 <= len(email) <= 30:
            current_user.email = email
        else:
            flash({'text': 'Email must be between 2 and 30 characters long'}, 'error')

    if name and name != current_user.name:
        if 2 <= len(name) <= 30:
            current_user.name = name.title()
        else:
            flash({'text': 'Name must be between 2 and 30 characters long'}, 'error')

    if old_password and new_password:
        if 3 <= len(new_password) and check_password_hash(current_user.password, old_password):
            current_user.password = generate_password_hash(new_password)
        elif len(new_password) <=3 :
            flash({'text': 'New password must be over 3 characters.'}, 'error')
        elif not check_password_hash(current_user.password, old_password):
            flash({'text': 'Incorrect password.'}, 'error')

    if not old_password:
        flash({'text': 'Please enter your password to save changes'}, 'error')
    elif check_password_hash(current_user.password, old_password):
        db.session.commit()
    elif not check_password_hash(current_user.password, old_password):
        flash({'text': 'Incorrect password. Make sure you have entered your current password into the \'Current password\' box'}, 'error')

    return redirect(url_for('main.profile'))


@main.route('/admin')
@login_required
@access_required(1)
def admin():
    users = User.query.all()
    return render_template('admin.html', users=users)

@main.route('/admin', methods=['POST'])
@login_required
@access_required(2)
def admin_post():
    email = request.form.get('email')
    user = User.query.filter_by(email=email).first()

    if request.form.get('name'):
        user.name = request.form.get('name')

    if request.form.get('accessLevel'):
        user.accessLevel = request.form.get('accessLevel')

    db.session.commit()
    print(user.name)

    return redirect(url_for('main.admin'))
