from flask import Blueprint
from flask_jwt_extended import jwt_required
from flasgger.utils import swag_from
from app.utils.middleware import role_required
import os

# Controladores
from app.controllers.units_controller import (
    get_all_units_controller,
    get_unit_by_id_controller,
    create_unit_controller,
    update_unit_controller,
    deactivate_unit_controller
)

units_bp = Blueprint("units", __name__, url_prefix="/units")

BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "units")
)


# Obtener todas las unidades
@units_bp.route("/", methods=["GET"])
@jwt_required()
@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "get_all.yml"))
def get_all_units():
    return get_all_units_controller()


# Obtener unidad por ID
@units_bp.route("/<int:unit_id>", methods=["GET"])
@jwt_required()
@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "get_by_id.yml"))
def get_unit_by_id(unit_id):
    return get_unit_by_id_controller(unit_id)


# Crear nueva unidad
@units_bp.route("/", methods=["POST"])
# @jwt_required()
# @role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "create.yml"))
def create_unit():
    return create_unit_controller()


# Actualizar unidad
@units_bp.route("/<int:unit_id>", methods=["PATCH"])
@jwt_required()
@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "update.yml"))
def update_unit(unit_id):
    return update_unit_controller(unit_id)


# Desactivar unidad
@units_bp.route("/<int:unit_id>", methods=["DELETE"])
@jwt_required()
@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "delete.yml"))
def deactivate_unit(unit_id):
    return deactivate_unit_controller(unit_id)