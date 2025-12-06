from flask import Blueprint
from flasgger import swag_from
from flask_jwt_extended import jwt_required
import os

from app.controllers.notes_controller import create_note_controller

note_bp = Blueprint('notes', __name__, url_prefix="/notes")

BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "note")
)

@note_bp.route('/', methods=['POST'])
@jwt_required()
@swag_from(os.path.join(BASE_DOCS, 'create.yml'))
def create_note():
    return create_note_controller()