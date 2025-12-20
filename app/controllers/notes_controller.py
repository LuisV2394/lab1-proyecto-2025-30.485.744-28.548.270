from flask import request, jsonify
from app.models.note import ClinicalNote
from app.models.episodes import Episode
from app.models.professional import Professional
from app import db

def create_note_controller():
    data = request.json or {}

    try:
        # 1️⃣ Validar campos obligatorios
        episode_id = data.get('episode_id')
        if not episode_id:
            return jsonify({"error": "Debe enviar 'episode_id'"}), 400

        # 2️⃣ Validar existencia del episodio y que esté abierto
        episode = Episode.query.get(episode_id)
        if not episode or episode.status == 'CLOSED':
            return jsonify({"error": "El episodio no existe o está cerrado"}), 400

        # 3️⃣ Validar existencia del profesional si se envía
        professional_id = data.get('professional_id')
        if professional_id and not Professional.query.get(professional_id):
            return jsonify({"error": "El profesional no existe"}), 404

        # 4️⃣ Determinar contenido
        content = data.get('content')
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

        # 5️⃣ Validar note_type (opcional, ejemplo de enum)
        note_type = data.get('note_type', 'EVOLUTION')
        allowed_types = ['EVOLUTION', 'INITIAL', 'DISCHARGE']
        if note_type not in allowed_types:
            return jsonify({"error": f"note_type inválido. Valores permitidos: {allowed_types}"}), 400

        # 6️⃣ Validar version
        version = data.get('version', 1)
        try:
            version = int(version)
            if version < 1:
                raise ValueError
        except ValueError:
            return jsonify({"error": "version debe ser un entero positivo"}), 400

        # 7️⃣ Crear nota clínica
        new_note = ClinicalNote(
            episode_id=episode_id,
            professional_id=professional_id,
            note_type=note_type,
            content=content,
            version=version
        )

        db.session.add(new_note)
        db.session.commit()

        return jsonify({
            "message": "Nota clínica registrada",
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