from flask import Blueprint
from flask_jwt_extended import jwt_required
from flasgger.utils import swag_from
from app.utils.middleware import role_required
import os

from app.controllers.services_controller import (
    get_all_services_controller,
    get_service_by_id_controller,
    create_service_controller,
    update_service_controller,
    deactivate_service_controller
)

services_bp = Blueprint("services", __name__, url_prefix="/services")

# Ruta base de los YAML de documentación
BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "services")
)

# Obtener todos los servicios
@services_bp.route("/", methods=["GET"])
#@jwt_required()
#@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "get_all.yml"))
def get_all_services():
    return get_all_services_controller()

# Obtener servicio por ID
@services_bp.route("/<int:service_id>", methods=["GET"])
#@jwt_required()
#@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "get_by_id.yml"))
def get_service_by_id(service_id):
    return get_service_by_id_controller(service_id)

# Crear nuevo servicio
@services_bp.route("/", methods=["POST"])
#@jwt_required()
#@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "create.yml"))
def create_service():
    return create_service_controller()

# Actualizar servicio existente
@services_bp.route("/<int:service_id>", methods=["PATCH"])
#@jwt_required()
#@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "update.yml"))
def update_service(service_id):
    return update_service_controller(service_id)

# Desactivar servicio
@services_bp.route("/<int:service_id>", methods=["DELETE"])
#@jwt_required()
#@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "delete.yml"))
def deactivate_service(service_id):
    return deactivate_service_controller(service_id)