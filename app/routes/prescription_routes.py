from flask import Blueprint
from flask_jwt_extended import jwt_required
from flasgger.utils import swag_from
from app.utils.middleware import role_required
import os

from app.controllers.prescription_controller import (
    get_all_prescriptions_controller,
    get_prescription_by_id_controller,
    create_prescription_controller,
    update_prescription_controller,
    delete_prescription_controller
)

prescriptions_bp = Blueprint("prescriptions", __name__, url_prefix="/prescriptions")

BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "prescription")
)

@prescriptions_bp.route("/", methods=["GET"])
#@jwt_required()
#@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "get_all.yml"))
def get_all_prescriptions():
    return get_all_prescriptions_controller()

@prescriptions_bp.route("/<int:prescription_id>", methods=["GET"])
#@jwt_required()
#@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "get_by_id.yml"))
def get_prescription_by_id(prescription_id):
    return get_prescription_by_id_controller(prescription_id)

@prescriptions_bp.route("/", methods=["POST"])
#@jwt_required()
#@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "create.yml"))
def create_prescription():
    return create_prescription_controller()

@prescriptions_bp.route("/<int:prescription_id>", methods=["PATCH"])
#@jwt_required()
#@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "update.yml"))
def update_prescription(prescription_id):
    return update_prescription_controller(prescription_id)

@prescriptions_bp.route("/<int:prescription_id>", methods=["DELETE"])
#@jwt_required()
#@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "delete.yml"))
def delete_prescription(prescription_id):
    return delete_prescription_controller(prescription_id)