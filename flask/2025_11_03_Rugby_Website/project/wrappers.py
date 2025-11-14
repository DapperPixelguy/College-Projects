from flask_login import current_user
from functools import wraps
from flask import redirect, url_for


def logged_out_required(f):
    @wraps(f)
    def decorated_func(*args, **kwargs):
        if current_user.is_authenticated:
            return redirect(url_for('main.index'))
        return f(*args, **kwargs)
    return decorated_func