from flask import Blueprint
from flasgger import swag_from
import os

from app.controllers.episodes_controller import (
    create_episode_controller,
    get_all_episodes_controller,
    get_episode_by_id_controller,
    update_episode_controller,
    close_episode_controller,
    delete_episode_controller
)

episode_bp = Blueprint("episodes", __name__, url_prefix="/episodes")

BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "episodes")
)

# CREATE – Abrir episodio
@episode_bp.route("/", methods=["POST"])
@swag_from(os.path.join(BASE_DOCS, "create.yml"))
def create_episode():
    return create_episode_controller()

# READ ALL – Obtener todos los episodios
@episode_bp.route("/", methods=["GET"])
@swag_from(os.path.join(BASE_DOCS, "get_all.yml"))
def get_all_episodes():
    return get_all_episodes_controller()


# READ BY ID – Obtener episodio por ID
@episode_bp.route("/<int:episode_id>", methods=["GET"])
@swag_from(os.path.join(BASE_DOCS, "get_by_id.yml"))
def get_episode_by_id(episode_id):
    return get_episode_by_id_controller(episode_id)

# UPDATE – Actualizar episodio
@episode_bp.route("/<int:episode_id>", methods=["PUT"])
@swag_from(os.path.join(BASE_DOCS, "update.yml"))
def update_episode(episode_id):
    return update_episode_controller(episode_id)

# CLOSE – Cerrar episodio
@episode_bp.route("/<int:episode_id>/close", methods=["PUT"])
@swag_from(os.path.join(BASE_DOCS, "close.yml"))
def close_episode(episode_id):
    return close_episode_controller(episode_id)


# DELETE – Eliminar episodio
@episode_bp.route("/<int:episode_id>", methods=["DELETE"])
@swag_from(os.path.join(BASE_DOCS, "delete.yml"))
def delete_episode(episode_id):
    return delete_episode_controller(episode_id)