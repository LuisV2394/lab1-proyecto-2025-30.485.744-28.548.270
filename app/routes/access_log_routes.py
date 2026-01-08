from flask import Blueprint
from flask_jwt_extended import jwt_required
from flasgger import swag_from
from app.utils.middleware import role_required
import os

# Controladores
from app.controllers.access_logs_controller import (
    get_all_logs_controller,
    get_log_by_id_controller,
    get_logs_by_user_controller,
    create_log_controller,
    update_log_controller,
    delete_log_controller
)

access_log_bp = Blueprint("access_logs", __name__, url_prefix="/logs")

BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "access_logs")
)

# GET ALL LOGS
@access_log_bp.route("/", methods=["GET"])
# @jwt_required()
# @role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "get_all.yml"))
def get_logs():
    return get_all_logs_controller()

# GET LOG BY ID
@access_log_bp.route("/<int:log_id>", methods=["GET"])
@jwt_required()
@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "get_by_id.yml"))
def get_log_by_id(log_id):
    return get_log_by_id_controller(log_id)


# GET LOGS BY USER
@access_log_bp.route("/user/<int:user_id>", methods=["GET"])
# @jwt_required()
# @role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "get_by_user.yml"))
def get_user_logs(user_id):
    return get_logs_by_user_controller(user_id)

# CREATE LOG MANUALLY (API)
@access_log_bp.route("/", methods=["POST"])
# @jwt_required()
# @role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "create.yml"))
def create_log():
    return create_log_controller()

# UPDATE LOG
@access_log_bp.route("/<int:log_id>", methods=["PATCH"])
# @jwt_required()
# @role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "update.yml"))
def update_log(log_id):
    return update_log_controller(log_id)

# DELETE LOG
@access_log_bp.route("/<int:log_id>", methods=["DELETE"])
# @jwt_required()
# @role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "delete.yml"))
def delete_log(log_id):
    return delete_log_controller(log_id)