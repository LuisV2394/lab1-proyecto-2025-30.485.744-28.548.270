from flask import Blueprint
from flasgger import swag_from
from flask_jwt_extended import jwt_required
import os

from app.controllers.diagnosis_controller import add_diagnosis_controller

diagnosis_bp = Blueprint("diagnoses", __name__, url_prefix="/diagnoses")

BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "diagnosis")
)


@diagnosis_bp.route("/", methods=["POST"])
@jwt_required()
@swag_from(os.path.join(BASE_DOCS, "create.yml"))
def add_diagnosis():
    return add_diagnosis_controller()