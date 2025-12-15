from flask import Blueprint
from flasgger import swag_from
import os

from app.controllers.consent_controller import (
    create_consent_controller,
    get_all_consents_controller,
    get_consent_by_id_controller,
    update_consent_controller,
    delete_consent_controller
)

consent_bp = Blueprint("consents", __name__, url_prefix="/consents")

BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "consent")
)

# CREATE
@consent_bp.route("/", methods=["POST"])
@swag_from(os.path.join(BASE_DOCS, "create.yml"))
def create_consent():
    return create_consent_controller()

# READ ALL
@consent_bp.route("/", methods=["GET"])
@swag_from(os.path.join(BASE_DOCS, "get_all.yml"))
def get_all_consents():
    return get_all_consents_controller()

# READ BY ID
@consent_bp.route("/<int:consent_id>", methods=["GET"])
@swag_from(os.path.join(BASE_DOCS, "get_by_id.yml"))
def get_consent_by_id(consent_id):
    return get_consent_by_id_controller(consent_id)

# UPDATE
@consent_bp.route("/<int:consent_id>", methods=["PUT"])
@swag_from(os.path.join(BASE_DOCS, "update.yml"))
def update_consent(consent_id):
    return update_consent_controller(consent_id)

# DELETE
@consent_bp.route("/<int:consent_id>", methods=["DELETE"])
@swag_from(os.path.join(BASE_DOCS, "delete.yml"))
def delete_consent(consent_id):
    return delete_consent_controller(consent_id)