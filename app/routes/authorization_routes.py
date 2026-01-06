from flask import Blueprint
from flasgger import swag_from
# from flask_jwt_extended import jwt_required
# from app.utils.middleware import role_required
import os

from app.controllers.authorization_controller import (
    create_authorization_controller,
    get_all_authorizations_controller,
    get_authorization_by_id_controller,
    update_authorization_controller,
    delete_authorization_controller
)

authorization_bp = Blueprint("authorizations", __name__, url_prefix="/authorizations")

BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "authorization")
)

# CREATE
@authorization_bp.route("/", methods=["POST"])
#@jwt_required()
#@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "create.yml"))
def create_authorization():
    return create_authorization_controller()

# GET ALL
@authorization_bp.route("/", methods=["GET"])
#@jwt_required()
#@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "get_all.yml"))
def get_all_authorizations():
    return get_all_authorizations_controller()

# GET BY ID
@authorization_bp.route("/<int:auth_id>", methods=["GET"])
#@jwt_required()
#@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "get_by_id.yml"))
def get_authorization_by_id(auth_id):
    return get_authorization_by_id_controller(auth_id)

# UPDATE
@authorization_bp.route("/<int:auth_id>", methods=["PUT"])
#@jwt_required()
#@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "update.yml"))
def update_authorization(auth_id):
    return update_authorization_controller(auth_id)

# DELETE
@authorization_bp.route("/<int:auth_id>", methods=["DELETE"])
#@jwt_required()
#@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "delete.yml"))
def delete_authorization(auth_id):
    return delete_authorization_controller(auth_id)