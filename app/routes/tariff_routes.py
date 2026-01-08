from flask import Blueprint
from flask_jwt_extended import jwt_required
from flasgger import swag_from
from app.utils.middleware import role_required  
import os

# Controladores
from app.controllers.tariff_controller import (
    get_all_tariffs_controller,
    create_tariff_controller,
    get_tariff_by_id_controller,
    update_tariff_controller,
    delete_tariff_controller
)

tariff_bp = Blueprint("tariffs", __name__, url_prefix="/tariffs")

BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "tariffs")
)

# GET ALL TARIFFS
@tariff_bp.route("/", methods=["GET"])
#@jwt_required()
# @role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "get_all.yml"))
def get_all_tariffs():
    return get_all_tariffs_controller()

# CREATE TARIFF
@tariff_bp.route("/", methods=["POST"])
#@jwt_required()
# @role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "create.yml"))
def create_tariff():
    return create_tariff_controller()

# GET TARIFF BY ID
@tariff_bp.route("/<int:tariff_id>", methods=["GET"])
#@jwt_required()
# @role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "get_by_id.yml"))
def get_tariff_by_id(tariff_id):
    return get_tariff_by_id_controller(tariff_id)

# UPDATE TARIFF
@tariff_bp.route("/<int:tariff_id>", methods=["PATCH"])
#@jwt_required()
# @role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "update.yml"))
def update_tariff(tariff_id):
    return update_tariff_controller(tariff_id)

# DELETE TARIFF
@tariff_bp.route("/<int:tariff_id>", methods=["DELETE"])
#@jwt_required()
# @role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "delete.yml"))
def delete_tariff(tariff_id):
    return delete_tariff_controller(tariff_id)