from flask import Blueprint
from flask_jwt_extended import jwt_required
from flasgger import swag_from
from app.controllers.tariff_controller import (
    create_tariff_controller,
    get_tariff_by_id_controller,
    update_tariff_controller,
    delete_tariff_controller
)
import os

tariff_bp = Blueprint("tariffs", __name__, url_prefix="/tariffs")

BASE_DOCS = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "docs", "tariffs"))

@tariff_bp.route("/", methods=["POST"])
@jwt_required()
@swag_from(os.path.join(BASE_DOCS, "create.yml"))
def create_tariff():
    return create_tariff_controller()

@tariff_bp.route("/<int:tariff_id>", methods=["GET"])
@jwt_required()
@swag_from(os.path.join(BASE_DOCS, "get_by_id.yml"))
def get_tariff(tariff_id):
    return get_tariff_by_id_controller(tariff_id)

@tariff_bp.route("/<int:tariff_id>", methods=["PUT"])
@jwt_required()
@swag_from(os.path.join(BASE_DOCS, "update.yml"))
def update_tariff(tariff_id):
    return update_tariff_controller(tariff_id)

@tariff_bp.route("/<int:tariff_id>", methods=["DELETE"])
@jwt_required()
@swag_from(os.path.join(BASE_DOCS, "delete.yml"))
def delete_tariff(tariff_id):
    return delete_tariff_controller(tariff_id)