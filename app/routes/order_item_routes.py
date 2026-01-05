from flask import Blueprint
from flask_jwt_extended import jwt_required
from flasgger import swag_from
from app.controllers.order_item_controller import (
    create_order_item_controller,
    update_item_status_controller,
    get_items_by_order_controller
)
import os

order_items_bp = Blueprint("order_items", __name__, url_prefix="/order-items")

BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "order_items")
)

@order_items_bp.route("/", methods=["POST"])
@jwt_required()
@swag_from(os.path.join(BASE_DOCS, "create.yml"))
def create_item():
    return create_order_item_controller()

@order_items_bp.route("/order/<int:order_id>", methods=["GET"])
@jwt_required()
@swag_from(os.path.join(BASE_DOCS, "get_by_id.yml"))
def get_by_order(order_id):
    return get_items_by_order_controller(order_id)

@order_items_bp.route("/<int:item_id>/status", methods=["PATCH"])
@jwt_required()
@swag_from(os.path.join(BASE_DOCS, "update.yml"))
def update_status(item_id):
    return update_item_status_controller(item_id)