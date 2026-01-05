from flask import Blueprint
from flask_jwt_extended import jwt_required
from flasgger import swag_from
from app.controllers.prescription_controller import (
    create_prescription_controller,
    get_prescriptions_by_episode_controller,
    delete_prescription_controller
)
import os

prescription_bp = Blueprint("prescriptions", __name__, url_prefix="/prescriptions")

BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "prescription")
)

# Crear receta
@prescription_bp.route("/", methods=["POST"])
@jwt_required()
@swag_from(os.path.join(BASE_DOCS, "create.yml"))
def create_prescription():
    return create_prescription_controller()

# Obtener recetas de un episodio
@prescription_bp.route("/episode/<int:episode_id>", methods=["GET"])
@jwt_required()
@swag_from(os.path.join(BASE_DOCS, "get_by_id.yml"))
def get_prescriptions_by_episode(episode_id):
    return get_prescriptions_by_episode_controller(episode_id)

# Eliminar receta
@prescription_bp.route("/<int:prescription_id>", methods=["DELETE"])
@jwt_required()
@swag_from(os.path.join(BASE_DOCS, "delete.yml"))
def delete_prescription(prescription_id):
    return delete_prescription_controller(prescription_id)