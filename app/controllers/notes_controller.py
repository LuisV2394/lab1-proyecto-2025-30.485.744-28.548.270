from flask import request, jsonify
from app.models.note import ClinicalNote
from app.models.episodes import Episode
from app import db

def create_note_controller():
    data = request.json

    episode_id = data.get('episode_id')
    professional_id = data.get('professional_id')

    # Validar episodio
    episode = Episode.query.get(episode_id)
    if not episode or episode.status == 'CLOSED':
        return jsonify({"error": "El episodio no existe o está cerrado"}), 400

    # Determinar contenido
    content = data.get('content')

    # Si no envían content, generar desde SOAP
    if not content:
        sub = data.get('sub_objective', "")
        obj = data.get('objective', "")
        test = data.get('test', "")
        plan = data.get('plan', "")

        if any([sub, obj, test, plan]):
            content = (
                f"S: {sub}\n"
                f"O: {obj}\n"
                f"A: {test}\n"
                f"P: {plan}"
            )
        else:
            return jsonify({"error": "Debe enviar 'content' o campos SOAP"}), 400

    new_note = ClinicalNote(
        episode_id=episode_id,
        professional_id=professional_id,
        note_type=data.get('note_type', 'EVOLUTION'),
        content=content,
        version=data.get('version', 1)
    )

    db.session.add(new_note)
    db.session.commit()

    return jsonify({
        "message": "Nota clínica registrada",
        "id": new_note.id
    }), 201


def get_all_notes_controller():
    notes = ClinicalNote.query.all()

    return jsonify([
        {
            "id": note.id,
            "episode_id": note.episode_id,
            "professional_id": note.professional_id,
            "note_type": note.note_type,
            "content": note.content,
            "version": note.version,
            "created_at": note.created_at.isoformat() if hasattr(note, "created_at") and note.created_at else None
        }
        for note in notes
    ]), 200


def get_note_by_id_controller(note_id):
    note = ClinicalNote.query.get(note_id)

    if not note:
        return jsonify({"message": "Nota clínica no encontrada"}), 404

    return jsonify({
        "id": note.id,
        "episode_id": note.episode_id,
        "professional_id": note.professional_id,
        "note_type": note.note_type,
        "content": note.content,
        "version": note.version,
        "created_at": note.created_at.isoformat() if hasattr(note, "created_at") and note.created_at else None
    }), 200


def update_note_controller(note_id):
    note = ClinicalNote.query.get(note_id)

    if not note:
        return jsonify({"message": "Nota clínica no encontrada"}), 404

    data = request.json

    episode = Episode.query.get(note.episode_id)
    if episode.status == 'CLOSED':
        return jsonify({"error": "No se puede modificar una nota de un episodio cerrado"}), 409

    note.content = data.get("content", note.content)
    note.note_type = data.get("note_type", note.note_type)
    note.version = data.get("version", note.version)

    db.session.commit()

    return jsonify({
        "message": "Nota clínica actualizada",
        "id": note.id
    }), 200


def delete_note_controller(note_id):
    note = ClinicalNote.query.get(note_id)

    if not note:
        return jsonify({"message": "Nota clínica no encontrada"}), 404

    episode = Episode.query.get(note.episode_id)
    if episode.status == 'CLOSED':
        return jsonify({"error": "No se puede eliminar una nota de un episodio cerrado"}), 409

    db.session.delete(note)
    db.session.commit()

    return jsonify({
        "message": "Nota clínica eliminada"
    }), 200