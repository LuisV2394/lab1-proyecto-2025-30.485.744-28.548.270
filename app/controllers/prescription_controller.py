from flask import request, jsonify
from app import db
from app.models.prescription import Prescription 
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

    # Validar que el episodio exista
    episode = Episode.query.get(data["episode_id"])
    if not episode:
        return jsonify({"error": "Episode not found"}), 404

    prescription = Prescription(
        episode_id=data["episode_id"],
        items=data["items"],
        observations=data.get("observations")
    )

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
    return jsonify({"message": "Prescription created successfully", "prescription_id": prescription.id}), 201
def update_prescription_controller(prescription_id):
    prescription = Prescription.query.get(prescription_id)
    if not prescription:
        return jsonify({"error": "Prescription not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON payload"}), 400

    if "items" in data:
        if not isinstance(data["items"], list) or not data["items"]:
            return jsonify({"error": "items must be a non-empty list"}), 400
        prescription.items = data["items"]

    if "observations" in data:
        prescription.observations = data["observations"]

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