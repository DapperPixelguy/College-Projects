from flask_login import current_user
from functools import wraps
from flask import redirect, url_for, jsonify


def logged_out_required(f):
    @wraps(f)
    def decorated_func(*args, **kwargs):
        if current_user.is_authenticated:
            return redirect(url_for('main.index'))
        return f(*args, **kwargs)
    return decorated_func

def access_level_required(level, requestonly=False):
    def decorator(f):
        @wraps(f)
        def decorated_func(*args, **kwargs):
            if current_user.is_authenticated and current_user.accessLevel >= level:
                return f(*args, **kwargs)
            if requestonly:
                return jsonify({'Error': 'You are not authorized to access this page'}), 405
            return redirect(url_for('main.index'))
        return decorated_func
    return decorator
