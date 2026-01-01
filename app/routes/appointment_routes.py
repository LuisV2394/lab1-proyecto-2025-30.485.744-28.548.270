from flask import Blueprint
from flasgger import swag_from
from flask_jwt_extended import jwt_required
import os

from app.controllers.appointment_controller import (
    create_appointment_controller,
    list_appointments_controller,
    get_appointment_controller,
    update_appointment_controller,
    update_appointment_status_controller,
    delete_appointment_controller
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


@appt_bp.route('/', methods=['GET'])
#@jwt_required()
@swag_from(os.path.join(BASE_DOCS, 'get_all.yml'))
def list_appointments():
    return list_appointments_controller()


@appt_bp.route('/<int:id>', methods=['GET'])
#@jwt_required()
@swag_from(os.path.join(BASE_DOCS, 'get.yml'))
def get_appointment(id):
    return get_appointment_controller(id)


@appt_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
@swag_from(os.path.join(BASE_DOCS, 'update.yml'))
def update_appointment(id):
    return update_appointment_controller(id)


@appt_bp.route('/<int:id>/status', methods=['PUT'])
@jwt_required()
@swag_from(os.path.join(BASE_DOCS, 'update_status.yml'))
def update_status(id):
    return update_appointment_status_controller(id)


@appt_bp.route('/<int:id>', methods=['DELETE'])
#@jwt_required()
@swag_from(os.path.join(BASE_DOCS, 'delete.yml'))
def delete_appointment(id):
    return delete_appointment_controller(id)