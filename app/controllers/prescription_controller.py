from flask import request, jsonify
from app import db
from app.models.prescription import Prescription, PrescriptionItem
from app.models.episodes import Episode

def get_all_prescriptions_controller():
    prescriptions = Prescription.query.all()
    return jsonify([p.to_dict() for p in prescriptions]), 200

def get_prescription_by_id_controller(prescription_id):
    prescription = Prescription.query.get(prescription_id)
    if not prescription:
        return jsonify({"error": "Prescription not found"}), 404
    return jsonify(prescription.to_dict()), 200

def create_prescription_controller():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON payload"}), 400

    required_fields = ["episode_id", "items"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    if not isinstance(data["items"], list) or not data["items"]:
        return jsonify({"error": "items must be a non-empty list"}), 400

    # Validate that the episode exists
    episode = Episode.query.get(data["episode_id"])
    if not episode:
        return jsonify({"error": "Episode not found"}), 404

    # Create Prescription instance
    prescription = Prescription(
        episode_id=data["episode_id"],
        observations=data.get("observations")
    )

    # Create PrescriptionItem instances
    for item_data in data["items"]:
        item = PrescriptionItem(
            medicine_code=item_data.get("medicine_code"),
            name=item_data.get("name"),
            dosage=item_data.get("dosage"),
            route=item_data.get("route"),
            frequency=item_data.get("frequency"),
            duration=item_data.get("duration")
        )
        prescription.items.append(item)

    db.session.add(prescription)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error creating prescription", "details": str(e)}), 500

    return jsonify({
        "message": "Prescription created successfully",
        "prescription_id": prescription.id
    }), 201

def update_prescription_controller(prescription_id):
    prescription = Prescription.query.get(prescription_id)
    if not prescription:
        return jsonify({"error": "Prescription not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON payload"}), 400

    if "observations" in data:
        prescription.observations = data["observations"]

    if "items" in data:
        if not isinstance(data["items"], list) or not data["items"]:
            return jsonify({"error": "items must be a non-empty list"}), 400
        
        # Remove existing items
        prescription.items.clear()

        # Add new items
        for item_data in data["items"]:
            item = PrescriptionItem(
                medicine_code=item_data.get("medicine_code"),
                name=item_data.get("name"),
                dosage=item_data.get("dosage"),
                route=item_data.get("route"),
                frequency=item_data.get("frequency"),
                duration=item_data.get("duration")
            )
            prescription.items.append(item)

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error updating prescription", "details": str(e)}), 500

    return jsonify({"message": "Prescription updated successfully", "prescription_id": prescription.id}), 200

def delete_prescription_controller(prescription_id):
    prescription = Prescription.query.get(prescription_id)
    if not prescription:
        return jsonify({"error": "Prescription not found"}), 404

    db.session.delete(prescription)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error deleting prescription", "details": str(e)}), 500

    return jsonify({"message": "Prescription deleted successfully"}), 200