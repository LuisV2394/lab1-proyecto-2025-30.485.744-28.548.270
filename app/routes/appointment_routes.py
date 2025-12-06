from flask import Blueprint
from flasgger import swag_from
from flask_jwt_extended import jwt_required
import os

from app.controllers.appointment_controller import (
    create_appointment_controller,
    update_appointment_status_controller
)

appt_bp = Blueprint('appointments', __name__, url_prefix="/appointments")

BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "appointment")
)

@appt_bp.route('/', methods=['POST'])
@jwt_required()
@swag_from(os.path.join(BASE_DOCS, 'create.yml'))
def create_appointment():
    return create_appointment_controller()

@appt_bp.route('/<int:id>/status', methods=['PUT'])
@jwt_required()
@swag_from(os.path.join(BASE_DOCS, 'update.yml'))
def update_appointment_status(id):
    return update_appointment_status_controller(id)