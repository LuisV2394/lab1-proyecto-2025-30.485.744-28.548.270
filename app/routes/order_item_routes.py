from flask import Blueprint
from flask_jwt_extended import jwt_required
from flasgger.utils import swag_from
from app.utils.middleware import role_required
import os

# Controllers
from app.controllers.order_item_controller import (
    create_order_item,
    get_order_item,
    get_all_order_items,
    get_order_items_by_order,
    update_order_item,
    delete_order_item
)

order_items_bp = Blueprint("order_items", __name__, url_prefix="/order-items")

BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "order_items")
)

# Get All Order Items
@order_items_bp.route("/", methods=["GET"])
#@jwt_required()
#@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "get_all.yml"))
def get_all_order_items_route():
    return get_all_order_items()

# Create Order Item
@order_items_bp.route("/", methods=["POST"])
#@jwt_required()
#@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "create.yml"))
def create_order_item_route():
    return create_order_item()

# Get Order Item by ID
@order_items_bp.route("/<int:order_item_id>", methods=["GET"])
#@jwt_required()
#@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "get_by_id.yml"))
def get_order_item_route(order_item_id):
    return get_order_item(order_item_id)

# Get Order Items by Order
@order_items_bp.route("/order/<int:order_id>", methods=["GET"])
#@jwt_required()
#@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "get_by_order.yml"))
def get_order_items_by_order_route(order_id):
    return get_order_items_by_order(order_id)

# Update Order Item
@order_items_bp.route("/<int:order_item_id>", methods=["PATCH"])
#@jwt_required()
#@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "update.yml"))
def update_order_item_route(order_item_id):
    return update_order_item(order_item_id)

# Delete Order Item
@order_items_bp.route("/<int:order_item_id>", methods=["DELETE"])
#@jwt_required()
#@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "delete.yml"))
def delete_order_item_route(order_item_id):
    return delete_order_item(order_item_id)