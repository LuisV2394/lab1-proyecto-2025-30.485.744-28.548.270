from flask import Blueprint
from flask_jwt_extended import jwt_required
from flasgger import swag_from
from app.utils.middleware import role_required
import os

# Controladores
from app.controllers.clinical_versions_controller import (
    get_all_versions_controller,
    get_version_by_id_controller,
    get_history_by_entity_controller,
    create_version_controller,
    update_version_controller,
    delete_version_controller
)

version_bp = Blueprint("versions", __name__, url_prefix="/versions")

BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "clinical_version")
)
# GET ALL VERSIONS
@version_bp.route("/", methods=["GET"])
#@jwt_required()
# @role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "get_all.yml"))
def get_all_versions():
    return get_all_versions_controller()

# GET VERSION BY ID
@version_bp.route("/id/<int:version_id>", methods=["GET"])
#@jwt_required()
# @role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "get_by_id.yml"))
def get_version_by_id(version_id):
    return get_version_by_id_controller(version_id)

# GET HISTORY BY ENTITY
@version_bp.route("/<string:entity_type>/<int:entity_id>", methods=["GET"])
#@jwt_required()
# @role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "get_history.yml"))
def get_version_history(entity_type, entity_id):
    # Validar tipo de entidad
    allowed_types = ['note', 'result', 'prescription', 'episode']
    if entity_type not in allowed_types:
        return {"error": f"Invalid entity_type. Allowed: {allowed_types}"}, 400

    return get_history_by_entity_controller(entity_type, entity_id)

# CREATE VERSION (manual)
@version_bp.route("/", methods=["POST"])
#@jwt_required()
# @role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "create.yml"))
def create_version():
    return create_version_controller()

# UPDATE VERSION
@version_bp.route("/<int:version_id>", methods=["PATCH"])
#@jwt_required()
# @role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "update.yml"))
def update_version(version_id):
    return update_version_controller(version_id)

# DELETE VERSION
@version_bp.route("/<int:version_id>", methods=["DELETE"])
#@jwt_required()
# @role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "delete.yml"))
def delete_version(version_id):
    return delete_version_controller(version_id)