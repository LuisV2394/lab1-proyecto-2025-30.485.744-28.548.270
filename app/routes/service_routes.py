from flask import Blueprint
from flask_jwt_extended import jwt_required
from flasgger import swag_from
from app.controllers.services_controller import (
    get_all_services_controller,
    create_service_controller,
    update_service_controller,
    delete_service_controller
)
import os

services_bp = Blueprint("services", __name__, url_prefix="/services")

BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "services")
)

@services_bp.route("/", methods=["GET"])
@jwt_required()
@swag_from(os.path.join(BASE_DOCS, "get_all.yml"))
def get_services():
    return get_all_services_controller()

@services_bp.route("/", methods=["POST"])
@jwt_required()
@swag_from(os.path.join(BASE_DOCS, "create.yml"))
def create_service():
    return create_service_controller()

@services_bp.route("/<int:service_id>", methods=["PUT"])
@jwt_required()
@swag_from(os.path.join(BASE_DOCS, "update.yml"))
def update_service(service_id):
    return update_service_controller(service_id)

@services_bp.route("/<int:service_id>", methods=["DELETE"])
@jwt_required()
@swag_from(os.path.join(BASE_DOCS, "delete.yml"))
def delete_service(service_id):
    return delete_service_controller(service_id)