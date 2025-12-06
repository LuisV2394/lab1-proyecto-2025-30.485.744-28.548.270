from flask import Blueprint
from flask_jwt_extended import jwt_required
from flasgger.utils import swag_from
from app.utils.middleware import role_required
import os

# Controladores
from app.controllers.professionals_controller import (
    get_all_professionals_controller,
    get_professional_by_id_controller,
    create_professional_controller,
    update_professional_controller,
    deactivate_professional_controller
)

professionals_bp = Blueprint("professionals", __name__, url_prefix="/professionals")

BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "professionals")
)

# Obtener todos los profesionales
@professionals_bp.route("/", methods=["GET"])
@jwt_required()
@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "get_all.yml"))
def get_all_professionals():
    return get_all_professionals_controller()


# Buscar profesional por ID
@professionals_bp.route("/<int:professional_id>", methods=["GET"])
@jwt_required()
@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "get_by_id.yml"))
def get_professional_by_id(professional_id):
    return get_professional_by_id_controller(professional_id)

# Crear nuevo profesional
@professionals_bp.route("/", methods=["POST"])
@jwt_required()
@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "create.yml"))
def create_professional():
    return create_professional_controller()

# Actualizar profesional existente
@professionals_bp.route("/<int:professional_id>", methods=["PATCH"])
@jwt_required()
@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "update.yml"))
def update_professional(professional_id):
    return update_professional_controller(professional_id)

# Desactivar profesional
@professionals_bp.route("/<int:professional_id>", methods=["DELETE"])
@jwt_required()
@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "delete.yml"))
def deactivate_professional(professional_id):
    return deactivate_professional_controller(professional_id)