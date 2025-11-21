from flask import Blueprint, jsonify, request
from app.models.person import Person
from app import db
from app.utils.middleware import role_required
from flask_jwt_extended import jwt_required
from flasgger.utils import swag_from
import os
from datetime import datetime

people_bp = Blueprint("people", __name__, url_prefix="/people")

BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "people")
)
print("BASE_DOCS:", BASE_DOCS)

# Obtener todas las personas
@people_bp.route("/", methods=["GET"])
@jwt_required()
@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "get_all.yml"))
def get_all_people():
    people = Person.query.all()
    return jsonify([p.to_dict() for p in people]), 200

# Obtener persona por ID
@people_bp.route("/<int:person_id>", methods=["GET"])
@jwt_required()
@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "get_by_id.yml"))
def get_person_by_id(person_id):
    person = Person.query.get(person_id)
    if not person:
        return jsonify({"error": "Person not found"}), 404
    return jsonify(person.to_dict()), 200

# Crear nueva persona
@people_bp.route("/", methods=["POST"])
@jwt_required()
@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "create.yml"))
def create_person():
    data = request.get_json()
    required_fields = ["first_name", "last_name"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    new_person = Person(
        document_number=data.get("document_number"),
        first_name=data["first_name"],
        last_name=data["last_name"],
        gender=data.get("gender"),
        birth_date=data.get("birth_date"),
        email=data.get("email"),
        phone=data.get("phone"),
        address=data.get("address"),
        active=data.get("active", True)
    )

    db.session.add(new_person)
    db.session.commit()

    return jsonify({
        "message": "Person created successfully",
        "person": new_person.to_dict()
    }), 201

# Actualizar persona
@people_bp.route("/<int:person_id>", methods=["PATCH"])
@jwt_required()
@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "update.yml"))
def update_person(person_id):
    person = Person.query.get(person_id)
    if not person:
        return jsonify({"error": "Person not found"}), 404

    data = request.get_json()

    for key, value in data.items():
        if hasattr(person, key):

            if key == "birth_date":
                if value:
                    # Convertir string "YYYY-MM-DD" -> date
                    value = datetime.strptime(value, "%Y-%m-%d").date()
                else:
                    value = None

            setattr(person, key, value)

    db.session.commit()

    return jsonify({
        "message": "Person updated successfully",
        "person": person.to_dict()
    }), 200

# Desactivar persona
@people_bp.route("/<int:person_id>", methods=["DELETE"])
@jwt_required()
@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "delete.yml"))
def deactivate_person(person_id):
    person = Person.query.get(person_id)
    if not person:
        return jsonify({"error": "Person not found"}), 404

    person.active = False
    db.session.commit()

    return jsonify({"message": "Person deactivated successfully"}), 200