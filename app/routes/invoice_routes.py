from flask import Blueprint
from flasgger import swag_from
import os

from app.controllers.invoice_controller import (
    get_all_invoices_controller,
    get_invoice_by_id_controller,
    create_invoice_controller,
    update_invoice_status_controller,
    cancel_invoice_controller
)

invoice_bp = Blueprint("invoices", __name__, url_prefix="/invoices")

BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "invoice")
)

# CREATE
@invoice_bp.route("/", methods=["POST"])
@swag_from(os.path.join(BASE_DOCS, "create.yml"))
def create_invoice():
    return create_invoice_controller()

# READ ALL
@invoice_bp.route("/", methods=["GET"])
@swag_from(os.path.join(BASE_DOCS, "get_all.yml"))
def get_all_invoices():
    return get_all_invoices_controller()

# READ BY ID
@invoice_bp.route("/<int:invoice_id>", methods=["GET"])
@swag_from(os.path.join(BASE_DOCS, "get_by_id.yml"))
def get_invoice_by_id(invoice_id):
    return get_invoice_by_id_controller(invoice_id)

# UPDATE STATUS
@invoice_bp.route("/<int:invoice_id>/status", methods=["PATCH"])
@swag_from(os.path.join(BASE_DOCS, "update.yml"))
def update_invoice_status(invoice_id):
    return update_invoice_status_controller(invoice_id)

# CANCEL
@invoice_bp.route("/<int:invoice_id>/cancel", methods=["PATCH"])
@swag_from(os.path.join(BASE_DOCS, "cancel.yml"))
def cancel_invoice(invoice_id):
    return cancel_invoice_controller(invoice_id)