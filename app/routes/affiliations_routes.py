from flask import Blueprint
from flask_jwt_extended import jwt_required
from flasgger import swag_from
from app.controllers.affiliation_controller import (
    create_affiliation_controller,
    get_person_affiliations_controller,
    deactivate_affiliation_controller
)
import os

affiliation_bp = Blueprint("affiliations", __name__, url_prefix="/affiliations")

BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "affiliations")
)

@affiliation_bp.route("/", methods=["POST"])
@jwt_required()
@swag_from(os.path.join(BASE_DOCS, "create.yml"))
def create_affiliation():
    return create_affiliation_controller()

@affiliation_bp.route("/person/<int:person_id>", methods=["GET"])
@jwt_required()
@swag_from(os.path.join(BASE_DOCS, "get_by_person.yml"))
def get_by_person(person_id):
    return get_person_affiliations_controller(person_id)

@affiliation_bp.route("/<int:affiliation_id>/deactivate", methods=["PATCH"])
@jwt_required()
@swag_from(os.path.join(BASE_DOCS, "deactivate.yml"))
def deactivate(affiliation_id):
    return deactivate_affiliation_controller(affiliation_id)