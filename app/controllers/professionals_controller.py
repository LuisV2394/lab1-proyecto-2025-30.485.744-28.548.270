from flask import jsonify, request
from app.models.professional import Professional
from app import db
import re
from app.models.professional import Professional


# Obtener todos los profesionales
def get_all_professionals_controller():
    professionals = Professional.query.all()
    data = [p.to_dict() for p in professionals]
    return jsonify(data), 200

# Buscar profesional por ID
def get_professional_by_id_controller(professional_id):
    professional = Professional.query.get(professional_id)

    if not professional:
        return jsonify({"error": "Professional not found"}), 404

    return jsonify({
        "message": "Professional retrieved successfully",
        "professional": professional.to_dict()
    }), 200

# Crear un nuevo profesional
def create_professional_controller():
    data = request.get_json()

    # Validar campos requeridos
    required_fields = ["first_name", "last_name", "professional_registry", "specialty"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    email = data.get("email")
    professional_registry = data["professional_registry"]

    if email:
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_regex, email):
            return jsonify({"error": "Invalid email format"}), 400

        existing_email = Professional.query.filter_by(email=email).first()
        if existing_email:
            return jsonify({"error": "Email already in use"}), 400

    existing_registry = Professional.query.filter_by(professional_registry=professional_registry).first()
    if existing_registry:
        return jsonify({"error": "Professional registry already in use"}), 400

    # Crear el profesional
    new_professional = Professional(
        first_name=data["first_name"],
        last_name=data["last_name"],
        professional_registry=professional_registry,
        specialty=data["specialty"],
        email=email,
        phone=data.get("phone"),
        status=data.get("status"),
        is_active=True,
        schedule_enabled=data.get("schedule_enabled", False)
    )

    db.session.add(new_professional)
    db.session.commit()

    return jsonify({
        "message": "Professional created successfully",
        "professional": new_professional.to_dict()
    }), 201

# Actualizar profesional existente
def update_professional_controller(professional_id):
    professional = Professional.query.get(professional_id)
    if not professional:
        return jsonify({"error": "Professional not found"}), 404

    data = request.get_json()

    for key, value in data.items():
        if hasattr(professional, key):

            if key == "email" and value:
                email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
                if not re.match(email_regex, value):
                    return jsonify({"error": "Invalid email format"}), 400
                
                existing_email = Professional.query.filter(
                    Professional.email == value,
                    Professional.id != professional.id
                ).first()
                if existing_email:
                    return jsonify({"error": "Email already in use"}), 400

            if key == "professional_registry" and value:
                existing_registry = Professional.query.filter(
                    Professional.professional_registry == value,
                    Professional.id != professional.id
                ).first()
                if existing_registry:
                    return jsonify({"error": "Professional registry already in use"}), 400

            setattr(professional, key, value)

    db.session.commit()

    return jsonify({
        "message": "Professional updated successfully",
        "professional": professional.to_dict()
    }), 200

# Desactivar profesional
def deactivate_professional_controller(professional_id):
    professional = Professional.query.get(professional_id)
    if not professional:
        return jsonify({"error": "Professional not found"}), 404

    professional.is_active = False
    db.session.commit()

    return jsonify({"message": "Professional deactivated successfully"}), 200