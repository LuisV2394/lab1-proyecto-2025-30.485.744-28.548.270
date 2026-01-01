from flask import jsonify, request
from app.models.unit import Unit
from app import db

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

    required_fields = ["name", "type"]
    for field in required_fields:
        if not data.get(field):
            return jsonify({"error": f"Missing required field: {field}"}), 400

    new_unit = Unit(
        name=data["name"],
        type=data["type"].upper(),
        description=data.get("description"),
        address=data.get("address"),
        phone=data.get("phone"),
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
            if field == "type" and value:
                value = value.upper()
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