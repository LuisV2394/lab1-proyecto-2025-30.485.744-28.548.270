from flask import Blueprint
from flask_jwt_extended import jwt_required
from flasgger import swag_from
from app.controllers.coverage_plan_controller import (
    create_coverage_plan_controller,
    get_plans_by_insurer_controller,
    update_coverage_plan_controller,
    delete_coverage_plan_controller
)
import os

coverage_bp = Blueprint("coverage_plans", __name__, url_prefix="/coverage-plans")

BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "coverage_plans")
)

@coverage_bp.route("/", methods=["POST"])
@jwt_required()
@swag_from(os.path.join(BASE_DOCS, "create.yml"))
def create_plan():
    return create_coverage_plan_controller()

@coverage_bp.route("/insurer/<int:insurer_id>", methods=["GET"])
@jwt_required()
@swag_from(os.path.join(BASE_DOCS, "get_by_insurer.yml"))
def get_by_insurer(insurer_id):
    return get_plans_by_insurer_controller(insurer_id)

@coverage_bp.route("/<int:plan_id>", methods=["PUT"])
@jwt_required()
@swag_from(os.path.join(BASE_DOCS, "update.yml"))
def update_plan(plan_id):
    return update_coverage_plan_controller(plan_id)

@coverage_bp.route("/<int:plan_id>", methods=["DELETE"])
@jwt_required()
@swag_from(os.path.join(BASE_DOCS, "delete.yml"))
def delete_plan(plan_id):
    return delete_coverage_plan_controller(plan_id)