from flask import Blueprint
from flask_jwt_extended import jwt_required
from flasgger.utils import swag_from
from app.utils.middleware import role_required
import os

# Controladores
from app.controllers.payment_controller import (
    create_payment_controller,
    get_all_payments_controller,
    get_payment_by_id_controller,
    update_payment_controller,
    delete_payment_controller
)

payments_bp = Blueprint("payments", __name__, url_prefix="/payments")

BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "payment")
)

# Obtener todos los pagos
@payments_bp.route("/", methods=["GET"])
#@jwt_required()
#@role_required(["admin", "billing"])
@swag_from(os.path.join(BASE_DOCS, "get_all.yml"))
def get_all_payments():
    return get_all_payments_controller()

# Obtener pago por ID
@payments_bp.route("/<int:payment_id>", methods=["GET"])
#@jwt_required()
#@role_required(["admin", "billing"])
@swag_from(os.path.join(BASE_DOCS, "get_by_id.yml"))
def get_payment_by_id(payment_id):
    return get_payment_by_id_controller(payment_id)

# Crear un pago
@payments_bp.route("/", methods=["POST"])
#@jwt_required()
#@role_required(["admin", "billing"])
@swag_from(os.path.join(BASE_DOCS, "create.yml"))
def create_payment():
    return create_payment_controller()

# Actualizar un pago
@payments_bp.route("/<int:payment_id>", methods=["PATCH"])
#@jwt_required()
#@role_required(["admin", "billing"])
@swag_from(os.path.join(BASE_DOCS, "update.yml"))
def update_payment(payment_id):
    return update_payment_controller(payment_id)

# Eliminar un pago
@payments_bp.route("/<int:payment_id>", methods=["DELETE"])
#@jwt_required()
#@role_required(["admin", "billing"])
@swag_from(os.path.join(BASE_DOCS, "delete.yml"))
def delete_payment(payment_id):
    return delete_payment_controller(payment_id)