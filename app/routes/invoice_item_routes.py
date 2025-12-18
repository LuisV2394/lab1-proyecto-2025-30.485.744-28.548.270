from flask import Blueprint
from flasgger import swag_from
import os

from app.controllers.invoice_item_controller import (
    get_all_invoice_items_controller,
    get_invoice_item_by_id_controller,
    create_invoice_item_controller,
    update_invoice_item_controller,
    delete_invoice_item_controller
)

invoice_item_bp = Blueprint("invoice_items", __name__, url_prefix="/invoice_items")

BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "invoice_item")
)

# CREATE
@invoice_item_bp.route("/", methods=["POST"])
@swag_from(os.path.join(BASE_DOCS, "create.yml"))
def create_invoice_item():
    return create_invoice_item_controller()

# READ ALL
@invoice_item_bp.route("/", methods=["GET"])
@swag_from(os.path.join(BASE_DOCS, "get_all.yml"))
def get_all_invoice_items():
    return get_all_invoice_items_controller()

# READ BY ID
@invoice_item_bp.route("/<int:item_id>", methods=["GET"])
@swag_from(os.path.join(BASE_DOCS, "get_by_id.yml"))
def get_invoice_item_by_id(item_id):
    return get_invoice_item_by_id_controller(item_id)

# UPDATE
@invoice_item_bp.route("/<int:item_id>", methods=["PATCH"])
@swag_from(os.path.join(BASE_DOCS, "update.yml"))
def update_invoice_item(item_id):
    return update_invoice_item_controller(item_id)

# DELETE
@invoice_item_bp.route("/<int:item_id>", methods=["DELETE"])
@swag_from(os.path.join(BASE_DOCS, "delete.yml"))
def delete_invoice_item(item_id):
    return delete_invoice_item_controller(item_id)