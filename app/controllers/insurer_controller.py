from flask import jsonify, request
from datetime import datetime
from app import db
from app.models.insurer import Insurer
import re

PHONE_REGEX = re.compile(r"^\+58\d{10}$") 

def get_all_insurers_controller():
    insurers = Insurer.query.all()
    result = []
    for ins in insurers:
        result.append({
            "id": ins.id,
            "name": ins.name,
            "taxId": ins.tax_id,
            "contact": ins.contact,
            "isActive": ins.is_active,
            "createdAt": ins.created_at.isoformat() if ins.created_at else None,
            "updatedAt": ins.updated_at.isoformat() if ins.updated_at else None,
        })
    return jsonify(result), 200


def get_insurer_by_id_controller(insurer_id):
    insurer = Insurer.query.get(insurer_id)
    if not insurer:
        return jsonify({"error": "Insurer not found"}), 404

    return jsonify({
        "id": insurer.id,
        "name": insurer.name,
        "taxId": insurer.tax_id,
        "contact": insurer.contact,
        "isActive": insurer.is_active,
        "createdAt": insurer.created_at.isoformat() if insurer.created_at else None,
        "updatedAt": insurer.updated_at.isoformat() if insurer.updated_at else None,
    }), 200

def create_insurer_controller():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON payload"}), 400

    required_fields = ["name", "taxId"]
    for field in required_fields:
        if field not in data or not data[field]:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    # Validar tax_id único
    existing = Insurer.query.filter_by(tax_id=data["taxId"]).first()
    if existing:
        return jsonify({"error": "taxId already exists"}), 409

    # Validar teléfono si viene
    contact = data.get("contact")
    if contact and not PHONE_REGEX.match(contact):
        return jsonify({"error": "Invalid phone number format. Use +58XXXXXXXXXX"}), 400

    insurer = Insurer(
        name=data["name"],
        tax_id=data["taxId"],
        contact=contact,
        is_active=data.get("isActive", True),
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    try:
        db.session.add(insurer)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error creating insurer", "details": str(e)}), 500

    return jsonify({
        "message": "Insurer created successfully",
        "insurerId": insurer.id
    }), 201

def update_insurer_controller(insurer_id):
    insurer = Insurer.query.get(insurer_id)
    if not insurer:
        return jsonify({"error": "Insurer not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON payload"}), 400

    if "name" in data:
        insurer.name = data["name"]
    if "taxId" in data:
        # Validar tax_id único si se cambia
        existing = Insurer.query.filter(Insurer.tax_id == data["taxId"], Insurer.id != insurer.id).first()
        if existing:
            return jsonify({"error": "taxId already exists"}), 409
        insurer.tax_id = data["taxId"]
    if "contact" in data:
        contact = data["contact"]
        if contact and not PHONE_REGEX.match(contact):
            return jsonify({"error": "Invalid phone number format. Use +58XXXXXXXXXX"}), 400
        insurer.contact = contact
    if "isActive" in data:
        insurer.is_active = data["isActive"]

    insurer.updated_at = datetime.utcnow()

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error updating insurer", "details": str(e)}), 500

    return jsonify({"message": "Insurer updated successfully"}), 200

def delete_insurer_controller(insurer_id):
    insurer = Insurer.query.get(insurer_id)
    if not insurer:
        return jsonify({"error": "Insurer not found"}), 404

    try:
        db.session.delete(insurer)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error deleting insurer", "details": str(e)}), 500

    return jsonify({"message": "Insurer deleted successfully"}), 200