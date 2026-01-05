from flask import Blueprint
from flask_jwt_extended import jwt_required
from flasgger.utils import swag_from
from app.utils.middleware import role_required
import os

# Controladores
from app.controllers.result_controller import (
    get_all_results_controller,
    get_result_by_id_controller,
    create_result_controller,
    update_result_controller,
    delete_result_controller
)

results_bp = Blueprint("results", __name__, url_prefix="/results")

BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "results")
)

# Obtener todos los resultados
@results_bp.route("/", methods=["GET"])
#@jwt_required()
#@role_required(["admin", "doctor"])
@swag_from(os.path.join(BASE_DOCS, "get_all.yml"))
def get_all_results():
    return get_all_results_controller()

# Obtener resultado por ID
@results_bp.route("/<int:result_id>", methods=["GET"])
#@jwt_required()
#@role_required(["admin", "doctor"])
@swag_from(os.path.join(BASE_DOCS, "get_by_id.yml"))
def get_result_by_id(result_id):
    return get_result_by_id_controller(result_id)

# Crear un nuevo resultado
@results_bp.route("/", methods=["POST"])
#@jwt_required()
#@role_required(["admin", "doctor"])
@swag_from(os.path.join(BASE_DOCS, "create.yml"))
def create_result():
    return create_result_controller()

# Actualizar un resultado existente
@results_bp.route("/<int:result_id>", methods=["PATCH"])
#@jwt_required()
#@role_required(["admin", "doctor"])
@swag_from(os.path.join(BASE_DOCS, "update.yml"))
def update_result(result_id):
    return update_result_controller(result_id)

# Eliminar un resultado
@results_bp.route("/<int:result_id>", methods=["DELETE"])
#@jwt_required()
#@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "delete.yml"))
def delete_result(result_id):
    return delete_result_controller(result_id)