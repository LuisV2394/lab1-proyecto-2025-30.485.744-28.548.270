from flask import request, jsonify
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity
)
from app.models.user import User
from app import db

def login_controller():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):
        role_names = [role.name for role in user.roles]

        additional_claims = {"roles": role_names}
        access_token = create_access_token(
            identity=str(user.id),
            additional_claims=additional_claims
        )
        refresh_token = create_refresh_token(identity=str(user.id))

        return jsonify({
            "access_token": access_token,
            "refresh_token": refresh_token,
            "user": user.to_dict()
        }), 200

    return jsonify({"error": "Invalid credentials"}), 401

@jwt_required(refresh=True)
def refresh_token_controller():
    current_user = get_jwt_identity()
    new_token = create_access_token(identity=current_user)
    return jsonify({"access_token": new_token}), 200

@jwt_required()
def profile_controller():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    return jsonify({
        "user": user.to_dict()
    }), 200
