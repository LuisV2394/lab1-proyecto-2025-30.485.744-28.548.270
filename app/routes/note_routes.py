from flask import Blueprint
from flasgger import swag_from
import os

from app.controllers.notes_controller import (
    create_note_controller,
    get_all_notes_controller,
    get_note_by_id_controller,
    update_note_controller,
    delete_note_controller
)

note_bp = Blueprint("clinical_notes", __name__, url_prefix="/notes")

BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "note")
)

# CREATE
@note_bp.route("/", methods=["POST"])
@swag_from(os.path.join(BASE_DOCS, "create.yml"))
def create_note():
    return create_note_controller()

# READ ALL
@note_bp.route("/", methods=["GET"])
@swag_from(os.path.join(BASE_DOCS, "get_all.yml"))
def get_all_notes():
    return get_all_notes_controller()

# READ BY ID
@note_bp.route("/<int:note_id>", methods=["GET"])
@swag_from(os.path.join(BASE_DOCS, "get_by_id.yml"))
def get_note_by_id(note_id):
    return get_note_by_id_controller(note_id)

# UPDATE
@note_bp.route("/<int:note_id>", methods=["PUT"])
@swag_from(os.path.join(BASE_DOCS, "update.yml"))
def update_note(note_id):
    return update_note_controller(note_id)

# DELETE
@note_bp.route("/<int:note_id>", methods=["DELETE"])
@swag_from(os.path.join(BASE_DOCS, "delete.yml"))
def delete_note(note_id):
    return delete_note_controller(note_id)