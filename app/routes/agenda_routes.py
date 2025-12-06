from flask import Blueprint
from flasgger import swag_from
from flask_jwt_extended import jwt_required
import os

from app.controllers.agenda_controller import create_block_controller

agenda_bp = Blueprint('agenda', __name__, url_prefix="/agenda")

BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "agenda")
)

@agenda_bp.route('/', methods=['POST'])
# @jwt_required()
@swag_from(os.path.join(BASE_DOCS, 'create.yml'))
def create_block():
    return create_block_controller()