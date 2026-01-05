from flask import Blueprint
from flasgger import swag_from
from flask_jwt_extended import jwt_required
from app.utils.middleware import role_required
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
#@jwt_required()
#@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "create.yml"))
def add_diagnosis():
    return add_diagnosis_controller()

# READ ALL
@diagnosis_bp.route("/", methods=["GET"])
#@jwt_required()
#@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "get_all.yml"))
def get_all_diagnoses():
    return get_all_diagnoses_controller()

# READ BY ID
@diagnosis_bp.route("/<int:diagnosis_id>", methods=["GET"])
#@jwt_required()
#@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "get_by_id.yml"))
def get_diagnosis_by_id(diagnosis_id):
    return get_diagnosis_by_id_controller(diagnosis_id)

# UPDATE
@diagnosis_bp.route("/<int:diagnosis_id>", methods=["PUT"])
#@jwt_required()
#@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "update.yml"))
def update_diagnosis(diagnosis_id):
    return update_diagnosis_controller(diagnosis_id)

# DELETE
@diagnosis_bp.route("/<int:diagnosis_id>", methods=["DELETE"])
#@jwt_required()
#@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "delete.yml"))
def delete_diagnosis(diagnosis_id):
    return delete_diagnosis_controller(diagnosis_id)