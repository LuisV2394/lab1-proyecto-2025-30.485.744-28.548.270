from flask import Blueprint
from flask_jwt_extended import jwt_required
from flasgger.utils import swag_from
from app.utils.middleware import role_required
import os

# Controllers
from app.controllers.order_detail_controller import (
    create_order_detail_controller,
    get_order_detail_controller,
    get_all_order_details_controller,
    get_order_details_by_order_controller,
    update_order_detail_controller,
    delete_order_detail_controller
)

order_details_bp = Blueprint("order_details", __name__, url_prefix="/order-details")

BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "order_details")
)

# Get All Order Details
@order_details_bp.route("/", methods=["GET"])
# @jwt_required()
# @role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "get_all.yml"))
def get_all_order_details_route():
    return get_all_order_details_controller()

# Create Order Detail
@order_details_bp.route("/", methods=["POST"])
# @jwt_required()
# @role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "create.yml"))
def create_order_detail_route():
    return create_order_detail_controller()

# Get Order Detail by ID
@order_details_bp.route("/<int:detail_id>", methods=["GET"])
# @jwt_required()
# @role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "get_by_id.yml"))
def get_order_detail_route(detail_id):
    return get_order_detail_controller(detail_id)

# Get Order Details by Order
@order_details_bp.route("/order/<int:order_id>", methods=["GET"])
# @jwt_required()
# @role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "get_by_order.yml"))
def get_order_details_by_order_route(order_id):
    return get_order_details_by_order_controller(order_id)

# Update Order Detail
@order_details_bp.route("/<int:detail_id>", methods=["PATCH"])
# @jwt_required()
# @role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "update.yml"))
def update_order_detail_route(detail_id):
    return update_order_detail_controller(detail_id)

# Delete Order Detail
@order_details_bp.route("/<int:detail_id>", methods=["DELETE"])
# @jwt_required()
# @role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "delete.yml"))
def delete_order_detail_route(detail_id):
    return delete_order_detail_controller(detail_id)