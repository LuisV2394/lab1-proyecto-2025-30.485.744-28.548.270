from flask import jsonify, request
from app.models.professional import Professional
from app.models.person import Person
from app import db

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

    required_fields = ["person_id", "registration_number", "specialty"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    # Validar persona existente
    person = Person.query.get(data["person_id"])
    if not person:
        return jsonify({
            "error": "Invalid person_id: Person does not exist"
        }), 400

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


# Actualizar profesional existente
def update_professional_controller(professional_id):
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

# Desactivar profesional
def deactivate_professional_controller(professional_id):
    professional = Professional.query.get(professional_id)
    if not professional:
        return jsonify({"error": "Professional not found"}), 404

    professional.is_active = False
    db.session.commit()

    return jsonify({"message": "Professional deactivated successfully"}), 200