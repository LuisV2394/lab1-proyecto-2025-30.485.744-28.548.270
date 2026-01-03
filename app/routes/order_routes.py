from flask import Blueprint
from flask_jwt_extended import jwt_required
from flasgger import swag_from
from app.controllers.order_controller import (
    create_order_controller,
    get_orders_by_episode_controller,
    update_order_status_controller,
    delete_order_controller
)
import os

orders_bp = Blueprint("orders", __name__, url_prefix="/orders")

BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "orders")
)

# Create a new order
@orders_bp.route("/", methods=["POST"])
@jwt_required()
@swag_from(os.path.join(BASE_DOCS, "create.yml"))
def create_order():
    return create_order_controller()

# get a order by episode
@orders_bp.route("/episode/<int:episode_id>", methods=["GET"])
@jwt_required()
@swag_from(os.path.join(BASE_DOCS, "get_by_episode.yml"))
def get_orders_by_episode(episode_id):
    return get_orders_by_episode_controller(episode_id)

# update order status
@orders_bp.route("/<int:order_id>/status", methods=["PATCH"])
@jwt_required()
@swag_from(os.path.join(BASE_DOCS, "update_status.yml"))
def update_order_status(order_id):
    return update_order_status_controller(order_id)

# delete order
@orders_bp.route("/<int:order_id>", methods=["DELETE"])
@jwt_required()
@swag_from(os.path.join(BASE_DOCS, "delete.yml"))
def delete_order(order_id):
    return delete_order_controller(order_id)