from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from flasgger.utils import swag_from
from app.models.user import User
from app import db
import os

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "auth")
)
print("BASE_DOCS:", BASE_DOCS) 

# Login de usuario
@auth_bp.route("/login", methods=["POST"])
@swag_from(os.path.join(BASE_DOCS, 'login.yml'))
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):
        role_names = [role.name for role in user.roles]  # ✅ obtiene todos los roles del usuario

        additional_claims = {"roles": role_names}
        access_token = create_access_token(identity=str(user.id), additional_claims=additional_claims)
        refresh_token = create_refresh_token(identity=str(user.id))

        return jsonify({
            "access_token": access_token,
            "refresh_token": refresh_token,
            "user": user.to_dict()
        }), 200

    return jsonify({"error": "Invalid credentials"}), 401

# Token refresh
@auth_bp.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
#@swag_from(os.path.join(BASE_DOCS, 'refresh.yml'))
def refresh_token():
    current_user = get_jwt_identity()
    new_token = create_access_token(identity=current_user)
    return jsonify({"access_token": new_token}), 200

@auth_bp.route("/me", methods=["GET"])
@jwt_required()
#@swag_from(os.path.join(BASE_DOCS, 'get_info.yml'))
def profile():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    return jsonify({
        "user": user.to_dict()
    }), 200