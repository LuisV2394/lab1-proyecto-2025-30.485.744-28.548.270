from flask import Blueprint
from flasgger import swag_from
from flask_jwt_extended import jwt_required
import os

from app.controllers.agenda_controller import (
    create_block_controller,
    list_blocks_controller,
    get_block_controller,
    update_block_controller,
    delete_block_controller
)

agenda_bp = Blueprint('agenda', __name__, url_prefix="/agenda")

BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "agenda")
)

@agenda_bp.route('/', methods=['POST'])
# @jwt_required()
@swag_from(os.path.join(BASE_DOCS, 'create.yml'))
def create_block():
    return create_block_controller()

@agenda_bp.route('/', methods=['GET'])
# @jwt_required()
@swag_from(os.path.join(BASE_DOCS, 'get_all.yml'))
def list_blocks():
    return list_blocks_controller()

@agenda_bp.route('/<int:block_id>', methods=['GET'])
# @jwt_required()
@swag_from(os.path.join(BASE_DOCS, 'get.yml'))
def get_block(block_id):
    return get_block_controller(block_id)

@agenda_bp.route('/<int:block_id>', methods=['PUT'])
# @jwt_required()
@swag_from(os.path.join(BASE_DOCS, 'update.yml'))
def update_block(block_id):
    return update_block_controller(block_id)

@agenda_bp.route('/<int:block_id>', methods=['DELETE'])
# @jwt_required()
@swag_from(os.path.join(BASE_DOCS, 'delete.yml'))
def delete_block(block_id):
    return delete_block_controller(block_id)