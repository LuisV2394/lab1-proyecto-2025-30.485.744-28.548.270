from flask import request, jsonify
from app.models.note import ClinicalNote
from app.models.episodes import Episode
from app.models.professional import Professional
from app import db

def create_note_controller():
    data = request.json or {}

    episode_id = data.get('episode_id')
    if not episode_id:
        return jsonify({"error": "You must provide 'episode_id'"}), 400

    episode = Episode.query.get(episode_id)
    if not episode or episode.status == 'CLOSED':
        return jsonify({"error": "Episode does not exist or is closed"}), 400

    professional_id = data.get('professional_id')
    if professional_id and not Professional.query.get(professional_id):
        return jsonify({"error": "Professional does not exist"}), 404

    subjective = data.get('subjective')
    objective = data.get('objective')
    assessment = data.get('assessment')
    plan = data.get('plan')
    attachments = data.get('attachments', [])

    if not any([subjective, objective, assessment, plan, attachments]):
        return jsonify({"error": "You must provide at least one field: subjective, objective, assessment, plan, or attachments"}), 400

    try:
        new_note = ClinicalNote(
            episode_id=episode_id,
            professional_id=professional_id,
            subjective=subjective,
            objective=objective,
            assessment=assessment,
            plan=plan,
            attachments=attachments
        )

        db.session.add(new_note)
        db.session.commit()

        return jsonify({
            "message": "Clinical note created",
            "id": new_note.id
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

def get_all_notes_controller():
    notes = ClinicalNote.query.all()

    return jsonify([
        {
            "id": note.id,
            "episode_id": note.episode_id,
            "professional_id": note.professional_id,
            "subjective": note.subjective,
            "objective": note.objective,
            "assessment": note.assessment,
            "plan": note.plan,
            "attachments": note.attachments,
            "created_at": note.created_at.isoformat() if note.created_at else None,
            "updated_at": note.updated_at.isoformat() if note.updated_at else None
        }
        for note in notes
    ]), 200

def get_note_by_id_controller(note_id):
    note = ClinicalNote.query.get(note_id)
    if not note:
        return jsonify({"message": "Clinical note not found"}), 404

    return jsonify({
        "id": note.id,
        "episode_id": note.episode_id,
        "professional_id": note.professional_id,
        "subjective": note.subjective,
        "objective": note.objective,
        "assessment": note.assessment,
        "plan": note.plan,
        "attachments": note.attachments,
        "created_at": note.created_at.isoformat() if note.created_at else None,
        "updated_at": note.updated_at.isoformat() if note.updated_at else None
    }), 200

def update_note_controller(note_id):
    note = ClinicalNote.query.get(note_id)
    if not note:
        return jsonify({"message": "Clinical note not found"}), 404

    episode = Episode.query.get(note.episode_id)
    if episode.status == 'CLOSED':
        return jsonify({"error": "Cannot modify a note of a closed episode"}), 409

    data = request.json

    note.subjective = data.get('subjective', note.subjective)
    note.objective = data.get('objective', note.objective)
    note.assessment = data.get('assessment', note.assessment)
    note.plan = data.get('plan', note.plan)
    note.attachments = data.get('attachments', note.attachments)

    db.session.commit()

    return jsonify({
        "message": "Clinical note updated",
        "id": note.id
    }), 200

def delete_note_controller(note_id):
    note = ClinicalNote.query.get(note_id)
    if not note:
        return jsonify({"message": "Clinical note not found"}), 404

    episode = Episode.query.get(note.episode_id)
    if episode.status == 'CLOSED':
        return jsonify({"error": "Cannot delete a note of a closed episode"}), 409

    db.session.delete(note)
    db.session.commit()

    return jsonify({
        "message": "Clinical note deleted"
    }), 200