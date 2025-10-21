from functools import wraps
from flask import redirect, url_for, flash, abort
from flask_login import current_user
from .models import User


def access_required(level):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not current_user.is_authenticated:
                flash({'text': 'Please log in.'}, 'error')
                return redirect(url_for('auth.login'))
            user = User.query.get(current_user.get_id())
            if user is None or current_user.accessLevel < level:
                # flash({'text': 'You are not authorized to access this page'}, 'error')
                abort(403)

            elif current_user.accessLevel >= level:
                return func(*args, **kwargs)

            return redirect(url_for('main.index'))
        return wrapper
    return decorator



