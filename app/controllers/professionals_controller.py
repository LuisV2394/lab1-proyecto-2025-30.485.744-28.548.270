from flask import jsonify, request
from sqlalchemy.exc import IntegrityError
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
    
def create_professional_controller():
    data = request.get_json()

    # Campos requeridos
    required_fields = ["first_name", "last_name", "professional_registry", "specialty"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    email = data.get("email")
    professional_registry = data["professional_registry"]
    phone = data.get("phone")

    # Validación formato email
    if email:
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_regex, email):
            return jsonify({"error": "Invalid email format"}), 400

        # Validación manual correo repetido
        existing_email = Professional.query.filter_by(email=email).first()
        if existing_email:
            return jsonify({"error": "Email already in use"}), 400

    # Validación manual registro profesional repetido
    existing_registry = Professional.query.filter_by(professional_registry=professional_registry).first()
    if existing_registry:
        return jsonify({"error": "Professional registry already in use"}), 400

    # Validación formato teléfono
    if phone:
        phone_regex = r'^\+?\d{7,15}$'
        if not re.match(phone_regex, phone):
            return jsonify({
                "error": "Invalid phone number format. Use only digits, optionally starting with '+', length 7-15."
            }), 400

    # Crear objeto
    new_professional = Professional(
        first_name=data["first_name"],
        last_name=data["last_name"],
        professional_registry=professional_registry,
        specialty=data["specialty"],
        email=email,
        phone=phone,
        status=data.get("status"),
        is_active=True,
        schedule_enabled=data.get("schedule_enabled", False)
    )

    db.session.add(new_professional)

    # Commit con manejo de error por si algo se escapa
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Database integrity error"}), 400

    return jsonify({
        "message": "Professional created successfully",
        "professional": new_professional.to_dict()
    }), 201

# Actualizar profesional
def update_professional_controller(professional_id):
    professional = db.session.get(Professional, professional_id)
    if not professional:
        return jsonify({"error": "Professional not found"}), 404

    data = request.get_json()

    # Solo permitir actualizar estos campos
    allowed_fields = ["first_name", "last_name", "professional_registry", "specialty",
                      "email", "phone", "status", "is_active", "schedule_enabled"]

    for key, value in data.items():
        if key not in allowed_fields:
            continue

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

        if key == "phone" and value:
            phone_regex = r'^\+?\d{7,15}$'
            if not re.match(phone_regex, value):
                return jsonify({
                    "error": "Invalid phone number format. Use only digits, optionally starting with '+', length 7-15."
                }), 400

        setattr(professional, key, value)

    # Commit con manejo de error
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Database integrity error"}), 400

    return jsonify({
        "message": "Professional updated successfully",
        "professional": professional.to_dict()
    }), 200

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