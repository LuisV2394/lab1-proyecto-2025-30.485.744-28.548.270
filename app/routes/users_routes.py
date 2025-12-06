from flask import Blueprint
from flask_jwt_extended import jwt_required
from flasgger.utils import swag_from
from app.utils.middleware import role_required
import os

from app.controllers.user_controller import (
    get_all_users_controller,
    get_user_by_id_controller,
    create_user_controller,
    update_user_controller,
    deactivate_user_controller
)

users_bp = Blueprint("users", __name__, url_prefix="/users")

BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "users")
)

# Obtener todos los usuarios
@users_bp.route("/", methods=["GET"])
@jwt_required()
@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "get_all.yml"))
def get_all_users():
    return get_all_users_controller()


# Obtener usuario por ID
@users_bp.route("/<int:user_id>", methods=["GET"])
@jwt_required()
@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "get_by_id.yml"))
def get_user_by_id(user_id):
    return get_user_by_id_controller(user_id)

# Crear usuario
@users_bp.route("/", methods=["POST"])
@jwt_required()
@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "create.yml"))
def create_user():
    return create_user_controller()


# Actualizar usuario
@users_bp.route("/<int:user_id>", methods=["PATCH"])
@jwt_required()
@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "update.yml"))
def update_user(user_id):
    return update_user_controller(user_id)

# Desactivar usuario
@users_bp.route("/<int:user_id>", methods=["DELETE"])
@jwt_required()
@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "delete.yml"))
def deactivate_user(user_id):
    return deactivate_user_controller(user_id)