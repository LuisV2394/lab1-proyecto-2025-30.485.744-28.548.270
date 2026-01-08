from flask import request, jsonify
from app import db
from datetime import datetime
from app.models.prescription import Prescription, PrescriptionItem

# GET ALL PRESCRIPTION ITEMS
def get_all_prescription_items_controller():
    items = PrescriptionItem.query.all()
    return jsonify([item.to_dict() for item in items]), 200

# GET PRESCRIPTION ITEM BY ID
def get_prescription_item_by_id_controller(item_id):
    item = PrescriptionItem.query.get(item_id)
    if not item:
        return jsonify({"error": "Prescription item not found"}), 404

    return jsonify(item.to_dict()), 200

# GET ITEMS BY PRESCRIPTION ID
def get_items_by_prescription_id_controller(prescription_id):
    prescription = Prescription.query.get(prescription_id)
    if not prescription:
        return jsonify({"error": "Prescription not found"}), 404

    items = PrescriptionItem.query.filter_by(prescription_id=prescription_id).all()
    return jsonify([item.to_dict() for item in items]), 200

# CREATE PRESCRIPTION ITEM
def create_prescription_item_controller():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON payload"}), 400

    required_fields = [
        "prescription_id",
        "medicine_code",
        "name"
    ]

    for field in required_fields:
        if field not in data or data[field] in (None, ""):
            return jsonify({"error": f"Missing required field: {field}"}), 400

    # Validate prescription exists
    prescription = Prescription.query.get(data["prescription_id"])
    if not prescription:
        return jsonify({"error": "Prescription not found"}), 404

    # Create item
    item = PrescriptionItem(
        prescription_id=data["prescription_id"],
        medicine_code=data["medicine_code"],
        name=data["name"],
        dosage=data.get("dosage"),
        route=data.get("route"),
        frequency=data.get("frequency"),
        duration=data.get("duration"),
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    db.session.add(item)

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({
            "error": "Error creating prescription item",
            "details": str(e)
        }), 500

    return jsonify({
        "message": "Prescription item created successfully",
        "item_id": item.id
    }), 201

# UPDATE PRESCRIPTION ITEM
def update_prescription_item_controller(item_id):
    item = PrescriptionItem.query.get(item_id)

    if not item:
        return jsonify({"error": "Prescription item not found"}), 404

    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON payload"}), 400

    # Optional updatable fields
    updatable_fields = [
        "medicine_code",
        "name",
        "dosage",
        "route",
        "frequency",
        "duration"
    ]

    for field in updatable_fields:
        if field in data:
            setattr(item, field, data[field])

    item.updated_at = datetime.utcnow()

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({
            "error": "Error updating prescription item",
            "details": str(e)
        }), 500

    return jsonify({
        "message": "Prescription item updated successfully",
        "item_id": item.id
    }), 200

# DELETE PRESCRIPTION ITEM
def delete_prescription_item_controller(item_id):
    item = PrescriptionItem.query.get(item_id)

    if not item:
        return jsonify({"error": "Prescription item not found"}), 404

    db.session.delete(item)

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({
            "error": "Error deleting prescription item",
            "details": str(e)
        }), 500

    return jsonify({"message": "Prescription item deleted successfully"}), 200