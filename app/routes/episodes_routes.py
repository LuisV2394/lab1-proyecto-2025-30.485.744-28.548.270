from flask import Blueprint
from flasgger import swag_from
from flask_jwt_extended import jwt_required
from datetime import datetime
import os

from app.controllers.episodes_controller import (
    create_episode_controller,
    close_episode_controller
)

episode_bp = Blueprint('episodes', __name__, url_prefix="/episodes")

BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "episodes")
)

@episode_bp.route('/', methods=['POST'])
@jwt_required()
@swag_from(os.path.join(BASE_DOCS, 'create.yml'))
def create_episode():
    return create_episode_controller()


@episode_bp.route('/<int:id>/close', methods=['PUT'])
@jwt_required()
@swag_from(os.path.join(BASE_DOCS, 'close.yml'))
def close_episode(id):
    return close_episode_controller(id)