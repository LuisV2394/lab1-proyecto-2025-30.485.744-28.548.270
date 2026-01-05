from flask import Blueprint
from flask_jwt_extended import jwt_required
from flasgger.utils import swag_from
from app.utils.middleware import role_required
import os

from app.controllers.affiliation_controller import (
    create_affiliation_controller,
    get_all_affiliations_controller,
    get_person_affiliations_controller,
    update_affiliation_controller,
    deactivate_affiliation_controller
)

affiliation_bp = Blueprint("affiliations", __name__, url_prefix="/affiliations")

BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "affiliation")
)

# -------------------- Crear afiliación --------------------
@affiliation_bp.route("/", methods=["POST"])
#@jwt_required()
#@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "create.yml"))
def create_affiliation():
    return create_affiliation_controller()

# -------------------- Obtener todas las afiliaciones --------------------
@affiliation_bp.route("/", methods=["GET"])
#@jwt_required()
#@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "get_all.yml"))
def get_all_affiliations():
    return get_all_affiliations_controller()

# -------------------- Obtener afiliaciones por persona --------------------
@affiliation_bp.route("/person/<int:person_id>", methods=["GET"])
#@jwt_required()
#@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "get_by_id.yml"))
def get_by_person(person_id):
    return get_person_affiliations_controller(person_id)

# -------------------- Actualizar afiliación --------------------
@affiliation_bp.route("/<int:affiliation_id>", methods=["PUT"])
#@jwt_required()
#@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "update.yml"))
def update_affiliation(affiliation_id):
    return update_affiliation_controller(affiliation_id)

# -------------------- Desactivar afiliación --------------------
@affiliation_bp.route("/<int:affiliation_id>/deactivate", methods=["PATCH"])
#@jwt_required()
#@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "desactivate.yml"))
def deactivate_affiliation(affiliation_id):
    return deactivate_affiliation_controller(affiliation_id)