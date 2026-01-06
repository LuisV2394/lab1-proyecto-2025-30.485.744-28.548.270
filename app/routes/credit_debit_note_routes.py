from flask import Blueprint
from flask_jwt_extended import jwt_required
from flasgger.utils import swag_from
import os

# Controllers
from app.controllers.credit_debit_note_controller import (
    get_all_credit_debit_notes,
    get_credit_debit_note_by_id,
    create_credit_debit_note,
    update_credit_debit_note,
    delete_credit_debit_note
)

credit_debit_notes_bp = Blueprint("credit_debit_notes", __name__, url_prefix="/credit-debit-notes")

# Base path for YAML documentation (if usas Flasgger)
BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "credit_debit_note")
)

# Get all notes
@credit_debit_notes_bp.route("/", methods=["GET"])
#@jwt_required()
#@role_required(["admin", "accounting"])
@swag_from(os.path.join(BASE_DOCS, "get_all.yml"))
def get_all_credit_debit_notes_route():
    return get_all_credit_debit_notes()

# Get note by ID
@credit_debit_notes_bp.route("/<int:note_id>", methods=["GET"])
#@jwt_required()
#@role_required(["admin", "accounting"])
@swag_from(os.path.join(BASE_DOCS, "get_by_id.yml"))
def get_credit_debit_note_by_id_route(note_id):
    return get_credit_debit_note_by_id(note_id)

# Create a new note
@credit_debit_notes_bp.route("/", methods=["POST"])
#@jwt_required()
#@role_required(["admin", "accounting"])
@swag_from(os.path.join(BASE_DOCS, "create.yml"))
def create_credit_debit_note_route():
    return create_credit_debit_note()

# Update an existing note
@credit_debit_notes_bp.route("/<int:note_id>", methods=["PATCH"])
#@jwt_required()
#@role_required(["admin", "accounting"])
@swag_from(os.path.join(BASE_DOCS, "update.yml"))
def update_credit_debit_note_route(note_id):
    return update_credit_debit_note(note_id)

# Delete a note
@credit_debit_notes_bp.route("/<int:note_id>", methods=["DELETE"])
#@jwt_required()
#@role_required(["admin", "accounting"])
@swag_from(os.path.join(BASE_DOCS, "delete.yml"))
def delete_credit_debit_note_route(note_id):
    return delete_credit_debit_note(note_id)