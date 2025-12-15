from flask import Blueprint
from flasgger import swag_from
import os

from app.controllers.diagnosis_controller import (
    add_diagnosis_controller,
    get_all_diagnoses_controller,
    get_diagnosis_by_id_controller,
    update_diagnosis_controller,
    delete_diagnosis_controller
)

diagnosis_bp = Blueprint("diagnoses", __name__, url_prefix="/diagnoses")

BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "diagnosis")
)

# CREATE
@diagnosis_bp.route("/", methods=["POST"])
@swag_from(os.path.join(BASE_DOCS, "create.yml"))
def add_diagnosis():
    return add_diagnosis_controller()

# READ ALL
@diagnosis_bp.route("/", methods=["GET"])
@swag_from(os.path.join(BASE_DOCS, "get_all.yml"))
def get_all_diagnoses():
    return get_all_diagnoses_controller()

# READ BY ID
@diagnosis_bp.route("/<int:diagnosis_id>", methods=["GET"])
@swag_from(os.path.join(BASE_DOCS, "get_by_id.yml"))
def get_diagnosis_by_id(diagnosis_id):
    return get_diagnosis_by_id_controller(diagnosis_id)


# UPDATE
@diagnosis_bp.route("/<int:diagnosis_id>", methods=["PUT"])
@swag_from(os.path.join(BASE_DOCS, "update.yml"))
def update_diagnosis(diagnosis_id):
    return update_diagnosis_controller(diagnosis_id)

# DELETE
@diagnosis_bp.route("/<int:diagnosis_id>", methods=["DELETE"])
@swag_from(os.path.join(BASE_DOCS, "delete.yml"))
def delete_diagnosis(diagnosis_id):
    return delete_diagnosis_controller(diagnosis_id)