from flask import Blueprint
from flasgger import swag_from
from flask_jwt_extended import jwt_required
from app.utils.middleware import role_required
import os

from app.controllers.insurer_controller import (
    get_all_insurers_controller,
    get_insurer_by_id_controller,
    create_insurer_controller,
    update_insurer_controller,
    delete_insurer_controller
)

insurer_bp = Blueprint("insurers", __name__, url_prefix="/insurers")

BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "insurer")
)

# CREATE
@insurer_bp.route("/", methods=["POST"])
#@jwt_required()
#@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "create.yml"))
def create_insurer():
    return create_insurer_controller()

# READ ALL
@insurer_bp.route("/", methods=["GET"])
#@jwt_required()
#@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "get_all.yml"))
def get_all_insurers():
    return get_all_insurers_controller()

# READ BY ID
@insurer_bp.route("/<int:insurer_id>", methods=["GET"])
#@jwt_required()
#@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "get_by_id.yml"))
def get_insurer_by_id(insurer_id):
    return get_insurer_by_id_controller(insurer_id)

# UPDATE
@insurer_bp.route("/<int:insurer_id>", methods=["PATCH"])
#@jwt_required()
#@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "update.yml"))
def update_insurer(insurer_id):
    return update_insurer_controller(insurer_id)

# DELETE
@insurer_bp.route("/<int:insurer_id>", methods=["DELETE"])
#@jwt_required()
#@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "delete.yml"))
def delete_insurer(insurer_id):
    return delete_insurer_controller(insurer_id)