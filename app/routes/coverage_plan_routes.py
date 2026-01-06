from flask import Blueprint
from flask_jwt_extended import jwt_required
from flasgger.utils import swag_from
from app.utils.middleware import role_required
import os

# Controladores
from app.controllers.coverage_plan_controller import (
    get_all_coverage_plans_controller,
    get_coverage_plan_by_id_controller,
    create_coverage_plan_controller,
    update_coverage_plan_controller,
    delete_coverage_plan_controller
)

plans_bp = Blueprint("plans", __name__, url_prefix="/plans")

BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "coverage_plans")
)

# Obtener todos los planes
@plans_bp.route("/", methods=["GET"])
#@jwt_required()
#@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "get_all.yml"))
def get_all_plans():
    return get_all_coverage_plans_controller()


# Obtener plan por ID
@plans_bp.route("/<int:plan_id>", methods=["GET"])
#@jwt_required()
#@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "get_by_id.yml"))
def get_plan_by_id(plan_id):
    return get_coverage_plan_by_id_controller(plan_id)


# Crear nuevo plan
@plans_bp.route("/", methods=["POST"])
#@jwt_required()
#@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "create.yml"))
def create_plan():
    return create_coverage_plan_controller()


# Actualizar plan existente
@plans_bp.route("/<int:plan_id>", methods=["PATCH"])
#@jwt_required()
#@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "update.yml"))
def update_plan(plan_id):
    return update_coverage_plan_controller(plan_id)


# Eliminar plan
@plans_bp.route("/<int:plan_id>", methods=["DELETE"])
#@jwt_required()
#@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "delete.yml"))
def delete_plan(plan_id):
    return delete_coverage_plan_controller(plan_id)