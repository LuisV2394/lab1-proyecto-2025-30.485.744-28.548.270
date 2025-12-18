from flask import Blueprint
from flask_jwt_extended import jwt_required
from flasgger.utils import swag_from
from app.utils.middleware import role_required
import os

from app.controllers.notification_controller import (
    get_all_notifications_controller,
    get_notification_by_id_controller,
    create_notification_controller,
    update_notification_status_controller
)

notifications_bp = Blueprint(
    "notifications",
    __name__,
    url_prefix="/notifications"
)

BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "notification")
)

# Obtener todas las notificaciones
@notifications_bp.route("/", methods=["GET"])
# @jwt_required()
# @role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "get_all.yml"))
def get_all_notifications():
    return get_all_notifications_controller()


# Obtener notificación por ID
@notifications_bp.route("/<int:notification_id>", methods=["GET"])
# @jwt_required()
# @role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "get_by_id.yml"))
def get_notification_by_id(notification_id):
    return get_notification_by_id_controller(notification_id)


# Crear notificación
@notifications_bp.route("/", methods=["POST"])
# @jwt_required()
# @role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "create.yml"))
def create_notification():
    return create_notification_controller()


# Actualizar estado de notificación
@notifications_bp.route("/<int:notification_id>", methods=["PATCH"])
# @jwt_required()
# @role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "update.yml"))
def update_notification(notification_id):
    return update_notification_status_controller(notification_id)