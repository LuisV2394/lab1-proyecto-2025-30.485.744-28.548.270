from flask import Blueprint
from flask_jwt_extended import jwt_required
from flasgger import swag_from
from app.controllers.result_controller import (
    create_result_controller,
    update_result_controller,
    delete_result_controller
)
import os

results_bp = Blueprint("results", __name__, url_prefix="/results")

BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "results")
)

@results_bp.route("/", methods=["POST"])
@jwt_required()
@swag_from(os.path.join(BASE_DOCS, "create.yml"))
def create_result():
    return create_result_controller()

@results_bp.route("/<int:result_id>", methods=["PUT"])
@jwt_required()
@swag_from(os.path.join(BASE_DOCS, "update.yml"))
def update_result(result_id):
    return update_result_controller(result_id)

@results_bp.route("/<int:result_id>", methods=["DELETE"])
@jwt_required()
@swag_from(os.path.join(BASE_DOCS, "delete.yml"))
def delete_result(result_id):
    return delete_result_controller(result_id)