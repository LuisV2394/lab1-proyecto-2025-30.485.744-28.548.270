from flask import Blueprint
from flask_jwt_extended import jwt_required
from flasgger.utils import swag_from
from app.utils.middleware import role_required
import os

from app.controllers.people_controller import (
    get_all_people_controller,
    get_person_by_id_controller,
    create_person_controller,
    update_person_controller,
    deactivate_person_controller
)

people_bp = Blueprint("people", __name__, url_prefix="/people")

BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "people")
)

# Obtener todas las personas
@people_bp.route("/", methods=["GET"])
#@jwt_required()
#@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "get_all.yml"))
def get_all_people():
    return get_all_people_controller()

# Obtener persona por ID
@people_bp.route("/<int:person_id>", methods=["GET"])
#@jwt_required()
#@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "get_by_id.yml"))
def get_person_by_id(person_id):
    return get_person_by_id_controller(person_id)

# Crear persona
@people_bp.route("/", methods=["POST"])
#@jwt_required()
#@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "create.yml"))
def create_person():
    return create_person_controller()

# Actualizar persona
@people_bp.route("/<int:person_id>", methods=["PATCH"])
#@jwt_required()
#@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "update.yml"))
def update_person(person_id):
    return update_person_controller(person_id)

# Desactivar persona
@people_bp.route("/<int:person_id>", methods=["DELETE"])
#@jwt_required()
#@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "delete.yml"))
def deactivate_person(person_id):
    return deactivate_person_controller(person_id)