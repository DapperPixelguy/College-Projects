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

            # Check if authenticated
            if not current_user.is_authenticated:
                if requestonly:
                    return jsonify({'error': 'Unauthenticated'}), 401
                return redirect(url_for('main.index'))

            # Check if level is high enough
            if current_user.accessLevel < level:
                if requestonly:
                    return jsonify({'error': 'Forbidden'}), 403
                return redirect(url_for('main.index'))

            # Both are satisfied, continue as normal
            return f(*args, **kwargs)

        return decorated_func
    return decorator
