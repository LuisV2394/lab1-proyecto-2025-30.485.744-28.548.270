from flask import Blueprint
from flask_jwt_extended import jwt_required
from flasgger import swag_from
from app.controllers.access_logs_controller import (
    get_all_logs_controller,
    get_logs_by_user_controller,
)
from app.utils.middleware import role_required # Asumiendo que solo admin ve logs
import os

access_log_bp = Blueprint("access_logs", __name__, url_prefix="/logs")

BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "logs")
)

@access_log_bp.route("/", methods=["GET"])
@jwt_required()
@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "get_all.yml"))
def get_logs():
    return get_all_logs_controller()

@access_log_bp.route("/user/<int:user_id>", methods=["GET"])
@jwt_required()
@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "get_by_user.yml"))
def get_user_logs(user_id):
    return get_logs_by_user_controller(user_id)

# create_log_entry is an internal function and does not need a route