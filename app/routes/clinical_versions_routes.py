from flask import Blueprint
from flask_jwt_extended import jwt_required
from flasgger import swag_from
from app.controllers.clinical_versions_controller import get_history_by_entity_controller
import os

version_bp = Blueprint("versions", __name__, url_prefix="/versions")

BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "versions")
)

@version_bp.route("/<string:entity_type>/<int:entity_id>", methods=["GET"])
@jwt_required()
@swag_from(os.path.join(BASE_DOCS, "get_history.yml"))
def get_version_history(entity_type, entity_id):
    # entity_type debe ser 'note' o 'result'
    if entity_type not in ['note', 'result']:
        return {"error": "Tipo de entidad inválido"}, 400
    return get_history_by_entity_controller(entity_type, entity_id)