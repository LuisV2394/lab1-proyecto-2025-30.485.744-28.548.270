from flask import jsonify, request
from app.models.prescription import Prescription
from app.models.episodes import Episode 
from app import db

def create_prescription_controller():
    data = request.get_json()
    
    # 1. validate required fields
    if 'episodeId' not in data or 'items' not in data:
        return jsonify({"error": "missing requerid fields (episodeId, items)"}), 400

    items = data.get('items')
    if not isinstance(items, list) or len(items) == 0:
        return jsonify({"error": "The 'items' field must be a non-empty list"}), 400

    # 2. Validate each item structure
    required_item_keys = ['name', 'dose', 'frequency', 'duration']
    for item in items:
        for key in required_item_keys:
            if key not in item:
                return jsonify({"error": f"Each item must contain at least: {key}"}), 400

    # 3. validate episode existence and status
    episode = Episode.query.get(data['episodeId'])
    if not episode:
        return jsonify({"error": "episode missing"}), 404
        
    if episode.status == 'close':
        return jsonify({"error": "You cannot create prescriptions for a closed episode"}), 409

    # 4. Crear la receta
    new_prescription = Prescription(
        episode_id=data['episodeId'],
        items=items,
        observations=data.get('observations')
    )

    try:
        db.session.add(new_prescription)
        db.session.commit()
        return jsonify({
            "message": "recipe created successfully",
            "prescription": new_prescription.to_dict()
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

def get_prescriptions_by_episode_controller(episode_id):
    episode = Episode.query.get(episode_id)
    if not episode:
        return jsonify({"error": "Episode not found"}), 404

    prescriptions = Prescription.query.filter_by(episode_id=episode_id).all()
    return jsonify([p.to_dict() for p in prescriptions]), 200

def delete_prescription_controller(prescription_id):
    prescription = Prescription.query.get(prescription_id)
    if not prescription:
        return jsonify({"error": "prescription not found"}), 404
        
    # Verificar estado del episodio asociado para integridad
    episode = Episode.query.get(prescription.episode_id)
    if episode and episode.status == 'close':
        return jsonify({"error": "you cannot deleate a prescription for a close episode"}), 409

    try:
        db.session.delete(prescription)
        db.session.commit()
        return jsonify({"message": "prescription deleate susefully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500