from flask import request, jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from functools import wraps

def fix_swagger_bearer():
    auth = request.headers.get("Authorization", "")
    if auth and not auth.startswith("Bearer "):
        request.environ["HTTP_AUTHORIZATION"] = "Bearer " + auth

def jwt_required_fixed(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        fix_swagger_bearer()
        verify_jwt_in_request()
        return fn(*args, **kwargs)
    return wrapper

def role_required(allowed_roles):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            fix_swagger_bearer()
            verify_jwt_in_request()
            claims = get_jwt()

            user_roles = claims.get("roles", [])

            if not any(role in allowed_roles for role in user_roles):
                return jsonify({"error": "Access denied"}), 403

            return fn(*args, **kwargs)
        return decorator
    return wrapper
