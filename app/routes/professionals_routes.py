from flask import Blueprint, jsonify, request
from app.models.professional import Professional
from app import db
from app.utils.middleware import role_required
from flask_jwt_extended import jwt_required
from flasgger.utils import swag_from
import os

professionals_bp = Blueprint("professionals", __name__, url_prefix="/professionals")

yaml_path = os.path.join(os.path.dirname(__file__), '../docs/professionals.yaml')

#Obtener todos los profesionales
@professionals_bp.route("/", methods=["GET"])
@jwt_required()
@role_required(["admin"])
@swag_from(yaml_path)
def get_all_professionals():
    professionals = Professional.query.all()
    data = [p.to_dict() for p in professionals]
    return jsonify(data), 200

#Obtener profesional por ID
@professionals_bp.route("/<int:professional_id>", methods=["GET"])
@jwt_required()
@role_required(["admin"])
def get_professional_by_id(professional_id):
    professional = Professional.query.get(professional_id)
    if not professional:
        return jsonify({"error": "Professional not found"}), 404
    return jsonify(professional.to_dict()), 200

#Crear nuevo profesional
@professionals_bp.route("/", methods=["POST"])
@jwt_required()
@role_required(["admin"])
@swag_from(yaml_path)
def create_professional():
    data = request.get_json()

    required_fields = ["person_id", "registration_number", "specialty"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    new_professional = Professional(
        person_id=data["person_id"],
        registration_number=data["registration_number"],
        specialty=data["specialty"],
        sub_specialty=data.get("sub_specialty"),
        is_active=True,
        schedule_enabled=data.get("schedule_enabled", False)
    )

    db.session.add(new_professional)
    db.session.commit()
    return jsonify({
        "message": "Professional created successfully",
        "professional": new_professional.to_dict()
    }), 201

#Actualizar profesional existente
@professionals_bp.route("/<int:professional_id>", methods=["PATCH"])
@jwt_required()
@role_required(["admin"])
@swag_from(yaml_path)
def update_professional(professional_id):
    professional = Professional.query.get(professional_id)
    if not professional:
        return jsonify({"error": "Professional not found"}), 404

    data = request.get_json()
    for key, value in data.items():
        if hasattr(professional, key):
            setattr(professional, key, value)

    db.session.commit()
    return jsonify({
        "message": "Professional updated successfully",
        "professional": professional.to_dict()
    }), 200

#Desactivar profesional
@professionals_bp.route("/<int:professional_id>", methods=["DELETE"])
@jwt_required()
@role_required(["admin"])
@swag_from(yaml_path)
def deactivate_professional(professional_id):
    professional = Professional.query.get(professional_id)
    if not professional:
        return jsonify({"error": "Professional not found"}), 404

    professional.is_active = False
    db.session.commit()
    return jsonify({"message": "Professional deactivated successfully"}), 200