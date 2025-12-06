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
    if not episode or episode.status == 'close':
        return jsonify({"error": "El episodio no existe o está cerrado"}), 400

    # Determinar contenido
    content = data.get('content')

    # Si están enviando SOAP, generar contenido automático
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

    # Crear nota clínica
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