from flask import Blueprint
from flask_jwt_extended import jwt_required
from flasgger import swag_from
from app.controllers.insurance_company_controller import (
    get_all_insurances_controller,
    create_insurance_controller,
    update_insurance_controller,
    delete_insurance_controller,
    get_insurance_by_id_controller
)
import os

insurance_bp = Blueprint("insurances", __name__, url_prefix="/insurances")

BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "insurances")
)

@insurance_bp.route("/", methods=["GET"])
@jwt_required()
@swag_from(os.path.join(BASE_DOCS, "get_all.yml"))
def get_all():
    return get_all_insurances_controller()

@insurance_bp.route("/<int:insurance_id>", methods=["GET"])
@jwt_required()
@swag_from(os.path.join(BASE_DOCS, "get_by_id.yml"))
def get_by_id(insurance_id):
    return get_insurance_by_id_controller(insurance_id)

@insurance_bp.route("/", methods=["POST"])
@jwt_required()
@swag_from(os.path.join(BASE_DOCS, "create.yml"))
def create_insurance():
    return create_insurance_controller()

@insurance_bp.route("/<int:insurance_id>", methods=["PUT"])
@jwt_required()
@swag_from(os.path.join(BASE_DOCS, "update.yml"))
def update_insurance(insurance_id):
    return update_insurance_controller(insurance_id)

@insurance_bp.route("/<int:insurance_id>", methods=["DELETE"])
@jwt_required()
@swag_from(os.path.join(BASE_DOCS, "delete.yml"))
def delete_insurance(insurance_id):
    return delete_insurance_controller(insurance_id)