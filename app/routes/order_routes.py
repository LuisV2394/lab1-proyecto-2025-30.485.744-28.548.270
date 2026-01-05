from flask import Blueprint
from flask_jwt_extended import jwt_required
from flasgger.utils import swag_from
from app.utils.middleware import role_required
import os

# Controladores
from app.controllers.order_controller import (
    get_all_orders_controller,
    get_order_by_id_controller,
    create_order_controller,
    update_order_status_controller,
    cancel_order_controller
)

orders_bp = Blueprint("orders", __name__, url_prefix="/orders")

BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "orders")
)

# Obtener todas las órdenes
@orders_bp.route("/", methods=["GET"])
#@jwt_required()
#@role_required(["admin", "doctor"])
@swag_from(os.path.join(BASE_DOCS, "get_all.yml"))
def get_all_orders():
    return get_all_orders_controller()

# Obtener orden por ID
@orders_bp.route("/<int:order_id>", methods=["GET"])
#@jwt_required()
#@role_required(["admin", "doctor"])
@swag_from(os.path.join(BASE_DOCS, "get_by_id.yml"))
def get_order_by_id(order_id):
    return get_order_by_id_controller(order_id)

# Crear nueva orden
@orders_bp.route("/", methods=["POST"])
#@jwt_required()
#@role_required(["admin", "doctor"])
@swag_from(os.path.join(BASE_DOCS, "create.yml"))
def create_order():
    return create_order_controller()

# Actualizar estado de la orden
@orders_bp.route("/<int:order_id>/status", methods=["PATCH"])
#@jwt_required()
#@role_required(["admin", "doctor"])
@swag_from(os.path.join(BASE_DOCS, "update.yml"))
def update_order_status(order_id):
    return update_order_status_controller(order_id)

# Cancelar orden
@orders_bp.route("/<int:order_id>/cancel", methods=["PATCH"])
#@jwt_required()
#@role_required(["admin", "doctor"])
@swag_from(os.path.join(BASE_DOCS, "cancel.yml"))
def cancel_order(order_id):
    return cancel_order_controller(order_id)