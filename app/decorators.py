from functools import wraps
from flask import abort
from flask_login import current_user
from .models import Permission

# https://stackoverflow.com/questions/5929107/decorators-with-parameters
def permission_required(permission):
    def decorator(f):
        @wraps(f) #https://stackoverflow.com/questions/308999/what-does-functools-wraps-do
        def decorated_function(*args, **kwargs):
            if not current_user.can(permission):
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator


def admin_required(f):
    return permission_required(Permission.ADMIN)(f)