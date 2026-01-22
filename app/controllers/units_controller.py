from flask import jsonify, request
from app.models.unit import Unit
from app import db
import re

# Enum válido para el campo type
VALID_TYPES = ["SEDE", "CONSULTORIO", "SERVICIO"]

# Expresión regular para validar teléfono (ej: 10-15 dígitos, puede incluir +, espacios o guiones)
PHONE_REGEX = re.compile(r'^\+?[\d\s-]{7,15}$')

def get_all_units_controller():
    units = Unit.query.all()
    return jsonify([u.to_dict() for u in units]), 200

def get_unit_by_id_controller(unit_id):
    unit = Unit.query.get(unit_id)
    if not unit:
        return jsonify({"error": "Unit not found"}), 404
    return jsonify(unit.to_dict()), 200

def create_unit_controller():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON body"}), 400

    # Validar campos requeridos
    required_fields = ["name", "type"]
    missing = [f for f in required_fields if not data.get(f)]
    if missing:
        return jsonify({"error": f"Missing required fields: {', '.join(missing)}"}), 400

    # Validar ENUM
    type_value = data["type"].upper()
    if type_value not in VALID_TYPES:
        return jsonify({"error": f"Invalid type. Must be one of: {', '.join(VALID_TYPES)}"}), 400

    # Validar teléfono si existe
    phone = data.get("phone")
    if phone and not PHONE_REGEX.match(phone):
        return jsonify({"error": "Invalid phone format"}), 400

    new_unit = Unit(
        name=data["name"],
        type=type_value,
        description=data.get("description"),
        address=data.get("address"),
        phone=phone,
        schedule_reference=data.get("schedule_reference"),
        is_active=data.get("is_active", True)
    )

    db.session.add(new_unit)
    db.session.commit()

    return jsonify({
        "message": "Unit created successfully",
        "unit": new_unit.to_dict()
    }), 201

def update_unit_controller(unit_id):
    unit = Unit.query.get(unit_id)
    if not unit:
        return jsonify({"error": "Unit not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON body"}), 400

    allowed_fields = [
        "name",
        "type",
        "description",
        "address",
        "phone",
        "schedule_reference",
        "is_active"
    ]

    for field in allowed_fields:
        if field in data:
            value = data[field]

            # Validaciones
            if field == "type" and value:
                value = value.upper()
                if value not in VALID_TYPES:
                    return jsonify({"error": f"Invalid type. Must be one of: {', '.join(VALID_TYPES)}"}), 400
            if field == "phone" and value and not PHONE_REGEX.match(value):
                return jsonify({"error": "Invalid phone format"}), 400

            setattr(unit, field, value)

    db.session.commit()

    return jsonify({
        "message": "Unit updated successfully",
        "unit": unit.to_dict()
    }), 200

def deactivate_unit_controller(unit_id):
    unit = Unit.query.get(unit_id)
    if not unit:
        return jsonify({"error": "Unit not found"}), 404

    unit.is_active = False
    db.session.commit()

    return jsonify({"message": "Unit deactivated successfully"}), 200