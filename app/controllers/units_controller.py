from flask import jsonify, request
from app.models.unit import Unit
from app import db

# Obtener todas las unidades
def get_all_units_controller():
    units = Unit.query.all()
    return jsonify([u.to_dict() for u in units]), 200

# Obtener unidad por ID
def get_unit_by_id_controller(unit_id):
    unit = Unit.query.get(unit_id)
    if not unit:
        return jsonify({"error": "Unit not found"}), 404

    return jsonify(unit.to_dict()), 200

# Crear nueva unidad
def create_unit_controller():
    data = request.get_json()

    required_fields = ["name", "type"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    new_unit = Unit(
        name=data["name"],
        type=data["type"],
        description=data.get("description"),
        phone=data.get("phone"),
        is_active=data.get("is_active", True)
    )

    db.session.add(new_unit)
    db.session.commit()

    return jsonify({
        "message": "Unit created successfully",
        "unit": new_unit.to_dict()
    }), 201

# Actualizar unidad
def update_unit_controller(unit_id):
    unit = Unit.query.get(unit_id)
    if not unit:
        return jsonify({"error": "Unit not found"}), 404

    data = request.get_json()
    for key, value in data.items():
        if hasattr(unit, key):
            setattr(unit, key, value)

    db.session.commit()

    return jsonify({
        "message": "Unit updated successfully",
        "unit": unit.to_dict()
    }), 200

# Desactivar unidad
def deactivate_unit_controller(unit_id):
    unit = Unit.query.get(unit_id)
    if not unit:
        return jsonify({"error": "Unit not found"}), 404

    unit.is_active = False
    db.session.commit()

    return jsonify({"message": "Unit deactivated successfully"}), 200