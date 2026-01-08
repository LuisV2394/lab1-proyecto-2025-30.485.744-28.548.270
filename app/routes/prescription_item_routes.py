from flask import Blueprint
from flask_jwt_extended import jwt_required
from flasgger.utils import swag_from
from app.utils.middleware import role_required
import os

from app.controllers.prescription_item_controller import (
    get_all_prescription_items_controller,
    get_prescription_item_by_id_controller,
    get_items_by_prescription_id_controller,
    create_prescription_item_controller,
    update_prescription_item_controller,
    delete_prescription_item_controller
)

prescription_items_bp = Blueprint("prescription_items", __name__, url_prefix="/prescription-items")

BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "prescription_item")
)

# GET ALL ITEMS
@prescription_items_bp.route("/", methods=["GET"])
# @jwt_required()
# @role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "get_all.yml"))
def get_all_prescription_items():
    return get_all_prescription_items_controller()

# GET ITEM BY ID
@prescription_items_bp.route("/<int:item_id>", methods=["GET"])
# @jwt_required()
# @role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "get_by_id.yml"))
def get_prescription_item_by_id(item_id):
    return get_prescription_item_by_id_controller(item_id)

# GET ITEMS BY PRESCRIPTION ID
@prescription_items_bp.route("/by-prescription/<int:prescription_id>", methods=["GET"])
# @jwt_required()
# @role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "get_by_prescription.yml"))
def get_items_by_prescription_id(prescription_id):
    return get_items_by_prescription_id_controller(prescription_id)

# CREATE ITEM
@prescription_items_bp.route("/", methods=["POST"])
# @jwt_required()
# @role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "create.yml"))
def create_prescription_item():
    return create_prescription_item_controller()

# UPDATE ITEM
@prescription_items_bp.route("/<int:item_id>", methods=["PATCH"])
# @jwt_required()
# @role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "update.yml"))
def update_prescription_item(item_id):
    return update_prescription_item_controller(item_id)

# DELETE ITEM
@prescription_items_bp.route("/<int:item_id>", methods=["DELETE"])
# @jwt_required()
# @role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "delete.yml"))
def delete_prescription_item(item_id):
    return delete_prescription_item_controller(item_id)