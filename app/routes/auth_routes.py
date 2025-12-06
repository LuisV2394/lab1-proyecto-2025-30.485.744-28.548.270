from flask import Blueprint
from flasgger import swag_from
import os

from app.controllers.auth_controller import (
    login_controller,
    refresh_token_controller,
    profile_controller
)

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "auth")
)

@auth_bp.route("/login", methods=["POST"])
@swag_from(os.path.join(BASE_DOCS, "login.yml"))
def login():
    return login_controller()

@auth_bp.route("/refresh", methods=["POST"])
def refresh():
    return refresh_token_controller()

@auth_bp.route("/me", methods=["GET"])
def me():
    return profile_controller()