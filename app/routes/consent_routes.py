from flask import Blueprint
from flasgger import swag_from
import os

from app.controllers.consent_controller import create_consent_controller

consent_bp = Blueprint("consents", __name__, url_prefix="/consents")

BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "consent")
)


@consent_bp.route("/", methods=["POST"])
@swag_from(os.path.join(BASE_DOCS, "create.yml"))
def create_consent():
    return create_consent_controller()