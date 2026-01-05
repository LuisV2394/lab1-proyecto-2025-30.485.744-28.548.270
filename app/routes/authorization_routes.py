from flask import Blueprint
from flask_jwt_extended import jwt_required
from flasgger import swag_from
from app.controllers.authorization_controller import (
    create_authorization_request_controller,
    update_authorization_response_controller,
    get_authorizations_by_order_controller
)
import os

auth_request_bp = Blueprint("authorizations", __name__, url_prefix="/authorizations")

BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "authorizations")
)

@auth_request_bp.route("/", methods=["POST"])
@jwt_required()
@swag_from(os.path.join(BASE_DOCS, "create.yml"))
def create_auth():
    return create_authorization_request_controller()

@auth_request_bp.route("/<int:auth_id>/response", methods=["PATCH"])
@jwt_required()
@swag_from(os.path.join(BASE_DOCS, "update_response.yml"))
def update_response(auth_id):
    return update_authorization_response_controller(auth_id)

@auth_request_bp.route("/order/<int:order_id>", methods=["GET"])
@jwt_required()
@swag_from(os.path.join(BASE_DOCS, "get_by_order.yml"))
def get_by_order(order_id):
    return get_authorizations_by_order_controller(order_id)